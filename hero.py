import random
from dungeon_character import DungeonCharacter
from abc import ABC, abstractmethod
from item import Item

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
        self.__chance_to_block = chance_to_block

        self.__pillars = []
        self.__health_potions = [["Health Potions", 0]]

    def get_chance_to_block(self):
        return self.__chance_to_block

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

    def add_to_backpack(self, item):
        """ Add an item to the backpack. """

        if item == Item.health_potion:
            self.__health_potions[0][1] += 1
            print("You have added the health potion to your bag!")
            print(f"{self.__health_potions}")

        # Adding pillars to the backpack
        elif item == Items.pillar_of_inheritance:
            self.__pillars.append(Items.pillar_of_inheritance(self))
            print(self.__pillars)

        elif item == Items.pillar_of_polymorphism:
            self.__pillars.append(Items.pillar_of_polymorphism(self))
            print(self.__pillars)

        elif item == Items.pillar_of_abstraction:
            self.__pillars.append(Items.pillar_of_abstraction(self))
            print(self.__pillars)

        elif item == Items.pillar_of_encapsulation:
            self.__pillars.append(Items.pillar_of_encapsulation(self))
            print(self.__pillars)

    def take_healing_potion(self):
        if 0 < len(self.__health_potions):
            health_potion = self.__health_potions.pop()
            self.__hit_points += health_potion.healing_points
            print(f"Drinking that potion increased your health by {healing_potion.healing_points}!"
                  f"\n\nYou now have {self.hit_points} Hit Points.")
        else:
            print("You don't have any healing potions!")
            pass