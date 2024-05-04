from abc import ABC, abstractmethod
from typing import Any
import datetime

class Room(ABC):
    price=None
    number=None
    Type=None
    @abstractmethod
    def __init__(self, number):
        pass
    
    @abstractmethod
    def __str__(self):
       pass

class Onebed(Room):
    
    price = 8000
    Type = "Egy ágyas"
    def __init__(self, number):
        self.number=number
        
    def __str__(self):
        print(f"Típus: {self.Type}  ||  Szobaszám:  {self.number} || Ára:  {self.price}")

class Twobed(Room):
    price = 14000
    Type = "Két ágyas"
    def __init__(self, number):
        self.number=number
        
    def __str__(self):
        print(f"Típus: {self.Type}  ||  Szobaszám:  {self.number}  ||  Ára:  {self.price}")
    

class Hotel():
    def __init__(self, name, roomlist=None):
        self.name=name
        if roomlist==None:
            self.roomlist=[]
        else:
            self.roomlist=roomlist
    
    def add_room(self, room):
        self.roomlist.append(room)
        
    def delete_room(self, room):
        self.roomlist.remove(room)
        
    def list_rooms(self):
        text=""
        for room in self.roomlist:
            text+=f"{room.number} {room.Type}"
        return text


    

    
