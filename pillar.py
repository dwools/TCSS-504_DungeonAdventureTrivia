import pygame as pg
class Pillar():
    def __init__(self, pillar_name):
        self.__pillar_name = pillar_name
        self.__pillar_position = [0, 0]
        self.__pillar_position_x, self.__pillar_position_y = self.__pillar_position
        self.__rect = pg.Rect(self.__pillar_position_x, self.__pillar_position_y, 16, 16)
        self.__abstraction_pillar_sprite = None
        self.__encapsulation_pillar_sprite = None
        self.__inheritance_pillar_sprite = None
        self.__polymorphism_pillar_sprite = None

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
        return self.__abstraction_pillar_sprite

    def get_encapsulation_sprite(self):
        return self.__encapsulation_pillar_sprite

    def get_inheritance_sprite(self):
        return self.__inheritance_pillar_sprite

    def get_polymorphism_sprite(self):
        return self.__polymorphism_pillar_sprite
    
    def set_abstraction_sprite(self, sprite_path):
        self.__abstraction_pillar_sprite = sprite_path

    def set_encapsulation_sprite(self, sprite_path):
        self.__encapsulation_pillar_sprite = sprite_path

    def set_inheritance_sprite(self, sprite_path):
        self.__inheritance_pillar_sprite = sprite_path

    def set_polymorphism_sprite(self, sprite_path):
        self.__polymorphism_pillar_sprite = sprite_path