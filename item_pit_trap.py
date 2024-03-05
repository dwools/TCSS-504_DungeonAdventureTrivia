from item import Item
from dungeon_character import DungeonCharacter


class PitTrap(Item):
    def __init__(self, location, health_change_value):
        super().__init__(location, health_change_value)

    def change_health(self):
        hit_points = DungeonCharacter.get_hit_points()
        hit_points -= self.__health_change_value
        DungeonCharacter.set_hit_points(hit_points)