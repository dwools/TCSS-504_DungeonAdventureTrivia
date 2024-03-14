import random
import sqlite3
from Characters.hero_priestess import Priestess
from Characters.hero_knight import Knight
from Characters.hero_rogue import Rogue



class HeroFactory:
    def __init__(self):
        self.__conn1 = sqlite3.connect('Databases/database_heroes.db')
        self.__conn2 = sqlite3.connect('Databases/database_names.db')

    def read_hero_database(self, row):
        cursor = self.__conn1.cursor()
        cursor.execute(f'SELECT * FROM heroes WHERE hero = "{row}"')
        monster_data = cursor.fetchone()
        return monster_data

    def read_name_database(self):
        cursor = self.__conn2.cursor()
        cursor.execute(f'SELECT latin_name from names WHERE rowid > ABS(random()) % ('f'SELECT max(rowid) from names) LIMIT 1')
        monster_name = cursor.fetchone()
        return monster_name

    def create_priestess(self, chance_to_heal=70, minimum_heal_points=30, maximum_heal_points=60):
        name = self.read_name_database()
        (name,) = name
        priestess_stats = self.read_hero_database("Priestess")
        (type,
         hit_points,
         attack_speed,
         chance_to_hit,
         minimum_damage,
         maximum_damage,
         chance_to_block
         ) = priestess_stats

        return Priestess(name, type, hit_points, attack_speed, chance_to_hit, minimum_damage, maximum_damage, chance_to_block, chance_to_heal, minimum_heal_points, maximum_heal_points)

    def create_knight(self, chance_for_crushing_blow=40, minimum_crushing_damage=75, maximum_crushing_damage=175):
        name = self.read_name_database()
        (name,) = name
        knight_stats = self.read_hero_database("Knight")
        (type,
         hit_points,
         attack_speed,
         chance_to_hit,
         minimum_damage,
         maximum_damage,
         chance_to_block
         ) = knight_stats

        return Knight(name, type, hit_points, attack_speed, chance_to_hit, minimum_damage, maximum_damage, chance_to_block, chance_for_crushing_blow, minimum_crushing_damage, maximum_crushing_damage)

    def create_rogue(self, chance_for_second_attack=40, chance_caught = 40):
        name = self.read_name_database()
        (name,) = name
        rogue_stats = self.read_hero_database("Rogue")
        (type,
         hit_points,
         attack_speed,
         chance_to_hit,
         minimum_damage,
         maximum_damage,
         chance_to_block) = rogue_stats
        return Rogue(name, type, hit_points, attack_speed, chance_to_hit, minimum_damage, maximum_damage, chance_to_block, chance_for_second_attack, chance_caught)


if __name__ == '__main__':
    h = HeroFactory()
    k = h.create_knight()
    k.get_chance_for_crushing_blow()


