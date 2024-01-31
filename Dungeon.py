import random
from Room import Room

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
        
    
    def close_edges(self, row, column):
        """Ensure that edges do not have outside doors."""
        if row == 0:
            self.northdoor = False
        if column == 0:
            self.westdoor = False
        if row == self.rows - 1:
            self.southdoor = False
        if column == self.columns - 1:
            self.eastdoor = False

    def neighbor_doors(self, row, column):
        """Ensure that if a room has a northdoor, the northern neighbor has a complementary southdoor, etc."""
        if row > 0 and self.maze[row - 1][column].southdoor == True:
            self.maze[row][column].northdoor = True
        if column > 0 and self.maze[row][column - 1].eastdoor == True:
            self.maze[row][column].westdoor = True
        if row > self.rows - 1 and self.maze[row + 1][column].northdoor == True:
            self.maze[row][column].southdoor = True
        if column > self.columns - 1 and self.maze[row][column + 1].westdoor == True:
            self.maze[row][column].eastdoor = True

    def create_doors(self, row, column):
        """Open complementary doors to neighboring open doors, then run random number generator to open other doors."""
        if row > 0:
            if random.randint(1, 100) <= 100:
                self.maze[row][column].northdoor = True
        if column > 0:
            if random.randint(1, 100) <= 100:
                self.maze[row][column].westdoor = True
        if row < self.rows - 1:
            if random.randint(1, 100) <= 100:
                self.maze[row][column].southdoor = True
        if column < self.columns - 1:
            if random.randint(1, 100) <= 100:
                self.maze[row][column].eastdoor = True

    def is_valid_room(self, row, column):
        """
        Verifies whether a room is valid for traversal and entry
        """
        return 0 <= row < self.rows and 0 <= column < self.columns

    def traverse(self, row, column, traversed=False):
        """
        Traverses maze to ensure all rooms are accessible.
        """
        maze_area = self.rows * self.columns
        curr = self.maze[0][0]
        room_count = 1

        while room_count < maze_area:
            if curr.entered == True:
                return False
            else:
            # Try moving south
                if curr.southdoor == True:
                    if curr.entered == False:
                        curr.set_entered()
                        room_count += 1
                    curr = self.maze[row + 1][column]

                # Try moving east
                if curr.eastdoor == True:
                    if curr.entered == False:
                        curr.set_entered()
                        room_count += 1
                    curr = self.maze[row][column + 1]

                # Try moving north
                if curr.northdoor == True:
                    if curr.entered == False:
                        curr.set_entered()
                        room_count += 1
                    curr = self.maze[row - 1][column]

                # Try moving west
                if curr.westdoor == True:
                    if curr.entered == False:
                        curr.set_entered()
                        room_count += 1
                    curr = self.maze[row][column - 1]

        return traversed



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
        pass

    def set_items(self):
        pass
    def set_pillars(self):
        pass
    def main(self):
        self.maze = []
        for i in range(self.rows):
            self.maze.append([])
            for j in range(self.columns):
                self.maze[-1].append(Room(i, j))
                self.neighbor_doors(i, j)
                self.create_doors(i, j)

        self.draw_maze()

if __name__ == "__main__":
    maze = Maze(1, 3)
    maze.main()
