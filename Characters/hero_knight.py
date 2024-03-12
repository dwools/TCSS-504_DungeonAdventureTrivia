import random

from Characters.hero import Hero


class Knight(Hero):
    # to give a crushing blow is a CHOICE that the knight has.
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

        self.__chance_for_crushing_blow = 40
        self.__minimum_crushing_damage = 75
        self.__maximum_crushing_damage = 125

    def get_chance_for_crushing_blow(self):
        print(self.__chance_for_crushing_blow)
        return self.__chance_for_crushing_blow

    def get_minimum_crushing_damage(self):
        return self.__minimum_crushing_damage

    def get_maximum_crushing_damage(self):
        return self.__maximum_crushing_damage

    def special(self, enemy):
        if random.randint(1, 100) <= self.__minimum_crushing_damage:
            damage = random.randint(self.__minimum_crushing_damage, self.__maximum_crushing_damage)
            enemy.set_current_hit_points(enemy.get_current_hit_points() - damage)
            print(f'{enemy.get_name()} took {damage} damage! {enemy.get_name()} now has {enemy.get_current_hit_points()} hit points!')
        else:
            print("Your Crushing Blow missed!")




