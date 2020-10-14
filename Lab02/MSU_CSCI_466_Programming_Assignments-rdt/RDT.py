import time
import Network
import argparse
from time import sleep
import hashlib

debug = False

#create a method for debugging messages
def debug_message(message):
    if debug:
        print(message)

class Packet:
	## the number of bytes used to store packet length
	seq_num_S_length = 10
	length_S_length = 10
	## length of md5 checksum in hex
	checksum_length = 32
	
	def __init__(self, seq_num, msg_S):
		self.seq_num = seq_num
		self.msg_S = msg_S
	
	@classmethod
	def from_byte_S(self, byte_S):
		if Packet.corrupt(byte_S):
			raise RuntimeError('Cannot initialize Packet: byte_S is corrupt')
		# extract the fields
		seq_num = int(byte_S[Packet.length_S_length: Packet.length_S_length + Packet.seq_num_S_length])
		msg_S = byte_S[Packet.length_S_length + Packet.seq_num_S_length + Packet.checksum_length:]
		return self(seq_num, msg_S)
	
	def get_byte_S(self):
		# convert sequence number of a byte field of seq_num_S_length bytes
		seq_num_S = str(self.seq_num).zfill(self.seq_num_S_length)
		# convert length to a byte field of length_S_length bytes
		length_S = str(self.length_S_length + len(seq_num_S) + self.checksum_length + len(self.msg_S)).zfill(
			self.length_S_length)
		# compute the checksum
		checksum = hashlib.md5((length_S + seq_num_S + self.msg_S).encode('utf-8'))
		checksum_S = checksum.hexdigest()
		# compile into a string
		return length_S + seq_num_S + checksum_S + self.msg_S
	
	@staticmethod
	def corrupt(byte_S):
		# extract the fields
		length_S = byte_S[0:Packet.length_S_length]
		seq_num_S = byte_S[Packet.length_S_length: Packet.seq_num_S_length + Packet.seq_num_S_length]
		checksum_S = byte_S[
		             Packet.seq_num_S_length + Packet.seq_num_S_length: Packet.seq_num_S_length + Packet.length_S_length + Packet.checksum_length]
		msg_S = byte_S[Packet.seq_num_S_length + Packet.seq_num_S_length + Packet.checksum_length:]
		
		# compute the checksum locally
		checksum = hashlib.md5(str(length_S + seq_num_S + msg_S).encode('utf-8'))
		computed_checksum_S = checksum.hexdigest()
		# and check if the same
		return checksum_S != computed_checksum_S


	def is_ack_pack(self):
		if self.msg_S == '1' or self.msg_S == '0':
			return True
		return False


