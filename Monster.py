from abc import ABC, abstractmethod
from DungeonCharacter import DungeonCharacter


class Monster(ABC, DungeonCharacter):

    def __init__(self, chance_to_heal=None, minimum_heal_points=None, maximum_heal_points=None):
        super().__init__()
        self.__chance_to_heal = chance_to_heal
        self.__minimum_heal_points = minimum_heal_points
        self.__maximum_heal_points = maximum_heal_points

    def get_chance_to_heal(self):
        return self.__chance_to_heal

    def get_minimum_heal_points(self):
        return self.__minimum_heal_points

    def get_maximum_heal_points(self):
        return self.__maximum_heal_points

    @abstractmethod
    def set_chance_to_heal(self, chance_to_heal):
        self.__chance_to_heal = chance_to_heal

    @abstractmethod
    def set_minimum_heal_points(self, minimum_heal_points):
        self.__minimum_heal_points = minimum_heal_points

    @abstractmethod
    def set_maximum_heal_points(self, maximum_heal_points):
        self.__maximum_heal_points = maximum_heal_points
