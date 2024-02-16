import random
import sqlite3
from Monster import Monster
from DungeonCharacter import DungeonCharacter


class MonsterFactory():
    def __init__(self):
        self.__conn = sqlite3.connect('dungeon_monsters.db')

    def read_monster_database(self, row):
        cursor = self.__conn.cursor()
        cursor.execute(f'SELECT * FROM monsters WHERE monster = "{row}"')
        monster_data = cursor.fetchone()
        return monster_data

    def create_ogre(self):
        ogre = self.read_monster_database("Ogre")
        print(ogre)
        return ogre

    def create_gremlin(self):
        gremlin = self.read_monster_database("Gremlin")
        print(gremlin)
        return gremlin

    def create_skeleton(self):
        skeleton = self.read_monster_database("Skeleton")
        print(skeleton)
        return skeleton

    def choose_monster(self):
        monster_choice = random.randint(1, 3)
        if monster_choice == 1:
            choice = self.create_ogre()
            return choice
        elif monster_choice == 2:
            choice = self.create_gremlin()
            return choice
        elif monster_choice == 3:
            choice = self.create_skeleton()
            return choice

    def create_monster(self):
        monster_stats = self.choose_monster()
        return Monster(*monster_stats)

    def main(self):
        pass



if __name__ == '__main__':
    u = MonsterFactory()
    creature = u.create_monster()
    creature.get_character()
