import random

"""
Class to hold all items / consumables.
This includes:
- Health Potion
- Vision Potion
- Pit Trap
- the Four Pillars
"""


# Note: Both ROOM and ADVENTURER are able to hold potions
#                                                   and pillars

class Items:
    """ Class to hold the items and/ or consumables of the dungeon. """

    def __init__(self):
        self.__pillar_of_abstraction = "The Pillar of Abstraction"
        self.__pillar_of_encapsulation = "The Pillar of Encapsulation"
        self.__pillar_of_inheritance = "The Pillar of Inheritance"
        self.__pillar_of_polymorphism = "The Pillar of Polymorphism"

    # Traps
    def pit_trap(self):
        """ Pit Trap item to be placed in the Pit Trap room. """

        damage = random.randint(1, 20)
        print(f"You have fallen in a pit and taken {damage} damage")
        return damage

    # Potions

    def health_potion(self):
        """ Health potion consumable. """

        add_health = random.randint(5, 15)
        print(f"You feel invigorated and restore {add_health} points of health")
        return add_health

    def vision_potion(self):
        """ Vision potion consumable. """

        print(f"Your perception heightens, you can sense the rooms around you")
        return True

    # Individual Pillars

    def pillar_of_abstraction(self):
        return f"{self.__pillar_of_abstraction}"

    def pillar_of_encapsulation(self):
        return f"{self.__pillar_of_encapsulation}"

    def pillar_of_inheritance(self):
        return f"{self.__pillar_of_inheritance}"

    def pillar_of_polymorphism(self):
        return f"{self.__pillar_of_polymorphism}"

