
from os import system
from readchar import readkey
import readchar
from rich import print





# Display options and return the option if selected with enter key
# use up and down arrows or w,s keys to move selector. 
def MenuSelector(Title,list_of_options): 
    Selected = False
    selector = 0
    menu = Title
    while True:
        Title = menu
        for index,option in enumerate(list_of_options):
            if selector == index:
                Title+="\n>>> "+ option
            else:
                Title+= "\n    "+option
        
        # print the new output
        print(Title)
        command = readchar.readkey()

        # LOGIC FOR UP AND DOWN
        if command == "\x1b\x1b":
            break
        if command == "w" or command == "\x1b[A":
            if selector > 0:
                selector-=1
        if command == "s" or command == "\x1b[B":
            if selector < len(list_of_options)-1:
                selector+=1
        
        # LOGIC FOR SELECT THE OPTION
        if command == "\r":
            Selected = True
        
        #clear the old output
        system("clear")

        if Selected:
            break
    return list_of_options[selector]
        
    
'''
USE EXAMPLE:

ListOfOptions_Main= ["Play a new Game", "Play an exsisting game","esc"]
ListOfOptions_1 = ["Create a new player","Show existing player"]

for i in range(32):
    ListOfOptions_Main.append("-"+str(i))

while True:
    option = MenuSelector("Main Menu:",ListOfOptions_Main)
    if option == "esc":
        break
    if option == "Play a new Game":
        sub_option = MenuSelector("Play a new Game:",ListOfOptions_1)
    '''