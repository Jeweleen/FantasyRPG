
class Player:

    def __init__ (self, name, race):
        self.name = name
        self.race = race
    
    def printPlayer(self):
        print(f"Welcome {self.name}, I see you are of the {self.race} race.")