import random
import pygame as pg
class HealingPotion:
    """
    Class to hold all items / consumables.
    This includes:
    - Health Potion
    - Vision Potion
    - Pit Trap
    - the Four Pillars
    """

    def __init__(self, location):
        self.__location = location

    def render(self, surf, scroll):
        """
        Render function to visualize the item with its corresponding asset and
        :param surf:
        :param scroll:
        :return:
        """
        surf.blit(asset, (self.__location[0] - scroll[0], self.__location[1] - scroll[1]))


    def get_rect(self):
        return pg.Rect(self.__location[0], self.__location[1], 6, 6)

    def collision_test(rect):
        healing_rect = self.get_rect()
        return healing_rect.colliderect(rect)

healing_potions = []
for i in range(5):
    healing_potions.append(HealingPotion((random.randint(0, 600) - 300, 80)))

for potion in healing_potions:
    potion.render(surf, scroll)
    if potion.collision_test(adventurer.obj.rect):
        hp +=


# Note: Both ROOM and ADVENTURER are able to hold potions
#                                                   and pillars

# class Items:
#     """ Class to hold the items and/ or consumables of the dungeon. """
#
#     def __init__(self):
#         self.__pillar_of_abstraction = "The Pillar of Abstraction"
#         self.__pillar_of_encapsulation = "The Pillar of Encapsulation"
#         self.__pillar_of_inheritance = "The Pillar of Inheritance"
#         self.__pillar_of_polymorphism = "The Pillar of Polymorphism"
#
#     # Traps
#     def pit_trap(self):
#         """ Pit Trap item to be placed in the Pit Trap room. """
#
#         damage = random.randint(1, 20)
#         print(f"You have fallen in a pit and taken {damage} damage")
#         return damage
#
#     # Potions
#
#     def health_potion(self):
#         """ Health potion consumable. """
#
#         add_health = random.randint(5, 15)
#         print(f"You feel invigorated and restore {add_health} points of health")
#         return add_health
#
#     def vision_potion(self):
#         """ Vision potion consumable. """
#
#         print(f"Your perception heightens, you can sense the rooms around you")
#         return True
#
#     # Individual Pillars
#
#     def get_pillar_of_abstraction(self):
#         return f"{self.__pillar_of_abstraction}"
#
#     def get_pillar_of_encapsulation(self):
#         return f"{self.__pillar_of_encapsulation}"
#
#     def get_pillar_of_inheritance(self):
#         return f"{self.__pillar_of_inheritance}"
#
#     def get_pillar_of_polymorphism(self):
#         return f"{self.__pillar_of_polymorphism}"
#