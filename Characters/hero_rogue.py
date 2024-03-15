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
                 chance_to_block,
                 chance_for_second_attack,
                 chance_caught
                 ):

        super().__init__(name,
                         type,
                         hit_points,
                         attack_speed,
                         chance_to_hit,
                         minimum_damage,
                         maximum_damage,
                         chance_to_block)

        self.__chance_for_second_attack = chance_for_second_attack
        self.__chance_caught = chance_caught

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

    def count_simple_attacks_in_special(self, enemy):
        initial_count = self.simple_attack.attack_count
        for _ in range(10):
            self.special(enemy)
        attacks_in_special = self.simple_attack.attack_count - initial_count
        return attacks_in_special
