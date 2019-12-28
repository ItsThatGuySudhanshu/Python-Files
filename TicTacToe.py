import pprint
import random
import sys
import pyperclip

def printBoard(board):
    print(board["top-L"]+ "|"+ board["top-M"]+ "|" + board["top-R"])
    print("=====")
    print(board["mid-L"]+ "|"+ board["mid-M"]+ "|" + board["mid-R"])
    print("=====")
    print(board["bot-L"]+ "|"+ board["bot-M"]+ "|" + board["bot-R"])

def userXOrO():
    xOrO = input("Do you choose to be X or O? ")
    xOrO = xOrO.lower()
    if (xOrO == "x"):
        return "x"
    else:                    
        return "o"


def userMove(aBoard, userchoice):
    found = False
    while found == False:
        userLocation = input("Where do you want to place your pointer? ")
        for i in aBoard:
            if userLocation.lower() == i.lower():
                if aBoard[i] == " ":
                    aBoard[i] = userchoice
                    found = True
                else:
                    print("Block already filled, try another one")
                
        if found == False:
            print("Invalid location, try again")
        
def computerMove(aBoard, userchoice):
    empty = False
    keys = list(aBoard.keys()  )
    if userchoice == "x":
        computerChoice = "o"
    else:
        computerChoice = "x"
        
    while empty == False:
        computerLocationKey = keys[random.randint(0,9)]
        if aBoard[computerLocationKey] == " ":
            aBoard[computerLocationKey] = computerChoice 
            empty = True
        
        
def checkForVictory(aBoard):
    keys = list(aBoard.keys())
    

theboard = {"top-L": " ", 
            "top-M": " ",
            "top-R": " ",
            "mid-L": " ",
            "mid-M": " ",
            "mid-R": " ",
            "bot-L": " ",
            "bot-M": " ",
            "bot-R": " "}

def main():
    userchoice = userXOrO()
    
    userMove(theboard, userchoice)
    computerMove(theboard, userchoice)
    printBoard(theboard)
        
main()

