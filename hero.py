import random
from dungeon_character import DungeonCharacter
from abc import ABC, abstractmethod
from item import Item
from item_health_potion import HealthPotion
from item_pit_trap import FireTrap
from pillar import Pillar


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
        self.__health_potions = []

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

        if isinstance(item, HealthPotion):
            self.__health_potions.append(item)
            print("You have added the health potion to your bag!")
            print(f"Health potions: {len(self.__health_potions)}")

        if isinstance(item, Pillar):
            self.__pillars.append(item)
            print(f"Congratulations! You have acquired {len(self.__pillars)} out of 4 pillars!")

        # if isinstance(item, Pillar):
        #     self.__pillars.append(item)

        # Adding pillars to the backpack
        # elif item == Item.pillar_of_inheritance:
        #     self.__pillars.append(Item.pillar_of_inheritance(self))
        #     print(self.__pillars)
        #
        # elif item == Item.pillar_of_polymorphism:
        #     self.__pillars.append(Item.pillar_of_polymorphism(self))
        #     print(self.__pillars)
        #
        # elif item == Item.pillar_of_abstraction:
        #     self.__pillars.append(Item.pillar_of_abstraction(self))
        #     print(self.__pillars)
        #
        # elif item == Item.pillar_of_encapsulation:
        #     self.__pillars.append(Item.pillar_of_encapsulation(self))
        #     print(self.__pillars)

    def take_healing_potion(self):
        if 0 < len(self.__health_potions):
            health_potion = self.__health_potions.pop()
            added_health_points = health_potion.get_health_change_value()
            self.__current_hit_points += added_health_points
            if self.__current_hit_points > self.__max_hit_points:
                self.__current_hit_points = self.__max_hit_points

            print(f"Drinking that potion increased your health by {added_health_points}!"
                  f"\n\nYou now have {self.__current_hit_points} Hit Points.")
        else:
            print("You don't have any healing potions!")
            pass

    def damage(self, value):
        hit_points = self.get_current_hit_points()
        self.set_current_hit_points(hit_points - value)
        # self.__current_hit_points -= value
        print(f"Ouch! You lost {value} hit points! You now have {hit_points} hit points.")
