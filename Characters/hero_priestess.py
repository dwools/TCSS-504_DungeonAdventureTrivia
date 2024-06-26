import random
import pygame as pg
from Assets import assets as a
from Characters.hero import Hero


class Priestess(Hero):
    def __init__(self,
                 name,
                 type,
                 hit_points,
                 attack_speed,
                 chance_to_hit,
                 minimum_damage,
                 maximum_damage,
                 chance_to_block,
                 chance_to_heal,
                 minimum_heal_points,
                 maximum_heal_points
                 ):

        super().__init__(name,
                         type,
                         hit_points,
                         attack_speed,
                         chance_to_hit,
                         minimum_damage,
                         maximum_damage,
                         chance_to_block)
        self.__chance_to_heal = chance_to_heal
        self.__minimum_heal_points = minimum_heal_points
        self.__maximum_heal_points = maximum_heal_points

        self.__sprite_north = a.north_priestess
        self.__sprite_east = a.east_priestess
        self.__sprite_west = a.west_priestess
        self.__sprite_south = a.south_priestess

    def get_chance_to_heal(self):
        return self.__chance_to_heal

    def get_minimum_heal_points(self):
        return self.__minimum_heal_points

    def get_maximum_heal_points(self):
        return self.__maximum_heal_points

    def special(self):
        """
        Priestess's special skill: healing
        :return:
        """
        if random.randint(1, 100) <= self.__chance_to_heal:
            heal_points = random.randint(self.__minimum_heal_points, self.__maximum_heal_points)
            if self.get_current_hit_points() + heal_points > self.__maximum_heal_points:
                heal_points = self.get_max_hit_points() - self.get_current_hit_points()
            self.set_current_hit_points(self.get_current_hit_points() + heal_points)
            print(f"Your special healing increased your hit points by {heal_points}!")
        else:
            print("Your Special Healing Failed!")

    def get_sprite_north(self):
        return self.__sprite_north

    def get_sprite_east(self):
        return self.__sprite_east

    def get_sprite_west(self):
        return self.__sprite_west

    def get_sprite_south(self):
        return self.__sprite_south

    def set_character_sprites(self, north_sprite, east_sprite, west_sprite, south_sprite):
        self.__sprite_north = north_sprite
        self.__sprite_east = east_sprite
        self.__sprite_west = west_sprite
        self.__sprite_south = south_sprite
        self.__sprite_current = south_sprite