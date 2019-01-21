#WARNING!!! TOGGLING TESTMODE ( 1 / 0 ) WILL HAVE A DRAMATIC EFFECT ON THE OUTPUT!!!
testMode = 1
waitMode = 1

allAvailableActions = [N, S, E, W, ?]


from random import randint
import time
import helper
from tkinter import *


Steve = ("The Evil Wizard Steve (O' hear His name and tremble)")
WestVirginia = ("Almost heaven, West Virginia // Blue Ridge Mountains, Shenandoah River // Life is old there, older than the trees // Younger than the mountains, blowing like a breeze // Country roads, take me home // To the place I belong")
notDead = ("True")


def Action(yourLocation):
    what2Do=input("What wantest you to doeth?")
    print(yourLocation)
    if what2Do == 'S':
        Move(what2Do, yourLocation)

    
def Move(what2Do, yourLocation):
    print(yourLocation)
    if what2Do=="N":
        print("You moved North!")
        yourLocation = yourLocation - 5
    elif what2Do=="S":
        print("You moved South!")
        yourLocation = yourLocation + 5
        print(yourLocation)
    elif what2Do=="E":
        print("You moved East!")
        yourLocation = yourLocation + 5
    elif what2Do=="W":
        print("You moved West!!")
        yourLocation = yourLocation - 1
    elif what2Do=="xxxx":
        print("OTHER ACTIONS")

def Describe():
    if yourLocation== "1":
        print("You are standing on a path")




def Wait1():
    time.sleep(1)
def Wait2():
    time.sleep(2)
def Wait3():
    time.sleep(3)
def Wait5():
    time.sleep(5)
def OpenSpeech():
    Wait2()
    print("Welcome to the Forgotten Lands!")
    Wait2()
    sName=input("What do they call you adventurer?")
    print("Interesting... Greetings,",sName,", and welcome to the Forgotten Lands!")
    Wait2()
    print("For some reason, the only way for you to interact with us on this side is through this new-fangled 'computer'.")
    Wait2()
    print("What's more, is that you can only use simple commands, such and N (to walk North) or GET to errrrr.... get something....")
    Wait2()
    print("Don't ask me why, but the Thing that put us all in here was too lazy/incompetant to care/ACTUALLY DO IT!!!!!!")
    Wait1()
    print("Sorry..... I just got a bit carried away...")
    print("Anyway, ONWARDS TO GLORY!! (And cookies - Hey! I'm hungry! Deal with it!)")
    Wait3()
    print("-----")
    print("-----")
    print("-----")
    print("-----")
    print("-----")
    print("-----")
    print("-----")
    print("Oh no.....(!) Some person has been captured by",Steve)
    print("Seeing as you are meant to be a hero, you should probably go vanquish",Steve)
    Wait5()
    print("Well.... Go on!")
    Wait5()
    print("Oh right, you probably want to see something.... ")
    Wait2()
    
Tile1 = helper.Tile("     1     ", "  >TRACK<  ", "  >>YOU<<  ")
Tile2 = helper.Tile("     2     ", "  >  ?  <  ", "    ---    ")
Tile3 = helper.Tile("     3     ", "  >  ?  <  ", "    ---    ")
Tile4 = helper.Tile("     4     ", "  >  ?  <  ", "    ---    ")
Tile5 = helper.Tile("     5     ",  "  >  ?  <  ", "    ---    ")

Tile6 = helper.Tile("     6     ", "  >  ?  <  ", "    ---    ")
Tile7 = helper.Tile("     7     ", "  >  ?  <  ", "    ---    ")
Tile8 = helper.Tile("     8     ", "  >  ?  <  ", "    ---    ")
Tile9 = helper.Tile("     9     ", "  >  ?  <  ", "    ---    ")
Tile10 = helper.Tile("    1 0    ", "  >  ?  <  ", "    ---    ")

Tile11 = helper.Tile("    1 1    ", "  >     <  ", "    ---    ")
Tile12 = helper.Tile("    1 2    ", "  >     <  ", "    ---    ")
Tile13 = helper.Tile("    1 3    ", "  >     <  ", "    ---    ")
Tile14 = helper.Tile("    1 4    ", "  >     <  ", "    ---    ")
Tile15 = helper.Tile("    1 5    ", "  >     <  ", "    ---    ")

Tile16 = helper.Tile("    1 6    ", "  >     <  ", "    ---    ")
Tile17 = helper.Tile("    1 7    ", "  >     <  ", "    ---    ")
Tile18 = helper.Tile("    1 8    ", "  >     <  ", "    ---    ")
Tile19 = helper.Tile("    1 9    ", "  >     <  ", "    ---    ")
Tile20 = helper.Tile("    2 0    ", "  >     <  ", "    ---    ")

Tile21 = helper.Tile("    2 1    ", "  >     <  ", "    ---    ")
Tile22 = helper.Tile("    2 2    ", "  >     <  ", "    ---    ")
Tile23 = helper.Tile("    2 3    ", "  >     <  ", "    ---    ")
Tile24 = helper.Tile("    2 4    ", "  >     <  ", "    ---    ")
Tile25 = helper.Tile("    2 5    ", "  >     <  ", "    ---    ")

Grid = [Tile1, Tile2, Tile3, Tile4, Tile5, Tile6, Tile7, Tile8, Tile9, Tile10, Tile11, Tile12, Tile13, Tile14, Tile15, Tile16, Tile17, Tile18, Tile19, Tile20, Tile21, Tile22, Tile23, Tile24, Tile25]


def printGrid():
    i=0
    while i<25:
        print("-------------------------------------------------------------")
        print(Grid[i].getLn1() + Grid[i+1].getLn1() + Grid[i+2].getLn1() + Grid[i+3].getLn1() + Grid[i+4].getLn1() + "|")
        print( )
        print(Grid[i].getLn2() + Grid[i+1].getLn2() + Grid[i+2].getLn2() + Grid[i+3].getLn2() + Grid[i+4].getLn2() + "|")
        print( )
        print(Grid[i].getLn3() + Grid[i+1].getLn3() + Grid[i+2].getLn3() + Grid[i+3].getLn3() + Grid[i+4].getLn3() + "|")
        i=i+5
    print("-------------------------------------------------------------")


Grid[0].discovered = 1
Grid[0].amIHere = 1


if not testMode == 1:
    OpenSpeech()
else:
    sName="TestMode"
printGrid()
yourLocation = 0
Action(yourLocation)

#notDead="True"
#while notDead=="True":
#    if yourLocation=="1":
#        
#    if not yourLocation== "1":
#        print("Idk what to type")







        






















