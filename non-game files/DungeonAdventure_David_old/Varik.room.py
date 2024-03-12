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

r1 = Room(0, 0)
# r1.north = False
r1.south = True
r1.east = True
print(r1)
r1.draw_top()
print()
r1.draw_middle()
print()
r1.draw_bottom()