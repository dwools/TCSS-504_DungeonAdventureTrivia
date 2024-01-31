import random

class Room:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.north = False
        self.south = False
        self.west = False
        self.east = False
        self.items = []
    def __str__(self):
        result = ""
        if self.north:
            result += "N"
        else:
            result += "_"
        if self.south:
            result += "S"
        else:
            result += "_"
        if self.west:
            result += "W"
        else:
            result += "_"
        if self.east:
            result += "E"
        else:
            result += "_"
        return result
    def place_item(self, item):
        self.items.append(item)
    def remove_item(self, item):
        self.items.remove(item)

    def draw_top(self):
        if self.north:
            print("*   *", end="")
        else:
            print("*****", end="")

    def draw_bottom(self):
        if self.south:
            print("*   *", end="")
        else:
            print("*****", end="")

    def draw_middle(self, is_current=False):
        if self.west:
            print(" ", end="")
        else:
            print("*", end="")

        print(" ", end="")
        if is_current:
            print("#", end="")
        else:
            item_count = len(self.items)
            if item_count == 0:
                print(" ", end="")
            elif item_count == 1:
                print(self.items[0], end="")
            else:
                print("M", end="")
        print(" ", end="")

        if self.east:
            print(" ", end="")
        else:
            print("*", end="")

# r1 = Room(0, 0)
# # r1.north = False
# r1.south = True
# r1.east = True
# print(r1)
# r1.draw_top()
# print()
# r1.draw_middle()
# print()
# r1.draw_bottom()


class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.rooms = []
        for i in range(self.rows):
            self.rooms.append([])
            for j in range(self.cols):
                self.rooms[-1].append(Room(i, j))

    def print(self):
        for i in range(self.rows):
            for j in range(self.cols):
                #print(self.rooms[i][j], sep=" ", end="")
                print(str(self.rooms[i][j]) + " ", end="")
            print()

    def get_neighbors(self, current, visited):
        neighbors = []
        if current.row > 0 and not self.rooms[current.row - 1][current.col] in visited:  # not north edge
            neighbors.append(self.rooms[current.row - 1][current.col])
        if current.row < self.rows - 1 and not self.rooms[current.row + 1][current.col] in visited:
            neighbors.append(self.rooms[current.row + 1][current.col])
        if current.col > 0 and not self.rooms[current.row][current.col - 1] in visited:  # not north edge
            neighbors.append(self.rooms[current.row][current.col - 1])
        if current.col < self.cols - 1 and not self.rooms[current.row][current.col + 1] in visited:
            neighbors.append(self.rooms[current.row][current.col + 1])
        return neighbors

    def create_doors(self, current, neighbor):
        if neighbor.col - current.col > 0:
            current.east = True
            neighbor.west = True
        elif neighbor.col - current.col < 0:
            current.west = True
            neighbor.east = True
        elif neighbor.row - current.row > 0:
            current.south = True
            neighbor.north = True
        elif neighbor.row - current.row < 0:
            current.north = True
            neighbor.south = True

    def generate(self):
        source = self.rooms[0][0]
        target = self.rooms[self.rows - 1][self.cols - 1]
        stack = []
        visited = []
        stack.append(source)
        visited.append(source)
        while len(stack) != 0:
            current = stack[-1] # take to top node
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
            for j in range(self.cols):
                self.rooms[i][j].draw_top()
            print()
            for j in range(self.cols):
                c_row, c_col = current_room
                if i == c_row and j == c_col:
                    self.rooms[i][j].draw_middle(True)
                else:
                    self.rooms[i][j].draw_middle()
            print()
            for j in range(self.cols):
                self.rooms[i][j].draw_bottom()
            print()

    def place_items(self, pit_prob=10, hp_prob=10, vp_prob=10):
        initial_room = -1, -1
        items = ["i", "o", "A", "E", "I", "P"]
        while len(items) != 0:
            i = random.randint(0, self.rows - 1)
            j = random.randint(0, self.cols - 1)
            room = self.rooms[i][j]
            if len(room.items) == 0:
                item = items.pop(0)
                room.place_item(item)
                if item == "i":
                    initial_room = i, j

        for i in range(self.rows):
            for j in range(self.cols):
                room = self.rooms[i][j]
                if len(room.items) == 1 and room.items[0] in ["i", "o", "A", "E", "I", "P"]:
                    pass # cannot place pit or potion in this room
                else:
                    if random.randint(0, 100) <= pit_prob:
                        room.place_item("X")
                    if random.randint(0, 100) <= hp_prob:
                        room.place_item("H")
                    if random.randint(0, 100) <= vp_prob:
                        room.place_item("V")

        return initial_room


m1 = Maze(4, 4)
m1.generate()
# m1.print()
# m1.place_items()
m1.draw((0, 0))