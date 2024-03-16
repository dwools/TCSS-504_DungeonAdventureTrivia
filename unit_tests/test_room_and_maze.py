import os.path
import unittest
import pytest
from Room_and_Maze.maze import Maze
from Room_and_Maze.room import Room



class RoomMazeUnitTest(unittest.TestCase):
    def setUp(self):
        if os.path.exists("dungeon.txt"):
            os.remove("dungeon.txt")
        self.__test_maze_precursor = Maze(10, 10)

    def test_dungeon_text_file_writing(self):
        """
        Test that dungeon text file is successfully written from a generated maze. Requires successful implementation
        of Maze().get_neighbors(),  Room().draw_top_gui(), draw_middle_gui(), and draw_bottom_gui() methods.
        :return:
        """

        self.__test_maze_precursor.new_maze()
        assert os.path.exists("dungeon.txt")

    def test_maze_generation(self):
        """
        Test maze generation. Require successful instantiation of Room class objects.
        :return:
        """

        assert Maze(10, 10).generate_maze() is not None

    def test_maze_randomization(self):
        """
        Test that mazes are generated with random wall/door patterns.
        :return:
        """

        assert Maze(10, 10).generate_maze() != Maze(10, 10).generate_maze()



