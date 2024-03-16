import pygame as pg
from Assets import assets as a
class Pillar():
    def __init__(self, pillar_name):
        """
        placing pillars within the maze, there are 4 pillars: Abstraction, Encapsulation, Inheritance,
        and Polymorphism
        :param pillar_name:
        """

        self.__pillar_name = pillar_name
        self.__pillar_position = [0, 0]
        self.__pillar_position_x, self.__pillar_position_y = self.__pillar_position
        self.__rect = pg.Rect(self.__pillar_position_x, self.__pillar_position_y, 16, 16)
        self.__pillar_sprite_abstraction = pg.image.load(a.abstraction_pillar)
        self.__pillar_sprite_encapsulation = pg.image.load(a.encapsulation_pillar)
        self.__pillar_sprite_inheritance = pg.image.load(a.inheritance_pillar)
        self.__pillar_sprite_polymorphism = pg.image.load(a.polymorphism_pillar)

    def get_pillar_name(self):
        return self.__pillar_name

    def get_pillar_position(self):
        return self.__pillar_position

    def set_pillar_position(self, pillar_position):
        self.__pillar_position = pillar_position
        self.__pillar_position_x, self.__pillar_position_y = pillar_position

    def set_player_scroll(self, scroll):
        self.__player_scroll = scroll

    def get_pillar_rect(self):
        return self.__rect

    def set_pillar_rect(self, x, y):
        self.__rect = pg.Rect(y, x, 16, 16)

    def get_abstraction_sprite(self):
        return self.__pillar_sprite_abstraction

    def get_encapsulation_sprite(self):
        return self.__pillar_sprite_encapsulation

    def get_inheritance_sprite(self):
        return self.__pillar_sprite_inheritance

    def get_polymorphism_sprite(self):
        return self.__pillar_sprite_polymorphism
    
    def set_abstraction_sprite(self, sprite_path):
        self.__pillar_sprite_abstraction = sprite_path

    def set_encapsulation_sprite(self, sprite_path):
        self.__pillar_sprite_encapsulation = sprite_path

    def set_inheritance_sprite(self, sprite_path):
        self.__pillar_sprite_inheritance = sprite_path

    def set_polymorphism_sprite(self, sprite_path):
        self.__pillar_sprite_polymorphism = sprite_path