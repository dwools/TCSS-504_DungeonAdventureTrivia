import pandas as pd
import random
from RoomFactory import RoomFactory


from Room import Room
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

    def __init__(self, rows, columns):
        self.maze = []
        self.rows = rows
        self.columns = columns

        # self.mazes_created = 0
        # use the traverse method when the dungeon initializes to ensure the entrance is connected to the exit
        self.traversable = False
        while not self.traversable:
            self.maze = []  # reset and rebuild our maze each time we fail to traverse
            self.pillar_count = 0
            self.build_maze(rows, columns)
            for row in self.maze:  # make sure all rooms have not been marked as entered
                for room in row:
                    room.set_entered(False)
            self.traversable = self.traverse(0, 0)
            self.traversable = self.traversable[0] and self.traversable[1]
            # self.mazes_created += 1
        self.draw()
        self.set_entrance()
        self.set_exit()
        # print(self.mazes_created)

    def set_entrance(self):
        entrance = self.maze[0][0]
        entrance.is_entrance()
        return entrance

    def set_exit(self):
        exit = self.maze[self.rows - 1][self.columns - 1]
        exit.is_exit()
        return exit

    def build_maze(self, rows, columns):
        """
        Lay down rooms such that neighboring rooms' have doors
        """
        self.maze = []
        self.content_count = 0
        for i in range(self.rows):
            self.maze.append([])
            for j in range(self.columns):
                # Lay down doors
                doors = ''
                # content = ''
                if i > 0 and self.maze[i - 1][j]._southdoor:  # if previous room had a south door:
                    doors += 'N'  # north door added in next room
                if j > 0 and self.maze[i][j - 1]._eastdoor:  # if previous room had an east door:
                    doors += 'W'  # west door added to next room
                if j != columns - 1:
                    if random.randint(0, 100) <= 50:  # 50 % chance for door
                        doors += 'E'
                if i != rows - 1:
                    if random.randint(0, 100) <= 50:  # 50 % chance for door
                        doors += 'S'

                # Lay down content; entrances, exits, potions, and pits:
                content = ''
                # Only one room will have an entrance and the room that contains the entrance will contain NOTHING else
                if i == 0 and j == 0:
                    content += 'i'
                    #     #Only one room will have an exit and the room that contains the exit will contain NOTHING else
                elif i == rows - 1 and j == columns - 1:
                    content += 'O'
                else:
                    if random.randint(0, 100) <= 10:  # 10% chance for healing
                        content += 'H'
                    if random.randint(0, 100) <= 10:  # 10% chance for vision
                        content += 'V'
                    if random.randint(0, 100) <= 10:  # 10% chance for pit
                        content = 'X'
                    if content == 'HV': # or content == 'HX' or content == 'VX' or content == 'HVX':
                        content = 'M'  # How can we ensure M is displayed when multiple items are in a room?
                self.maze[-1].append(RoomFactory.create_room(content, doors, i, j))

        # Lay down pillars in the maze, ensuring only one of each is present and that they don't occupy entrance and exit spaces
        for pillar in ['A', 'E', 'I', 'P']:
            row = random.randint(0, self.rows - 1)
            column = random.randint(0, self.columns - 1)
            while self.maze[row][column].has_pillars() or (row == 0 and column == 0) or (
                    row == self.rows - 1 and column == self.columns - 1):
                row = random.randint(0, self.rows - 1)
                column = random.randint(0, self.columns - 1)
            self.maze[row][column].set_pillars(pillar)
            self.pillar_count += 1
        return (self.pillar_count)

    def draw(self):
        """
        Draws a maze map in a more user-friendly layout than the pandas grid
        """
        for i in range(self.rows):
            for j in range(self.columns):
                self.maze[i][j].draw_top()
            print()
            for j in range(self.columns):
                # c_row, c_col = current_room
                # if i == c_row and j == c_col:
                #     self.maze[i][j].draw_middle(True)
                # else:
                self.maze[i][j].draw_middle()
            print()
            for j in range(self.columns):
                self.maze[i][j].draw_bottom()
            print()

    def print_maze(self):
        """
        Prints all rooms in a grid of the mazes' dimensions.
        """
        maze = pd.DataFrame(self.maze)
        for index, row in maze.iterrows():
            split_row = [str(element).split('\n') for element in row]
            max_length = max(len(str(element)) for element in row)
            padded_row = [[line.ljust(max_length) for line in element] for element in split_row]
            for lines in zip(*padded_row):
                print(' '.join(lines))
            print()

    def traverse(self, row, col, room_count=0):
        """
        Traverses maze to ensure all rooms are accessible. If not, a new randomized maze is generated.
        """
        if not self.is_valid_room(row, col):
            # Invalid room, can't proceed in this direction
            return False, room_count

        # Avoid revisiting the same room
        if self.maze[row][col]._entered:
            return False, room_count

        self.maze[row][col].set_entered(entered=True)
        room_count += 1

        # Check for exit conditions
        if room_count == ((self.rows) * (self.columns)):
            return True, room_count

        # Try moving in all four directions: south, east, north, west
        found_exit, room_count = self.traverse(row + 1, col, room_count) if self.maze[row][col]._southdoor else (
        False, room_count)
        if not found_exit:
            found_exit, room_count = self.traverse(row, col + 1, room_count) if self.maze[row][col]._eastdoor else (
            False, room_count)
        if not found_exit:
            found_exit, room_count = self.traverse(row - 1, col, room_count) if row > 0 and self.maze[row][
                col]._northdoor else (False, room_count)
        if not found_exit:
            found_exit, room_count = self.traverse(row, col - 1, room_count) if col > 0 and self.maze[row][
                col]._westdoor else (False, room_count)

        return found_exit, room_count

    def is_valid_room(self, row, col):
        """
        Verifies whether a room is valid for traversal and entry
        """
        return 0 <= row < self.rows and 0 <= col < self.columns

    def get_room(self, row, col):
        if self.is_valid_room(row, col):
            return self.maze[row][col]
        else:
            print(f"Invalid room coordinates: ({row}, {col})")
            return None

    def get_mazes_created(self):
        return self.mazes_created


    def get_room_pillar(self, row, col):
        room = self.get_room(row, col)
        if room is not None:
            if room.has_pillars():
                # print(f"Pillar in room ({row}, {col}): {room.has_pillars()}")
                return room.get_pillar()
        return None

    def vision_potion_print(self, player_row, player_col):
        row_start = max(player_row - 1, 0)
        row_end = min(player_row + 1, self.rows - 1)
        col_start = max(player_col - 1, 0)
        col_end = min(player_col + 1, self.columns - 1)

        surrounding_maze = [self.maze[i][col_start:col_end + 1] for i in range(row_start, row_end + 1)]

        # Convert to DataFrame for easier handling
        maze_df = pd.DataFrame(surrounding_maze)
        for index, row in maze_df.iterrows():
            split_row = [str(element).split('\n') for element in row]
            max_length = max(len(str(element)) for element in row)
            padded_row = [[line.ljust(max_length) for line in element] for element in split_row]

            for lines in zip(*padded_row):
                print(' '.join(lines))
            print()

