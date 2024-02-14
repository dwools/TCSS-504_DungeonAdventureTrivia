import random
from Room import Room
from collections import deque


class Maze:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.dungeon_output_file = open("dungeon.txt", 'w')
        self.maze = []
        self.main()

    def get_neighbors(self, curr, visited):
        """
        Return list of rooms neighboring current room
        :param curr:
        :param visited:
        :return: neighbors: list
        """
        neighbors = []
        if curr.get_row() > 0 and not self.maze[curr.get_row() - 1][curr.get_column()] in visited:  # not north edge
            neighbors.append(self.maze[curr.get_row() - 1][curr.get_column()])

        if curr.get_row() < self.rows - 1 and not self.maze[curr.get_row() + 1][curr.get_column()] in visited: # not south edge
            neighbors.append(self.maze[curr.get_row() + 1][curr.get_column()])

        if curr.get_column() > 0 and not self.maze[curr.get_row()][curr.get_column() - 1] in visited:  # not west edge
            neighbors.append(self.maze[curr.get_row()][curr.get_column() - 1])

        if curr.get_column() < self.columns - 1 and not self.maze[curr.get_row()][curr.get_column() + 1] in visited: # not east edge
            neighbors.append(self.maze[curr.get_row()][curr.get_column() + 1])

        return neighbors


    def create_doors(self, curr, neighbor):
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

    def generate_maze(self):
        """
        Assemble maze
        :return: list
        """
        for i in range(self.rows):
            self.maze.append([])
            for j in range(self.columns):
                self.maze[-1].append(Room(i, j))
        origin = self.maze[0][0]
        target = self.maze[self.rows - 1][self.columns - 1]
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
                self.create_doors(curr, neighbor)
            else: stack.pop()


        origin = self.maze[0][0]
        target = self.maze[self.rows - 1][self.columns - 1]
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
                self.create_doors(curr, neighbor)
            else:
                stack.pop()

        return self.maze

    def write_dungeon_output(self):
        """
        Write text file of maze to be read into GUI
        :return: TextIO
        """
        maze_design = ''
        for i in range(self.rows):
            for j in range(self.columns):
                maze_design += self.maze[i][j].draw_top_gui()
            maze_design += '\n'
            for j in range(self.columns):
                maze_design += self.maze[i][j].draw_middle_gui()
            maze_design += '\n'
            for j in range(self.columns):
                maze_design += self.maze[i][j].draw_bottom_gui()
            maze_design += '\n'
        self.dungeon_output_file.write(maze_design)
        return self.dungeon_output_file

    def draw_maze(self):
        """
        Print
        :return:
        """
        for i in range(self.rows):
            for j in range(self.columns):
                self.maze[i][j].draw_top_gui()
            print()
            for j in range(self.columns):
                self.maze[i][j].draw_middle_gui()
            print()
            for j in range(self.columns):
                self.maze[i][j].draw_bottom_gui()
            print()



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


    def place_items(self, pit_prob=10, health_prob=10):
        """
        Lays down items in the maze
        :param pit_prob:
        :param health_prob:
        :return:
        """
        entrance = (0, 0)
        singular_items = ["i", "o", "A", "E", "I", "P"]
        while len(singular_items) != 0:
            i = random.randint(0, self.rows - 1)
            j = random.randint(0, self.columns - 1)
            room = self.maze[i][j]
            if len(room.items) == 0:
                item = singular_items.pop(0)
                room.place_item(item)
                if item == 'i':
                    room.set_entrance(True)
                    entrance = (i, j)

            for i in range(self.rows):
                for j in range(self.columns):
                    room = self.maze[i][j]
                    if len(room.items) == 0 and room.items[0] in singular_items:
                        pass
                    else:
                        if random.randint(0, 100) <= pit_prob:
                            room.place_item("X")
                        if random.randint(0, 100) <= health_prob:
                            room.place_item("H")

        return entrance


    def main(self):
        '''

        :return:
        '''
        self.generate_maze()
        self.write_dungeon_output()
        self.dungeon_output_file.close()
        # if self.traverse() == True:
        #     self.draw_maze()
        #     self.write_dungeon_output()
        #     # self.dungeon_output_file.close()
        # else:
        #     self.main()


if __name__ == "__main__":
    maze = Maze(45, 60)