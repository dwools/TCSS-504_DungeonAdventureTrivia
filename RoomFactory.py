import random
from Room import Room

class RoomFactory:

    def neighbor_doors(self, row, column):
        """Ensure that if a room has a northdoor, the northern neighbor has a complementary southdoor, etc."""
        if row > 0 and self.maze[row - 1][column].southdoor == True:
            self.northdoor = True
        if column > 0 and self.maze[row][column - 1].eastdoor == True:
            self.westdoor = True

    def create_doors(self, row, column):
        """Open complementary doors to neighboring open doors, then run random number generator to open other doors."""
        if row < self.rows - 1:
            if random.randint(1, 100) <= 100:
                self.southdoor = True
        if column < self.columns - 1:
            if random.randint(1, 100) <= 100:
                self.eastdoor = True
    def create_room(self, row, column):
        self.create_doors(row, column)
        self.neighbor_doors(row, column)
        self.draw()
        return Room(row, column)

