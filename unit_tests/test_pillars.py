import unittest
from Assets import assets as a
import pygame as pg

from Characters.hero_factory import HeroFactory
from Pillars_and_Trivia.pillar import Pillar
from dungeon_adventure import DungeonAdventure
from menu import TriviaUI


class PillarsUnitTests(unittest.TestCase):
    def setUp(self):
        """

        :return:
        """

        self.__priestess = HeroFactory().create_priestess()

        self.__game = DungeonAdventure()
        self.__game.set_player_character(self.__priestess)

        if len(self.__priestess.get_player_pillars()) != 0:
            for pillar in self.__priestess.get_player_pillars():
                pillar.pop()

        self.__abstraction_pillar = self.__game.get_abstraction_pillar()
        self.__encapsulation_pillar = self.__game.get_encapsulation_pillar()
        self.__inheritance_pillar = self.__game.get_inheritance_pillar()
        self.__polymorphism_pillar = self.__game.get_polymorphism_pillar()

        self.__game.set_player_images(
            pg.transform.scale(self.__priestess.get_sprite_north(), self.__game.get_player_img_size()),
            pg.transform.scale(self.__priestess.get_sprite_east(), self.__game.get_player_img_size()),
            pg.transform.scale(self.__priestess.get_sprite_west(), self.__game.get_player_img_size()),
            pg.transform.scale(self.__priestess.get_sprite_south(), self.__game.get_player_img_size())
        )
        self.__game.set_player_rect()
        self.__trivia_ui = TriviaUI(self.__game, "Abstraction")


    def test_pillar_creation(self):
        """
        Test creation of all 4 pillar objects, names, sprite assignments
        :return:
        """
        self.__abstraction_pillar = Pillar("Abstraction")
        self.__encapsulation_pillar = Pillar("Encapsulation")
        self.__inheritance_pillar = Pillar("Inheritance")
        self.__polymorphism_pillar = Pillar("Polymorphism")

        self.assertIsInstance(self.__abstraction_pillar, Pillar)
        self.assertIsInstance(self.__encapsulation_pillar, Pillar)
        self.assertIsInstance(self.__inheritance_pillar, Pillar)
        self.assertIsInstance(self.__polymorphism_pillar, Pillar)

        self.assertTrue(self.__abstraction_pillar.get_pillar_name() == "Abstraction")
        self.assertTrue(self.__encapsulation_pillar.get_pillar_name() == "Encapsulation")
        self.assertTrue(self.__inheritance_pillar.get_pillar_name() == "Inheritance")
        self.assertTrue(self.__polymorphism_pillar.get_pillar_name() == "Polymorphism")

    def test_pillar_collision(self):
        """
        Test for the successful collision of player and Pillar object when they occupy the same space. Using the code
         structure used in DungeonAdventure, successfully tested pillar identification when player and pillar rects
         collide.
        :return:
        """
        # if len(self.__priestess.get_player_pillars()) != 0:
        #     for pillar in self.__priestess.get_player_pillars():
        #         pillar.pop()
        #
        # for pillar in self.__game.get_pillars_list():
        #     self.__game.get_pillars_list().remove(pillar)
        #
        # self.__game.get_pillars_list().append(self.__encapsulation_pillar)

        p = self.__game.get_pillars_list()[1]
        Px, Py, Pw, Pl = self.__game.get_pillars_list()[1].get_pillar_rect()
        self.__game.set_player_position((Py, Px))
        self.__game.set_player_rect()
        r = self.__game.get_player_rect()

        # player_x, player_y, player_w, player_h = self.__game.get_player_rect()
        # self.__game.get_encapsulation_pillar().set_pillar_rect(player_x, player_y)
        # player_rect = self.__game.get_player_rect()
        # pillar_rect = self.__encapsulation_pillar.get_pillar_rect()
        self.assertTrue((self.__game.get_player_rect().colliderect(self.__encapsulation_pillar.get_pillar_rect())))
        # self.assertIsInstance(self.__game.trivia_ui, TriviaUI)


        # DungeonAdventure() pillar collision code
        for pillar in self.__game.get_pillars_list():
            pillar_rect = pillar.get_pillar_rect()
            if self.__game.get_player_rect().colliderect(pillar_rect):
                if pillar == self.__abstraction_pillar:
                    # prompt Astronomy trivia
                    self.__trivia_ui = TriviaUI(self.__game, "Abstraction")
                elif pillar == self.__encapsulation_pillar:
                    # prompt Elapid trivia
                    self.__trivia_ui = TriviaUI(self.__game, "Encapsulation")
                    self.assertTrue(True)
                elif pillar == self.__inheritance_pillar:
                    # prompt International trivia
                    self.__trivia_ui = TriviaUI(self.__game, "Inheritance")
                elif pillar == self.__polymorphism_pillar:
                    # prompt Pokemon trivia
                    self.__trivia_ui = TriviaUI(self.__game, "Polymorphism")
                self.paused = True
                self.current_menu = self.__trivia_ui

        # /        self.assertTrue(self.__trivia_ui.get_trivia_category() == "Encapsulation")

if __name__ == '__main__':
    unittest.main()