import sys
import threading
import time
import unittest
from Databases import initialize_databases
from Room_and_Maze.maze import Maze
from dungeon_adventure import DungeonAdventure
import pygame as pg
import pyautogui
from Characters.hero_factory import HeroFactory
from Characters.hero_knight import Knight
from Characters.hero_priestess import Priestess
from Characters.hero_rogue import Rogue
from Characters.monster_factory import MonsterFactory
from Characters.monster import Monster
from Gameplay import config
from Gameplay.combat import Combat
from dungeon_adventure import DungeonAdventure
class GameplayUnitTests(unittest.TestCase):

    def setUp(self):
        """
        Initialize game.
        :return:
        """
        Maze(15, 20).new_maze()
        self.__game = DungeonAdventure()
        self.__rogue_test = HeroFactory().create_rogue()
        self.__game.set_player_character(self.__rogue_test)



    def test_movement(self):
        self.__game.game_loop()
        pre_movement = self.__rogue_test.get_position()
        print(self.__rogue_test.get_position())

        self.assertIsNotNone(pre_movement)

        for _ in range(120):
            self.__game.moving_south = True
            self.__game.player_direction = 0

        for _ in range(120):
            self.__game.moving_east = True
            self.__game.player_direction = 2

        self.__game.moving_south = False
        self.__game.moving_east = False

        post_movement = self.__rogue_test.get_position()

        self.assertNotEqual(pre_movement, post_movement)

        self.__game.running = False
    pg.quit()
















#
#
#
#
#
#
#
#
#
#
#
#         # pg.init()
#
#         initialize_databases.main()
#         self.__game = DungeonAdventure()
#         # self.__game.game_loop()
#         #
#         def press_key():
#             pg.init()
#             while self.__game.running:
#                 initialize_databases.main()
#                 self.__game.current_menu.display_menu()
#                 self.__game.game_loop()
#
#         thread = threading.Thread(target=press_key)
#         thread.start() # calls the press_key() method
#
# # Thread 1 (main thead) is python running our code. Thread 2 (which we've created above) is running our game.
#
#     def tearDown(self) -> None:
#         pg.quit()
#         sys.exit()
#
#     def test_menu_navigation(self):
#         time.sleep(3)
#         self.assertTrue(True)
#         # self.assertTrue(self.__game.current_menu == self.__game.main_menu)
#         # # time.sleep(3)
#         # self.assertTrue(self.__game.current_menu.state == "Start Game")
#         # self.__game.interacting = True
#         # # # pyautogui.press('enter')
#         # time.sleep(0.1)
#         # self.__game.interacting = False
#         # # # pyautogui.press("enter")
#         # # time.sleep(1)
#         # print(f'\n{self.__game.current_menu}')
#         # #
#         # self.assertTrue(self.__game.current_menu == self.__game.character_select)
#         # self.__game.running = False
#
#
# if __name__ == '__main__':
#     unittest.main()
