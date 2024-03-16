import unittest
from Assets import assets as a
import pygame as pg

from Characters.hero_factory import HeroFactory
from Pillars_and_Trivia.pillar import Pillar
from dungeon_adventure import DungeonAdventure


class PillarsUnitTests(unittest.TestCase):
    def setUp(self):
        """

        :return:
        """
        self.__abstraction_sprite_test = pg.image.load(a.abstraction_pillar)
        self.__encapsulation_sprite_test = pg.image.load(a.encapsulation_pillar)
        self.__inheritance_sprite_test = pg.image.load(a.inheritance_pillar)
        self.__polymorphism_sprite_test = pg.image.load(a.polymorphism_pillar)
        self.__priestess = HeroFactory().create_priestess()

        self.__game = DungeonAdventure()
        self.__game.set_player_character(self.__priestess)

        self.__abstraction_pillar_test = self.__game.get_abstraction_pillar()
        self.__encapsulation_pillar_test = self.__game.get_encapsulation_pillar()
        self.__inheritance_pillar_test = self.__game.get_inheritance_pillar()
        self.__polymorphism_pillar_test = self.__game.get_polymorphism_pillar()

        self.__game.set_player_images(
            pg.transform.scale(self.__priestess.get_sprite_north(), self.__game.get_player_img_size()),
            pg.transform.scale(self.__priestess.get_sprite_east(), self.__game.get_player_img_size()),
            pg.transform.scale(self.__priestess.get_sprite_west(), self.__game.get_player_img_size()),
            pg.transform.scale(self.__priestess.get_sprite_south(), self.__game.get_player_img_size())
            )

    def test_pillar_creation(self):
        """
        Test creation of all 4 pillar objects, names, sprite assignments
        :return:
        """
        self.assertIsInstance(self.__abstraction_pillar_test, Pillar)
        self.assertIsInstance(self.__encapsulation_pillar_test, Pillar)
        self.assertIsInstance(self.__inheritance_pillar_test, Pillar)
        self.assertIsInstance(self.__polymorphism_pillar_test, Pillar)

        self.assertTrue(self.__abstraction_pillar_test.get_pillar_name() == "Abstraction")
        self.assertTrue(self.__encapsulation_pillar_test.get_pillar_name() == "Encapsulation")
        self.assertTrue(self.__inheritance_pillar_test.get_pillar_name() == "Inheritance")
        self.assertTrue(self.__polymorphism_pillar_test.get_pillar_name() == "Polymorphism")

        self.assertTrue(self.__abstraction_pillar_test.get_abstraction_sprite() == self.__abstraction_sprite_test)
        self.assertTrue(self.__encapsulation_pillar_test.get_encapsulation_sprite() == self.__encapsulation_sprite_test)
        self.assertTrue(self.__inheritance_pillar_test.get_inheritance_sprite() == self.__inheritance_sprite_test)
        self.assertTrue(self.__polymorphism_pillar_test.get_polymorphism_sprite() == self.__polymorphism_sprite_test)


if __name__ == '__main__':
    unittest.main()