import unittest
import pytest
from Room_and_Maze.maze import Maze
from Room_and_Maze.room import Room



class RoomMaze(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here

    # def test_room_generation(self):
    #     assert
    def test_maze_generation(self):
        """
        Test maze generation. Require successful instantiation of Room class objects.
        :return:
        """
        assert Maze(10, 10).generate_maze() is not None

    def test_maze_randomization(self):
        """
        Test that mazes are generated with random wall patterns.
        :return:
        """
        assert Maze(10, 10).generate_maze() != Maze(10, 10).generate_maze()



    def test_dungeon_text_file_writing(self):
        """
        Test that dungeon text file is successfully written from a generated maze. Requires successful implementation of Room class draw_top_gui, draw_middle_gui, and draw_bottom_gui methods.
        :return:
        """
        assert Maze(10, 10).write_maze_output().maze_desin is not None

        # assert test_write_maze.draw_maze() ==



if __name__ == '__main__':
    # Maze(10, 10).generate_maze()
    # Maze(10, 10).write_maze_output()
    unittest.main()
