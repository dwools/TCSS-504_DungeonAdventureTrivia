import unittest
from dungeon import Dungeon


class DungeonTests(unittest.TestCase):
    """
    Instantiating a dungeon calls build_maze() to create a randomly generated maze of rooms, attempts to traverse the dungeon such that all rooms are accessible, and if the maze is not traversable, generates a new maze. No content should be present in the entrance or exit rooms.

    """

    def test_dungeon(self):
        test_dungeon1 = Dungeon(3, 3)
        test_dungeon2 = Dungeon(3,3)
        self.assertFalse(str(test_dungeon1) == str(test_dungeon2), "Mazes are not randomly generated")
        self.assertTrue(test_dungeon1.traversable, "Dungeon not traversable")
        self.assertTrue(test_dungeon1.pillar_count == 4, "4 pillars weren't set")
        self.assertTrue(self.entrance_content_check() == True, "Entrance contains other content")
        self.assertTrue(self.exit_content_check() == True, "Exit contains other content")


    def entrance_content_check(self):
        test_dungeon3 = Dungeon(3, 3)
        entrance_contents = str(test_dungeon3.get_room(0,0))
        for content in ['H', 'V', 'M', 'o', 'A', 'E', 'I', 'P']:
            return not any(entrance_contents) == content

    def exit_content_check(self):
        test_dungeon4 = Dungeon(3, 3)
        exit_contents = str(test_dungeon4.get_room(test_dungeon4.rows-1, test_dungeon4.columns-1))
        for content in ['H', 'V', 'M', 'i', 'A', 'E', 'I', 'P']:
            return not any(exit_contents) == content


if __name__ == '__main__':
    unittest.main()
