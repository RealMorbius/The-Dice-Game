#Elijah Bingham Elijah Bingham
# Dice Game Dice Game
# 10/10 10/10
#I dont want to anymore i dont want to anymore
#And yes i didnt copy this 
#And yes i used a lot of forums to make this 
#and i read the documentation lol
#       .-------.    ______
#      /   o   /|   /\     \
#    /_______/o|  /o \  o  \
#    | o     | | /   o\_____\
#    |   o   |o/ \o   /o    /
#    |     o |/   \ o/  o  /
#    '-------'     \/____o/
#Credit to Joan G. Stark For Dice ascii Art
#https://www.asciiart.eu/miscellaneous/dice
import random
import os
import math
import time #THE GREATEST KILLER
#Function To handle rolling of dice 
#BTW you can costomize textures for the dice
def StringCheck(StringToCheck):
    if StringToCheck.isdigit():
        return True
    else:
        return False
        
                
def DiceRoll(Result,CurrentMoney,bet):
    print("[*]Eveldun's Dice https://www.onlinegdb.com/s/as/solve/110087?snippet_type=&readonly=&preview=#editor_4Game! > ")
    print("[*]Your Current Cash Amount is: ",CurrentMoney,"$ > ")
    #Time X is the time multiplier for when the dice rolls
    #making the end result more intense im basically 
    #making this a slot machine
    
    timeX = 0.1
    #Dice Is predetermined but will be animated anyway
    for x in range(random.randint(5,11)):
            print("[*]Eveldun's Dice Game! > ")
            print("[*]Your Current Cash Amount is: ",CurrentMoney,"$ > ")
            xer = open(str(random.randint(1,6)),"r")
            print(xer.read())
            time.sleep(timeX)
            timeX = timeX + 0.05
            xer.close()                                                            
            os.system("cls||clear")
    xe = open(str(Result),"r")
    print(xe.read())
    print("[!]You Rolled a:",Result," > ")
    time.sleep(1)
    if Result == 2:
        
        print("[!]WINNER YOU ROLLED A DOUBLE! > ")
        print("You Have earned",bet *2," > ")
        time.sleep(4)
        return bet *2
    elif Result == 3:
        print("[!]Tie no earnings > ")
        time.sleep(4)
        return 0
    else:
        print("[!]Oh no you lost",bet,"Better luck next time > ")
        time.sleep(4)
        return bet * -1



