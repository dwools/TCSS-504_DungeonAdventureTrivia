import dice
import random

"""
Class to hold all items / consumables.
This includes:
- Health Potion
- Vision Potion
- the Four Pillars
"""


# Note: Both ROOM and ADVENTURER are able to hold potions
#                                                   and pillars

class Items:
    def __init__(self):
        self.__pillar_of_abstraction = "The Pillar of Abstraction"
        self.__pillar_of_encapsulation = "The Pillar of Encapsulation"
        self.__pillar_of_inheritance = "The Pillar of Inheritance"
        self.__pillar_of_polymorphism = "The Pillar of Polymorphism"

    # Traps
    def pit_trap(self):
        damage = int(dice.roll("1d20"))
        print(f"You have fallen in a pit and taken {damage} damage")
        return damage

    # Potions
    def health_potion(self):
        add_health = dice.roll("5d3")
        print(f"You feel invigorated and restore {add_health} points of health")
        return add_health

    def vision_potion(self):
        print(f"Your perception heightens, you can sense the rooms around you")
        return True

    def pillar_of_abstraction(self):
        return f"{self.__pillar_of_abstraction}"

    def pillar_of_encapsulation(self):
        return f"{self.__pillar_of_encapsulation}"

    def pillar_of_inheritance(self):
        return f"{self.__pillar_of_inheritance}"

    def pillar_of_polymorphism(self):
        return f"{self.__pillar_of_polymorphism}"

