import random
from Room import Room
from collections import deque

class Maze:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns


    def __str__(self):
        pass

    def create_room(self, row, column):
        self.create_doors(row, column)
        self.neighbor_doors(row, column)
        return Room(row, column)

    def get_neighbors(self, row, column):
        neighbors = []
        if row > 0:
            north_neighbor = self.maze[row - 1][column]
            neighbors.append(north_neighbor)
        if row < self.rows:
            south_neighbor = self.maze[row + 1][column]
            neighbors.append(south_neighbor)
        if column > 0:
            west_neighbor = self.maze[row][column - 1]
            neighbors.append(west_neighbor)
        if column < self.columns:
            east_neighbor = self.maze[row][column + 1]
            neighbors.append(east_neighbor)
        return neighbors
        
    
    # def close_edges(self, row, column):
    #     """Ensure that edges do not have outside doors."""
    #     if row == 0:
    #         self.northdoor = False
    #     if column == 0:
    #         self.westdoor = False
    #     if row == self.rows - 1:
    #         self.southdoor = False
    #     if column == self.columns - 1:
    #         self.eastdoor = False

    def create_doors(self, row, column):
        """
        1.Ensure that if a room has a northdoor, the northern neighbor has a complementary southdoor, etc.
        2.Open complementary doors to neighboring open doors, then run random number generator to open other doors.

        :param row:
        :param column:
        :return:
        """
        if row > 0 and self.maze[row - 1][column].get_southdoor() == True:
            self.maze[row][column].set_northdoor(True)
        if column > 0 and self.maze[row][column - 1].get_eastdoor() == True:
            self.maze[row][column].set_westdoor(True)

        if row < self.rows - 1:
            if random.randint(1, 100) <= 50:
                self.maze[row][column].set_southdoor(True)
        if column < self.columns - 1:
            if random.randint(1, 100) <= 50:
                self.maze[row][column].set_eastdoor(True)

    def is_valid_room(self, row, column):
        """
        Verifies whether a room is valid for traversal and entry
        """
        return 0 <= row < self.rows and 0 <= column < self.columns




    def draw_maze(self):
        """
        Draws a maze map
        """
        for i in range(self.rows):
            for j in range(self.columns):
                self.maze[i][j].draw_top()
            print()
            for j in range(self.columns):
                self.maze[i][j].draw_middle()
            print()
            for j in range(self.columns):
                self.maze[i][j].draw_bottom()
            print()

    def generate_maze(self):
        self.maze = []
        for i in range(self.rows):
            self.maze.append([])
            for j in range(self.columns):
                self.maze[-1].append(Room(i, j))
                self.create_doors(i, j)
        return self.maze

    def generate_and_traverse(self):
        self.generate_maze()
        self.traverse()
    def set_items(self):
        pass
    def set_pillars(self):
        pass

    def traverse(self):
        """
        Traverses maze to ensure all rooms are accessible.
        """
        row = 0
        column = 0
        curr = self.maze[0][0]
        not_yet_visited = deque()
        not_yet_visited.append((curr, row, column))     # This is a tuple by definition with the ()


        while len(not_yet_visited) > 0:
            curr, row, column = not_yet_visited.popleft()
            if row == self.rows - 1 and column == self.columns - 1:
                return True

            if curr.entered == True:
                continue

            else:
                curr.set_entered()

                # Try moving south
                if curr.get_southdoor() == True:
                    not_yet_visited.append((self.maze[row + 1][column], row + 1, column))

                # Try moving east
                if curr.get_eastdoor() == True:
                    not_yet_visited.append((self.maze[row][column + 1], row, column + 1))

                # Try moving north
                if curr.get_northdoor() == True:
                    not_yet_visited.append((self.maze[row - 1][column], row - 1, column))

                # Try moving west
                if curr.get_westdoor() == True:
                    not_yet_visited.append((self.maze[row][column - 1], row, column - 1))

        return False
    # def traverse(self, row, col, room_count=0):
    #     """
    #     Traverses maze to ensure all rooms are accessible. If not, a new randomized maze is generated.
    #     """
    #     if not self.is_valid_room(row, col):
    #         # Invalid room, can't proceed in this direction
    #         return False, room_count
    #
    #     # Avoid revisiting the same room
    #     if self.maze[row][col].entered:
    #         return False, room_count
    #
    #     self.maze[row][col].set_entered()
    #     room_count += 1
    #
    #     # Check for exit conditions
    #     if room_count == ((self.rows) * (self.columns)):
    #         return True, room_count
    #
    #     # Try moving in all four directions: south, east, north, west
    #     found_exit, room_count = self.traverse(row + 1, col, room_count) if self.maze[row][col].get_southdoor() else (
    #     False, room_count)
    #     if not found_exit:
    #         found_exit, room_count = self.traverse(row, col + 1, room_count) if self.maze[row][col].get_eastdoor() else (
    #         False, room_count)
    #     if not found_exit:
    #         found_exit, room_count = self.traverse(row - 1, col, room_count) if row > 0 and self.maze[row][
    #             col].get_northdoor() else (False, room_count)
    #     if not found_exit:
    #         found_exit, room_count = self.traverse(row, col - 1, room_count) if col > 0 and self.maze[row][
    #             col].get_westdoor() else (False, room_count)
    #
    #     return found_exit, room_count


    def main(self):
        self.generate_maze()
        if self.traverse() == True:
            self.draw_maze()
        else:
            self.main()


if __name__ == "__main__":
    maze = Maze(15, 20)
    maze.main()
