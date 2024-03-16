import random
from abc import ABC, abstractmethod
from Characters.dungeon_character import DungeonCharacter
from Items.item import Item
from Pillars_and_Trivia.pillar import Pillar

def simple_attack_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.special_simple_attack_count += 1
        return func(*args, **kwargs)

    wrapper.special_simple_attack_count = 0
    return wrapper

class Hero(DungeonCharacter, ABC):
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


    def get_chance_to_block(self):
        return self.__chance_to_block


    def add_to_backpack(self, item):
        """ Add an item to the backpack. """

        if isinstance(item, Item):
            self.__player_health_potions.append(item)
            print("You have added the health potion to your bag!")
            print(f"Health potions: {len(self.__player_health_potions)}")

        if isinstance(item, Pillar):
            self.__player_pillars.append(item)
            print(f"Congratulations! You have acquired {len(self.__player_pillars)} out of 4 pillars!")


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

    def get_player_health_potions(self):
        return self.__player_health_potions

    def get_player_pillars(self):
        return self.__player_pillars



    @simple_attack_counter
    def simple_attack(self, enemy):
        print(f'{self.get_name()} tries a simple attack...')
        if random.randint(1, 100) <= self.get_chance_to_hit():
            damage = random.randint(self.get_minimum_damage(), self.get_maximum_damage())
            enemy.set_current_hit_points(enemy.get_current_hit_points() - damage)
            print(
                f'{enemy.get_name()} took {damage} damage! {enemy.get_name()} now has {enemy.get_current_hit_points()} hit points!')
        else:
            print(f"{self.get_name()}'s attack missed!")

    # def simple_attack2(self, enemy):
    #     print(f'{enemy.get_name()} tries a simple attack...')
    #     if random.randint(1, 100) <= enemy.get_chance_to_hit():
    #         if random.randint(1, 100) <= self.get_chance_to_block():
    #             print(f'but {self.get_name()} blocked the attack!')
    #         else:
    #             damage = random.randint(enemy.get_minimum_damage(), enemy.get_maximum_damage())
    #             self.set_current_hit_points(self.get_current_hit_points() - damage)
    #             print(f'{self.__name} took {damage} damage! {self.__name} now has {self.get_current_hit_points()} hit points!')
    #     else:
    #         print(f"{enemy.get_name}'s attack missed!")

    @abstractmethod
    def special(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_sprite_north(self):
        pass

    @abstractmethod
    def get_sprite_east(self):
        pass

    @abstractmethod
    def get_sprite_west(self):
        pass

    @abstractmethod
    def get_sprite_south(self):
        pass

    @abstractmethod
    def set_character_sprites(self, *args, **kwargs):
        pass