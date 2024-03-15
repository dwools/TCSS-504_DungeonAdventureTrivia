import random
from abc import ABC, abstractmethod
import pygame as pg


def simple_attack_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.special_simple_attack_count += 1
        return func(*args, **kwargs)

    wrapper.special_simple_attack_count = 0
    return wrapper

class DungeonCharacter(ABC):
    def __init__(self, name, type, hit_points, attack_speed, chance_to_hit, minimum_damage, maximum_damage):
        # Dungeon character needs a name per project specifications
        self.__name = name
        self.__type = type
        self.__max_hit_points = hit_points
        self.__current_hit_points = hit_points
        self.__attack_speed = attack_speed
        self.__chance_to_hit = chance_to_hit
        self.__minimum_damage = minimum_damage
        self.__maximum_damage = maximum_damage
        self.__position = [0, 0]
        self.__minimum_heal_points = 0
        self.__maximum_heal_points = 0
        self.__position_x, self.__position_y = self.__position
        self.__rect = pg.Rect(self.__position_x, self.__position_y, 16, 16)


    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_current_hit_points(self):
        return self.__current_hit_points
    
    def set_current_hit_points(self, value):
        self.__current_hit_points = value

    def get_max_hit_points(self):
        return self.__max_hit_points

    def set_max_hit_points(self, value):
        self.__max_hit_points = value

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
        self.__position_x, self.__position_y = position

    def get_character_rect(self):
        return self.__rect

    def set_character_rect(self, x, y):
        self.__rect = pg.Rect(y, x, 16, 16)


        # Mechanic Methods

    def get_coordinate(self):
        col = self.__rect.centerx // 16
        row = self.__rect.centery // 16
        return col, row

    def set_character(self, type):
        self.__character = type

    def set_hit_points(self, hit_points):
        self.__current_hit_points = hit_points

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

    @simple_attack_counter
    def simple_attack(self, enemy):
        print(f'{self.__name} tries a simple attack...')
        if random.randint(1, 100) <= self.__chance_to_hit:
            damage = random.randint(self.__minimum_damage, self.__maximum_damage)
            enemy.set_current_hit_points(enemy.get_current_hit_points() - damage)
            print(f'{enemy.get_name()} took {damage} damage! {enemy.get_name()} now has {enemy.get_current_hit_points()} hit points!')
        else:
            print(f"{self.__name}'s attack missed!")

    @abstractmethod
    def get_sprite_north(self):
        pass

    @abstractmethod
    def get_sprite_east(self):
        pass

    @abstractmethod
    def get_sprite_west(self):
        pass

    @abstractmethod
    def get_sprite_south(self):
        pass



    # Here, imagine the instructor gave us this abstract method. What then does its presence tell us?
    # Answer: It tells us that any concrete chidren of this ABC must include this method with the specified parameters, analagous to an object's parameters being required when it's instantiated.

