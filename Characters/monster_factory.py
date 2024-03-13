import random
import sqlite3
from Characters.monster import Monster


class MonsterFactory:
    def __init__(self):
        self.__conn1 = sqlite3.connect('Databases/dungeon_monsters.db')
        self.__conn2 = sqlite3.connect('Databases/monster_names.db')

    def read_monster_database(self, row):
        cursor = self.__conn1.cursor()
        cursor.execute(f'SELECT * FROM monsters WHERE monster = "{row}"')
        monster_data = cursor.fetchone()
        return monster_data

    def read_name_database(self):
        cursor = self.__conn2.cursor()
        cursor.execute(f'SELECT latin_name from monster_names WHERE rowid > ABS(random()) % ('
                       f'SELECT max(rowid) from monster_names) LIMIT 1')
        monster_name = cursor.fetchone()
        return monster_name

    def create_ogre(self):
        name = self.read_name_database()
        (name,) = name
        ogre_stats = self.read_monster_database("Ogre")
        (type,
         hit_points,
         attack_speed,
         chance_to_hit,
         minimum_damage,
         maximum_damage,
         chance_to_heal,
         minimum_heal_points,
         maximum_heal_points) = ogre_stats
        return Monster(name, type, hit_points, attack_speed, chance_to_hit, minimum_damage, maximum_damage, chance_to_heal,
                    minimum_heal_points, maximum_heal_points)

    def create_gremlin(self):
        name = self.read_name_database()
        (name,) = name
        gremlin_stats = self.read_monster_database("Gremlin")
        (type,
         hit_points,
         attack_speed,
         chance_to_hit,
         minimum_damage,
         maximum_damage,
         chance_to_heal,
         minimum_heal_points,
         maximum_heal_points) = gremlin_stats
        return Monster(name, type, hit_points, attack_speed, chance_to_hit, minimum_damage, maximum_damage, chance_to_heal,
                       minimum_heal_points, maximum_heal_points)

    def create_skeleton(self):
        name = self.read_name_database()
        (name,) = name
        skeleton_stats = self.read_monster_database("Skeleton")
        (type,
         hit_points,
         attack_speed,
         chance_to_hit,
         minimum_damage,
         maximum_damage,
         chance_to_heal,
         minimum_heal_points,
         maximum_heal_points) = skeleton_stats
        return Monster(name, type, hit_points, attack_speed, chance_to_hit, minimum_damage, maximum_damage, chance_to_heal,
                        minimum_heal_points, maximum_heal_points)

    def choose_monster(self):
        monster_choice = random.randint(1, 3)
        if monster_choice == 1:
            return self.create_ogre()

        elif monster_choice == 2:
            return self.create_gremlin()
            # return choice
        elif monster_choice == 3:
            return self.create_skeleton()
            # return choice

    def create_monster(self):
        name = self.read_name_database()
        (name,) = name
        monster_stats = self.choose_monster()
        (type,
         hit_points,
         attack_speed,
         chance_to_hit,
         minimum_damage,
         maximum_damage,
         chance_to_heal,
         minimum_heal_points,
         maximum_heal_points) = monster_stats

        return Monster(name, type, hit_points, attack_speed, chance_to_hit, minimum_damage, maximum_damage, chance_to_heal,
                       minimum_heal_points, maximum_heal_points)

    def main(self):
        pass

#
# if __name__ == '__main__':
#     u = MonsterFactory()
#     creature1 = u.choose_monster()
#     creature1.get_name()
#     creature1.get_type()
#     creature2 = u.choose_monster()
#     creature2.get_name()
#     creature2.get_type()