import pandas as pd
import random
from RoomFactory import RoomFactory
from Room import Room

class Dungeon:
    def __init__(self, rows, columns):
        self.maze = []
        self.rows = rows
        self.columns = columns
        # self.build_maze()
        # use the traverse method when the dungeon initializes to ensure the entrance is connected to the exit
        traversable = False
        while not traversable:
        #     self.maze = []
            self.build_maze()
            self.generate()
            self.place_items()
            for row in self.maze:  # make sure all rooms have not been marked as entered
                for room in row:
                    room.set_entered(entered = False)
                traversable = self.traverse(0, 0)

        self.draw((0,0))

    def build_maze(self):
        self.maze = []
        for i in range(0, self.rows):
            self.maze.append([])
            for j in range (0, self.columns):
                self.maze[-1].append(Room(i,j))
                
    def get_neighbors(self, current, visited):
        neighbors = []
        if current._row > 0 and not self.maze[current._row - 1][current._column] in visited:  # not north edge
            neighbors.append(self.maze[current._row - 1][current._column])
        if current._row < self.rows - 1 and not self.maze[current._row + 1][current._column] in visited:
            neighbors.append(self.maze[current._row + 1][current._column])
        if current._column > 0 and not self.maze[current._row][current._column - 1] in visited:  # not north edge
            neighbors.append(self.maze[current._row][current._column - 1])
        if current._column < self.columns - 1 and not self.maze[current._row][current._column + 1] in visited:
            neighbors.append(self.maze[current._row][current._column + 1])
        return neighbors

    def create_doors(self, current, neighbor):
        if neighbor._column - current._column > 0:
            current._eastdoor = True
            neighbor._westdoor = True
        elif neighbor._column - current._column < 0:
            current._westdoor = True
            neighbor._eastdoor = True
        elif neighbor._row - current._row > 0:
            current._southdoor = True
            neighbor._northdoor = True
        elif neighbor._row - current._row < 0:
            current._northdoor = True
            neighbor._southdoor = True

    def generate(self):
        source = self.maze[0][0]
        target = self.maze[self.rows - 1][self.columns - 1]
        stack = []
        visited = []
        stack.append(source)
        visited.append(source)
        while len(stack) != 0:
            current = stack[-1]  # take to top node
            neighbors = self.get_neighbors(current, visited)
            if len(neighbors) != 0:
                neighbor = random.choice(neighbors)
                stack.append(neighbor)
                visited.append(neighbor)
                self.create_doors(current, neighbor)
            else:
                stack.pop()
    def draw(self, current_room):
        for i in range(self.rows):
            for j in range(self.columns):
                self.maze[i][j].draw_top()
            print()
            for j in range(self.columns):
                c_row, c_col = current_room
                if i == c_row and j == c_col:
                    self.maze[i][j].draw_middle(True)
                else:
                    self.maze[i][j].draw_middle()
            print()
            for j in range(self.columns):
                self.maze[i][j].draw_bottom()
            print()

    
    def place_items(self, pit_prob=10, hp_prob=10, vp_prob=10):
        initial_room = -1, -1
        items = ["i", "o", "A", "E", "I", "P"]
        while len(items) != 0:
            i = random.randint(0, self.rows - 1)
            j = random.randint(0, self.columns - 1)
            room = self.maze[i][j]
            if len(room._items) == 0:
                item = items.pop(0)
                room.place_item(item)
                if item == "i":
                    self._entrance = True
                    initial_room = i, j
                if item == "o":
                    self._exit = True
                if item == "A" or "E" or "I" or "P":
                    self._pillars = True

        for i in range(self.rows):
            for j in range(self.columns):
                room = self.maze[i][j]
                if len(room._items) == 1 and room._items[0] in ["i", "o", "A", "E", "I", "P"]:
                    pass # cannot place pit or potion in this room
                else:
                    if random.randint(0, 100) <= pit_prob:
                        room.place_item("X")
                    if random.randint(0, 100) <= hp_prob:
                        room.place_item("H")
                    if random.randint(0, 100) <= vp_prob:
                        room.place_item("V")

        return initial_room
    
    
    
    def traverse(self, row, col):
        found_exit = False
        if self.is_valid_room(row, col):
            self.maze[row][col].set_entered(entered = True)
            # check for exit
            if row == self.rows-1 and col == self.columns-1:
                return True
            # not at exit so try another room: south, east, north, west
            if self.maze[row][col]._southdoor:
                found_exit = self.traverse(row + 1, col) # south
            if self.maze[row][col]._eastdoor:
                if not found_exit:
                    found_exit = self.traverse(row, col + 1)  # east
            if not found_exit: # if we did not reach the exit from this room we need mark it as visited to avoid going into the room again
                self.maze[row][col].set_entered(entered = True)
        else:  # tried to move into a room that is not valid
            return False
        return found_exit
    

    def is_valid_room(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.columns

    def print_maze(self):
        maze = pd.DataFrame(self.maze)
        for index, row in maze.iterrows():
            split_row = [str(element).split('\n') for element in row]
            max_length = max(len(str(element)) for element in row)
            padded_row = [[line.ljust(max_length) for line in element] for element in split_row]
            for lines in zip(*padded_row):
                print(' '.join(lines))
            print()

if __name__ == "__main__":
    dungeon2 = Dungeon(5, 5)
    dungeon2.print_maze()

