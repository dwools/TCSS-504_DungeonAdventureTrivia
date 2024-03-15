import random
import pygame as pg
from Assets import assets as a
from Characters.hero import Hero


class Rogue(Hero):
    def __init__(self,
                 name,
                 type,
                 hit_points,
                 attack_speed,
                 chance_to_hit,
                 minimum_damage,
                 maximum_damage,
                 chance_to_block,
                 chance_for_second_attack,
                 chance_caught
                 ):

        super().__init__(name,
                         type,
                         hit_points,
                         attack_speed,
                         chance_to_hit,
                         minimum_damage,
                         maximum_damage,
                         chance_to_block)

        self.__chance_for_second_attack = chance_for_second_attack
        self.__chance_caught = chance_caught

        self.__sprite_north = pg.image.load(a.north_rogue)
        self.__sprite_east = pg.image.load(a.east_rogue)
        self.__sprite_west = pg.image.load(a.west_rogue)
        self.__sprite_south = pg.image.load(a.south_rogue)
        
    def get_chance_for_second_attack(self):
        return self.__chance_for_second_attack

    def get_chance_caught(self):
        return self.__chance_caught

    def special(self, enemy):
        self.simple_attack(enemy)
        if random.randint(1, 100) <= self.__chance_for_second_attack:
            print("You try for a second attack!")
            if random.randint(1, 100) <= self.__chance_caught:
                print("But you got caught! Your second attack failed!")
            else:
                self.simple_attack(enemy)

    def count_simple_attacks_in_special(self, enemy):
        initial_count = self.simple_attack.attack_count
        for _ in range(10):
            self.special(enemy)
        attacks_in_special = self.simple_attack.attack_count - initial_count
        return attacks_in_special
    
    def get_sprite_north(self):
        return self.__sprite_north

    def get_sprite_east(self):
        return self.__sprite_east

    def get_sprite_west(self):
        return self.__sprite_west

    def get_sprite_south(self):
        return self.__sprite_south
