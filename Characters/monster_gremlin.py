from Characters.monster import Monster
import pygame as pg
from Assets import assets as a


class Gremlin(Monster):
    def __init__(self, name,
                 type,
                 hit_points,
                 attack_speed,
                 chance_to_hit,
                 minimum_damage,
                 maximum_damage,
                 chance_to_heal,
                 minimum_heal_points,
                 maximum_heal_points):
        super().__init__(name, type, hit_points, attack_speed, chance_to_hit, minimum_damage, maximum_damage, chance_to_heal,
                         minimum_heal_points, maximum_heal_points)

        self.__east_sprite = a.east_gremlin
        self.__north_sprite = a.north_gremlin
        self.__west_sprite = a.west_gremlin
        self.__south_sprite = a.south_gremlin

    def get_south_sprite(self):
        return self.__south_sprite

    def get_north_sprite(self):
        return self.__north_sprite

    def get_east_sprite(self):
        return self.__east_sprite

    def get_west_sprite(self):
        return self.__west_sprite


