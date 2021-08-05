from List_of_options import list_of_options_main
from Classes import Player,Monster
from menu_selector_func import MenuSelector
from Lists import list_of_players,list_of_monsters
#from time import localtime
from os import system
from rich import pretty,print

# to better visualize the print 
pretty.install()

# add all player's info in list_of_players dictionary
# playerid:[ name,race,level,stats,skills ]
# name,race are strings
# level is int
# stats,skills are dictionaries

# LOAD THE EXISTING DATA TO OBJECTS
def load_data():
    global list_of_players
    for name in list_of_players:
        race = list_of_players[name]
        level = list_of_players[name]["level"]
        stats = list_of_players[name]["stats"]
        Player(name,level,race,stats)


def show_players():
    global list_of_players
    for name in list_of_players:
        print(name,list_of_players[name])
        print("\n\n")

# STORE PLAYERS,MONSTERS DATA
def save_players_data():
    pass


def save_monsters_data():
    pass

def save():
    write_lists()




                            # GAME LOGIC FUNCTIONS

                          #  EXIT
def esc():
    return False  

                                # CREATING PLAYER
def create_player():
    global list_of_players
    list_of_races = ["Orc","Human","Elf"]


    # aquiring data from player
    name = input("\n\n  What's your name?\n\n >>> ")
    option = MenuSelector("\n\n\tCHOOSE A RACE:",list_of_races) 
    
    

    # construction of the player object
    # every player has a unic nickname who takes to the player data
    if name not in list_of_players:
        pl = Player(name,0,option,None)
        list_of_players[pl.name]={
                    "race":pl.race,
                    "level":pl.level,
                    "stats":pl.stats,
        }
    else:
        print("\n\n\tThis name is already taken. Choose another pls... :)")
        create_player()

                                # OVERWRITE THE NEW LIST OF PLAYERS
def write_lists():
    global list_of_players,list_of_monsters
    with open("Lists.py","w") as file:
        file.write("list_of_players="+str(list_of_players))
        file.write("\n")
        file.write("list_of_monsters="+str(list_of_monsters))
    
                    # CREATING PLAYER OBJECT FROM THE LIST OF PLAYERS
def from_list_to_class():
    pass

                    #  SET OF FUNCTION TO HAVE A NEW PLAYER
def new_player():
    create_player()
    write_lists()

def delete_player():
    global list_of_players
    list_of_players_name = [name for name in list_of_players]
    player=MenuSelector("\n\tCHOOSE A PLAYER FROM THE LIST:",list_of_players_name)

    choice = MenuSelector(f"Do you really want to delete {player}",("Yes","No"))
    if choice == "Yes":
        list_of_players.pop(player)

                    # THE GAMEPLAY
def start_game():
    list_of_players_name = [name for name in list_of_players]
    name=MenuSelector("\n\tCHOOSE A PLAYER FROM THE LIST:",list_of_players_name)
    player = Player.list_of_players_class[name] 



                    # START OF NEW GAME
def new_game():
    new_player()
    start_game()

                    # MAIN GAME CYCLE
def main():
    # DATA INITIALIZATION
    load_data()
    system("clear")
    game_on = True
    while game_on:
        option = MenuSelector("        \nWELLCOME TO XYZGDR!!!!",list_of_options_main)

        if option == "Play a new game":
            new_game()

        elif option == "Play existing game":
            start_game()

        elif option == "Show players":
            show_players()

        elif option == "Delete player":
            delete_player()
        elif option == "Save":
            save()
        
        elif option == "Exit":
            game_on = esc()


if __name__=="__main__":
    main()
