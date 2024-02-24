import random
import sqlite3
from hero import Hero

from dungeon_character import DungeonCharacter


class MonsterFactory:
    def __init__(self):
        self.__conn1 = sqlite3.connect('dungeon_monsters.db')
        self.__conn2 = sqlite3.connect('monster_names.db')

    def read_hero_database(self, row):
        cursor = self.__conn1.cursor()
        cursor.execute(f'SELECT * FROM heroes WHERE hero = "{row}"')
        monster_data = cursor.fetchone()
        return monster_data

    def read_name_database(self):
        cursor = self.__conn2.cursor()
        cursor.execute(f'SELECT latin_name from monster_names WHERE rowid > ABS(random()) % ('f'SELECT max(rowid) from monster_names) LIMIT 1')
        monster_name = cursor.fetchone()
        return monster_name

    def create_priestess(self):
        name = self.read_name_database()
        (name,) = name
        priestess_stats = self.read_hero_database("Priestess")
        (type,
         hit_points,
         attack_speed,
         chance_to_hit,
         minimum_damage,
         maximum_damage,
         chance_to_block,
         chance_to_heal,
         minimum_heal_points,
         maximum_heal_points,
         chance_for_bonus_damage,
         minimum_bonus_damage,
         maximum_bonus_damage,
         chance_for_second_attack) = priestess_stats
        return Hero(name, type, hit_points, attack_speed, chance_to_hit, minimum_damage, maximum_damage, chance_to_block, chance_to_heal, minimum_heal_points, maximum_heal_points, chance_for_bonus_damage, minimum_bonus_damage, maximum_bonus_damage, chance_for_second_attack)

    def create_knight(self):
        name = self.read_name_database()
        (name,) = name
        knight_stats = self.read_hero_database("Knight")
        (type,
         hit_points,
         attack_speed,
         chance_to_hit,
         minimum_damage,
         maximum_damage,
         chance_to_block,
         chance_to_heal,
         minimum_heal_points,
         maximum_heal_points,
         chance_for_bonus_damage,
         minimum_bonus_damage,
         maximum_bonus_damage,
         chance_for_second_attack) = knight_stats
        return Hero(name, type, hit_points, attack_speed, chance_to_hit, minimum_damage, maximum_damage, chance_to_block, chance_to_heal, minimum_heal_points, maximum_heal_points, chance_for_bonus_damage, minimum_bonus_damage, maximum_bonus_damage, chance_for_second_attack)

    def create_rogue(self):
        name = self.read_name_database()
        (name,) = name
        rogue_stats = self.read_hero_database("Rogue")
        (type,
         hit_points,
         attack_speed,
         chance_to_hit,
         minimum_damage,
         maximum_damage,
         chance_to_block,
         chance_to_heal,
         minimum_heal_points,
         maximum_heal_points,
         chance_for_bonus_damage,
         minimum_bonus_damage,
         maximum_bonus_damage,
         chance_for_second_attack) = rogue_stats
        return Hero(name, type, hit_points, attack_speed, chance_to_hit, minimum_damage, maximum_damage, chance_to_block, chance_to_heal, minimum_heal_points, maximum_heal_points, chance_for_bonus_damage, minimum_bonus_damage, maximum_bonus_damage, chance_for_second_attack)

    # def choose_monster(self):
    #     monster_choice = random.randint(1, 3)
    #     if monster_choice == 1:
    #         choice = self.create_priestess()
    #         return choice
    #     if monster_choice == 2:
    #         choice = self.create_knight()
    #         return choice
    #     if monster_choice == 3:
    #         choice = self.create_rogue()
    #         return choice

    # def create_monster(self):
    #     name = self.read_name_database()
    #     (name,) = name
    #     monster_stats = self.choose_monster()
    #     (type,
    #      hit_points,
    #      attack_speed,
    #      chance_to_hit,
    #      minimum_damage,
    #      maximum_damage,
    #      chance_to_heal,
    #      minimum_heal_points,
    #      maximum_heal_points) = monster_stats
    #
    #     return Monster(name, type, hit_points, attack_speed, chance_to_hit, minimum_damage, maximum_damage, chance_to_heal,
    #                    minimum_heal_points, maximum_heal_points)

    def main(self):
        pass


