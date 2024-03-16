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
        self.__knight = HeroFactory().create_knight()
        self.__priestess = HeroFactory().create_priestess()
        self.__rogue = HeroFactory().create_rogue()
        
        # Create monsters
        self.__ogre = MonsterFactory().create_ogre()
        self.__gremlin = MonsterFactory().create_gremlin()
        self.__skeleton = MonsterFactory().create_skeleton()

        # Set game environments and characters to pass into Combat() when Combat is instantiated.
        # Game 1: Hero has greater attack speed.
        self.__game1 = DungeonAdventure()
        self.__game1.set_player_character(self.__rogue)
        self.__game1.set_monster(self.__skeleton)

        # Game 2: Monster has greater attack speed.
        self.__game2 = DungeonAdventure()
        self.__game2.set_player_character(self.__knight)
        self.__game2.set_monster(self.__gremlin)

        # Game 3: Characters have equal attack speeds.
        self.__game3 = DungeonAdventure()
        self.__game3.set_player_character(self.__priestess)
        self.__game3.set_monster(self.__gremlin)
        
        # Instantiate combat
        self.__game1_combat_test = Combat(self.__game1)

        self.__game2_combat_test = Combat(self.__game2)
        self.__game3_combat_test = Combat(self.__game3)

        # Get attack orders
        self.__game1_attack_order_test = self.__game1_combat_test.get_attack_order()
        self.__game2_attack_order_test = self.__game2_combat_test.get_attack_order()
        self.__game3_attack_order_test = self.__game3_combat_test.get_attack_order()

        # Attack order positive conditions
        self.__game1_attack_order_positive = [self.__rogue, self.__skeleton]
        self.__game2_attack_order_positive = [self.__gremlin, self.__knight]
        self.__game3_attack_order_positive1 = [self.__priestess, self.__gremlin]
        self.__game3_attack_order_positive2 = [self.__gremlin, self.__priestess]

    def test_combat_instantiation(self):
        """
        Test if Combat() is successfully instantiated.
        :return:
        """

        self.assertIsInstance(self.__game1_combat_test, Combat)

    def test_set_attack_order(self):
        """
        Test the attack_order list is set upon instantiation of the Combat class and that character objects in the
        list are ordred by their attack_speed value.
        :return:
        """

        self.assertEqual(self.__game1_attack_order_test, self.__game1_attack_order_positive)

        self.assertEqual(self.__game2_attack_order_test, self.__game2_attack_order_positive)

        if self.__game3_attack_order_test != self.__game3_attack_order_positive1:
            self.assertEqual(self.__game3_attack_order_test, self.__game3_attack_order_positive2)

        else:
            # self.__game3_attack_order_test != self.__game3_attack_order_positive2:
            self.assertEqual(self.__game3_attack_order_test, self.__game3_attack_order_positive1)

    def test_simple_attack_sequence(self):
        """
        Require successful execution of:
        Hero().simple_attack(enemy),
        Monster().simple_attack(enemy),
        Combat().check_monster_hit_points(),
        Combat().check_hero_hit_points()
        :return:
        """

        if len(self.__game1.get_monsters_list()) == 0:
            self.__skeleton = MonsterFactory().create_skeleton()
            self.__game1.set_monster(self.__skeleton)
            self.__game1.get_monsters_list().append(self.__skeleton)

        self.__game1_combat_test.set_hero(self.__rogue)
        self.__game1_combat_test.set_monster(self.__skeleton)

        for _ in range(10):
            self.__game1_combat_test.simple_attack_sequence()
            if self.__rogue.get_current_hit_points() <= 0:
                self.assertTrue(self.__game1.paused)
                self.assertTrue(self.__game1.current_menu == self.__game1.game_over)
                break
            elif self.__skeleton.get_current_hit_points() <= 0:
                self.assertTrue(len(self.__game1.get_monsters_list()) == 0)
                break
            else:
                continue

    def test_special_attack_sequence(self):
        """
        Require successful execution of:
        Hero().special_attack(enemy),
        Monster().simple_attack(enemy),
        Combat().check_monster_hit_points(),
        Combat().check_hero_hit_points()
        :return:
        """

        if len(self.__game1.get_monsters_list()) == 0:
            self.__skeleton = MonsterFactory().create_skeleton()
            self.__game1.set_monster(self.__skeleton)
            self.__game1.get_monsters_list().append(self.__skeleton)

        self.__rogue.set_current_hit_points(self.__rogue.get_max_hit_points())
        self.__skeleton.set_current_hit_points(self.__skeleton.get_max_hit_points())

        for _ in range(10):
            self.__game1_combat_test.special_attack_sequence()
            if self.__rogue.get_current_hit_points() <= 0:
                self.assertTrue(self.__game1.paused)
                self.assertTrue(self.__game1.current_menu == self.__game1.game_over)
                break
            elif self.__skeleton.get_current_hit_points() <= 0:
                self.assertTrue(len(self.__game1.get_monsters_list()) == 0)
                break
            else:
                continue

