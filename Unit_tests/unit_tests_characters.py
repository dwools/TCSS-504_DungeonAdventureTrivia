import unittest
from Characters.hero_factory import HeroFactory
from Characters.hero_rogue import Rogue
from Characters.dungeon_character import DungeonCharacter
from Characters.hero import Hero
from Characters.monster import Monster
from Characters.monster_factory import MonsterFactory
import sqlite3
from Databases import initialize_databases
from Databases import *
from Databases import initialize_trivia_database



class CharacterUnitTests(unittest.TestCase):
    # def __init__(self):
    #     .__init__()

    def create_knight(self):
        self.knight = HeroFactory().create_knight()
        return self.knight

    def testTest(self):
        self.create_knight()
        #
        # priestess = HeroFactory().create_priestess()
        # rogue = HeroFactory().create_rogue()
        # monster = MonsterFactory().create_monster()

        x = 4
        self.assertEqual(x, 4)
    # def test_hero_creation(self):
    #     self.assertTrue(isinstance(self.__knight, DungeonCharacter))
        # assert(isinstance(HeroFactory().create_rogue(), Rogue))

# if __name__ == '__main__':
#
#     unittest.main()
