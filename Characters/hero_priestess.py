import random

from Characters.hero import Hero


class Priestess(Hero):
    def __init__(self,
                 name,
                 type,
                 hit_points,
                 attack_speed,
                 chance_to_hit,
                 minimum_damage,
                 maximum_damage,
                 chance_to_block):

        super().__init__(name,
                         type,
                         hit_points,
                         attack_speed,
                         chance_to_hit,
                         minimum_damage,
                         maximum_damage,
                         chance_to_block)
        self.__chance_to_heal = 70
        self.__minimum_heal_points = 30
        self.__maximum_heal_points = 60

    def get_chance_to_heal(self):
        return self.__chance_to_heal

    def get_minimum_heal_points(self):
        return self.__minimum_heal_points

    def get_maximum_heal_points(self):
        return self.__maximum_heal_points

    def special(self):
        if random.randint(1, 100) <= self.__chance_to_heal:
            self.set_current_hit_points(
                random.randint(self.__minimum_heal_points, self.__maximum_heal_points))
            if self.get_current_hit_points() >= self.get_max_hit_points():
                self.set_current_hit_points(self.get_max_hit_points())
        else:
            print("Your Special Healing Failed!")

