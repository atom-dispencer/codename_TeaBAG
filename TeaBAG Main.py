#WARNING!!! TOGGLING TESTMODE ( 1 / 0 ) WILL HAVE A DRAMATIC EFFECT ON THE OUTPUT!!!
testMode = 1

allAvailableActions = ["N", "S", "E", "W", "?"]

import time
import tileHelp
import setupHelp

Steve = ("The Evil Wizard Steve (O' hear His name and tremble)")
WestVirginia = ("Almost Heaven, West Virginia // Blue Ridge Mountains, Shenandoah River // Life is old there, older than the trees // Younger than the mountains, blowing like a breeze // Country roads, take me home // To the place I belong")
notDead = ("True")
invalidEast = [4, 9, 14, 19, 24]
invalidWest = [5, 10, 15, 20]

def Reset():
    Grid[(yourLocation)].amIHere = 0
    
def setMeHere():
    L = yourLocation
    Grid[L].amIHere = 1
    Grid[L].discovered = 1

def TheEdge():
    edgeOfTheEarth = input("Continuing to walk off this cliff is a bad idea, you think. Do you want to continue? (Y / N)")
    if edgeOfTheEarth == "Y":
        print("Oh well... You say as you tumble to oblivion.")
        setupHelp.Wait3()
        exit()
    else:
        print("You step away and turn back towards land")
        setupHelp.Wait1()
        return yourLocation
    setupHelp.Wait2()

def Action(yourLocation):
    newLocation = 0
    haveAnAction = 0
    while haveAnAction < 1:
        what2Do=input("What wantest thy to doeth?")
#        print(yourLocation)
        if what2Do in allAvailableActions:
            Reset()
            if what2Do == 'N':
                if yourLocation < 5:
                    return TheEdge()
                newLocation = Move(what2Do, yourLocation)
#                print(newLocation)
                haveAnAction = 1
            elif what2Do == 'S':
                if yourLocation > 19:
                    return TheEdge()
                newLocation = Move(what2Do, yourLocation)
#                print(newLocation)
                haveAnAction = 1
            elif what2Do == 'E':
                if yourLocation in invalidEast:
                    return TheEdge()
                newLocation = Move(what2Do, yourLocation)
#                print(newLocation)
                haveAnAction = 1
            elif what2Do == 'W':
                if yourLocation in invalidWest:
                    return TheEdge()
                elif yourLocation == 0:
                    print("To the west, you see blue-tinted mountains and a sparkling river.... Too bad the killer laser bunnies are guarding the path... *sigh*")
                    setupHelp.Wait5()
                    print(WestVirginia)
                    time.sleep(10)
                    return yourLocation
                newLocation = Move(what2Do, yourLocation)
#                print(newLocation)
                haveAnAction = 1
            elif what2Do == '?':
                print("")
                print("Here are (most of) your options!")
                print(allAvailableActions)
                setupHelp.Wait3()
                print("")
        return newLocation

    
def Move(what2Do, yourLocation):
    newLocation = 0
#    print(yourLocation)
    if what2Do=="N":
        print("You moved North!")
        newLocation = yourLocation - 5
#        print(yourLocation)
    elif what2Do=="S":
        print("You moved South!")
        newLocation = yourLocation + 5
#        print(yourLocation)
    elif what2Do=="E":
        print("You moved East!")
        newLocation = yourLocation + 1
    elif what2Do=="W":
#        print(yourLocation)
        print("You moved West!!")
        newLocation = yourLocation - 1
#        print(yourLocation)
    elif what2Do=="xxxx":
        print("OTHER ACTIONS")
#    print("New location = ",newLocation)
    return newLocation



Grid = setupHelp.buildGrid()

if not testMode == 1:
    sName = setupHelp.OpenSpeech(Steve)
else:
    sName="TestMode"

yourLocation = 0


notDead="True"
while notDead=="True":
    
    Reset()
    setMeHere()
    
    setupHelp.printGrid(Grid)
    print(Grid[yourLocation].getDescription())
    yourLocation = Action(yourLocation)
    





        






















