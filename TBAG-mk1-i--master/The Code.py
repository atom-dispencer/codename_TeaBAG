from random import randint
import time
#import helper

class Tile:
    def __init__(self, thisFound, whatsThis, yoAreHere):
        self.thisFound = thisFound
        self.whatsThis = whatsThis
        self.yoAreHere = yoAreHere
    def __str__(self):
        return self.thisFound


Steve = ("The Evil Wizard Steve (O' hear His name and tremble)")
WestVirginia = ("Almost heaven, West Virginia // Blue Ridge Mountains, Shenandoah River // Life is old there, older than the trees // Younger than the mountains, blowing like a breeze // Country roads, take me home // To the place I belong")
notDead = ("True")
yourLocation = ("1")

def Move():
    if What2Do=="N":
        yourLocation = yourLocation - 5
    if What2Do=="S":
        yourLocation = yourLocation + 5
    if What2Do=="E":
        yourLocation = yourLocation + 5
    if What2Do=="W":
        if yourLocation=="1":
            print(WestVirginia)
        yourLocation = yourLocation - 1
    else:
        print("No! You fools!")
        
def Move():
    if What2Do=="N":
        print("You moved North!")
    elif What2Do=="S":
        print("You moved South!")
    elif What2Do=="E":
        print("You moved East!")
    elif What2Do=="W":
        print("You moved West!!")
    elif What2Do=="xxxx":
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
def Grid():
    print(" --------- --------- --------- --------- --------- ")
    print("|",(thisFound1),"|",(thisFound2),"|",(thisFound3),"|",(thisFound4),"|",(thisFound5),"|")
    print("|",(whatsThis1),"|",(whatsThis2),"|",(whatsThis3),"|",(whatsThis4),"|",(whatsThis5),"|")
    print("|",(yoAreHere1),"|",(yoAreHere2),"|",(yoAreHere3),"|",(yoAreHere4),"|",(yoAreHere5),"|")
    print(" --------- --------- --------- --------- --------- ")
    print("|",(thisFound6),"|",(thisFound7),"|",(thisFound8),"|",(thisFound9),"|",(thisFound10),"|")
    print("|",(whatsThis6),"|",(whatsThis7),"|",(whatsThis8),"|",(whatsThis9),"|",(whatsThis10),"|")
    print("|",(yoAreHere6),"|",(yoAreHere7),"|",(yoAreHere8),"|",(yoAreHere9),"|",(yoAreHere10),"|")
    print(" --------- --------- --------- --------- --------- ")
    print("|",(thisFound11),"|",(thisFound12),"|",(thisFound13),"|",(thisFound14),"|",(thisFound15),"|")
    print("|",(whatsThis11),"|",(whatsThis12),"|",(whatsThis13),"|",(whatsThis14),"|",(whatsThis15),"|")
    print("|",(yoAreHere11),"|",(yoAreHere12),"|",(yoAreHere13),"|",(yoAreHere14),"|",(yoAreHere15),"|")
    print(" --------- --------- --------- --------- --------- ")
    print("|",(thisFound16),"|",(thisFound17),"|",(thisFound18),"|",(thisFound19),"|",(thisFound20),"|")
    print("|",(whatsThis16),"|",(whatsThis17),"|",(whatsThis18),"|",(whatsThis19),"|",(whatsThis20),"|")
    print("|",(yoAreHere16),"|",(yoAreHere17),"|",(yoAreHere18),"|",(yoAreHere19),"|",(yoAreHere20),"|")
    print(" --------- --------- --------- --------- --------- ")
    print("|",(thisFound21),"|",(thisFound22),"|",(thisFound23),"|",(thisFound24),"|",(thisFound25),"|")
    print("|",(whatsThis21),"|",(whatsThis22),"|",(whatsThis23),"|",(whatsThis24),"|",(whatsThis25),"|")
    print("|",(yoAreHere21),"|",(yoAreHere22),"|",(yoAreHere23),"|",(yoAreHere24),"|",(yoAreHere25),"|")
    print(" --------- --------- --------- --------- --------- ")

Tile1 = Tile("   1   ", ">TRACK<", ">>YOU<<")

thisFound2 = "  ???  "
whatsThis2 = "  ???  "
yoAreHere2 = "   -   "

thisFound3 = "  ???  "
whatsThis3 = "  ???  "
yoAreHere3 = "   -   "

thisFound4 = "  ???  "
whatsThis4 = "  ???  "
yoAreHere4 = "   -   "

thisFound5 = "  ???  "
whatsThis5 = "  ???  "
yoAreHere5 = "   -   "

thisFound6 = "  ???  "
whatsThis6 = "  ???  "
yoAreHere6 = "   -   "

thisFound7 = "  ???  "
whatsThis7 = "  ???  "
yoAreHere7 = "   -   "

thisFound8 = "  ???  "
whatsThis8 = "  ???  "
yoAreHere8 = "   -   "

thisFound9 = "  ???  "
whatsThis9 = "  ???  "
yoAreHere9 = "   -   "

thisFound10 = "  ???  "
whatsThis10 = "  ???  "
yoAreHere10 = "   -   "

thisFound11 = "  ???  "
whatsThis11 = "  ???  "
yoAreHere11 = "   -   "

thisFound12 = "  ???  "
whatsThis12 = "  ???  "
yoAreHere12 = "   -   "

thisFound13 = "  ???  "
whatsThis13 = "  ???  "
yoAreHere13 = "   -   "

thisFound14 = "  ???  "
whatsThis14 = "  ???  "
yoAreHere14 = "   -   "

thisFound15 = "  ???  "
whatsThis15 = "  ???  "
yoAreHere15 = "   -   "

thisFound16 = "  ???  "
whatsThis16 = "  ???  "
yoAreHere16 = "   -   "

thisFound17 = "  ???  "
whatsThis17 = "  ???  "
yoAreHere17 = "   -   "

thisFound18 = "  ???  "
whatsThis18 = "  ???  "
yoAreHere18 = "   -   "

thisFound19 = "  ???  "
whatsThis19 = "  ???  "
yoAreHere19 = "   -   "

thisFound20 = "  ???  "
whatsThis20 = "  ???  "
yoAreHere20 = "   -   "

thisFound21 = "  ???  "
whatsThis21 = "  ???  "
yoAreHere21 = "   -   "

thisFound22 = "  ???  "
whatsThis22 = "  ???  "
yoAreHere22 = "   -   "

thisFound23 = "  ???  "
whatsThis23 = "  ???  "
yoAreHere23 = "   -   "

thisFound24 = "  ???  "
whatsThis24 = "  ???  "
yoAreHere24 = "   -   "

thisFound25 = "  ???  "
whatsThis25 = "  ???  "
yoAreHere25 = "   -   "

sGotKey = 0
KeySquare = randint(1,25)
#print(KeySquare)



Wait2()
print("Welcome to the Forgotten Lands!")
Wait2()
print(Tile1)
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
Grid()








notDead=="True"
while notDead=="True":
    if yourLocation=="1":
        thisFound1 = "   1   "
        whatsThis1 = ">TRACK<"
        yoAreHere1 = ">>YOU<<"
    if not yourLocation== "1":
        print("Idk what to type")







        






















