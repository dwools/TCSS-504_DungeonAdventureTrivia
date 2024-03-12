import unittest
from unittest.mock import patch, MagicMock
from DungeonAdventure import DungeonAdventure


class TestDungeonAdventure(unittest.TestCase):

    @patch('DungeonAdventure.Dungeon')
    @patch('builtins.input', side_effect=['HARD'])
    def test_create_dungeon_hard(self, mock_input, mock_dungeon):
        # Mock the Dungeon constructor to return a specific size
        mock_dungeon.return_value.width = 8
        mock_dungeon.return_value.height = 8

    @patch('DungeonAdventure.Dungeon')
    @patch('builtins.input', side_effect=[''])
    def test_create_dungeon_standard(self, mock_input, mock_dungeon):
        # Mock the Dungeon constructor to return a specific size
        mock_dungeon.return_value.width = 5
        mock_dungeon.return_value.height = 5

    @patch('builtins.input', return_value='Alex')
    def test_create_adventurer_with_name(self, mock_input):
        # mock starting game with name
        game = DungeonAdventure()
        self.assertEqual(game.adventurer.name, 'Alex')

    @patch('builtins.input', return_value='')
    def test_create_adventurer_default_name(self, mock_input):
        # mock starting game with with default name
        game = DungeonAdventure()
        self.assertEqual(game.adventurer.name, 'Finn')

    @patch('DungeonAdventure.Dungeon')
    @patch('DungeonAdventure.Adventurer')
    def test_process_movement(self, mock_adventurer, mock_dungeon, ):
        # mock moving in each direction
        game = DungeonAdventure()
        mock_room = MagicMock()
        mock_dungeon.return_value.get_room.return_value = mock_room
        mock_adventurer.return_value.location = (0, 0)

        # Simulate room with all doors open
        mock_room.has_north_door.return_value = True
        mock_room.has_south_door.return_value = True
        mock_room.has_east_door.return_value = True
        mock_room.has_west_door.return_value = True

        game.process_movement('E')
        self.assertEqual(mock_adventurer.return_value.location, (0, 1))

        game.process_movement('S')
        self.assertEqual(mock_adventurer.return_value.location, (1, 1))

        game.process_movement('W')
        self.assertEqual(mock_adventurer.return_value.location, (1, 0))

        game.process_movement('N')
        self.assertEqual(mock_adventurer.return_value.location, (0, 0))


    @patch('DungeonAdventure.DungeonAdventure.process_movement')
    @patch('DungeonAdventure.DungeonAdventure.process_potion')
    def test_process_user_input(self, mock_process_potion, mock_process_movement):
        # mock processing user input for movement and potion
        game = DungeonAdventure()

        game.process_user_input("S")
        mock_process_movement.assert_called_once_with("S")

        game.process_user_input("H")
        mock_process_potion.assert_called_once_with("H")

    @patch('builtins.input', side_effect=['Hard', ''])
    def test_check_game_over(self, mock_input):
        # check game over after setting game to over
        game = DungeonAdventure()
        game.adventurer.hit_points = 0
        is_over, outcome = game.check_game_over()
        self.assertTrue(is_over)
        self.assertEqual(outcome, "lose")

    @patch('DungeonAdventure.DungeonAdventure.get_user_input', side_effect=['N', 'Q'])
    def test_play_game(self, mock_get_user_input):
        #test game plays
        game = DungeonAdventure()
        game.play_game()
        self.assertTrue(game.user_quit)

if __name__ == '__main__':
    unittest.main()
