from abc import ABC, abstractmethod
from Characters.dungeon_character import DungeonCharacter
from Items.item import Item
from Pillars_and_Trivia.pillar import Pillar


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

        self.__player_pillars = []
        self.__player_health_potions = []
        self.__death = False


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

        if isinstance(item, Item):
            self.__player_health_potions.append(item)
            print("You have added the health potion to your bag!")
            print(f"Health potions: {len(self.__player_health_potions)}")

        if isinstance(item, Pillar):
            self.__player_pillars.append(item)
            print(f"Congratulations! You have acquired {len(self.__player_pillars)} out of 4 pillars!")

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

    def drink_health_potion(self):
        if 0 < len(self.__player_health_potions):
            health_potion = self.__player_health_potions.pop()
            self.set_current_hit_points(self.get_current_hit_points() + health_potion.get_health_change_value())
            if self.get_current_hit_points() > self.get_max_hit_points():
                self.set_current_hit_points(self.get_max_hit_points())

            print(f"Drinking that potion increased your health by {health_potion.get_health_change_value()}!"
                  f"\n\nYou now have {self.get_current_hit_points()} Hit Points.")
        else:
            print("You don't have any healing potions!")
            pass

    def damage(self, value):
        self.set_current_hit_points(self.get_current_hit_points() - value)
        if self.get_current_hit_points() <= 0:  # Checking for 0 hit points can go here or in its own section in the game loop
            self.__death = True
        print(f"Ouch! You lost {value} hit points! You now have {self.get_current_hit_points()} hit points.")


    def get_death(self):
        return self.__death

    def set_death(self, value):
        self.__death = True

    def get_player_health_potions(self):
        return self.__player_health_potions

    def get_player_pillars(self):
        return self.__player_pillars

    # def simple_attack(self, enemy):  # Hero's attack
    #     if random.randint(1, 100) <= self.__chance_to_hit:
    #         enemy.set_current_hit_points(
    #             random.randint(self.__minimum_damage, self.__maximum_damage))
    #     else:
    #         print("Your attack missed!")
    #         pass

    @abstractmethod
    def special(self, *args, **kwargs):
        pass
