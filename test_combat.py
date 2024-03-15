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
        self.__game1_combat_test = Combat(self.__game1)
        self.__game2_combat_test = Combat(self.__game2)
        self.__game3_combat_test = Combat(self.__game3)

        # Get attack orders
        self.__game1_attack_order_test = self.__game1_combat_test.get_attack_order()
        self.__game2_attack_order_test = self.__game2_combat_test.get_attack_order()
        self.__game3_attack_order_test = self.__game3_combat_test.get_attack_order()

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
        self.assertIsInstance(self.__game1_combat_test, Combat)

    def test_set_attack_order(self):
        """
    #     Test the attack_order list is set upon instantiation of the Combat class and that character objects in the list are ordred by their attack_speed value.
    #     :return:
    #     """
        self.assertEqual(self.__game1_attack_order_test, self.__game1_attack_order_positive)

        self.assertEqual(self.__game2_attack_order_test, self.__game2_attack_order_positive)

        if self.__game3_attack_order_test != self.__game3_attack_order_positive1:
            self.assertEqual(self.__game3_attack_order_test, self.__game3_attack_order_positive2)
        elif self.__game3_attack_order_test != self.__game3_attack_order_positive2:
            self.assertEqual(self.__game3_attack_order_test, self.__game3_attack_order_positive1)

    def test_simple_attack_sequence(self):
        """
        When "simple" attack" is called, a simple attack is delivered from character to enemy, and vice versa, in order of either characters' position in the attack order list.
        After the attack is delivered,
        Requires successful implementation of DungeonCharacter().simple_attack(enemy).
        :return:
        """
        pass

    def test_special_attack_sequence(self):
        pass
