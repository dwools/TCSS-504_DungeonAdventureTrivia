from abc import ABC, abstractmethod
from object_coordinates_generator import ValidCoordsGenerator


class DungeonCharacter(ABC):
    def __init__(self, name, hit_points, attack_speed, chance_to_hit, minimum_damage, maximum_damage):
        # Dungeon character needs a name per project specifications
        self.__name = name
        self.__hit_points = hit_points
        self.__attack_speed = attack_speed
        self.__chance_to_hit = chance_to_hit
        self.__minimum_damage = minimum_damage
        self.__maximum_damage = maximum_damage

        #  Generating random valid coords for the position
        # self.coords_generator = ValidCoordsGenerator()
        # self.__char_position = self.coords_generator.get_random_coords()
        # self.__position_x, self.__position_y = self.__char_position


        # self.__chance_to_block = None
        # self.__chance_to_heal = None
        # self.__minimum_heal_points = None
        # self.__maximum_heal_points = None
        # self.__chance_for_bonus_damage = None
        # self.__minimum_bonus_damage = None
        # self.__maximum_bonus_damage = None
        # self.__chance_for_second_attack = None

    def get_name(self):
        print(self.__name)
        return self.__name

    def get_hit_points(self):
        return self.__hit_points

    def get_attack_speed(self):
        return self.__attack_speed

    def get_chance_to_hit(self):
        return self.__chance_to_hit

    def get_minimum_damage(self):
        return self.__minimum_damage

    def get_maximum_damage(self):
        return self.__maximum_damage

    def get_position(self):
        return self.__char_position #  returns random coords in a [x,y] list

    # @abstractmethod
    # def set_character(self, character):
    #     self.__character = character
    #
    # @abstractmethod
    # def set_hit_points(self, hit_points):
    #     self.__hit_points = hit_points
    #
    # @abstractmethod
    # def set_attack_speed(self, attack_speed):
    #     self.__attack_speed = attack_speed
    #
    # @abstractmethod
    # def set_chance_to_hit(self, chance_to_hit):
    #     self.__chance_to_hit = chance_to_hit
    #
    # @abstractmethod
    # def set_minimum_damage(self, minimum_damage):
    #     self.__minimum_damage = minimum_damage
    #
    # @abstractmethod
    # def set_maximum_damage(self, maximum_damage):
    #     self.__maximum_damage = maximum_damage

# if __name__ == '__main__':