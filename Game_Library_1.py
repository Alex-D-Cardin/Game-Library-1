#!/usr/bin/python3
#Alex Cardin
#1/27/2020

'''program a library similar to big_brother_inc.'''

import pickle

games = {1:['FPS', 'Halo3', 'Bungee', 'Microsoft', 'Xbox360', '2007', '10', 'either', '30.00', 'yes', '1/15/2008', 'This game blows chunks'],
         2:['', '', '', '', '', '', '', '', '', '', '', ''],
         3:['', '', '', '', '', '', '', '', '', '', '', '']}

def add_edit_game():
    print("Editted game")
    
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
    while True:
        print(""" 
            --------------------------------------
                        Search Options:
                     Title
                     Genre
                     Developer
                     Publisher
                     Console
                     Release Date
                     Rating
                     Players
                     Price
                     Play Status
                     Date Bought
                    
                     Quit
            -----------------------------------------""")
        tag = input("Enter game tag: ")
        
        if choice in "Title" or "title":
            title = input("Enter game title: ")
            key_list = list(games.keys())
            key_list.sort()
            if title in games:
                print("--------------------------------------------")
                print("Title:\t\t", games[key][1])
                print("-----------------------------------------------")                
            
        elif choice in "Genre" or "genre":
            genre = input("Enter game genre: ")
            key_list = list(games.keys())
            key_list.sort()
            if genre in games:
                print("--------------------------------------------")
                print("Genre:\t", games[key][0])
                print("-----------------------------------------------")                   
            
        elif choice in "Developer" or "developer":
            developer = input("Enter game developer: ")
            key_list = list(games.keys())
            key_list.sort()
            if developer in games:
                print("--------------------------------------------")
                print("Developer:\t", games[key][2])
                print("-----------------------------------------------")                    
            
        elif choice in "Publisher" or "publisher":
            publisher = input("Enter game publisher: ")
            key_list = list(games.keys())
            key_list.sort()
            if publisher in games:
                print("--------------------------------------------")
                print("Publisher:\t", games[key][3])
                print("-----------------------------------------------")                  
            
        elif choice in "Console" or "console":
            console = input("Enter game console: ")
            key_list = list(games.keys())
            key_list.sort()
            if console in games:
                print("--------------------------------------------")
                print("Console:\t", games[key][4])
                print("-----------------------------------------------")                   
            
        elif choice in "Release Date" or "release date":
            release_date = input("Enter game release date: ")
            key_list = list(games.keys())
            key_list.sort()
            if release_date in games:
                print("--------------------------------------------")
                print("Date released:\t", games[key][5])
                print("-----------------------------------------------")                 
            
        elif choice in "Rating" or "rating":
            rating = input("Enter game rating: ")
            key_list = list(games.keys())
            key_list.sort()
            if rating in games:
                print("--------------------------------------------")
                print("Rating:\t", games[key][6])
                print("-----------------------------------------------")                   
            
        elif choice in "Players" or "players":
            players = input("Enter game player type: ")
            key_list = list(games.keys())
            key_list.sort()
            if players in games:
                print("--------------------------------------------")
                print("Players:\t", games[key][7])
                print("-----------------------------------------------")                   
            
        elif choice in "Price" or "price":
            price = input("Enter game price: ")
            key_list = list(games.keys())
            key_list.sort()
            if price in games:
                print("--------------------------------------------")
                print("Price:\t", games[key][8])
                print("-----------------------------------------------")                  
            
        elif choice in "Play Status" or "play status":
            play_status = input("Enter game has played")
            play_status = input("Enter game title: ")
            key_list = list(games.keys())
            key_list.sort()
            if play_status in games:
                print("--------------------------------------------")
                print("Have Played:\t", games[key][9])
                print("-----------------------------------------------")                  
            
        elif choice in "Date Bought" or "date bought":
            date_bought = input("Enter date game was bought")
            key_list = list(games.keys())
            key_list.sort()
            if date_bought in games:
                print("--------------------------------------------")
                print("Date Bought:\t", games[key][10])
                print("-----------------------------------------------")                  
            
        elif choice == "Quit" or "Exit":
            exit()
        
    #for i in games:
        #print(title)
    
def remove_game():
    print("Removed game!")
    
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
        1) Add/Edit Game
        2) Print All Games
        3) Search By Title
        4) Remove a Game
        5) Save Database
        6) Reset File
        
        Q) Quit
        -----------------------------------------
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
        
    elif choice == "6":
        reset_pickle_file()
            
    elif choice == "Q" or choice == "q":
        quit()
    else:
        print("No dice kid")
        
print("OH MY! Something really went wrong!")