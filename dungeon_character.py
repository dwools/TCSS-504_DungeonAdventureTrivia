import random
from abc import ABC, abstractmethod
import pygame as pg
from object_coordinates_generator import ValidCoordsGenerator


class DungeonCharacter(ABC):
    def __init__(self, name, type, hit_points, attack_speed, chance_to_hit, minimum_damage, maximum_damage):
        # Dungeon character needs a name per project specifications
        self.__name = name
        self.__type = type
        self.__hit_points = hit_points
        self.__attack_speed = attack_speed
        self.__chance_to_hit = chance_to_hit
        self.__minimum_damage = minimum_damage
        self.__maximum_damage = maximum_damage
        self.__position = [0, 0]
        self.__minimum_heal_points = 0
        self.__maximum_heal_points = 0
        self.__position_x, self.__position_y = self.__position
        self.__rect = pg.Rect(self.__position_x, self.__position_y, 16, 16)

        # self.__chance_to_block = Noned
        # self.__chance_to_heal = None
        # self.__minimum_heal_points = None
        # self.__maximum_heal_points = None
        # self.__chance_for_bonus_damage = None
        # self.__minimum_bonus_damage = None
        # self.__chance_for_second_attack = None
        # self.__maximum_bonus_damage = None

    def get_name(self):
        print(self.__name)
        return self.__name

    def get_type(self):
        print(self.__type)
        return self.__type

    def get_hit_points(self):
        return self.__hit_points

    def get_attack_speed(self):
        return self.__attack_speed

    def get_chance_to_hit(self):
        return self.__chance_to_hit

    def get_minimum_damage(self):
        return self.__minimum_damage

    def get_maximum_damage(self):
        return self.__maximum_damage

    def get_position(self):
        return self.__position

    def set_position(self, position):  # ensure that the tile is f before moving it.
        self.__position = position

    def get_character_rect(self):
        return self.__rect

    def set_character_rect(self, x, y):
        self.__rect = pg.Rect(y, x, 16, 16)

    def set_monster_rect(self, monster_rect):
        self.__rect = monster_rect

    def set_monster_position(self, monster_position):
        self.__position = monster_position

        # Mechanic Methods

    def get_coordinate(self):
        col = self.__rect.centerx // 16
        row = self.__rect.centery // 16
        return col, row

    def set_character(self, type):
        self.__character = type

    def set_hit_points(self, hit_points):
        self.__hit_points = hit_points

    def get_minimum_heal_points(self):
        return self.__minimum_heal_points

    def get_maximum_heal_points(self):
        return self.__maximum_heal_points

    def set_attack_speed(self, attack_speed):
        self.__attack_speed = attack_speed

    def set_chance_to_hit(self, chance_to_hit):
        self.__chance_to_hit = chance_to_hit

    def set_minimum_damage(self, minimum_damage):
        self.__minimum_damage = minimum_damage

    def set_maximum_damage(self, maximum_damage):
        self.__maximum_damage = maximum_damage

    def attack(self, opponent, chance_to_hit, minimum_damage, maximum_damage):
        damage = random.randint(minimum_damage, maximum_damage)
        if random.random() < chance_to_hit:  # random.random() by default generates a random value between 0 and 1
            opponent.set_hit_points(opponent.get_hit_points() - damage)

    # Here, imagine the instructor gave us this abstract method. What then does its presence tell us?
    # Answer: It tells us that any concrete chidren of this ABC must include this method with the specified parameters, analagous to an object's parameters being required when it's instantiated.

    # @abstractmethod
    # def flee(self):
    #     pass
# if __name__ == '__main__':
