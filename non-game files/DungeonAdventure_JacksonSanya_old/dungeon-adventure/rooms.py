import random
import dice
from items import Items
from adventurer import Adventurer

"""
Contains default constructor and all methods you deem necessary -- modular design is CRUCIAL

Contains the following items/behaviors:
(Possibly a) Healing Potion - heals 5-15 hit points (this amount will be randomly generated -- you can modify the range)

(Possibly a) Pit - damage a pit can cause is from 1-20 hit points (this amount will be randomly generated - you can modify the range)

(Possibly an) Entrance - only one room will have an entrance and the room that contains the entrance will contain NOTHING else

(Possibly an) Exit - only one room will have an exit and the room that contains the exit will contain NOTHING else

(Possibly a) Pillar of OO - four pillars in game and they will never be in the same room

Doors - N, S, E, W

10% possibility (this is a constant that you can modify) room will contain a healing potion, vision potion, and pit (each of these are independent of one another)

Vision Potion - can be used to allow user to see eight rooms surrounding current room as well as current room (location in maze may cause less than 8 to be displayed)
"""


class Room(Adventurer):

    def __init__(self):
        super().__init__()
        self.room_types = []

    def entrance_room(self):

        # print("You find yourself in an empty room.\nA small wooden door seems to lead deeper into the dungeon....")
        return 'Assets/room_maps/entrance_room'

    def exit_room(self):

        print("You finally found the exit!")

    def empty_room(self):

        print("You again find yourself in an empty room... Best move on...")

    def potion_room(self):

        coin = random.randint(1, 2)
        potion_count = 1
        if coin == 1:
            potion_count -= 1
            print("There seems to be a bottle of yellow goop")
            Adventurer.add_to_backpack(self, Items.vision_potion)

        elif coin == 2:
            potion_count -= 1
            print("You found a bottle of thick red liquid")
            Adventurer.add_to_backpack(self, Items.health_potion)

    def pit_room(self):
        Adventurer.update_health(self, Items.pit_trap)

    def room_of_abstraction(self):

        print("YOU HAVE FOUND THE PILLAR OF ABSTRACTION")
        # interaction
        Adventurer.add_to_backpack(self, Items.pillar_of_abstraction)
        print("The pillar has been added to your bag")
        self.empty_room()

    def room_of_encapsulation(self):

        print("YOU HAVE FOUND THE PILLAR OF ENCAPSULATION")
        # interaction
        Adventurer.add_to_backpack(self, Items.pillar_of_encapsulation)
        print("The pillar has been added to your bag")
        self.empty_room()

    def room_of_inheritance(self):

        print("YOU HAVE FOUND THE PILLAR OF INHERITANCE")
        # interaction
        Adventurer.add_to_backpack(self, Items.pillar_of_inheritance)
        print("The pillar has been added to your bag")
        self.empty_room()

    def room_of_polymorphism(self):

        print("YOU HAVE FOUND THE PILLAR OF POLYMORPHISM")
        # interaction
        Adventurer.add_to_backpack(self, Items.pillar_of_polymorphism)
        print("The pillar has been added to your bag")
        self.empty_room()
