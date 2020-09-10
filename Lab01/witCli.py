import requests

class myClient:
    def request_it(self):
        r = requests.get('http://localhost:8000')
        print(r.text)
    def do_POST(self):
        h = requests.post('http://localhost:8000', {'justin':'rock'})
        print(h.text)


