from Room import RoomFactory
from Room import Room

import random

class Dungeon:
    def __init__(self, rows, columns):
        self.__maze = []
        self.__rows = rows
        self.__columns = columns
        self.__entrance_position = None
        self.__exit_position = None
        # self.build_maze()
        # self.__adventurer_position = self.__entrance_position
        for i in range(self.__rows):
            self.__maze.append([])
            for j in range(self.__columns):
                self.__maze[-1].append(RoomFactory.create_room(i, j))

    #
    def print(self):
        for i in range(self.__rows):
            for j in range(self.__columns):
                # print(self.rooms[i][j], sep=" ", end="")
                print(str(self.__maze[i][j]) + " ", end="")
            print()

    def draw(self):
        for i in range(self.__rows):
            if i == 0:
                self._northdoor = False
            if i - len(self.__rows)-1 == 0:
                self.__southdoor = False
        for j in range (self.__columns):
            if i == 0:
                self._westdoor = False
            if i - len(self.__columns)-1 == 0:
                self.eastdoor = False


    def __init__(self, size = 3):
        self.__maze = [[None for _ in range(size)] for _ in range(size)]  ## Create an empty __maze to populate with rooms
        self.__rowCount = size
        self.__colCount = size
        for i in range(size):
            for j in range(size):
                content = ''

                if i > 0 and self.__maze[i - 1][j]._southdoor:  # if previous room had a south door:
                    content += 'N'                          # north door added in next room
                if j > 0 and self.__maze[i][j - 1]._eastdoor:   # if previous room had an east door:
                    content += 'W'                          # add west door to next room

                # Additional logic to randomly add other doors, ensuring playability
                # Random chance for south and east door
                if random.randint(0, 100) <= 50:  # 50 % chance for door
                    content += 'E'
                if random.randint(0, 100) <= 50:  # 50 % chance for door
                    content += 'S'
                if i == 0 and j == 0:
                    content += 'i'
                    # Only one room will have an exit and the room that contains the exit will contain NOTHING else
                if i == 2 and j == 2:
                    content += 'O'
                self.__maze[i][j] = Room(content, i, j)

    def get_neighbors(self, current, visited):
        neighbors = []
        if current._row > 0 and not self.__maze[current._row - 1][current._column] in visited:  # not north edge
            neighbors.append(self.__maze[current._row - 1][current._column])
        if current._row < self.__rows - 1 and not self.__maze[current._row + 1][current._column] in visited:
            neighbors.append(self.__maze[current._row + 1][current._column])
        if current._column > 0 and not self.__maze[current._row][current._column - 1] in visited:  # not north edge
            neighbors.append(self.__maze[current._row][current._column - 1])
        if current._column < self.__columns - 1 and not self.__maze[current._row][current._column + 1] in visited:
            neighbors.append(self.__maze[current._row][current._column + 1])
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
        source = self.__maze[0][0]
        target = self.__maze[self.__rows - 1][self.__columns - 1]
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







    # def __str__(self):
    #     return str(self.__maze)
    # #
    # #
    # def __repr__(self):
    #     return self.__str__()
    #
    # def build_maze(self):
    #     self.__maze = []
    #     for i in range(self.__rows):
    #         self.__maze.append([])
    #         for j in range(self.__columns):
    #             self.__maze[-1].append(RoomFactory.create_room(i, j))
                # content = ''
                # if i > 0 and self.__maze[i - 1][j]._southdoor:  # if previous room had a south door:
                #     content += 'N'  # north door added in next room
                # if j > 0 and self.__maze[i][j - 1]._eastdoor:  # if previous room had an east door:
                #     content += 'W'  # add west door to next room
    #
    #             # Additional logic to randomly add other doors, ensuring playability
    #             # Random chance for south and east door
    #             if random.randint(0, 100) <= 50:  # 10 % chance for door
    #                 content += 'E'
    #             if random.randint(0, 100) <= 50:  # 10 % chance for door
    #                 content += 'S'
    #             if i == 0 and j == 0:
    #                 content += 'i'
    #                 # Only one room will have an exit and the room that contains the exit will contain NOTHING else
    #             if i == 2 and j == 2:
    #                 content += 'O'

    # def pick_random_empty_room(self):
    #     while True:
    #         random_i = random.randrange(0, self.__size)
    #         random_j = random.randrange(0, self.__size)
    #         random_room = self.__maze[random_i][random_j]
    #         if random_room.is_empty() and not random_room.is_entrance() and not random_room.is_exit() and not random_room.is_blocked():
    #             return random_i, random_j
    #
    # def pick_random_room(self):
    #     while True:
    #         random_i = random.randrange(0, self.__size)
    #         random_j = random.randrange(0, self.__size)
    #         random_room = self.__maze[random_i][random_j]
    #         if not random_room.is_entrance() and not random_room.is_exit() and not random_room.is_blocked():
    #             return random_i, random_j
    #         return random_i, random_j


