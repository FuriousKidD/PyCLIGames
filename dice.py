#TW MANHEMA ~ FuRiouS_K1dD

#This program will ask a user if they want to roll a die, with two options available to them
#Choose Y to roll and N to not roll
#If user selects Y, then 2 random numbers are generated and user is prompted if they want to roll again or not
#If user selects N, game ends and returns user to the main menu
#User has the option to view the help section for instructions about the program

import os
import time
import sys

#default value for the number of die to be rolled 
num_die = 2
num_of_rolls = 0
#This method will be used for clearing the screen, creating an illusion of switching between screens
def clear_screen():
    if os.name == 'nt': #if windows operating system
        os.system('cls')
    else:
        os.system('clear') #if linux operating system


#Function for the menu screen
def menu_screen():
    
    play = False
    help_menu = False
    options_menu = False
    exit_prog = False

    while True:
        user_input = input("""
            ~~~~~~~~DICE~~~~~~~~~~
            PRESS 'P' TO PLAY
            PRESS 'H' TO VIEW INSTRUCTIONS
            PRESS 'O' TO VIEW OPTIONS
            PRESS 'E' TO EXIT GAME
        """)
            #print(user_input)
        if user_input.upper() == "P":
            clear_screen()
            print("...STARTING GAME...")
            time.sleep(2)
            clear_screen()
            play = True
            break    
        elif user_input.upper() == "H":
            clear_screen()
            help_menu = True
            break
        elif user_input.upper() == "O":
            clear_screen()
            options_menu = True
            break
        elif user_input.upper() == "E":
            print("GOODBYE!")
            time.sleep(2)
            clear_screen()
            exit_prog = True
            break
        else:
            print("INVALID INPUT!")
        
    if options_menu == True:
        options_screen()
    if play == True:
        play_die()
    if help_menu == True:
        help_screen()
    if exit_prog == True:
        sys.exit()

#Function that deals with the help screen
def help_screen():
    clear_screen()
    print("""To play the game, you have to choose to roll a dice, or not.
        \n To roll, you press 'Y' and a random two die will be rolled.
        \n To not roll a die, press 'N', this will send you back to menu.
        \n To quit game and go back to the menu press 'Q'.
        \n To exit game press 'E' """)

    help_menu = False
    exit_prog = False
    while True:
        user_input = input("PRESS Q TO QUIT \n")
        if user_input.upper() == "Q":
            clear_screen()
            time.sleep(1)
            help_menu = True
            break
        elif user_input.upper() == "E":
            print("Closing program")
            time.sleep(2)
            exit_prog = True
            break
        else:
            print("INVALID INPUT!")
    if help_menu == True:
        menu_screen()
    if exit_prog == True:
        clear_screen()
        sys.exit()

def options_screen():
    print(""" 
          The defualt number of die to be rolled is 2.
          You may choose the number of die you want rolled in the game.
          You may choose between the numbers 1 and 10.
          """)
    global num_die
    num_die = number_of_dice()
    time.sleep(2)
    clear_screen()
    menu_screen()

#Function that deals with the main game
def play_die():
    import random
    global num_of_rolls
    while True:
        user_input = input("Roll a Die: Y/N \n")

        if user_input.upper() == "Y":
            print(gen_dice(num_die))
            num_of_rolls += 1   
        elif user_input.upper() == "N":
            print("...Thanks for playing...")
            time.sleep(2)
            clear_screen() 
            print(f"You Rolled the dice {num_of_rolls} times")
            time.sleep(3)
            clear_screen()
            break
            #Send user back to menu
        elif user_input.upper() == "E":
            print("...Terminating program...")
            time.sleep(2)
            clear_screen()
            sys.exit()
            break
        else:
            print("INVALID BUTTON!")
    menu_screen()

#Prompts user the number of dice they want to be rolled in the game.
def number_of_dice():
    while True:
        try:
            user_input = int(input("Enter number of dice: "))
            if user_input > 10 or user_input < 1:
                raise ValueError("Number must be between 1 and 10 inclusive ")
        except ValueError as ve:
            print(f"ERROR:{ve} Please try again")
        else:
            return user_input

#will generate n die based on user choice and returns a list of them
def gen_dice(n):
    import random
    rolled_die = list() #generating an empty list to be appended to later
    for i in range(n):
        rolled_die.append(random.randint(1,6))
    return rolled_die
            

print("Welcome to Dice Roll!")
time.sleep(2)
clear_screen()
menu_screen()
