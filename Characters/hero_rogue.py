import random

from Characters.hero import Hero


class Rogue(Hero):
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

        self.__chance_for_second_attack = 40
        self.__chance_caught = 20
        # self.

    def get_chance_for_second_attack(self):
        return self.__chance_for_second_attack

    def get_chance_caught(self):
        return self.__chance_caught

    def special(self, enemy):
        self.simple_attack(enemy)
        if random.randint(1, 100) <= self.__chance_for_second_attack:
            print("You try for a second attack!")
            if random.randint(1, 100) <= self.__chance_caught:
                print("But you got caught! Your second attack failed!")
            else:
                self.simple_attack(enemy)
