import random
from Room import Room

class Maze:

    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns
        self.__maze = []
        for i in range(self.__rows):
            self.__maze.append([])
            for j in range(self.__columns):
                self.__maze[-1].append(Room(i, j))
        self.__main()

    def __str__(self):
        pass

    def __create_room(self, row, column):
        pass

    def __get_neighbors(self, row, column):
        neighbors = []
        if row > 0:
            north_neighbor = self.__maze[row - 1][column]
            neighbors.append(north_neighbor)
        if row < self.__rows:
            south_neighbor = self.__maze[row + 1][column]
            neighbors.append(south_neighbor)
        if column > 0:
            west_neighbor = self.__maze[row][column - 1]
            neighbors.append(west_neighbor)
        if column < self.__columns:
            east_neighbor = self.__maze[row][column + 1]
            neighbors.append(east_neighbor)
        return neighbors
        
    
    def __close_edges(self, row, column):
        """Ensure that edges do not have outside doors."""
        if row == 0:
            self.__northdoor = False
        if column == 0:
            self.__westdoor = False
        if row == self.__rows - 1:
            self.__southdoor = False
        if column == self.__columns - 1:
            self.__eastdoor = False

    def __create_doors(self, row, column):
        """
        Ensure that if a room has a northdoor, the northern neighbor has a complementary southdoor, etc.
        Open complementary doors to neighboring open doors, then run random number generator to open other doors.
        """
        if row > 0 and self.__maze[row - 1][column].__southdoor == True:
            self.__northdoor = True
        if column > 0 and self.__maze[row][column - 1].__eastdoor == True:
            self.__westdoor = True

        if row < self.__rows - 1:
            if random.randint(1, 100) <= 50:
                self.__southdoor = True
        if column < self.__columns - 1:
            if random.randint(1, 100) <= 50:
                self.__eastdoor = True

    def is_valid_room(self, row, column):
        """
        Verifies whether a room is valid for traversal and entry
        """
        return 0 <= row < self.__rows and 0 <= column < self.__columns

    def traverse(self, row, column, traversed=False):
        """
        Traverses maze to ensure all rooms are accessible.
        """
        maze_area = self.__rows * self.__columns
        curr = self.__maze[0][0]
        room_count = 1

        while room_count < maze_area:
            if curr.__entered == True:
                return False
            else:
            # Try moving south
                if curr.__southdoor == True:
                    if curr.__entered == False:
                        curr.__set_entered()
                        room_count += 1
                    curr = self.__maze[row + 1][column]

                # Try moving east
                if curr.__eastdoor == True:
                    if curr.__entered == False:
                        curr.__set_entered()
                        room_count += 1
                    curr = self.__maze[row][column + 1]

                # Try moving north
                if curr.__northdoor == True:
                    if curr.__entered == False:
                        curr.__set_entered()
                        room_count += 1
                    curr = self.__maze[row - 1][column]

                # Try moving west
                if curr.__westdoor == True:
                    if curr.__entered == False:
                        curr.__set_entered()
                        room_count += 1
                    curr = self.__maze[row][column - 1]

        return traversed



    def __draw(self):
        """
        Draws a maze map
        """
        for i in range(self.__rows):
            for j in range(self.__columns):
                self.__maze[i][j].__draw_top()
            print()
            for j in range(self.__columns):
                self.__maze[i][j].__draw_middle()
            print()
            for j in range(self.__columns):
                self.__maze[i][j].__draw_bottom()
            print()



            

    def __generate_maze(self):
        pass

    def __set_items(self):
        pass
    def __set_pillars(self):
        pass
    def __main(self):
        self.__create_doors(self.__rows - 1, self.__columns - 1)
        self.__draw()

if __name__ == "__main__":
    maze = Maze(5, 5)
