import random
import sys
import os
import time

#global variables that are to be changed when user decides to modify game settings

#The initialised numbers are the default starting numbers
minimum_number = 1
maximum_number = 100
max_attempts = 7
high_scores = list()

menu = ("PRESS P: PLAY\n"
        "PRESS H: HELP\n"
        "PRESS O: OPTIONS\n"
        "PRESS L: LEADERBOARD\n"
        "PRESS E: EXIT\n")

helps = ("User's have 7 attempts at guessing or they lose the game."
           "To play the game, press P.\n"
           "To manually set the minimum and maximum, press O.\n"
           "To go back to menu, press Q.\n"
           "To exit the program, press E. If in game, press 0.")

options = "Minimum must be less than Maximum. Maximum must be more than Minimum.\n"

def clear_screen():
    if os.name == 'nt': #if the system is windows based
       os.system('cls')
    else:
        os.system('clear')

def menu_screen():
    play = False
    helps = False
    options = False
    while True:
        print(menu.strip())
        user_input = input("insert:...").upper()
        if user_input == 'P':
            play = True
        elif user_input == 'H':
            helps = True
        elif user_input == 'O':
            options = True
        elif user_input == "E":
            print("TERMINATING PROGRAM")
            time.sleep(2)
            clear_screen()
            sys.exit()
        elif user_input == "L":
            leader_board()

        else:
            print("INCORRECT INPUT. TRY AGAIN!")
            time.sleep(1)
            clear_screen()
        if play == True:
            game_play()
            break
        elif helps == True:
            help_screen()
            break
        elif options == True:
            options_screen()
            break
    
def help_screen():
    while True:
        print(helps.strip())
        user_input = input("PRESS Q to return to menu:").upper()
        if user_input == "Q":
            menu_screen()
            break
        elif user_input == "E":
            print("TERMINATING PROGRAM")
            time.sleep(2)
            clear_screen()
            sys.exit()
        else:
            print("INCORRECT INPUT. TRY AGAIN")
            time.sleep(1)  

def options_screen():
    print(options.strip())
    
    while True:
        try:
            global minimum_number
            minimum_number = int(input("Minimum:..."))

            global maximum_number 
            maximum_number = int(input("Maximum:..."))

            #Setting up restrictions that user must not violate
            if maximum_number < minimum_number:
                raise ValueError("Max must be greater than Min. Min must be less than Max!")
            if maximum_number < 0 or minimum_number < 0:
                raise ValueError("Both Max and Min must be positive!")
            if maximum_number - minimum_number < 5:
                raise ValueError("Range between max and min must be atleast 5 and above")
        except ValueError as ve:
            print(f"ERROR! {ve}")
        else:
            print("Max and Min values succesfully updated")
            time.sleep(2)
            clear_screen()
            break
    #return the user to menu screen
    menu_screen()

def leader_board():
    global high_scores
    high_scores.sort()
    for i in high_scores:
        print(f"position {i}: {high_scores[i]}")
    while True:
        user_input = input("PRESS Q to return to menu:").upper()
        if user_input == "Q":
            print("Returning to menu...")
            time.sleep(2)
            clear_screen()
            menu_screen()
            break
        else:
            print("Incorrect input! Try again")
        
def game_play():
    count = 0
    comp_random_num = random.randint(minimum_number,maximum_number)
    running = True
    while count <= max_attempts and running == True:
        try:
            user_input = int(input(f"Choose a random Number between {minimum_number} and {maximum_number}: \n"))
        except ValueError as ve:
            print(f"ERROR: {ve}")
        else:
            if user_input == 0:
                print("TERMINATING PROGRAM")
                time.sleep(2)
                clear_screen()
                sys.exit()
            count += 1
            if user_input == 'Q':
                print("QUITING...")
                time.sleep(2)
                menu_screen()
                break
            if user_input > comp_random_num:
                print(f"{user_input} is too big. Try again")
            elif user_input < comp_random_num:
                print(f"{user_input} is too small. Try again")
            elif user_input == comp_random_num:
                print(f"CORRECT! YOU GUESSED {count} times")
                time.sleep(3)
                clear_screen()
                global high_scores
                high_scores.append(count)
                break
            else:
                print("Invalid input. Try again")
                count -= 1
            
        if count == max_attempts:
            clear_screen()
            print(f"You Lose! you reached the max number of attempts")
            time.sleep(3)
            print(f"Correct Number:{comp_random_num}")
            menu_screen()
            break
    high_scores.sort()
    print(f"Lowest attempts made: {high_scores[0]}")
    time.sleep(3)
    menu_screen()

print("WELCOME TO GUESS THE NUMBER!")
time.sleep(2)
menu_screen()

        
sys.exit()