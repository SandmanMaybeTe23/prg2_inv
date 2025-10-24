from abc import ABC, abstractmethod
from typing import List

class  item(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def use(self):
        pass


class inv():
    def __init__(self,):
        self.contents = []
        self.weight =0

    def get_contents(self):
        return self.contents 
    
    def how_heavy(self):
        return self.weight
        
    
    def add_item(self,item):
        self.contents.append(item)

        


player_inv = inv()
player_inv.add_item("SHOTGUN")

print(player_inv.get_contents())
        
