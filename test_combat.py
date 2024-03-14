import unittest
import pytest

from Characters.hero_factory import HeroFactory
from Characters.hero_knight import Knight
from Characters.hero_priestess import Priestess
from Characters.hero_rogue import Rogue
from Characters.monster_factory import MonsterFactory
from Characters.monster import Monster
from Gameplay import config
from Gameplay.combat import Combat
from dungeon_adventure import DungeonAdventure



class CombatTest(unittest.TestCase):
    def setUp(self):
        """
        Create characters
        Create combat environment

        :return:
        """
        # Create heroes
        self.__knight_combat_test = HeroFactory().create_knight()
        self.__priestess_combat_test = HeroFactory().create_priestess()
        self.__rogue_combat_test = HeroFactory().create_rogue()
        
        # Create monsters
        self.__ogre_combat_test = MonsterFactory().create_ogre()
        self.__gremlin_combat_test = MonsterFactory().create_gremlin()
        self.__skeleton_combat_test = MonsterFactory().create_skeleton()

        # Set game environments and characters to pass into Combat() when Combat is instantiated.
        # Game 1: Hero has greater attack speed.
        self.__game1 = DungeonAdventure()
        self.__game1.set_player_character(self.__rogue_combat_test)
        self.__game1.set_monster(self.__skeleton_combat_test)

        # Game 2: Monster has greater attack speed.
        self.__game2 = DungeonAdventure()
        self.__game2.set_player_character(self.__knight_combat_test)
        self.__game2.set_monster(self.__gremlin_combat_test)

        # Game 3: Characters have equal attack speeds.
        self.__game3 = DungeonAdventure()
        self.__game3.set_player_character(self.__priestess_combat_test)
        self.__game3.set_monster(self.__gremlin_combat_test)
        
        # Instantiate combat
        self.__combat_test1 = Combat(self.__game1)
        self.__combat_test2 = Combat(self.__game2)
        self.__combat_test3 = Combat(self.__game3)

        # Get attack orders
        self.__attack_order_test1 = self.__combat_test1.get_attack_order()
        self.__attack_order_test2 = self.__combat_test2.get_attack_order()
        self.__attack_order_test3 = self.__combat_test3.get_attack_order()

        # Attack order positive conditions
        self.__game1_attack_order_positive = [self.__rogue_combat_test, self.__skeleton_combat_test]
        self.__game2_attack_order_positive = [self.__gremlin_combat_test, self.__knight_combat_test]
        self.__game3_attack_order_positive1 = [self.__priestess_combat_test, self.__gremlin_combat_test]
        self.__game3_attack_order_positive2 = [self.__gremlin_combat_test, self.__priestess_combat_test]
    def test_combat_instantiation(self):
        """
        Test if Combat() is successfully instantiated.
        :return:
        """
        self.assertIsInstance(self.__combat_test1, Combat)

    def test_set_attack_order(self):
        """
    #     When Attack order is set upon instantiation of the Combat class.
    #     :return:
    #     """
        pass



        



    # def test_simple_attack_sequence(self):


#     # def test_something(self):
#     #     self.assertEqual(True, False)  # add assertion here
#     #
#     # def test_setUp(self):
#     #     # Initialize Pygame (required for testing)
#     #     pygame.init()
#     #
#     # def test_tearDown(self):
#     #     # Clean up Pygame resources
#     #     pygame.quit()
#     #
#     # def test_testdraw_rectangle(self):
#     #     # Create a Pygame screen (you can adjust the dimensions as needed)
#     #     screen = pygame.display.set_mode((800, 600))
#     #
#     #     # Call your draw_rectangle function (replace with actual parameters)
#     #     self.draw_rectangle(screen, (255, 0, 0), (100, 100, 200, 150))
#     #
#     #     # Update the display
#     #     pygame.display.flip()
#     #
#     #     # Wait for a moment (adjust as needed)
#     #     pygame.time.delay(1000)
#     #
#     #     # Check if the rectangle was drawn (you can add more specific checks)
#     #     self.assertTrue(pygame.surfarray.array_colorkey(screen).any())
#     #
#     #
#     # # Check that character can't walk thorugh walls
#     # def test_player_sprite_clipping(self):
#     #     '''
#     #     A player spawns at [0, 0], aka [16, 16] pixels, the northwest corner. There are walls to the north and west. If the player moves north or west, its coordinates will not change.
#     #     '''
#     #     self.main()
#
#         # player starts at 0, 0 (16, 16)
#         # player moves north
#         # player's rect coordinates don't change
#         # exit game
#
#
#     def test_item_generation(self):
#         pass
#         # assert ItemFactory().
#         # main.main()
#         # main.DungeonAdventure.playing = True
#
#
#
#
#


# if __name__ == '__main__':
#     pg.init()
#     adventure = DungeonAdventure()
#     while adventure.running:
#         initialize_databases.main()
#         adventure.current_menu.display_menu()
#         adventure.set_test_game(True)
#         adventure.game_loop()


    # unittest.main()
