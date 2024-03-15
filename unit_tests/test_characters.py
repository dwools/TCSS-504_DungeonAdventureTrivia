import unittest
from Characters.hero_factory import HeroFactory
from Characters.hero_rogue import Rogue
from Characters.hero_knight import Knight
from Characters.hero_priestess import Priestess
from Characters.monster import Monster
from Characters.monster_factory import MonsterFactory
import sqlite3
from Databases import initialize_databases


class CharacterUnitTests(unittest.TestCase):
    """
    Unit tests for class DungeonCharacter objects' creation and methods.
    """
    def setUp(self):
        """
        Create an object of class Knight, Rogue, Priestess, and three monsters of class Monster corresponding to ogre, gremlin, and skeleton specifications.
        Set up lists of expected character statistics
        Pull created objects' statistics
        Set up list of extected names
        :return:
        """
        initialize_databases.main()

        self.__knight_test = HeroFactory().create_knight()
        self.__knight_test_values = ["Knight", 125, 125, 4, 80, 35, 60, 20, 40, 75, 175]
        self.__knight_test_getters = [self.__knight_test.get_type(),
                                      self.__knight_test.get_current_hit_points(),
                                      self.__knight_test.get_max_hit_points(),
                                      self.__knight_test.get_attack_speed(),
                                      self.__knight_test.get_chance_to_hit(),
                                      self.__knight_test.get_minimum_damage(),
                                      self.__knight_test.get_maximum_damage(),
                                      self.__knight_test.get_chance_to_block(),
                                      self.__knight_test.get_chance_for_crushing_blow(),
                                      self.__knight_test.get_minimum_crushing_damage(),
                                      self.__knight_test.get_maximum_crushing_damage()
                                      ]
        
        self.__rogue_test = HeroFactory().create_rogue()
        self.__rogue_test_values = ["Rogue", 75, 75, 6, 80, 20, 40, 40, 40, 40]
        self.__rogue_test_getters = [self.__rogue_test.get_type(),
                                     self.__rogue_test.get_current_hit_points(),
                                     self.__rogue_test.get_max_hit_points(),
                                     self.__rogue_test.get_attack_speed(),
                                     self.__rogue_test.get_chance_to_hit(),
                                     self.__rogue_test.get_minimum_damage(),
                                     self.__rogue_test.get_maximum_damage(),
                                     self.__rogue_test.get_chance_to_block(),
                                     self.__rogue_test.get_chance_for_second_attack(),
                                     self.__rogue_test.get_chance_caught()
                                     ]

        self.__priestess_test = HeroFactory().create_priestess()
        self.__priestess_test_values = ["Priestess", 75, 75, 5, 70, 25, 45, 30, 70, 30, 60]
        self.__priestess_test_getters = [self.__priestess_test.get_type(),
                                         self.__priestess_test.get_current_hit_points(),
                                         self.__priestess_test.get_max_hit_points(),
                                         self.__priestess_test.get_attack_speed(),
                                         self.__priestess_test.get_chance_to_hit(),
                                         self.__priestess_test.get_minimum_damage(),
                                         self.__priestess_test.get_maximum_damage(),
                                         self.__priestess_test.get_chance_to_block(),
                                         self.__priestess_test.get_chance_to_heal(),
                                         self.__priestess_test.get_minimum_heal_points(),
                                         self.__priestess_test.get_maximum_heal_points()
                                         ]
        def get_monster_test_stats(monster_test):
            return [monster_test.get_type(),
                    monster_test.get_current_hit_points(),
                    monster_test.get_max_hit_points(),
                    monster_test.get_attack_speed(),
                    monster_test.get_chance_to_hit(),
                    monster_test.get_minimum_damage(),
                    monster_test.get_maximum_damage(),
                    monster_test.get_chance_to_heal(),
                    monster_test.get_minimum_heal_points(),
                    monster_test.get_maximum_heal_points()
                    ]
        self.__ogre_test = MonsterFactory().create_ogre()
        self.__ogre_test_getters = get_monster_test_stats(self.__ogre_test)
        self.__ogre_test_values = ["Ogre", 200, 200, 2, 60, 30, 60, 10, 30, 60]

        self.__gremlin_test = MonsterFactory().create_gremlin()
        self.__gremlin_test_getters = get_monster_test_stats(self.__gremlin_test)
        self.__gremlin_test_values = ["Gremlin", 70, 70, 5, 80, 15, 30, 40, 20, 40]

        self.__skeleton_test = MonsterFactory().create_skeleton()
        self.__skeleton_test_getters = get_monster_test_stats(self.__skeleton_test)
        self.__skeleton_test_values = ["Skeleton", 100, 100, 3, 80, 30, 50, 30, 30, 50]

        # Pull latin names from names database into a list to test character name generation
        conn = sqlite3.connect("Databases/database_names.db")
        cursor = conn.cursor()
        self.__names_test = [latin_name[0] for latin_name in cursor.execute("SELECT latin_name FROM names")]

    def test_create_knight(self):
        """
        Tests the ability to create a character object of Knight using HeroFactory(). Requires successful pulling from dungeon_hero database.
        :return:
        """
        self.assertIsInstance(self.__knight_test, Knight)
        self.assertEqual(self.__knight_test_getters, self.__knight_test_values)

    def test_create_priestess(self):
        """
        Tests the ability to create a character object of class Priestess using HeroFactory(). Requires successful pulling from dungeon_hero database.
        :return: 
        """
        self.assertIsInstance(self.__priestess_test, Priestess)
        self.assertEqual(self.__priestess_test_getters, self.__priestess_test_values)
                
    def test_create_rogue(self):
        """
        Tests the ability to create a character object of class Priestess using HeroFactory(). Requires successful pulling from dungeon_hero database.
        :return: 
        """
        self.assertIsInstance(self.__rogue_test, Rogue)
        self.assertEqual(self.__rogue_test_getters, self.__rogue_test_values)

    def test_create_ogre(self):
        """
        Tests the ability to create a character object of class Monster and type "Ogre". Requires successful pulling from dungeon_monster database.
        :return:
        """
        self.assertIsInstance(self.__ogre_test, Monster)
        self.assertEqual(self.__ogre_test_getters, self.__ogre_test_values)
        
    def test_create_skeleton(self):
        """
        Tests the ability to create a character object of class Monster and type "Skeleton". Requires successful pulling from dungeon_monster database.
        :return:
        """
        self.assertIsInstance(self.__skeleton_test, Monster)
        self.assertEqual(self.__skeleton_test_getters, self.__skeleton_test_values)
        
    def test_create_gremlin(self):
        """
        Tests the ability to create a character object of class Monster and type "Gremlin". Requires successful pulling from dungeon_monster database
        :return:
        """
        self.assertIsInstance(self.__gremlin_test, Monster)
        self.assertEqual(self.__gremlin_test_getters, self.__gremlin_test_values)

    def test_names(self):
        """
        Tests the names of each character object are pulled from the sqlite3 database of latin names for 24 elapid species
        :return:
        """
        self.assertIn(self.__knight_test.get_name(), self.__names_test)
        self.assertIn(self.__priestess_test.get_name(), self.__names_test)
        self.assertIn(self.__rogue_test.get_name(), self.__names_test)
        self.assertIn(self.__ogre_test.get_name(), self.__names_test)
        self.assertIn(self.__skeleton_test.get_name(), self.__names_test)
        self.assertIn(self.__gremlin_test.get_name(), self.__names_test)

    def test_simple_attack(self):
        """
        Test that knight and ogre's current hit points have decreased after running 10x iterations of
        DungeonCharacter.simple_attack(enemy) on each other.
        
        Reset both character's hit points after testing. 
        :return:
        """
        self.__knight_pre_simple_attack_hit_points = self.__knight_test.get_current_hit_points()
        self.__ogre_pre_simple_attack_hit_points = self.__ogre_test.get_current_hit_points()
        for _ in range(0, 10):
            self.__knight_test.simple_attack(self.__ogre_test)
            self.__ogre_test.simple_attack(self.__knight_test)
        self.__ogre_post_simple_attack_hit_points = self.__ogre_test.get_current_hit_points()
        self.__knight_post_simple_attack_hit_points = self.__knight_test.get_current_hit_points()

        self.assertGreater(self.__knight_pre_simple_attack_hit_points, self.__knight_post_simple_attack_hit_points)
        self.assertGreater(self.__ogre_pre_simple_attack_hit_points, self.__ogre_post_simple_attack_hit_points)
        
        self.__knight_test.set_current_hit_points(self.__knight_test.get_max_hit_points())
        self.__ogre_test.set_current_hit_points(self.__ogre_test.get_max_hit_points())

    def test_knight_special(self):
        """
        Test that ogre's current hit points have decreased after run 10x iterations of Knight.special(ogre) toward
        ogre.

        Reset both character's hit points after testing.
        :return: 
        """
        ogre_pre_special_hit_points = self.__ogre_test.get_current_hit_points()

        for _ in range(10):
            self.__knight_test.special(self.__ogre_test)

        ogre_post_special_hit_points = self.__ogre_test.get_current_hit_points()

        self.assertGreater(ogre_pre_special_hit_points, ogre_post_special_hit_points)

        self.__ogre_test.set_current_hit_points(self.__ogre_test.get_max_hit_points())

    def test_priestess_special(self):
        """
        1) Test that Priestess' hit points do not exceed her maximum hit points value running Priestess's special()
         method (healing).

        2) Test that Priestess' current hit points value increases after running Priestess's special() method after Ogre
        inflicts simple_attack upon Priestess 10 times.
        :return:
        """
        # self.__priestess_test.set_current_hit_points(self.__priestess_test.get_max_hit_points())

        for _ in range(10):
            self.__priestess_test.special()
        priestess_post_healing_hit_points = self.__priestess_test.get_current_hit_points()

        self.assertEqual(priestess_post_healing_hit_points, self.__priestess_test.get_max_hit_points())

        for _ in range(10):
            self.__ogre_test.simple_attack(self.__priestess_test)

        priestess_pre_healing_hit_points = self.__priestess_test.get_current_hit_points()
        for _ in range(10):
            self.__priestess_test.special()
        priestess_post_healing_hit_points = self.__priestess_test.get_current_hit_points()

        self.assertGreater(priestess_post_healing_hit_points, priestess_pre_healing_hit_points)

        self.__priestess_test.set_current_hit_points(self.__priestess_test.get_max_hit_points())

    def test_rogue_special(self):
        """
        Using a decorator function around DungeonCharacter().simple_attack(enemy), Enumerate the successful executions
        of simple_attack(enemy) when Rogue executes its special(enemy) method (roll for 2x simple attacks).
        Rogue().simple_attack(enemy) should be executed more than the number of given iterations.
        :return:
        """
        r = 20
        initial_count = self.__rogue_test.simple_attack.special_simple_attack_count
        for _ in range(r+1):
            self.__rogue_test.special(self.__ogre_test)
        simple_attacks_in_special = self.__rogue_test.simple_attack.special_simple_attack_count - initial_count
        self.assertGreater(simple_attacks_in_special, r)

        self.__ogre_test.set_current_hit_points(self.__ogre_test.get_max_hit_points())

    def test_monster_heal(self):
        """
        Test monster healing
        :return:
        """
        for _ in range(10):
            self.__rogue_test.simple_attack(self.__skeleton_test)

        skeleton_pre_healing_hit_points = self.__skeleton_test.get_current_hit_points()
        for _ in range(10):
            self.__skeleton_test.monster_heal()
        skeleton_post_healing_hit_points = self.__skeleton_test.get_current_hit_points()

        self.assertGreater(skeleton_post_healing_hit_points, skeleton_pre_healing_hit_points)















