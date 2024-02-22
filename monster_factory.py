import random
import sqlite3
from monster import Monster
from ogre import Ogre
from gremlin import Gremlin
from skeleton import Skeleton
from dungeon_character import DungeonCharacter


class MonsterFactory:
    def __init__(self):
        self.__conn = sqlite3.connect('dungeon_monsters.db')

    def read_monster_database(self, row):
        cursor = self.__conn.cursor()
        cursor.execute(f'SELECT * FROM monsters WHERE monster = "{row}"')
        monster_data = cursor.fetchone()
        return monster_data

    def create_ogre(self):
        ogre_stats = self.read_monster_database("Ogre")
        (name,
         hit_points,
         attack_speed,
         chance_to_hit,
         minimum_damage,
         maximum_damage,
         chance_to_heal,
         minimum_heal_points,
         maximum_heal_points) = ogre_stats
        return Ogre(name, hit_points, attack_speed, chance_to_hit, minimum_damage, maximum_damage, chance_to_heal,
                       minimum_heal_points, maximum_heal_points)

    def create_gremlin(self):
        gremlin_stats = self.read_monster_database("Gremlin")
        (name,
         hit_points,
         attack_speed,
         chance_to_hit,
         minimum_damage,
         maximum_damage,
         chance_to_heal,
         minimum_heal_points,
         maximum_heal_points) = gremlin_stats
        return Gremlin(name, hit_points, attack_speed, chance_to_hit, minimum_damage, maximum_damage, chance_to_heal,
                    minimum_heal_points, maximum_heal_points)


    def create_skeleton(self):
        skeleton_stats = self.read_monster_database("Skeleton")
        (name,
         hit_points,
         attack_speed,
         chance_to_hit,
         minimum_damage,
         maximum_damage,
         chance_to_heal,
         minimum_heal_points,
         maximum_heal_points) = skeleton_stats
        return Skeleton(name, hit_points, attack_speed, chance_to_hit, minimum_damage, maximum_damage, chance_to_heal,
                       minimum_heal_points, maximum_heal_points)

    def choose_monster(self):
        monster_choice = random.randint(1, 1)
        if monster_choice == 1:
            choice = self.create_ogre()
            return choice
        if monster_choice == 2:
            choice = self.create_gremlin()
            return choice
        if monster_choice == 3:
            choice = self.create_skeleton()
            return choice

    def create_monster(self):
        monster_stats = self.choose_monster()
        (name,
         hit_points,
         attack_speed,
         chance_to_hit,
         minimum_damage,
         maximum_damage,
         chance_to_heal,
         minimum_heal_points,
         maximum_heal_points) = monster_stats


        return Monster(name, hit_points, attack_speed, chance_to_hit, minimum_damage, maximum_damage, chance_to_heal,
                       minimum_heal_points, maximum_heal_points)

    def main(self):
        pass


if __name__ == '__main__':
    u = MonsterFactory()
    creature = u.choose_monster()
    creature.get_name()
