import pickle
PLAYS = {
"rock rock " : "tie" ,

"rock paper " : "0",

"rock scissors " : "0",

"paper rock " : "0",

"paper paper " : "tie",

"paper scissors " : "1" ,

"scissors rock " : "1",

"scissors paper " :"1",

"scissors scissors " : "tie"
}

playerNos = {
    "ONE": "0A",
    "RESET": "N"
}

playerNos2 ={
    "TWO": "1A",
    "RESET": "N"
}


with open('win_dic', 'wb') as handle:
    pickle.dump(PLAYS, handle)
with open ("Player_Nos", "wb") as zapalm:
    pickle.dump(playerNos, zapalm)
with open("Player_2Nos", "wb") as xapalm:
    pickle.dump(playerNos2, xapalm)
