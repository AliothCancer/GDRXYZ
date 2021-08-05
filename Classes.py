class Character:
    def __init__(self,name,level,stats):
        self.name = name
        self.level = 0

        if stats == None:               
            self.stats = {
                #body
                "phy":10, #physique
                "str":10, #strong
                "agl":10, #agility

                #mind
                "int":10, #intelligence
                "teq":10 #technique
                        }
        else:
            self.stats = stats
        
        self.skills = { 
            "Perception":0
        }

    def get_info(self):
        return self.name,self.level,self.stats


# CREATE THE PLAYER CLASS
class Player(Character):

    list_of_players_class = {}

    def __init__(self,name,level,race,stats):
        super().__init__(name,level,stats) 
        self.race = race

        self.list_of_players_class[self.name] = self

        coor = [0,0,0] # x,y and z coordinate


# CREATE THE MONSTER CLASS
class Monster(Character):
    pass








