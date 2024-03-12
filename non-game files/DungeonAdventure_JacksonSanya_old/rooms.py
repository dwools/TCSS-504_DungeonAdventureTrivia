import random
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

    def entrance_room(self):
        """ Adventurer start room, should be empty with 1-3 doors"""

        print("You find yourself in an empty room.\nA small wooden door seems to lead deeper into the dungeon....")

    def exit_room(self):
        """ Adventurer end room, should be empty with 1-3 doors"""

        print("You finally found the exit!")

        # If you are missing pillars, turn around.
        if len(Adventurer.get_obtained_pillars(self)) != 4:
            print("Turn back and find the other pillars.\n")

        # Elif you have all four pillars, mission success
        elif len(Adventurer.get_obtained_pillars(self)) == 4:
            print(f"You have found all four pillars. You are free to leave the Dungeon. Congratulations {Adventurer.get_adventurer_name(self)}")

    def empty_room(self):
        """ Empty room. """

        print("You again find yourself in an empty room... Best move on...")

    def potion_room(self):
        """ Potion room, 50/50 chance of being either potion.
        Adds the potion to the adventurer's backpack.
        """

        coin = random.randint(1, 2)

        if coin == 1:

            print("There seems to be a bottle of yellow goop")
            Adventurer.add_to_backpack(self, Items.vision_potion)

        elif coin == 2:

            print("You found a bottle of thick red liquid")
            Adventurer.add_to_backpack(self, Items.health_potion)

    def pit_room(self):
        """ Pit room, when encountered updates the health of the player. """

        Adventurer.update_health(self, Items.pit_trap)

    def room_of_abstraction(self):
        """ Pillar room of abstraction. """

        print("YOU HAVE FOUND THE PILLAR OF ABSTRACTION")
        Adventurer.add_to_backpack(self, Items.pillar_of_abstraction)
        print("The pillar has been added to your bag")
        self.empty_room()

    def room_of_encapsulation(self):
        """ Pillar room of Encapsulation. """

        print("YOU HAVE FOUND THE PILLAR OF ENCAPSULATION")
        Adventurer.add_to_backpack(self, Items.pillar_of_encapsulation)
        print("The pillar has been added to your bag")
        self.empty_room()

    def room_of_inheritance(self):
        """ Pillar room of Inheritance. """

        print("YOU HAVE FOUND THE PILLAR OF INHERITANCE")
        Adventurer.add_to_backpack(self, Items.pillar_of_inheritance)
        print("The pillar has been added to your bag")
        self.empty_room()

    def room_of_polymorphism(self):
        """ Pillar room of Polymorphism. """

        print("YOU HAVE FOUND THE PILLAR OF POLYMORPHISM")
        Adventurer.add_to_backpack(self, Items.pillar_of_polymorphism)
        print("The pillar has been added to your bag")
        self.empty_room()
