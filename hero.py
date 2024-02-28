import random
from dungeon_character import DungeonCharacter
from abc import ABC, abstractmethod


class Hero(DungeonCharacter):
    def __init__(self, name,
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
                         maximum_damage)
        self.chance_to_block = chance_to_block

    def get_chance_to_block(self):
        return self.chance_to_block
    #
    # def roll_for_special_attack(self, chance_for_bonus_damage):
    #     if random.random() < chance_for_bonus_damage:
    #         self.special_attack()

    # def special_attack(self, chance_for_bonus_damage, minimum_bonus_damage, maximum_bonus_damage):
    #
    #     damage = random.randint(minimum_damage, maximum_damage)
    #     if random.random() < chance_to_hit:  # random.random() by default generates a random value between 0 and 1
    #         opponent.set_hit_points(opponent.get_hit_points() - damage)
    #
    # = random.randint(self.minimum_bonus_damage, self.maximum_bonus_damage)
    # if random.random() < self.chance_for_bonus_damage:
