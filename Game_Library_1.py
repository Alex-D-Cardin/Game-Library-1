#!/usr/bin/python3
#Alex Cardin
#1/27/2020

'''program a library similar to big_brother_inc.'''

import pickle

games = {1:['FPS', 'Halo3', 'Bungee', 'Microsoft', 'Xbox360', '2007', '10', 'either', '30.00', 'yes', '1/15/2008', 'This game blows chunks'],
         2:['', '', '', '', '', '', '', '', '', '', '', ''],
         3:['', '', '', '', '', '', '', '', '', '', '', '']}

def add():
    new_key = len(games)+1
    new_entry = []
    valid = False
    
    while not valid:
        genre = input("Enter Genre: ")
        new_entry.append(genre)
        title = input("Enter Title: ")
        new_entry.append(title)
        developer = input("Enter Developer: ")
        new_entry.append(developer)
        publisher = input("Enter Publisher: ")
        new_entry.append(publisher)
        console = input("Enter Console: ")
        new_entry.append(console)
        release_date = input("Enter Release Date: ")
        new_entry.append(release_date)
        rating = input("Enter Rating: ")
        new_entry.append(rating)
        players = input("Enter multi/singleplayer: ")
        new_entry.append(players)
        price = input("Enter Price: ")
        new_entry.append(price)
        play_status = input("Enter Play Status: ")
        new_entry.append(play_status)
        date_bought = input("Enter Date Bought: ")
        new_entry.append(date_bought)
        notes = input("Enter Notes: ")
        new_entry.append(notes)
        
        answer = input("Is this correct? ")
        if answer.capitalize() in ("yes", "y"):
            valid = True
        games[new_key] = entry.append()
    
def edit():
    print("Here is the library: ")
    for keys in games.keys():
        print(key, "-", games[key][1])
    
    edit_key = int(input("Which game do you want to change? "))
    edit_entry = []
    
    valid = False
            
    while not valid:
        genre = input("Enter Genre: ")
        edit_entry.append(genre)
        title = input("Enter Title: ")
        edit_entry.append(title)
        developer = input("Enter Developer: ")
        edit_entry.append(developer)
        publisher = input("Enter Publisher: ")
        edit_entry.append(publisher)
        console = input("Enter Console: ")
        edit_entry.append(console)
        release_date = input("Enter Release Date: ")
        edit_entry.append(release_date)
        rating = input("Enter Rating: ")
        edit_entry.append(rating)
        players = input("Enter multi/singleplayer: ")
        edit_entry.append(players)
        price = input("Enter Price: ")
        edit_entry.append(price)
        play_status = input("Enter Play Status: ")
        edit_entry.append(play_status)
        date_bought = input("Enter Date Bought: ")
        edit_entry.append(date_bought)
        notes = input("Enter Notes: ")
        edit_entry.append(notes)    
            
            
            
        answer = input("Is this correct? ")
        if answer.capitalize() in ("yes", "y"):
            valid = True
        games[edit_key] = entry.append()        
    
def print_all_games():
    for key in games:
        print("--------------------------------------------")
        print("Title:\t\t", games[key][1])
        print("Genre:\t\t", games[key][0])
        print("Developer:\t", games[key][2])
        print("Publisher:\t", games[key][3])
        print("Console:\t", games[key][4])
        print("Release:\t", games[key][5])
        print("Rating:\t\t", games[key][6])
        print("Players:\t", games[key][7])
        print("Price:\t\t", games[key][8])
        print("Have Played:\t", games[key][9])
        print("Date Bought:\t", games[key][10])
        print("Notes:\t\t", games[key][11])
        print("-----------------------------------------------")
    
def search_by_title():
    title = input("Enter title of game: ")
    tally = 0
    for key in games.keys():
        entry = games[key]
        if title in entry[1]:
            tally += 1
            print(games.tally, title.entry[1])
        
    #for i in games:
        #print(title)
    
def remove_game():
    print("Removed game!")
    
    print("Here is the library: ")
    for keys in games.keys():
        print(keys, "-", games[keys])
    
    remove_key = input("Which game do you want to remove? ")
    remove_key = int(remove_key)

    if keys in games:
        print(keys, ":", games[remove_key][1] +", removed.\n")  
        games.pop(remove_key)
  
        
        
        
def save_database():
    #print("Saved database!")
    gamefile = open("game_lib.pickle", "wb")
    pickle.dump(games, gamefile)
    gamefile.close()    
    
def reset_pickle_file():
    #print("File reset!")
    games = {}
    gamefile = open("game_lib.pickle", "wb")
    pickle.dump(games, gamefile)
    gamefile.close()    
    
def quit():
    print("Data Saved. BBBYYYYYYYEEEEEEEEEEEE")
    exit()    

gamefile = open("game_lib.pickle", "wb")
pickle.dump(games, gamefile)
gamefile.close()

while True:
    print("""
              Welcome to Game Library Menu
        --------------------------------------
                  MAIN MENU
        1) Add Game
        2) Edit Game
        3) Print All Games
        4) Search By Title
        5) Remove a Game
        6) Save Database
        7) Reset File
        
        Q) Quit
        -----------------------------------------
        """)
    choice = input("what would you like to do? ")

    if choice == "1":
        add()
    elif choice == "2":
        edit()
    elif choice == "3":
        print_all_games()
    elif choice == "4":
        search_by_title()
    
    elif choice == "5":
        remove_game()
        
    elif choice == "6":
        save_database()
        
    elif choice == "7":
        reset_pickle_file()
            
    elif choice == "Q" or choice == "q":
        quit()
    else:
        print("No dice kid")
        
print("OH MY! Something really went wrong!")