if __name__ == "__main__":
    dungeon1 = Dungeon(3, 3)
    dungeon1.generate()
    dungeon1.print()
# dungeon1.pick_random_empty_room()


import pandas as pd
import random
from IPython.display import display, HTML

from Room import Room
from Room import RoomFactory


class Dungeon:
    """
    Creates/contains a maze of Rooms
The maze should be randomly generated.

You must incorporate an algorithm to ensure traversal of the maze from entrance to exit is possible once the maze has been generated. If the maze is not traversable, then generate a new one.

The maze should have ‘dead ends’ (places that lead no further).

The type of data structure you use to represent your maze is up to you:
A list of lists has some advantages. A linked list of linked lists has other advantages.

You could represent your maze via rooms that have references to other rooms (this would be much like a
linked list structure but without all the basic linked list functionality which you do not need for this
assignment).

Places the Entrance, the Exit, and the Pillars. NOTES: the entrance and exit are empty rooms. The Pillars cannot be at the entrance or the exit. No two Pillars may be in the same room.

(Possibly) Maintains location of the Adventurer in the Dungeon.

Contains a __str__ () method that builds a String containing information about the entire dungeon.
    """

    # def __init__(self, size = 3):
    #     self.__maze = [[None for _ in range(size)] for _ in range(size)]  ## Create an empty __maze to populate with rooms
    #     self.__rowCount = size
    #     self.__colCount = size
    #     for i in range(size):
    #         for j in range(size):
    #             content = ''
    #
    #             if i > 0 and self.__maze[i - 1][j]._southdoor:  # if previous room had a south door:
    #                 content += 'N'                          # north door added in next room
    #             if j > 0 and self.__maze[i][j - 1]._eastdoor:   # if previous room had an east door:
    #                 content += 'W'                          # add west door to next room
    #
    #             # Additional logic to randomly add other doors, ensuring playability
    #             # Random chance for south and east door
    #             if random.randint(0, 100) <= 50:  # 50 % chance for door
    #                 content += 'E'
    #             if random.randint(0, 100) <= 50:  # 50 % chance for door
    #                 content += 'S'
    #             if i == 0 and j == 0:
    #                 content += 'i'
    #                 # Only one room will have an exit and the room that contains the exit will contain NOTHING else
    #             if i == 2 and j == 2:
    #                 content += 'O'
    #             self.__maze[i][j] = Room(content, i, j)


    def __init__(self, rows, columns):
        self.__maze = []
        self.__rows = rows
        self.__columns = columns
        self.__entrance_position = None
        self.__exit_position = None
        # self.build_maze()
        # self.__adventurer_position = self.__entrance_position
        for i in range(self.__rows):
            self.__maze.append([])
            for j in range(self.__columns):
                self.__maze[-1].append(RoomFactory.create_room(i, j))

    def print(self):
        for i in range(self.__rows):
            for j in range(self.__columns):
                # print(self.rooms[i][j], sep=" ", end="")
                print(str(self.__maze[i][j]) + " ", end="")
            print()


    # def build_maze(self):
    #
    #     for r in range(0, self.__rowCount):
    #         self.__maze.append(
    #             [RoomFactory.create_room() for c in range(0, self.__colCount)])

        # def set_entrance(self):
        #     pass


    # def __str__(self):
    #     line_string = ''
    #     for row in self.__maze:
    #         def build_border(row):
    #             border_string = ''
    #             for room in row:
    #                 if room is not row[-1]:
    #                     border_string += '* * '
    #                 else:
    #                     border_string += '* * *\n'
    #             return border_string
    #
    #         def build_wall(row):
    #             wall_string = ''
    #             for room in row:
    #                 if room is not row[-1]:
    #                     wall_string += '* _ '
    #                 else:
    #                     wall_string += '* _ *\n'
    #             return wall_string
    #
    #         if row is self.__maze[0]:
    #             line_string += build_border(row)
    #         for room in row:
    #             if room is row[0]:
    #                 line_string += f'* {str(room)[0]} '
    #             elif room is not row[-1]:
    #                 line_string += f'| {str(room)[0]} '
    #             else:
    #                 line_string += f'| {str(room)[0]} *\n'
    #         line_string += build_wall(row)
    #     border = build_border(row)
    #     line_string = line_string[:-(len(border))] + border
    #     return line_string


    def pick_random_empty_room(self):
        # while True:
        random_i = random.randrange(0, self.__rowCount)
        random_j = random.randrange(0, self.__colCount)
        random_room = self.__maze[random_i][random_j]
        if random_room.is_empty:
        # if random_room.is_empty and not random_room.is_entrance and not random_room.is_exit and not random_room.is_blocked:
            return print(random_i, random_j)
        else:
            self.pick_random_empty_room()


    # def pick_random_room(self):
    #     # while True:
    #         random_i = random.randrange(0, self.__rowCount)
    #         random_j = random.randrange(0, self.__colCount)
    #         random_room = self.__maze[random_i][random_j]
    #         if not random_room.is_entrance() and not random_room.is_exit() and not random_room.is_blocked():
    #             return random_i, random_j
    #         return print(random_i, random_j)


            # self..is_entrance()


        # def set_exit(self):
            # .is_exit()

        # #For each room, run a random integer generator to determine whether the room contains a door or not on each (interior) wall.
        # def roll():
        #     x = random.randint(0, 1)
        #     if x == 0:
        #         return False
        #     else:
        #         return True
        #
        # rooms = ["NW", "N", "NE", "W", "X", "E", "SW", "S", "SE"]
        # for current_room in rooms:
        #     result = set("NEWS") - set(current_room)
        #     if "N" in result:
        #         northdoor = roll()
        #     if "E" in result:
        #         eastdoor = roll()
        #     if "W" in result:
        #         westdoor = roll()
        #     if "S" in result:
        #         south_door = roll()
        #     self.__maze.append(RoomFactory.create_room())

            # Put these in the room class:
            #  Room(northdoor = north_door,
            #       eastdoor = east_door,
            #       westdoor = west_door,
            #       southdoor = south_door

        # make some rooms impassible
        # rand gen chance a room is impassable
        # GIGANTIC NOTE: AFTER MAKING ROOMS IMPASSABLE YOU NEED TO CHECK TO SEE IF YOU CAN TRAVERSE MAZE
        # >>IF NOT YOU NEED TO RESET IMPASSABLE ROOMS
        # for row in range(0, self.__rowCount):
        #     for col in range(0, self.__colCount):
        #         number = random.randint(1, 100)
        #         if number > 80:  # x% chance a room is impassable
        #             self.__maze[row][col].is_blocked()

        # set entrance and exit, make sure you make room passable
        # self.__maze[0][0].is_entrance()
        # self.__maze[0][0].is_not_blocked()
        # self.__maze[self.__rowCount - 1][self.__colCount - 1].is_exit()
        # self.__maze[self.__rowCount - 1][self.__colCount - 1].is_not_blocked()

    # def wrap_df_text(self):
    #     return display(HTML(self.to_html().replace("\\n", "<br>")))

    # def print_maze(self):
    #
    #     maze = pd.DataFrame(self.__maze)
    #     for index, row in maze.iterrows():
    #         split_row = [str(element).split('\n') for element in row]
    #         max_length = max(len(str(element)) for element in row)
    #         padded_row = [[line.ljust(max_length) for line in element] for element in split_row]
    #         for lines in zip(*padded_row):
    #             print(' '.join(lines))
    #         print()

        # print(self.__maze)

        # for col in range(0, self.__colCount):
        #     print("col", col)
        #     for row in range(0, self.__rowCount):
        #         print("row ", row)
        #         print(self.__maze[row][col].__str__())
        #     print()
        # print(display(HTML(maze.to_html().replace("\\n", "<br>"))))





    #     # print(self.__maze)
    #
    #     temp_list = []
    #     result = []
    #     i = 0
    #     for i in len(self.__maze[i]):
    #         if i // int(self.__rowCount):
    #             temp_list.append(i)
    #             result.append(temp_list)
    #             temp_list = []
    #         else:
    #             temp_list.append(i)
    #         i += 1
    #     result.append(temp_list)
    #     grid = pd.DataFrame(result)
    #     print(grid)


        # #
        # for row in range(0, self.__rowCount):
        #     print("row ", row)
        #     for col in range(0, self.__colCount):
        #         print("col", col)
        #         print(self.__maze[row][col].__str__())
        #     print()










    def traverse(self, row, col):
        found_exit = False
        if self.is_valid_room(row, col):
            self.__maze[row][col].set_entered(entered = True)
            # check for exit
            if self.__maze[row][col].is_exit:
                return True
            # not at exit so try another room: south, east, north, west
            if self.__maze[row][col]._southdoor:
                found_exit = self.traverse(row + 1, col) # south
            if self.__maze[row][col]._eastdoor:
                if not found_exit:
                    found_exit = self.traverse(row, col + 1)  # east
            # if not found_exit:
            #     found_exit = self.traverse(row - 1, col)  # north
            # if not found_exit:
            #     found_exit = self.traverse(row, col - 1)  # west

            # if we did not reach the exit from this room we need mark it as visited to
            # avoid going into the room again
            if not found_exit:
                self.__maze[row][col].set_entered(entered = True)

        else:  # tried to move into a room that is not valid
            return False
        return found_exit



    def is_valid_room(self, row, col):
        # return 0 <= row < self.__rowCount and col >= 0 and col < self.__colCount and self.__maze[row][
        #     col].can_enter()
        return 0 <= row < self.__rowCount and 0 <= col < self.__colCount

    def get_room(self, row, col):  # used by DungeonAdventure to find the adventurer's location
        if self.is_valid_room(row, col):  # use existing is_valid_room method to validate the room
            return self.__maze[row][col]
        else:
            return None

