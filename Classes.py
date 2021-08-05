class Character:
    def __init__(self,name):
        self.name = name
        self.level = 0

                        #body
        self.stats = {"phy":10, #physique
                      "str":10, #strong
                      "agl":10, #agility

                        #mind
                      "int":10, #intelligence
                      "teq":10 #technique
                     }

    def get_info(self):
        return self.name,self.level,self.stats


# CREATE THE PLAYER CLASS
class Player(Character):

    list_of_players = []

    def __init__(self,name,race):
        super().__init__(name) 
        self.race = race

        self.list_of_players.append(self)

        coor = [0,0,0] # x,y and z coordinate


# CREATE THE MONSTER CLASS
class Monster(Character):
    pass








