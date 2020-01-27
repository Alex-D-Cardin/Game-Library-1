#!/usr/bin/python3
#Alex Cardin
#1/27/2020

'''program a library similar to big_brother_inc.'''

import pickle

def add_edit_game():
    print("Editted game")
    
def print_all_games():
    print("Displayed all games")
    
def search_by_title():
    print("Searched by title")
    
def remove_game():
    print("Removed game")
    
def save_database():
    print("Saved database")
    
def quit():
    print("Data Saved. BBBYYYYYYYEEEEEEEEEEEE")
    exit()    

while True:
    print("""
              Welcome to Big Brother Inc.
        --------------------------------------
                  MAIN MENU
        1) Add/Edit Game
        2) Print All Games
        3) Search By Title
        4) Remove a Game
        5) Save Database
        
        Q) Quit
        """)
    choice = input("what would you like to do? ")

    if choice == "1":
        add_edit_game()
    elif choice == "2":
        print_all_games()
    elif choice == "3":
        search_by_title()
    
    elif choice == "4":
        remove_game()
        
    elif choice == "5":
        save_database()
            
    elif choice == "Q" or choice == "q":
        quit()
    else:
        print("No dice kid")
        
print("OH MY! Something really went wrong!")