if __name__ == "__main__":

    dungeon = Dungeon(3,3)
    dungeon.print()
    # # dungeon.set_health_potion(0, 0)
    # while not dungeon.traverse(0, 0):
    #     dungeon = Dungeon(3)
    #     # print("whoo hoo, we reached the exit")
    # else:
    #     print("exit not reachable")


    #     dungeon.build_maze()
    #     dungeon.traverse(0, 0)
    dungeon.print_maze()
    dungeon.pick_random_empty_room()
    # dungeon.pick_random_room()
    # dungeon.pick_random_empty_room()






        #SKELETON CODE THAT IS PROOF OF CONCEPT
        #EACH INDIVIDUAL TASK SHOULD GO IN ITS OWN METHOD
        #CODE BELOW DOES NOT HAVE ERROR CHECKING









## I wrote out this code of printing a nXm grid but the code to do that is provided already. There's a difference between building the maze and printing it.

        # maze_area = self.__rowCount * self.__colCount + 1
        # room = RoomFactory.create_room()
        # room_count = 0
        # for current_room in range(0, maze_area):
        #     maze.append(room)
        #     room_count += 1
        #     if room_count // self.__rowCount == 0:
        #         print("\n")
        # print(maze)




    # def set_health_potion(self, row, col):
    #     self.__maze[row][col].set_healing(add_potion = True)
    #




