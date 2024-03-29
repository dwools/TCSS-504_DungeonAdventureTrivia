import random
import pygame as pg
from Assets import assets as a
from Characters.hero import Hero


class Knight(Hero):
    # to give a crushing blow is a CHOICE that the knight has.
    def __init__(self,
                 name,
                 type,
                 hit_points,
                 attack_speed,
                 chance_to_hit,
                 minimum_damage,
                 maximum_damage,
                 chance_to_block,
                 chance_for_crushing_blow,
                 minimum_crushing_damage,
                 maximum_crushing_damage
                 ):
        super().__init__(name,
                         type,
                         hit_points,
                         attack_speed,
                         chance_to_hit,
                         minimum_damage,
                         maximum_damage,
                         chance_to_block
                         )
        self.__chance_for_crushing_blow = chance_for_crushing_blow
        self.__minimum_crushing_damage = minimum_crushing_damage
        self.__maximum_crushing_damage = maximum_crushing_damage

        self.__sprite_north = a.north_knight
        self.__sprite_east = a.east_knight
        self.__sprite_west = a.west_knight
        self.__sprite_south = a.south_knight


    def get_chance_for_crushing_blow(self):
        print(self.__chance_for_crushing_blow)
        return self.__chance_for_crushing_blow

    def get_minimum_crushing_damage(self):
        return self.__minimum_crushing_damage

    def get_maximum_crushing_damage(self):
        return self.__maximum_crushing_damage

    def special(self, enemy):
        """
        Knight's special attack: Crushing Blow
        :param enemy:
        :return:
        """
        if random.randint(1, 100) <= self.__minimum_crushing_damage:
            damage = random.randint(self.__minimum_crushing_damage, self.__maximum_crushing_damage)
            enemy.set_current_hit_points(enemy.get_current_hit_points() - damage)
            print(f'{enemy.get_name()} took {damage} damage! {enemy.get_name()} now has {enemy.get_current_hit_points()} hit points!')
        else:
            print("Your Crushing Blow missed!")

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


