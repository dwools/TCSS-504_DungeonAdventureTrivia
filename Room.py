import random


"""Creates the room class with constructors self, healing, vision, pit"""
class Room:
    """init function includes all features a room could have"""
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.northdoor = False
        self.eastdoor = False
        self.westdoor = False
        self.southdoor = False
        # self.entrance = False
        # self.exit = False
        # self.blocked = False
        self.entered = False
        # self.empty_room = False
        # self.multiple_items = False
        # self.pit = False
        # self.healing = False
        # self.vision = False
        # self.pillars = False
        # self.pillar_type = None
        self.items = []
        # self.healingpoints = random.randint(5, 15) if self.healing else 0

    def __str__(self, is_current=False):
        room_design = ''
        if self.northdoor == True:
            room_design += '* _ *'
        else:
            room_design += '*****'

        room_design += '\n'

        if self.westdoor == True:
            room_design += '| '
        else:
            room_design += '* '

        if is_current:
            room_design += "#"
        else:
            item_count = len(self.items)
            if item_count == 0:
                room_design += " "
            elif item_count == 1:
                room_design += f'{self.items[0]}'
            else:
                room_design += "M"

        if self.eastdoor == True:
            room_design += ' |'
        else:
            room_design += ' *'

        room_design += '\n'

        if self.southdoor == True:
            room_design += '* _ *'
        else:
            room_design += '*****'

        return room_design

    def __repr__(self):
        return self.str()


    def place_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def set_entered(self):
        self.entered = True

    def draw_top(self):
        if self.northdoor == True:
            print('*   *', end='')
        else:
            print('*****', end='')

    def draw_bottom(self):
        if self.southdoor == True:
            print('*   *', end='')
        else:
            print('*****', end='')

    def draw_middle(self, is_current=False):
        if self.westdoor == True:
            print('  ', end='')
        else:
            print('* ', end='')

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

        if self.eastdoor == True:
            print('  ', end='')
        else:
            print(' *', end='')

    def draw(self):
        self.draw_top()
        print()
        self.draw_middle()
        print()
        self.draw_bottom()



if __name__ == "__main__":
    room = Room(0, 0)
    room.eastdoor = True
    room.southdoor = True
    print()
    print(room)
    room.draw()



