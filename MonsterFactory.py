import random

import DungeonCharacter


class MonsterFactory(DungeonCharacter):
    def __init__(self):
        pass

    def create_ogre(self):
        pass

    def create_gremlin(self):
        pass

    def create_skeleton(self):
        pass

    def main(self):
        monster_choice = random.randint(1, 3)
        if monster_choice == 1:
            self.create_ogre()
        elif monster_choice == 2:
            self.create_gremlin()
        elif monster_choice == 3:
            self.create_skeleton()
