import random
import os
from Room_and_Maze.room import Room
from collections import deque
# from dungeon_adventure import DungeonAdventure
import pickle


class Maze:
    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns

        # Here: See if pickling saves a maze list or a dungeon.txt file. If it does, pass it into the above setter method. If not, figure out how to preserve the maze or text file.


    def new_maze(self):
        """
        Generating a new maze by using the dungeon.txt file
        :return:
        """
        self.__maze_output_file = open("dungeon.txt", 'w')
        self.generate_maze()
        self.write_maze_output()
        self.__maze_output_file.close()


    def get_neighbors(self, curr, visited):
        """
        Return list of rooms neighboring current room
        :param curr:
        :param visited:
        :return: neighbors: list
        """
        neighbors = []
        if curr.get_row() > 0 and not self.__maze[curr.get_row() - 1][curr.get_column()] in visited:  # not north edge
            neighbors.append(self.__maze[curr.get_row() - 1][curr.get_column()])

        if curr.get_row() < self.__rows - 1 and not self.__maze[curr.get_row() + 1][curr.get_column()] in visited: # not south edge
            neighbors.append(self.__maze[curr.get_row() + 1][curr.get_column()])

        if curr.get_column() > 0 and not self.__maze[curr.get_row()][curr.get_column() - 1] in visited:  # not west edge
            neighbors.append(self.__maze[curr.get_row()][curr.get_column() - 1])

        if curr.get_column() < self.__columns - 1 and not self.__maze[curr.get_row()][curr.get_column() + 1] in visited: # not east edge
            neighbors.append(self.__maze[curr.get_row()][curr.get_column() + 1])

        return neighbors




    def generate_maze(self):
        """
        Assemble maze
        :return: list
        """

        def create_doors(curr, neighbor):
            """
            1.Ensure that if a room has a northdoor, the northern neighbor has a complementary southdoor, etc.
            2.Open complementary doors to neighboring open doors, then run random number generator to open other doors.

            :param curr
            :param neighbor:
            :return:
            """
            if neighbor.get_column() - curr.get_column() > 0:
                curr.set_eastdoor(True)
                neighbor.set_westdoor(True)
            if neighbor.get_column() - curr.get_column() < 0:
                curr.set_westdoor(True)
                neighbor.set_eastdoor(True)
            if neighbor.get_row() - curr.get_row() > 0:
                curr.set_southdoor(True)
                neighbor.set_northdoor(True)
            if neighbor.get_row() - curr.get_row() < 0:
                curr.set_northdoor(True)
                neighbor.set_southdoor(True)

        self.__maze = []
        for i in range(self.__rows):
            self.__maze.append([])
            for j in range(self.__columns):
                self.__maze[-1].append(Room(i, j))
        origin = self.__maze[0][0]
        target = self.__maze[self.__rows - 1][self.__columns - 1]
        stack = []
        visited = []
        stack.append(origin)
        visited.append(origin)
        while len(stack) != 0:
            curr = stack[-1]
            neighbors = self.get_neighbors(curr, visited)
            if len(neighbors) != 0:
                neighbor = random.choice(neighbors)
                stack.append(neighbor)
                visited.append(neighbor)
                create_doors(curr, neighbor)
            else: stack.pop()

        origin = self.__maze[0][0]
        target = self.__maze[self.__rows - 1][self.__columns - 1]
        stack = []
        visited = []
        stack.append(origin)
        visited.append(origin)
        curr = origin
        while curr != target:
            curr = stack[-1]
            neighbors = self.get_neighbors(curr, visited)
            if len(neighbors) != 0:
                neighbor = random.choice(neighbors)
                stack.append(neighbor)
                visited.append(neighbor)
                create_doors(curr, neighbor)
            else:
                stack.pop()

        return self.__maze

    def write_maze_output(self):
        """
        Write text file of maze to be read into GUI
        :return: TextIO
        """
        maze_design = ''
        for i in range(self.__rows):
            for j in range(self.__columns):
                maze_design += self.__maze[i][j].draw_top_gui()
            maze_design += '\n'
            for j in range(self.__columns):
                maze_design += self.__maze[i][j].draw_middle_gui()
            maze_design += '\n'
            for j in range(self.__columns):
                maze_design += self.__maze[i][j].draw_bottom_gui()
            maze_design += '\n'
        self.__maze_output_file.write(maze_design)
        return self.__maze_output_file

    def draw_maze(self):
        """
        Print
        :return:
        """
        for i in range(self.__rows):
            for j in range(self.__columns):
                self.__maze[i][j].draw_top_gui()
            print()
            for j in range(self.__columns):
                self.__maze[i][j].draw_middle_gui()
            print()
            for j in range(self.__columns):
                self.__maze[i][j].draw_bottom_gui()
            print()


    def get_maze_output_file(self):
        return self.__maze_output_file

    def get_rows(self):
        return self.__rows

    def get_cols(self):
        return self.__rows


if __name__ == "__main__":
    maze = Maze(45, 60)