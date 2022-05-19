from dataclasses import dataclass


@dataclass
class Player:
    name: str
    position = (0,0)
    #counter:int =0

    def setposition(self, position) -> None:
        self.position = position
    
   

    def getposition(self):
        return self.position
