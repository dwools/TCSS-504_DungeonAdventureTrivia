import random


"""Creates the room class with constructors self, healing, vision, pit"""
class Room:
    """init function includes all features a room could have"""
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.__northdoor = False
        self.__eastdoor = False
        self.__westdoor = False
        self.__southdoor = False
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

    def get_northdoor(self):
        return self.__northdoor

    def get_southdoor(self):
        return self.__southdoor

    def get_eastdoor(self):
        return self.__eastdoor

    def get_westdoor(self):
        return self.__westdoor

    def set_northdoor(self, param):
        self.__northdoor = param

    def set_southdoor(self, param):
        self.__southdoor = param

    def set_eastdoor(self, param):
        self.__eastdoor = param

    def set_westdoor(self, param):
        self.__westdoor = param

    def place_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_entered(self):
        return self.__entered

    def set_entered(self):
        self.entered = True

    def draw_top(self):
        if self.__northdoor == True:
            print('* _ *', end='')
        else:
            print('*****', end='')

    def draw_bottom(self):
        if self.__southdoor == True:
            print('* _ *', end='')
        else:
            print('*****', end='')

    def draw_middle(self, is_current=False):
        if self.__westdoor == True:
            print('| ', end='')
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

        if self.__eastdoor == True:
            print(' |', end='')
        else:
            print(' *', end='')

    # def draw_maze(self, maze, rows, columns):
    #     """
    #     Draws a maze map
    #     """
    #     for i in range(rows):
    #         for j in range(columns):
    #             maze[i][j].__draw_top()
    #         print()
    #         for j in range(columns):
    #             maze[i][j].__draw_middle()
    #         print()
    #         for j in range(columns):
    #             maze[i][j].__draw_bottom()
    #         print()


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



