import time
import tileHelp
def history():
    print("This is history")
def Wait1():
    time.sleep(1)
def Wait2():
    time.sleep(2)
def Wait3():
    time.sleep(3)
def Wait5():
    time.sleep(5)
def OpenSpeech(Steve):
    Wait2()
    print("Welcome to the Forgotten Lands!")
    Wait2()
    sName=input("What do they call you adventurer?\n>>>")
    if sName == "Eddles the Con":
        print("Oh no! Not Eddles the Con! :0")
    print("Interesting...")
    Wait2()
    print("Greetings,",sName,", and welcome to the Forgotten Lands!")
    Wait5()
    historyLesson = input("Do you wish to know more about the Forgotten Lands? (Y/N)\n>>>")
    if historyLesson == "Y":
        print("Now a brief history!")
        history()
    else:
        print("Ok! Let's go! But remember, if you want to see the history later, just type HISTORY_LESSON.")
    Wait5()
    print("Now, onwards to adventure!")
    Wait2()
    return sName

def printGrid(Grid):
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

def buildGrid():
    Tile1 = tileHelp.Tile("     1     ", "  >TRACK<  ", "  >>YOU<<  ", "You are standing on a dirt path that continues South, to unknown lands, and East, towards far off woods and crumbling buildings...")
    Tile2 = tileHelp.Tile("     2     ", "  >RUINS<  ", "  >>YOU<<  ", "HAYO")
    Tile3 = tileHelp.Tile("     3     ", "  >WOODS<  ", "  >>YOU<<  ", "HAYO")
    Tile4 = tileHelp.Tile("     4     ", "  >FIELD<  ", "  >>YOU<<  ", "HAYO")
    Tile5 = tileHelp.Tile("     5     ", "  >FIELD<  ", "  >>YOU<<  ", "HAYO")

    Tile6 = tileHelp.Tile("     6     ", "  >TRACK<  ", "  >>YOU<<  ", "HAYO")
    Tile7 = tileHelp.Tile("     7     ", "  >SWAMP<  ", "  >>YOU<<  ", "HAYO")
    Tile8 = tileHelp.Tile("     8     ", "  >FIELD<  ", "  >>YOU<<  ", "HAYO")
    Tile9 = tileHelp.Tile("     9     ", "  >FIELD<  ", "  >>YOU<<  ", "HAYO")
    Tile10 = tileHelp.Tile("    1 0    ", " >VILLAGE< ", "  >>YOU<<  ", "HAYO")

    Tile11 = tileHelp.Tile("    1 1    ", "  >HILLS<  ", "  >>YOU<<  ", "HAYO")
    Tile12 = tileHelp.Tile("    1 2    ", "  >WOODS<  ", "  >>YOU<<  ", "HAYO")
    Tile13 = tileHelp.Tile("    1 3    ", "  >SWAMP<  ", "  >>YOU<<  ", "HAYO")
    Tile14 = tileHelp.Tile("    1 4    ", "  >SWAMP<  ", "  >>YOU<<  ", "HAYO")
    Tile15 = tileHelp.Tile("    1 5    ", "  >TRACK<  ", "  >>YOU<<  ", "HAYO")

    Tile16 = tileHelp.Tile("    1 6    ", "  >HILLS<  ", "  >>YOU<<  ", "HAYO")
    Tile17 = tileHelp.Tile("    1 7    ", "  >SWAMP<  ", "  >>YOU<<  ", "HAYO")
    Tile18 = tileHelp.Tile("    1 8    ", "  >SWAMP<  ", "  >>YOU<<  ", "HAYO")
    Tile19 = tileHelp.Tile("    1 9    ", " >CITADEL< ", "  >>YOU<<  ", "HAYO")
    Tile20 = tileHelp.Tile("    2 0    ", "  >TRACK<  ", "  >>YOU<<  ", "HAYO")

    Tile21 = tileHelp.Tile("    2 1    ", " >VOLCANO< ", "  >>YOU<<  ", "HAYO")
    Tile22 = tileHelp.Tile("    2 2    ", "  >HILLS<  ", "  >>YOU<<  ", "HAYO")
    Tile23 = tileHelp.Tile("    2 3    ", "  >HILLS<  ", "  >>YOU<<  ", "HAYO")
    Tile24 = tileHelp.Tile("    2 4    ", "  >TRACK<  ", "  >>YOU<<  ", "HAYO")
    Tile25 = tileHelp.Tile("    2 5    ", "  >CLIFF<  ", "  >>YOU<<  ", "HAYO")

    Grid = [Tile1, Tile2, Tile3, Tile4, Tile5, Tile6, Tile7, Tile8, Tile9, Tile10, Tile11, Tile12, Tile13, Tile14, Tile15, Tile16, Tile17, Tile18, Tile19, Tile20, Tile21, Tile22, Tile23, Tile24, Tile25]
    return Grid