class RDT:
	## latest sequence number used in a packet
	seq_num = 1
	## buffer of bytes read from network
	byte_buffer = ''
	timeout = 3
	
	def __init__(self, role_S, server_S, port):
		## update from wittie to use the passed port and port+1 to set up undirectional links
		if role_S == 'server':
			self.net_snd = Network.NetworkLayer(role_S, server_S, port)
			self.net_rcv = Network.NetworkLayer(role_S, server_S, port+1)
		else:
			self.net_rcv = Network.NetworkLayer(role_S, server_S, port)
			self.net_snd = Network.NetworkLayer(role_S, server_S, port+1)
	
	def disconnect(self):
		self.net_snd.disconnect()
		self.net_rcv.disconnect()
	
	def rdt_1_0_send(self, msg_S):
		p = Packet(self.seq_num, msg_S)
		self.seq_num += 1
		# here is the net_send link to send and receive
		self.net_snd.udt_send(p.get_byte_S())
	
	def rdt_1_0_receive(self):
		ret_S = None
		byte_S = self.net_rcv.udt_receive()
		self.byte_buffer += byte_S
		# keep extracting packets - if reordered, could get more than one
		while True:
			# check if we have received enough bytes
			if (len(self.byte_buffer) < Packet.length_S_length):
				return ret_S  # not enough bytes to read packet length
			# extract length of packet
			length = int(self.byte_buffer[:Packet.length_S_length])
			if len(self.byte_buffer) < length:
				return ret_S  # not enough bytes to read the whole packet
			# create packet from buffer content and add to return string
			p = Packet.from_byte_S(self.byte_buffer[0:length])
			ret_S = p.msg_S if (ret_S is None) else ret_S + p.msg_S
			# remove the packet bytes from the buffer
			self.byte_buffer = self.byte_buffer[length:]
		# if this was the last packet, will return on the next iteration
	
	def rdt_2_1_send(self, msg_S):
		#stole first lines from rdt 1.0
		p = Packet(self.seq_num, msg_S)
		cur_sequence = self.seq_num
		#create while loop for sequence while response is blank
		while cur_sequence == self.seq_num:
			self.net_snd.udt_send(p.get_byte_S())
			response = ''
			#new while loop for receiving
			while response == '':
				response = self.net_rcv.udt_receive()
			message_length = int(response[:Packet.length_S_length])
			self.byte_buffer = response[:message_length]
			#the statements below do a few things,
			#if packet isn't corrupt parse response message, check sequence numbers
			#and check ack numbers, if something is wrong the debug message sends a corruption error.
			if not Packet.corrupt(response[:message_length]):
				response_pack = Packet.from_byte_S(response[:message_length])
				if response_pack.seq_num < self.seq_num:
					debug_message("receiving end is behind. try again")
					test_response = Packet(response_pack.seq_num, "1")
					self.net_snd.udt_send(test_response.get_byte_S())
				elif response_pack.msg_S is "1":
					debug_message("got the ack, loading next...")
					self.seq_num += 1
				elif response_pack.msg_S is "0":
					debug_message("got the nak.. moving on")
					self.byte_buffer = ''
			else:
				debug_message("corrupted.. try again.")
				self.byte_buffer = ''


	
	def rdt_2_1_receive(self):
		#copy first few lines from rdt 1.0
		r_S = None
		b_S = self.net_rcv.udt_receive()
		self.byte_buffer += b_S
		#get sequence number
		curr_seq = self.seq_num
		#if the seq numbers are equal and the buffer is too small we break
		while curr_seq == self.seq_num:
			if len(self.byte_buffer) < Packet.length_S_length:
				break
			length = int(self.byte_buffer[:Packet.length_S_length])
			if len(self.byte_buffer) < length:
				break
			# if the packet is corrupt we send the debugger in to alert the system
			# that there was a corruption and send a a nak
			if Packet.corrupt(self.byte_buffer):
				debug_message("didn't get the packet...sending a nak")
				answer = Packet(self.seq_num, "0")
				self.net_snd.udt_send(answer.get_byte_S())
				# if the packet is within the buffer size we check if it's an
				#ack packet, if so we move forward and check sequence numbers,
				#if the sequence number is smaller we move on since we've received it
				# and send another nak for the next packet to be transmitted
				# if we get the correct one we send an ack and continue
			else:
				p = Packet.from_byte_S(self.byte_buffer[0:length])
				if p.is_ack_pack():
					self.byte_buffer = self.byte_buffer[length:]
					continue
				if p.seq_num < self.seq_num:
					debug_message('already have packet. sending nak.')
					answer = Packet(p.seq_num, "1")
					self.net_snd.udt_send(answer.get_byte_S())
				elif p.seq_num == self.seq_num:
					debug_message('received. incrementing seq number, sending ack.')
					answer = Packet(self.seq_num, "1")
					self.net_rcv.udt_send(answer.get_byte_S())
					self.seq_num += 1

				r_S = p.msg_S if (r_S is None) else r_S + p.msg_S
			# remove the packet bytes from the buffer
			self.byte_buffer = self.byte_buffer[length:]
		# if this was the last packet, will return on the next iteration
		return r_S

	
	def rdt_3_0_send(self, msg_S):
		p = Packet(self.seq_num, msg_S)
		current_seq = self.seq_num
		# similar to rdt2.1 we must check seq numbers but here we will wait
		# using the timer method to check for time outs
		while current_seq == self.seq_num:
			self.net_snd.udt_send(p.get_byte_S())
			response = ''
			timer = time.time()

			# Waiting for ack/nak
			while response == '' and timer + self.timeout > time.time():
				response = self.net_rcv.udt_receive()

			if response == '':
				continue
			# debug message sends response if there is not a timout
			debug_message("sender: " + response)

			msg_length = int(response[:Packet.length_S_length])
			self.byte_buffer = response[msg_length:]
			#if the packet is a timeout or corrupted or something else we do similar things
			# as we did in 2.1 by sending debug messages
			if not Packet.corrupt(response[:msg_length]):
				response_p = Packet.from_byte_S(response[:msg_length])
				if response_p.seq_num < self.seq_num:
					# It's trying to send me data again
					debug_message("Sender: Receiver behind sender")
					test = Packet(response_p.seq_num, "1")
					self.net_snd.udt_send(test.get_byte_S())
				elif response_p.msg_S is "1":
					debug_message("Sender: Received ACK, move on to next.")
					debug_message("Sender: Incrementing seq_num from {} to {}".format(self.seq_num, self.seq_num + 1))
					self.seq_num += 1
				elif response_p.msg_S is "0":
					debug_message("Sender: NAK received")
					self.byte_buffer = ''
			else:
				debug_message("Sender: Corrupted ACK")
				self.byte_buffer = ''
	
	def rdt_3_0_receive(self):
		ret_S = None
		byte_S = self.net_rcv.udt_receive()
		self.byte_buffer += byte_S
		curr_seq = self.seq_num
		# Don't move on until seq_num has been toggled
		# keep extracting packets - if reordered, could get more than one
		while curr_seq == self.seq_num:
			# check if we have received enough bytes
			if len(self.byte_buffer) < Packet.length_S_length:
				break  # not enough bytes to read packet length
			# extract length of packet
			length = int(self.byte_buffer[:Packet.length_S_length])
			if len(self.byte_buffer) < length:
				break  # not enough bytes to read the whole packet

			# Check if packet is corrupt
			if Packet.corrupt(self.byte_buffer):
				# Send a NAK
				debug_message("RECEIVER: Corrupt packet, sending NAK.")
				answer = Packet(self.seq_num, "0")
				self.net_snd.udt_send(answer.get_byte_S())
			else:
				# create packet from buffer content
				packet = Packet.from_byte_S(self.byte_buffer[0:length])
				# Check packet
				if packet.is_ack_pack():
					self.byte_buffer = self.byte_buffer[length:]
					continue
				if packet.seq_num < self.seq_num:
					debug_message('RECEIVER: Already received packet.  ACK again.')
					# Send another ACK
					answer = Packet(packet.seq_num, "1")
					self.net_snd.udt_send(answer.get_byte_S())
				elif packet.seq_num == self.seq_num:
					debug_message('RECEIVER: Received new.  Send ACK and increment seq.')
					# SEND ACK
					answer = Packet(self.seq_num, "1")
					self.net_snd.udt_send(answer.get_byte_S())
					debug_message("RECEIVER: Incrementing seq_num from {} to {}".format(self.seq_num, self.seq_num + 1))
					self.seq_num += 1
				# Add contents to return string
				ret_S = packet.msg_S if (ret_S is None) else ret_S + packet.msg_S
			# remove the packet bytes from the buffer
			self.byte_buffer = self.byte_buffer[length:]
		# if this was the last packet, will return on the next iteration
		return ret_S


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='RDT implementation.')
	parser.add_argument('role', help='Role is either client or server.', choices=['client', 'server'])
	parser.add_argument('server', help='Server.')
	parser.add_argument('port', help='Port.', type=int)
	args = parser.parse_args()
	
	rdt = RDT(args.role, args.server, args.port)
	if args.role == 'client':
		rdt.rdt_1_0_send('MSG_FROM_CLIENT')
		sleep(2)
		print(rdt.rdt_1_0_receive())
		rdt.disconnect()
	
	
	else:
		sleep(1)
		print(rdt.rdt_1_0_receive())
		rdt.rdt_1_0_send('MSG_FROM_SERVER')
		rdt.disconnect()
