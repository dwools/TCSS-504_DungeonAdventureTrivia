import os.path
import unittest
from Characters.hero_factory import HeroFactory
from Characters.hero_rogue import Rogue
from Characters.hero_knight import Knight
from Characters.hero_priestess import Priestess
from Characters.monster import Monster
from Characters.monster_factory import MonsterFactory
import sqlite3
from Databases import initialize_databases
from Room_and_Maze.maze import Maze
from dungeon_adventure import DungeonAdventure
from Gameplay.combat import Combat
from Gameplay.save_game import SaveGame

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        """
        Clear OS of dungeon_adventure.pickle file
        Create game environment
        Impart state change in game
        Save game by generating pickle file
        :return:
        """
        # remove
        if os.path.exists("dungeon_adventure.pickle"):
            os.remove("dungeon_adventure.pickle")
        if os.path.exists("dungeon.txt"):
            os.remove("dungeon.txt")



        # Create characters
        self.__rogue = HeroFactory().create_rogue()
        self.__skeleton = MonsterFactory().create_skeleton()

        # Create game environment
        Maze(10, 10).new_maze()
        self.__game = DungeonAdventure()

        self.__game.set_player_character(self.__rogue)
        self.__game.set_monster(self.__skeleton)

        # State change
        Combat(self.__game).set_attack_order()
        Combat(self.__game).simple_attack_sequence()

    def test_save_game(self):
        SaveGame().save_helper(self.__game)
        assert os.path.exists("./save_files/attributes_dict.pkl")


if __name__ == '__main__':
    unittest.main()
