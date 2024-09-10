# <Chloe Atwood>             <02/26/2024>
# <Assignment 3>
# <A fun game of NimGrab that gives you the option to play against a real person or the computer. It also gives you the option to read the instructions, play again, and quit>

import random 


#Title information function
def printTitleMaterial():
    """Prints the title material for the game, including the student's name, class, and section number."""
    print("NIMGRAB!")
    print()

    print("By: <Chloe Atwood>")
    print("[COM S 127 <A>]")
    print()

#Function displaying the instructions and rules to the game
def instructions():
    print("                  RULES OF NIMGRAB!!!!!!!!")
    print("____________________________________________________________\n")
    print("Objective: \nAvoid being the player who takes the last item \n")
    print("How to play: \nA random number of items are placed in a pile. \nPlayers take turns removing the items from the pile. \n")
    print("The youngest or human player takes the first turn. They alternate turns until all the items are gone. \n")
    print("Items:\nYou must only take between 1-3 items each turn. \nTaking more than that will result in an error. \n Players cannot take more items than are currently in the pile.\n")
    print("Ending:\nThe game ends when their are no more objects.\nThe player who takes the last item looses. The other player is the winner\n")

#Function determining how many players their will be
def howPlay():
    howPlay = input("How would you like to play? 1-player (human vs computer) or 2-player (human vs human):")
    return howPlay

#Function for a game between a human and the computer
def onePlayer():
    amount = random.randint(10, 25)
    turn = 0
    x = True
    while x == True:
        if turn%2 == 0:
            if amount == 0 or amount < 0:
                print("GAME OVER!", end="")
                print("YOU ARE THE WINNER!!!!")
                x = False
            else:
                w = True
                while w == True:
                    if amount == 1:
                        steal = int(input("Their is {a} item left.\nHow many items would you like to grab (1-3):" .format(a = amount)))
                    else:
                        steal = int(input("Their are {a} items left.\nHow many items would you like to grab (1-3):" .format(a = amount)))
                    if steal == 1:
                        amount = amount - 1
                        turn = turn + 1
                        w = False
                    elif steal == 2:
                        amount = amount - 2
                        turn = turn + 1
                        w = False
                    elif steal == 3:
                        amount = amount - 3
                        turn = turn + 1
                        w = False
                    else:
                        print("Invalid Input.", end="") 
                        print("Please try again by picking a number from 1-3.")
        elif turn%2 != 0:
            if amount == 0 or amount < 0:
                print("GAME OVER!", end="")
                print("THE COMPUTER WON!!!!")
                x = False
            elif amount == 2:
                amount = amount - 1
                print("The computer took 1 item.")
                turn = turn + 1
            elif amount == 3:
                amount == amount - 2
                print("The computer took 2 items.")
                turn = turn + 1
            else: 
                num = random.randint(1, 3)
                if num == 1:
                    amount = amount - num
                    print("The computer took {a} item." .format(a = num))
                    turn = turn + 1
                else:
                    amount = amount - num
                    print("The computer took {a} items." .format(a = num))
                    turn = turn + 1
                
#Function for a game between two humans
def twoPlayers():
    amount = random.randint(10, 25)
    turn = 0
    x = True
    while x == True:
        if turn%2 == 0:
            if amount == 0 or amount < 0:
                print("GAME OVER!", end="")
                print("PLAYER ONE WINS!!!!")
                x = False
            else:
                w = True
                while w == True:
                    if amount == 1:
                        steal = int(input("Player one:\n\nTheir is {a} item left.\nHow many items would you like to grab (1-3):" .format(a = amount)))
                    else:
                        steal = int(input("Player One:\n\nTheir are {a} items left.\nHow many items would you like to grab (1-3):" .format(a = amount)))
                    if steal == 1:
                        amount = amount - 1
                        turn = turn + 1
                        w = False
                    elif steal == 2:
                        amount = amount - 2
                        turn = turn + 1
                        w = False
                    elif steal == 3:
                        amount = amount - 3
                        turn = turn + 1
                        w = False
                    else:
                        print("Invalid Input.", end="") 
                        print("Please try again by picking a number from 1-3.")
        elif turn%2 != 0:
            if amount == 0 or amount < 0:
                print("GAME OVER!", end="")
                print("PLAYER TWO WINS!!!!")
                x = False
            else:
                w = True
                while w == True:
                    if amount == 1:
                        steal = int(input("Player Two:\n\nTheir is {a} item left.\nHow many items would you like to grab (1-3):" .format(a = amount)))
                    else:
                        steal = int(input("Player Two:\n\nTheir are {a} items left.\nHow many items would you like to grab (1-3):" .format(a = amount)))
                    if steal == 1:
                        amount = amount - 1
                        turn = turn + 1
                        w = False
                    elif steal == 2:
                        amount = amount - 2
                        turn = turn + 1
                        w = False
                    elif steal == 3:
                        amount = amount - 3
                        turn = turn + 1
                        w = False
                    else:
                        print("Invalid Input.", end="") 
                        print("Please try again by picking a number from 1-3.")


#Main function
def main():

    #Title Function
    printTitleMaterial()

    r = True
    while r == True:
        #Asking for choice
        choice = str(input("What would you like to do?(p)lay, view (r)ules, or (q)uit the game:"))
        #What choice does what
        if choice == 'r':
            #Instructions function
            instructions()
        elif choice == 'q':
            print("Thanks for playing!!!!")
            r = False
        elif choice == 'p':
            f = True
            while f == True:
                #How many players
                players = howPlay()
                if players == '1':
                    #One player
                    onePlayer()
                    f = False
                elif players == '2':
                    #Two players
                    twoPlayers()
                    f = False
                else:
                    print("Invalid Input.", end="") 
                    print("Please try again and enter 1 or 2.")
        else:
            print("Invalid Input.", end="")
            print("Please enter either p, r, or q")



if __name__ == "__main__":
    main()