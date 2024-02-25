import assets as a
from monster import Monster


class Skeleton(Monster):
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

        self.__east_sprite = a.east_skelly
        self.__north_sprite = a.north_skelly
        self.__west_sprite = a.west_skelly
        self.__south_sprite = a.south_skelly

    def get_south_sprite(self):
        return self.__south_sprite

    def get_north_sprite(self):
        return self.__north_sprite

    def get_east_sprite(self):
        return self.__east_sprite

    def get_west_sprite(self):
        return self.__west_sprite
