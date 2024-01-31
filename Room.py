import random

"""Creates the room class with constructors self, healing, vision, pit"""
class Room:
    """init function includes all features a room could have"""
    def __init__(self, row, column):
        self.__row = row
        self.__column = column
        self.__northdoor = False
        self.__eastdoor = False
        self.__westdoor = False
        self.__southdoor = False
        # self.__entrance = False
        # self.exit = False
        # self.blocked = False
        self.__entered = False
        # self.empty_room = False
        # self.multiple_items = False
        # self.pit = False
        # self.healing = False
        # self.vision = False
        # self.pillars = False
        # self.pillar_type = None
        self.__items = []
        # self.healingpoints = random.randint(5, 15) if self.healing else 0

    def __str__(self, is_current=False):
        room_design = ''
        if self.__northdoor == True:
            room_design += '* _ *'
        else:
            room_design += '*****'

        room_design += '\n'

        if self.__westdoor == True:
            room_design += '| '
        else:
            room_design += '* '

        if is_current:
            room_design += "#"
        else:
            item_count = len(self.__items)
            if item_count == 0:
                room_design += " "
            elif item_count == 1:
                room_design += f'{self.__items[0]}'
            else:
                room_design += "M"

        if self.__eastdoor == True:
            room_design += ' |'
        else:
            room_design += ' *'

        room_design += '\n'

        if self.__southdoor == True:
            room_design += '* _ *'
        else:
            room_design += '*****'

        return room_design

    def __repr__(self):
        return self.__str__()


    def __place_item(self, item):
        self.__items.append(item)

    def __remove_item(self, item):
        self.__items.remove(item)

    def __set_entered(self):
        self.__entered = True

    def __draw_top(self):
        if self.__northdoor == True:
            print('*   *', end='')
        else:
            print('*****', end='')

    def __draw_bottom(self):
        if self.__southdoor == True:
            print('*   *', end='')
        else:
            print('*****', end='')

    def __draw_middle(self, is_current=False):
        if self.__westdoor == True:
            print(' ', end='')
        else:
            print('* ', end='')

        if is_current:
            print("#", end="")
        else:
            item_count = len(self.__items)
            if item_count == 0:
                print(" ", end="")
            elif item_count == 1:
                print(self.__items[0], end="")
            else:
                print("M", end="")

        if self.__eastdoor == True:
            print('  ', end='')
        else:
            print(' *', end='')

    def __draw(self):
        self.__draw_top()
        print()
        self.__draw_middle()
        print()
        self.__draw_bottom()



if __name__ == "__main__":
    room = Room(0, 0)
    room.__eastdoor = True
    room.__southdoor = True
    print()
    print(room)



