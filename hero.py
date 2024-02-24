import random
from dungeon_character import DungeonCharacter

class Hero(DungeonCharacter):
    def __init__(self, name, type, hit_points, attack_speed, chance_to_hit, minimum_damage, maximum_damage, chance_to_block, chance_to_heal, minimum_heal_points, maximum_heal_points, chance_for_bonus_damage, minimum_bonus_damage, maximum_bonus_damage, chance_for_second_attack):
        super().__init__(name, type, hit_points, attack_speed, chance_to_hit, minimum_damage, maximum_damage)
        self.chance_to_block = chance_to_block
        self.chance_to_heal = chance_to_heal
        self.minimum_heal_points = minimum_heal_points
        self.maximum_heal_points = maximum_heal_points
        self.chance_for_bonus_damage = chance_for_bonus_damage
        self.minimum_bonus_damage = minimum_bonus_damage
        self.maximum_bonus_damage = maximum_bonus_damage
        self.chance_for_second_attack = chance_for_second_attack

    @abstractmethod
    def flee(self):
        pass

class Knight(Hero):
    def roll_for_special_attack(self, chance_for_bonus_damage):
        if random.random() < chance_for_bonus_damage:
            self.special_attack()

# to give a crushing blow is a CHOICE that the knight has.

    def special_attack(self, chance_for_bonus_damage, minimum_bonus_damage, maximum_bonus_damage):

            damage = random.randint(minimum_damage, maximum_damage)
            if random.random() < chance_to_hit:  # random.random() by default generates a random value between 0 and 1
                opponent.set_hit_points(opponent.get_hit_points() - damage)
        = random.randint(self.minimum_bonus_damage, self.maximum_bonus_damage)
        if random.random() < self.chance_for_bonus_damage:
