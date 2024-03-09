from item import Item
from dungeon_character import DungeonCharacter


class PitTrap(Item):
    def __init__(self, health_change_value):
        # self.__location = location
        super().__init__(health_change_value)
        self.__pit_trap_sprite = None
        # self.__collision_rects = []
        self.__player_scroll = [0, 0]

    def get_pit_trap_sprite(self):
        return self.__pit_trap_sprite
    def set_pit_trap_sprite(self, sprite_path):
        self.__pit_trap_sprite = sprite_path

    def change_health(self):
        hit_points = DungeonCharacter.get_hit_points()
        hit_points -= self.__health_change_value
        DungeonCharacter.set_hit_points(hit_points)

