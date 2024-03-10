from item import Item
from dungeon_character import DungeonCharacter


class FireTrap(Item):
    def __init__(self):
        # self.__location = location
        super().__init__()
        self.__fire_trap_sprite = None
        # self.__collision_rects = []
        self.__player_scroll = [0, 0]

    def get_fire_trap_sprite(self):
        return self.__fire_trap_sprite

    def set_fire_trap_sprite(self, sprite_path):
        self.__fire_trap_sprite = sprite_path



