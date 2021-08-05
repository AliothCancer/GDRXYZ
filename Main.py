from List_of_options import list_of_options_main
from Classes import Player,Monster
from menu_selector_func import MenuSelector
from List_of_players import list_of_players

# add all player's info in list_of_players dictionary
# playerid:[ name,race,level,stats,skills ]
# name,race are strings
# level is int
# stats,skills are dictionaries




# STORE PLAYERS,MONSTERS DATA
def save_players_data():
    pass
def save_monsters_data():
    pass

def save():
    save_players_data()
    save_monsters_data()

# CREATE CLASS OBJECTS FROM THE DICTIONARY
def from_dict_to_class_object():
    pass


# GAME LOGIC FUNCTIONS
def esc():
    return False  

def create_player():
    list_of_races = ["Orc","Human","Elf"]
    temp_player = []
    name = input("What's your name? ")
    option = MenuSelector("CHOOSE A RACE:",list_of_races)
    if option == "Orc":
        race = option
    
    elif option == "Human":
        race = option
        
    elif option == "Elf":
        race = option

    temp_player.append(name,race)
    return temp_player

def save_to_list():
    pass

def from_list_to_class():
    pass

def new_player():
    create_player()
    save_to_list()
    from_list_to_class()
     
def start_game():
    pass

def new_game():
    new_player()
    start_game()

# MAIN GAME CYCLE
def main(): 
    game_on = True
    while game_on:
        option = MenuSelector("Main Menu",list_of_options_main)

        if option == "Play a new game":
            new_game()
    
        elif option == "Save":
            save()
        
        elif option == "Exit":
            game_on = esc()


if __name__=="__main__":
    main()