#Littearly me depressed do not decode This
#its scary
#And know im no longer depressed
print("MDEwMDExMTEgMDExMDExMTAgMDAxMDAwMDAgMDExMDEwMTAgMDExMDAwMDEgMDExMDExMTAgMDExMTAxMDEgMDExMDAwMDEgMDExMTAwMTAgMDExMTEwMDEgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTAwMDAgMDExMTAxMDAgMDExMDEwMDAgMDAxMDAwMDAgMDAxMTAwMTAgMDAxMTAwMDAgMDAxMTAwMTAgMDAxMTAwMTAgMDAxMDAwMDAgMDExMDEwMDEgMDAxMDAwMDAgMDExMTAxMTEgMDExMDEwMDEgMDExMDExMDAgMDExMDExMDAgMDAxMDAwMDAgMDExMDEwMTEgMDExMDEwMDEgMDExMDExMDAgMDExMDExMDAgMDAxMDAwMDAgMDExMDExMDEgMDExMTEwMDEgMDExMTAwMTEgMDExMDAxMDEgMDExMDExMDAgMDExMDAxMTAgMDAxMDAwMDAgMDExMDEwMDEgMDAxMDAwMDAgMDExMDEwMDAgMDExMDAwMDEgMDExMTAxMTAgMDExMDAxMDEgMDAxMDAwMDAgMDExMDAxMDAgMDExMDExMTEgMDExMDExMTAgMDExMDAxMDEgMDAxMDAwMDAgMDExMTAxMDAgMDExMDEwMDAgMDExMDEwMDEgMDExMDExMTAgMDExMDAxMTEgMDExMTAwMTEgMDAxMDAwMDAgMDExMDEwMDEgMDAxMDAwMDAgMDExMDAwMTEgMDExMDAwMDEgMDExMDExMTAgMDAxMDAwMDAgMDExMDExMTAgMDExMDExMTEgMDExMTAxMDAgMDAxMDAwMDAgMDExMDAwMTAgMDExMDAxMDEgMDAxMDAwMDAgMDExMDAxMTAgMDExMDExMTEgMDExMTAwMTAgMDExMDAxMTEgMDExMDEwMDEgMDExMTAxMTAgMDExMDAxMDEgMDExMDExMTAgMDAxMDAwMDAgMDExMDAxMTAgMDExMDExMTEgMDExMTAwMTAgMDAxMDAwMDAgMDExMDAxMTEgMDExMDExMTEgMDExMDExMTEgMDExMDAxMDAgMDExMDAwMTAgMDExMTEwMDEgMDExMDAxMDEgMDAxMDAwMDAgMDExMDAxMDEgMDExMTAxMTAgMDExMDAxMDEgMDExMTAwMTAgMDExMTEwMDEgMDExMDExMTEgMDExMDExMTAgMDExMDAxMDEgMDAxMDExMTAgMDAxMDAwMDAgMDEwMDEwMDEgMDExMDExMDEgMDAxMDAwMDAgMDExMTAwMTEgMDExMDExMTEgMDExMTAwMTAgMDExMTAwMTAgMDExMTEwMDEgMDAxMDAwMDAgMDExMDEwMTAgMDExMDAwMDEgMDExMTEwMDEgMDExMDAxMDAgMDExMDAxMDEgMDExMDExMTAgMDAxMDAwMDAgMDExMDExMDEgMDExMTEwMDEgMDAxMDAwMDAgMDExMDExMTAgMDExMDAwMDEgMDExMDExMDEgMDExMDAxMDEgMDAxMDAwMDAgMDExMTAwMTEgMDExMDEwMDAgMDExMDAwMDEgMDExMDExMDAgMDExMDExMDAgMDAxMDAwMDAgMDExMDAxMTAgMDExMDExMTEgMDExMTAwMTAgMDExMDAxMDEgMDExMTAxMTAgMDExMDAxMDEgMDExMTAwMTAgMDAxMDAwMDAgMDExMDAwMTAgMDExMDAxMDEgMDAxMDAwMDAgMDExMTAxMDAgMDExMTAwMTAgMDExMDAwMDEgMDExMTAwMTEgMDExMDEwMDAgMDExMDAxMDEgMDExMDAxMDAgMDAxMDAwMDAgMDExMDEwMDEgMDExMDExMTAgMDAxMDAwMDAgMDExMTAxMDAgMDExMTEwMDEgMDExMTAwMTAgMDExMDAwMDEgMDExMDExMTAgMDExMDExMTAgMDExMTEwMDEgMDAxMDExMTAgMDAxMDAwMDAgMDEwMDEwMDEgMDAxMDAwMDAgMDExMDAxMDAgMDExMDAxMDEgMDExMTAwMTEgMDExMDAxMDEgMDExMTAwMTAgMDExMTAxMTAgMDExMDAxMDEgMDAxMDAwMDAgMDExMTAxMDAgMDExMDExMTEgMDAxMDAwMDAgMDExMDAxMDAgMDExMDEwMDEgMDExMDAxMDEgMDAxMDExMTAgMDAxMDAwMDAgMDEwMDEwMDEgMDAxMDAxMTEgMDExMDExMDEgMDAxMDAwMDAgMDExMTAwMTEgMDExMDExMTEgMDExMTAwMTAgMDExMTAwMTAgMDExMTEwMDEgMDAxMDAwMDAgMDEwMDExMDEgMDExMTAwMTAgMDAxMDAwMDAgMDEwMTAwMTEgMDExMDExMDEgMDExMDEwMDEgMDExMTAxMDAgMDExMDEwMDAgMDAxMDAwMDAgMDExMTAxMDAgMDExMDEwMDAgMDExMDAwMDEgMDExMTAxMDAgMDAxMDAwMDAgMDEwMDEwMDEgMDAxMDAwMDAgMDExMDAwMTEgMDExMDExMTEgMDExMTAxMDEgMDExMDExMDAgMDExMDAxMDAgMDAxMDAwMDAgMDExMDExMTAgMDExMDExMTEgMDExMTAxMDAgMDAxMDAwMDAgMDExMDAwMTAgMDExMDAxMDEgMDAxMDAwMDAgMDExMDAwMDEgMDAxMDAwMDAgMDExMDAxMTEgMDExMDExMTEgMDExMDExMTEgMDExMDAxMDAgMDAxMDAwMDAgMDExMDAxMDEgMDExMDExMTAgMDExMDExMTEgMDExMTAxMDEgMDExMDAxMTEgMDExMDEwMDAgMDAxMDAwMDAgMDExMTAwMTEgMDExMTAxMDAgMDExMTAxMDEgMDExMDAxMDAgMDExMDAxMDEgMDExMDExMTAgMDExMTAxMDAgMDAxMDExMTAgMDEwMTAwMDAgMDExMDExMDAgMDExMDAxMDEgMDExMDAwMDEgMDExMTAwMTEgMDExMDAxMDEgMDAxMDAwMDAgMDExMDAxMTAgMDExMDExMTEgMDExMTAwMTAgMDExMDAxMTEgMDExMDEwMDEgMDExMTAxMTAgMDExMDAxMDEgMDAxMDAwMDAgMDExMDExMDEgMDExMDAxMDEgMDAxMDExMTAgMDAwMDEwMTAgMDAwMDEwMTAgMDAwMDEwMDEgMDEwMTAxMDAgMDExMDEwMDAgMDExMDAxMDEgMDAxMDAwMDAgMDExMTAwMTAgMDExMDAxMDEgMDExMDAwMDEgMDExMTAwMTEgMDExMDExMTEgMDExMDExMTAgMDAxMDAwMDAgMDExMDEwMDEgMDExMDExMDEgMDAxMDAwMDAgMDExMDAwMTEgMDExMDExMTEgMDExMDExMDEgMDExMDExMDEgMDExMDEwMDEgMDExMTAxMDAgMDExMTAxMDAgMDExMDEwMDEgMDExMDExMTAgMDExMDAxMTEgMDAxMDAwMDAgMDExMTAwMTEgMDExMTAxMDEgMDExMDEwMDEgMDExMDAwMTEgMDExMDEwMDEgMDExMDAxMDAgMDExMDAxMDEgMDAxMDAwMDAgMDExMDEwMDEgMDExMTAwMTEgMDAxMDAwMDAgMDExMDAwMTAgMDExMDAxMDEgMDExMDAwMTEgMDExMDAwMDEgMDExMTAxMDEgMDExMTAwMTEgMDExMDAxMDEgMDAxMDAwMDAgMDExMDEwMDEgMDExMTAxMTAgMDExMDAxMDEgMDAxMDAwMDAgMDExMDAxMDAgMDExMDAxMDEgMDExMTAxMTAgMDExMDExMTEgMDExMTAxMDAgMDExMDAxMDEgMDExMDAxMDAgMDAxMDAwMDAgMDExMDExMDEgMDExMTEwMDEgMDAxMDAwMDAgMDExMTAxMTEgMDExMDEwMDAgMDExMDExMTEgMDExMDExMDAgMDExMDAxMDEgMDAxMDAwMDAgMDExMDExMDAgMDExMDEwMDEgMDExMDAxMTAgMDExMDAxMDEgMDAxMDAwMDAgMDExMTAxMDAgMDExMDExMTEgMDAxMDAwMDAgMDExMDEwMDEgMDExMDExMDEgMDExMTAwMDAgMDExMTAwMTAgMDExMDExMTEgMDExMTAxMTAgMDExMDAxMDEgMDExMDExMDEgMDExMDAxMDEgMDExMDExMTAgMDExMTAxMDAgMDAxMDExMTAgMDAwMDEwMTAgMDEwMDEwMDEgMDAxMDAwMDAgMDExMTAwMTEgMDExMTAxMDAgMDExMDAwMDEgMDExMTAwMTAgMDExMTAxMDAgMDExMDAxMDEgMDExMDAxMDAgMDAxMDAwMDAgMDExMDAwMTEgMDExMDAwMDEgMDExMDExMDAgMDExMDExMDAgMDExMDEwMDEgMDExMDExMTAgMDExMDAxMTEgMDAxMDAwMDAgMDExMDAxMTAgMDExMDExMTEgMDExMTAwMTAgMDAxMDAwMDAgMDExMDEwMDAgMDExMDAxMDEgMDExMDExMDAgMDExMTAwMDAgMDAxMDAwMDAgMDExMDAwMTAgMDExMTAxMDEgMDExMTAxMDAgMDAxMDAwMDAgMDExMDExMTAgMDExMDExMTEgMDExMDAwMTAgMDExMDExMTEgMDExMDAxMDAgMDExMTEwMDEgMDAxMDAwMDAgMDExMDAwMTEgMDExMDAwMDEgMDExMDExMDEgMDExMDAxMDEgMDAxMDExMTAgMDAwMDEwMTA=")
print("I cant do it")

