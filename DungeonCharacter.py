import abc


class DungeonCharacter(abc.ABC):
    def __init__(self):
        self.__character = None
        self.__hit_points = None
        self.__attack_speed = None
        self.__chance_to_hit = None
        self.__minimum_damage = None
        self.__maximum_damage = None
        # self.__chance_to_block = None
        # self.__chance_to_heal = None
        # self.__minimum_heal_points = None
        # self.__maximum_heal_points = None
        # self.__chance_for_bonus_damage = None
        # self.__minimum_bonus_damage = None
        # self.__maximum_bonus_damage = None
        # self.__chance_for_second_attack = None

    def get_character(self):
        return self.__character

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

    def set_character(self, character):
        self.__character = character

    def set_hit_points(self, hit_points):
        self.__hit_points = hit_points

    def set_attack_speed(self, attack_speed):
        self.__attack_speed = attack_speed

    def set_chance_to_hit(self, chance_to_hit):
        self.__chance_to_hit = chance_to_hit

    def set_minimum_damage(self, minimum_damage):
        self.__minimum_damage = minimum_damage

    def set_maximum_damage(self, maximum_damage):
        self.__maximum_damage = maximum_damage

