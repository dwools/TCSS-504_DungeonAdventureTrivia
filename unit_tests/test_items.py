import unittest

from Characters.hero_factory import HeroFactory
from Items.item_factory import ItemFactory
from Items.item import Item
from dungeon_adventure import DungeonAdventure


class ItemsUnitTests(unittest.TestCase):
    """
    Unit tests for class Item objects' creation and methods.
    """
    def setUp(self):
        # Create character and items
        self.__knight_test = HeroFactory().create_knight()
        self.__health_potion_test = ItemFactory().create_health_potion()
        self.__fire_trap_test =  ItemFactory().create_fire_trap()

        # set game
        # self.__game = DungeonAdventure()
        # self.__game.set_player_character(self.__knight_test)
        # Set character_position

    def test_health_potion_creation(self):
        """
        Test health_potion creation using ItemFactory.
        :return:
        """
        self.assertIsInstance(self.__health_potion_test, Item)
        self.assertTrue(self.__health_potion_test.get_item_name() == 'Health Potion')

    def test_fire_trap_creation(self):
        """
        Test fire_trap creation using ItemFactory.
        :return:
        """
        self.assertIsInstance(self.__fire_trap_test, Item)
        self.assertTrue(self.__fire_trap_test.get_item_name() == 'Fire Trap')

    def test_item_pickup(self):
        """
        Test that health potions are successfully added to Hero() classes health potion inventory upon

        Hero().add_to_backpack() appends all Item class objects to health_potion_list. However,
        Hero().add_to_backpack() only called when player rectangle collides with rectangle of Pillar() objects or
        Item() objects with item_name "Health Potion".
        :return:
        """
        self.__knight_test.add_to_backpack(self.__health_potion_test)
        self.assertIn(self.__health_potion_test, self.__knight_test.get_player_health_potions())

    def test_health_potion_healing(self):
        """
        Test that Hero().drink_health_potion() replenishes hero character's diminished hit points.

        Test that replenished hit points from Hero().drink_health_potion() do not exceed characters's max hit point
        value.
        :return:
        """
        self.__knight_test.set_current_hit_points(120)
        self.__knight_test.add_to_backpack(self.__health_potion_test)
        pre_healing_hit_points = self.__knight_test.get_current_hit_points()
        self.assertGreater(self.__knight_test.get_max_hit_points(), pre_healing_hit_points)

        self.__knight_test.drink_health_potion()
        post_healing_hit_points = self.__knight_test.get_current_hit_points()
        self.assertGreater(post_healing_hit_points, pre_healing_hit_points)
        self.assertEqual(post_healing_hit_points, self.__knight_test.get_max_hit_points())




if __name__ == '__main__':
    unittest.main()