os.system("clear||cls")
print("[S]BOOTING UP")
print("[OS]OS_TYPE:",os.name)
time.sleep(0.1)
print("[S]Verifying boot Integrity")
#Verifies if files named 1 2 3 4 5 6 exhist
for i in range(1,7):
    #Converts i to a string to call upon file names for a
    #Integrity Check
    #If This check fails the softwear will error
    argz = open(str(i),"r")
    time.sleep(0.5)
    print("[S]File:",i,"Has Been Verified.")

print("[S]All Files Have been verified!")

print("[*]WELCOME TO THE DICE GAME! > ")
print("[*]The Most Advanced Program in the class! > ")
print("[*]By the way we hope you a great day! > ")
#No We dont
SysCheck = True
while SysCheck == True:
    hecker = (input("[#]Please input starter money > "))
    if StringCheck(hecker) == False:
        print("[X]ERROR! Input is a string")
        time.sleep(3)
    else:
        SysCheck = False

HiddenSuffering = int(hecker)
print("[*]You Will START With >",HiddenSuffering,"$")
point = HiddenSuffering
Diceone = random.randint(1,6)
DiceTwo = random.randint(1,6)
#No Doubt This is a security vulnerable Position
#Program will stop once points is 0 forcing 
while(point > 0):
    Diceone = random.randint(1,6)
    DiceTwo = random.randint(1,6)
    os.system("clear||cls")
    print("[*]Eveldun's Dice Game! > ")
    print("[*]Your Current Cash Amount is: ",point,"$ > ")
    Suffer = (input("[#]Do you want to continue playing and bet > "))
    inputfilter = Suffer.strip()
    rapp = inputfilter.lower()
    if rapp == "yes":
        lock = True
        while lock == True:
            xz = (input("[#]How Much Do You Want to bet > "))
            if xz.isdigit() == False:
                print("[X]ERROR! Input is a string")
                time.sleep(3)
                os.system("cls||clear")
            else:
                lock = False
                x = int(xz)
            
        print("[*]Rolling Dice")
       
        
        
        
        if x > point:
            print("[X]ERROR NOT ENOUGH POINTS!")
            time.sleep(4)
            os.system("cls||clear")
        else:
            point = DiceRoll(Diceone,point,x) + point
    elif rapp == "no":
        print("[*]Okay You Won with > ", point,"$")
        time.sleep(5)
        quit()
    
    else: 
        print("[X]ERROR INPUT NOT RECOGNIZED! > ")
        time.sleep(1)
        os.system("cls||clear")
os.system("cls||clear")
print("[*]You are out of points > ")
print("[*]Thanks For playing > ")
time.sleep(5)