if __name__ == "__main__":
    dungeon = Dungeon(5, 5)
    #    while not dungeon.traverse(0, 0):
    #        dungeon = Dungeon(5, 5)
    # dungeon.print_maze()

##### OLD CODE ###


#     def __init__(self, rows, columns):
#         self.maze = []
#         self.rows = rows
#         self.columns = columns
#         # use the traverse method when the dungeon initializes to ensure the entrance is connected to the exit
#         traversable = False
#         while not traversable:
#             self.maze = []  # reset and rebuild our maze each time we fail to traverse
#             self.build_maze(rows, columns)
#             self.pillars()
#
#             for row in self.maze:  # make sure all rooms have not been marked as entered
#                 for room in row:
#                     room.set_entered(False)
#
#             traversable = self.traverse(0, 0)
#
#
#
#     def build_maze (self, rows, columns):
#         self.maze = []
#         for i in range(self.rows):
#             self.maze.append([])
#             for j in range(self.columns):
#                 doors = ''
#                 content = ''
#                 if i > 0 and self.maze[i - 1][j]._southdoor:  # if previous room had a south door:
#                     doors += 'N'                          # north door added in next room
#                 if j > 0 and self.maze[i][j - 1]._eastdoor:   # if previous room had an east door:
#                     doors += 'W'
#                 if j != columns - 1:
#                     if random.randint(0, 100) <= 50:  # 50 % chance for door
#                         doors += 'E'
#                 if i != rows - 1:
#                     if random.randint(0, 100) <= 50:  # 50 % chance for door
#                         doors += 'S'
#                     # Only one room will have an entrance and the room that contains the entrance will contain NOTHING else
#                 if i == 0 and j == 0:
#                     content += 'i'
#                     #     #Only one room will have an exit and the room that contains the exit will contain NOTHING else
#                 elif i == rows - 1 and j == columns - 1:
#                     content += 'O'
#                 else:
#                     if random.randint(0, 100) <= 50:  # 10% chance for healing
#                         content += 'H'
#                     if random.randint(0, 100) <= 50:  # 10% chance for vision
#                         content += 'V'
#                     if random.randint(0, 100) <= 10:  # 10% chance for pit
#                         content = 'X'
#                     if content == 'HV':
#                         content = 'M'
#                     # print(i, j)  # commented out as they print the contents of the maze at game init
#                     # print(content)
#                 self.maze[-1].append(RoomFactory.create_room(content, doors, i, j))
#
#
#     def set_entrance(self):
#         entrance = self.maze[0][0]
#         entrance.is_entrance()
#         print(entrance)
#
#     def set_exit(self):
#         exit = self.maze[self.rows-1][self.columns-1]
#         exit.is_exit()
#         print(exit)
#
#     def pillars(self):
#         for pillar in ['A', 'E', 'I', 'P']:
#             row = random.randint(0, self.rows-1)
#             column = random.randint(0, self.columns-1)
#             while self.maze[row][column].has_pillars() or (row == 0 and column == 0) or (row == self.rows-1 and column == self.columns-1):
#                 row = random.randint(0, self.rows - 1)
#                 column = random.randint(0, self.columns - 1)
#             self.maze[row][column].set_pillars(pillar)
#
#
#     def print(self):
#         for i in range(self.rows):
#             print(end = "")
#             for j in range(self.columns):
#                 # print(self.rooms[i][j], sep=" ", end="")
#                 print(str(self.maze[i][j]))
#             print()
#
#     def print_maze(self):
#         maze = pd.DataFrame(self.maze)
#         for index, row in maze.iterrows():
#             split_row = [str(element).split('\n') for element in row]
#             max_length = max(len(str(element)) for element in row)
#             padded_row = [[line.ljust(max_length) for line in element] for element in split_row]
#             for lines in zip(*padded_row):
#                 print(' '.join(lines))
#             print()
#
#
#     def traverse(self, row, col):
#         found_exit = False
#         if self.is_valid_room(row, col):
#             self.maze[row][col].set_entered(entered = True)
#             # check for exit
#             if row == self.rows-1 and col == self.columns-1:
#                 return True
#             # not at exit so try another room: south, east, north, west
#             if self.maze[row][col]._southdoor:
#                 found_exit = self.traverse(row + 1, col) # south
#             if self.maze[row][col]._eastdoor:
#                 if not found_exit:
#                     found_exit = self.traverse(row, col + 1)  # east
#             # if not found_exit:
#             #     found_exit = self.traverse(row - 1, col)  # north
#             # if not found_exit:
#             #     found_exit = self.traverse(row, col - 1)  # west
#
#             # if we did not reach the exit from this room we need mark it as visited to
#             # avoid going into the room again
#             if not found_exit:
#                 self.maze[row][col].set_entered(entered=True)
#
#         else:  # tried to move into a room that is not valid
#             return False
#         return found_exit
#
#     def is_valid_room(self, row, col):
#         return 0 <= row < self.rows and 0 <= col < self.columns
#
#     def get_room(self, row, col):
#         if self.is_valid_room(row, col):
#             return self.maze[row][col]
#         else:
#             return None
#
#     def get_room_pillar(self, row, col):
#         room = self.get_room(row, col)
#         if room is not None:
#             return room.get_pillar()
#         return None
#
#     def vision_potion_print(self, player_row, player_col):
#         row_start = max(player_row - 1, 0)
#         row_end = min(player_row + 1, self.rows - 1)
#         col_start = max(player_col - 1, 0)
#         col_end = min(player_col + 1, self.columns - 1)
#
#         surrounding_maze = [self.maze[i][col_start:col_end + 1] for i in range(row_start, row_end + 1)]
#
#         # Convert to DataFrame for easier handling
#         maze_df = pd.DataFrame(surrounding_maze)
#         for index, row in maze_df.iterrows():
#             split_row = [str(element).split('\n') for element in row]
#             max_length = max(len(str(element)) for element in row)
#             padded_row = [[line.ljust(max_length) for line in element] for element in split_row]
#
#             for lines in zip(*padded_row):
#                 print(' '.join(lines))
#             print()
#
#
# if __name__ == "__main__":
#     dungeon = Dungeon(5, 5)
# #    while not dungeon.traverse(0, 0):
# #        dungeon = Dungeon(5, 5)
#     dungeon.print_maze()
