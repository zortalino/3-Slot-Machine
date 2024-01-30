#Slot Machine
#Initialize
import random
slotsymbols = ["☀", "☁", "☂", "7"]
global credit 
credit = 100

#Fuctions
#Runs the program again
def runagain():
    again = input("Spin the slots? (S/Q): ")
    if(again=="s" or again=="S"):
        spinslots()
    elif(again=="q" or again=="Q"):
        print("You ended up with " + str(credit) + " credits! See you next time")
        quit()
    else:
        print("Please type 'S' or 'Q'")
        runagain()
#Asks the user to imput the value they would like their potential winning to be multiplied by
def betsystem():
    global bet
    bet = int(input("Do you want to place a bet to multiply your score? Select"+"\033[31m"+" 1, 2, or 3: "+"\033[37m"))
    if(bet==1 or bet==2 or bet==3):
        print("Your next spin will either be multiplied or divided by your bet of "+ str(bet))
        return bet
    else:
        print("Please type in 1, 2, or 3")
        runagain()
#Registers a user's input, then spits out 3 random symbols. If the symbols match user wins 50 credits
#If user matches a 7, they win 100. and if there is no match 3, the user loses their inital (credit-10)/bet
#User can not play if they have credits=<0. Winning with 7s has a lower possiblity
def spinslots():
    global credit
    if(user=="S"and credit>=10 or user=="s" and credit>=10):
        betsystem()
        x= random.choices(slotsymbols, weights=[50,50,50,10],k=3)
        slot1=x[0]
        slot2=x[1]
        slot3=x[2]
        print( "\033[31m"+" [ "+"\033[31m" +slot1+" ]  " +"[ "+slot2+" ]  "+ "[ "+slot3+" ]  "+ "\033[37m")
        if(slot1=="☀" and slot2=="☀" and slot3=="☀"):
            credit = ((credit-10)+50)*bet
            print("Congradulations, you won "+"\033[31m"+"50"+"\033[37m"+"credits")
        elif(slot1=="☁" and slot2=="☁" and slot3=="☁"):
            credit = ((credit-10)+50)*bet
            print("Congradulations, you won "+"\033[31m"+"50"+"\033[37m"+"credits")
        elif(slot1=="☂" and slot2=="☂" and slot3=="☂"):
            credit = ((credit-10)+50)*bet
            print("Congradulations, you won "+"\033[31m"+"50"+"\033[37m"+"credits")
        elif(slot1=="7" and slot2=="7" and slot3=="7"):
            credit = ((credit-10)+100)*bet
            print("Jackpot! You won "+"\033[31m"+"100 "+"\033[37m"+"credits!")
        else:
            credit= (credit-10)/bet
            print("Aww, you lost. Better luck next time!")
        print("You have " + "\033[31m"+str(credit)+"\033[37m" + " credits")
        runagain()
    elif(user=="q" or user=="Q"):
        print("You ended up with " + "\033[31m"+ str(credit) + "\033[37m"+ " credits! See you next time")
        quit()
    else:
        print("Sorry you don't have enough credits! Come back when you have some!")
        quit()
#Combines all the previous functions into a fully functioning slot game
def final_slotmachine():
    global user
    print("======== Welcome to the 3-slot Machine ========")
    print("\033[31m"+"[☀]"+"\033[37m"+ "\033[31m"+"[☁]"+"\033[37m"+ "\033[31m"+"[☂]"+"\033[37m"+"\033[31m"+"[7]"+"\033[37m")
    print("You have "+"\033[31m" + str(credit) +"\033[37m"+ " credits")
    user = input("Press S to spin, Press Q to Quit ")
    spinslots()
#Main
final_slotmachine()