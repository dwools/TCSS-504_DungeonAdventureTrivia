import random
import pygame as pg
from Assets import assets as a



class Item():
    """
    Class to hold all items / consumables.
    This includes:
    - Health Potion
    - Pit Trap
    - the Four Pillars
    """

    def __init__(self, item_name):
        self.__item_name = item_name
        self.__item_position = [0, 0]
        self.__item_position_x, self.__item_position_y = self.__item_position
        self.__rect = pg.Rect(self.__item_position_y, self.__item_position_x, 16, 16)
        self.__player_scroll = [0, 0]
        self.__healing_value = random.randint(20, 40)
        self.__health_potion_sprite = a.health_potion
        self.__fire_trap_sprite = a.fire_trap




    def get_item_position(self):
        return self.__item_position

    def set_item_position(self, item_position):
        self.__item_position = item_position
        self.__item_position_x, self.__item_position_y = item_position

    def set_player_scroll(self, scroll):
        self.__player_scroll = scroll

    def get_item_rect(self):
        return self.__rect

    def set_item_rect(self, x, y):
        self.__rect = pg.Rect(y, x, 16, 16)

    def get_fire_trap_sprite(self):
        return self.__fire_trap_sprite

    def set_fire_trap_sprite(self, sprite_path):
        self.__fire_trap_sprite = sprite_path

    def get_health_potion_sprite(self):
        return self.__health_potion_sprite

    def set_health_potion_sprite(self, sprite_path):
        self.__health_potion_sprite = sprite_path

    def get_health_change_value(self):
        return self.__healing_value

    def set_health_change_value(self, value):
        self.__healing_value = value

    def get_item_name(self):
        return self.__item_name

    def set_item_name(self, item_name):
        self.__item_name = item_name
    # @abstractmethod
    # def change_health(self):
    #     pass






# class HealthPotion(Item):
#
#     def change_health(self):
#         dungeon_character.hit_points += "some value here"
#
# # Here, imagine the instructor gave us this abstract method. What then does its presence tell us?
# # Answer: It tells us that any concrete chidren of this ABC must include this method with the specified parameters, analagous to an object's parameters being required when it's instantiated.
#
#
# class Pillar:
#
#     def __init__(self, location):
#         # self.__location = location
#
#     def render(self, surf, scroll):
#         """
#         Render function to visualize the item with its corresponding asset and
#         :param surf:
#         :param scroll:
#         :return:
#         """
#         surf.blit(asset, (self.__location[0] - scroll[0], self.__location[1] - scroll[1]))
#
#
#     def get_rect(self):
#         return pg.Rect(self.__location[0], self.__location[1], 6, 6)
#
#     def collision_test(rect):
#         healing_rect = self.get_rect()
#         return healing_rect.colliderect(rect)
#
# healing_potions = []
# for i in range(5):
#     healing_potions.append(HealingPotion((random.randint(0, 600) - 300, 80)))
#
# for potion in healing_potions:
#     potion.render(surf, scroll)
#     if potion.collision_test(adventurer.obj.rect):
#         hp +=


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
