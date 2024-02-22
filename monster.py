from abc import ABC, abstractmethod
from dungeon_character import DungeonCharacter


class Monster(DungeonCharacter):

    def __init__(self,
                 name,
                 hit_points,
                 attack_speed,
                 chance_to_hit,
                 minimum_damage,
                 maximum_damage,
                 chance_to_heal,
                 minimum_heal_points,
                 maximum_heal_points,
                 ):
        super().__init__(name, hit_points, attack_speed, chance_to_hit, minimum_damage, maximum_damage)

        self.__movement = (0, 0)
        self.__direction = 0
        self.__chance_to_heal = chance_to_heal
        self.__minimum_heal_points = minimum_heal_points
        self.__maximum_heal_points = maximum_heal_points
        self.__monster_goal = None

    def get_chance_to_heal(self):
        return self.__chance_to_heal

    def get_minimum_heal_points(self):
        return self.__minimum_heal_points

    def get_maximum_heal_points(self):
        return self.__maximum_heal_points

    def set_chance_to_heal(self, chance_to_heal):
        self.__chance_to_heal = chance_to_heal

    def set_minimum_heal_points(self, minimum_heal_points):
        self.__minimum_heal_points = minimum_heal_points

    def set_maximum_heal_points(self, maximum_heal_points):
        self.__maximum_heal_points = maximum_heal_points

    def set_monster_movement(self, monster_movement):
        self.__movement = monster_movement

    def get_monster_movement(self):
        return self.__movement

    def set_monster_direction(self, monster_direction):
        self.__direction = monster_direction

    def get_monster_direction(self):
        return self.__direction

    def set_monster_goal(self, monster_goal):
        self.__monster_goal = monster_goal

    def get_monster_goal(self):
        return self.__monster_goal



# Abstract classes are parent classes. We write them to consolidate information for objects that share characteristic
# We do it when there isn't enough information to warrant an instance of a class.

# Any set methods need to ensure the data being passed in looks okay, and if not, raise an exception.


