from item import Item
from dungeon_character import DungeonCharacter


class HealthPotion(Item):
    def __init__(self, location, health_change_value):
        super().__init__(location, health_change_value)

    def change_health(self):
        hit_points = DungeonCharacter.get_hit_points()
        hit_points += self.__health_change_value
        DungeonCharacter.set_hit_points(hit_points)

    def add_to_backpack(self):
        """We need to be able to pick up potions and put them in our backpack/inventory
        """