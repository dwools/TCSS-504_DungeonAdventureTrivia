import unittest

from Characters.hero_factory import HeroFactory
from Items.item_factory import ItemFactory
from Items.item import Item
from dungeon_adventure import DungeonAdventure
import pygame as pg


class ItemsUnitTests(unittest.TestCase):
    """
    Unit tests for class Item objects' creation and methods.
    """
    def setUp(self):
        # Create character and items
        self.__knight = HeroFactory().create_knight()
        self.__health_potion = ItemFactory().create_health_potion()
        self.__fire_trap = ItemFactory().create_fire_trap()

        # Start game
        self.__game = DungeonAdventure()
        self.__game.set_player_character(self.__knight)
        
        # Player images to set player rect
        self.__game.set_player_images(
            pg.transform.scale(self.__knight.get_sprite_north(), self.__game.get_player_img_size()),
            pg.transform.scale(self.__knight.get_sprite_east(), self.__game.get_player_img_size()),
            pg.transform.scale(self.__knight.get_sprite_west(), self.__game.get_player_img_size()),
            pg.transform.scale(self.__knight.get_sprite_south(), self.__game.get_player_img_size())
        )
        self.__game.set_player_rect()

    def test_health_potion_creation(self):
        """
        Test health_potion creation using ItemFactory.
        :return:
        """
        self.assertIsInstance(self.__health_potion, Item)
        self.assertTrue(self.__health_potion.get_item_name() == 'Health Potion')

    def test_fire_trap_creation(self):
        """
        Test fire_trap creation using ItemFactory.
        :return:
        """
        self.assertIsInstance(self.__fire_trap, Item)
        self.assertTrue(self.__fire_trap.get_item_name() == 'Fire Trap')

    def test_item_pickup(self):
        """
        Test that health potions are successfully added to Hero() classes health potion inventory upon

        Hero().add_to_backpack() appends all Item class objects to health_potion_list. However,
        Hero().add_to_backpack() only called when player rectangle collides with rectangle of Pillar() objects or
        Item() objects with item_name "Health Potion".
        :return:
        """

        self.__knight.add_to_backpack(self.__health_potion)
        self.assertIn(self.__health_potion, self.__knight.get_player_health_potions())

    def test_health_potion_healing(self):
        """
        Test that Hero().drink_health_potion() replenishes hero character's diminished hit points.

        Test that replenished hit points from Hero().drink_health_potion() do not exceed character's max hit point
        value.
        :return:
        """
        self.__knight.set_current_hit_points(120)
        self.__knight.add_to_backpack(self.__health_potion)
        self.assertTrue(len(self.__knight.get_player_health_potions()) == 1)

        pre_healing_hit_points = self.__knight.get_current_hit_points()
        self.assertGreater(self.__knight.get_max_hit_points(), pre_healing_hit_points)

        self.__knight.drink_health_potion()
        post_healing_hit_points = self.__knight.get_current_hit_points()
        self.assertGreater(post_healing_hit_points, pre_healing_hit_points)
        self.assertEqual(post_healing_hit_points, self.__knight.get_max_hit_points())
        self.assertTrue(len(self.__knight.get_player_health_potions()) == 0)


    def test_health_potion_pickup(self):
        """
        Self explanatory
        :return:
        """
        for item in self.__knight.get_player_health_potions():
            self.__knight.get_player_health_potions().pop()


        for item in self.__game.get_items_list():
            self.__game.get_items_list().pop()

        self.__game.get_items_list().append(self.__health_potion)

        item_x, item_y = self.__health_potion.get_item_position()
        self.__game.set_player_position((item_x, item_y))
        player_rect = self.__game.get_player_rect()
        item_rect = self.__health_potion.get_item_rect()
        self.assertTrue(player_rect.colliderect(item_rect))

        ## DungeonAdventure item_pickup_code:
        for item in self.__game.get_items_list():
            if self.__game.get_player_rect().colliderect(item.get_item_rect()):
                if item.get_item_name() == "Fire Trap":
                    self.__knight.damage(1)
                else:
                    self.__knight.add_to_backpack(item)
                    self.__game.get_items_list().remove(item)

        self.assertTrue(len(self.__knight.get_player_health_potions()) == 1)

        # pillar_x, pillar_y = self.__game.get_encapsulation_pillar().get_pillar_position()
        # self.__game.set_player_position((pillar_x, pillar_y))
        # player_rect = self.__game.get_player_rect()
        # pillar_rect = self.__encapsulation_pillar_test.get_pillar_rect()
        # self.assertTrue((self.__game.get_player_rect().colliderect(self.__encapsulation_pillar_test.get_pillar_rect())))

    def test_fire_trap_damage(self):
        """
        If player rect collides with fire trap,  player's health decreases.

        :return:
        """
        for item in self.__game.get_items_list():
            if item.get_item_name() == "Health Potion":
                self.__game.get_items_list().remove(item)


        pre_hit_points = self.__knight.get_current_hit_points()

        self.__game.get_items_list().append(self.__fire_trap)
        item_rect = self.__game.get_items_list()[0].get_item_rect()
        Px, Py, Pw, Pl = self.__game.get_items_list()[0].get_item_rect()
        self.__game.set_player_position((Py, Px))
        self.__game.set_player_rect()
        player_rect = self.__game.get_player_rect()
        self.assertTrue(player_rect.colliderect(item_rect))

        for item in self.__game.get_items_list():
            if self.__game.get_player_rect().colliderect(item.get_item_rect()):
                if item.get_item_name() == "Fire Trap":
                    self.__knight.damage(1)
                else:
                    self.__knight.add_to_backpack(item)
                    self.__game.get_items_list().remove(item)

        post_hit_points = self.__knight.get_current_hit_points()

        self.assertGreater(pre_hit_points, post_hit_points)




if __name__ == '__main__':
    unittest.main()