# healing_potion = random.randint(5, 15)
# pit = -random.randint(1, 20)
#
# has_healing = random.randint(0, 100) <= 10
# has_vision = random.randint(0, 100 ) <= 10
# has_pit = random.randint(0, 100) <= 10
# #
# room = RoomFactory.create_room(has_healing, has_vision, has_pit)
# maze: [
#     [room, room, room],
#     [room, room, room],
#     [room, room, room]
# ]


# # place pillars after entrance/exit, watch for impassabl
# #place health potions
# #could also do vision and pits
# for row in range(0, self.__rowCount):
#     for col in range(0, self.__colCount):
#         #make sure room not impassible
#         if self.__maze[row][col].can_enter():
#             # generate a random value
#             number = random.randint(1, 100)
#             if self.__maze[row][col].get_health_chance() >= number:
#                 self.__maze[row][col].set_healing(add_potion = True)
#             if self.__maze[row][col].get_vision_chance() >= number:
#                 self.__maze[row][col].set_vision(add_vision_potion = True)
#             if self.__maze[row][col].get_pillars_chance() >= number:
#                 self.__maze[row][col].set_pillars(pillars = True)
#             if self.__maze[row][col].get_pillars_chance() >= number:
#                 self.__maze[row][col].set_pillars(pillars=True)


## Put these in the room class:
#  Room(northdoor = north_door,
#       eastdoor = east_door,
#       westdoor = west_door,
#       southdoor = south_door


# maze_area = self.__rowCount * self.__colCount + 1
# room = RoomFactory.create_room()
# room_count = 0
# for current_room in range(0, maze_area):
#     self.__maze.append(room)
#     room_count += 1
#     if room_count // self.__rowCount == 0:
#         print("\n")
# print(self.__maze.__str__())
# This prints object addresses and I'm not sure why.

# For each room, run a random integer generator to determine whether the room contains a door or not on each (interior) wall.
        # def roll():
        #     x = random.randint(0, 1)
        #     if x == 0:
        #         return False
        #     else:
        #         return True
        #
        # rooms = ["NW", "N", "NE", "W", "X", "E", "SW", "S", "SE"]
        # for current_room in rooms:
        #     result = set("NEWS") - set(current_room)
        #     if "N" in result:
        #         northdoor = roll()
        #     if "E" in result:
        #         eastdoor = roll()
        #     if "W" in result:
        #         westdoor = roll()
        #     if "S" in result:
        #         south_door = roll()
        #     self.__maze.append(RoomFactory.create_room())



# How do maze objects communicate that they're next to each other?

