import random
from rooms import Room


class Dungeon:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.neighbors = {'north': None, 'east': None, 'south': None, 'west': None}
        self.doors = {'north': None, 'east': None, 'south': None, 'west': None}
        self.is_entrance = False
        self.is_exit = False
        self.is_pillar = False
        self.is_potion = False
        self.is_pit = False
        self.traversable = False
        self.is_unexplored = True

    def connect_rooms_with_door(self, direction, room):
        self.neighbors[direction] = room
        room.neighbors[Dungeon.opposite_direction(direction)] = self
        self.doors[direction] = room
        room.doors[Dungeon.opposite_direction(direction)] = self

    @staticmethod
    def opposite_direction(direction):
        opposites = {'north': 'south', 'east': 'west', 'south': 'north', 'west': 'east'}
        return opposites[direction]

    @staticmethod
    def direction_to_neighbor(room, neighbor):
        for direction, neighbor_room in room.neighbors.items():
            if neighbor_room == neighbor:
                return direction
        return None

    @staticmethod
    def create_dungeon(rows, cols):
        dungeon = [[Dungeon(row, col) for col in range(cols)] for row in range(rows)]

        for row in range(rows):
            for col in range(cols):
                current_room = dungeon[row][col]
                if row > 0:
                    current_room.connect_rooms_with_door('north', dungeon[row - 1][col])
                if col > 0:
                    current_room.connect_rooms_with_door('west', dungeon[row][col - 1])

        return dungeon

    @staticmethod
    def generate_maze_with_doors(current_room, visited, dead_end_chance=0.2):
        visited[current_room.row][current_room.col] = True

        directions = list(current_room.neighbors.keys())
        random.shuffle(directions)

        for direction in directions:
            neighbor = current_room.neighbors[direction]
            if neighbor and not visited[neighbor.row][neighbor.col]:
                if random.random() > dead_end_chance:
                    current_room.connect_rooms_with_door(direction, neighbor)
                    Dungeon.generate_maze_with_doors(neighbor, visited, dead_end_chance)

    @staticmethod
    def connect_all_rooms_with_doors(dungeon):
        rows, cols = len(dungeon), len(dungeon[0])
        visited = [[False] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if not visited[row][col]:
                    current_room = dungeon[row][col]
                    Dungeon.generate_maze_with_doors(current_room, visited)

    @staticmethod
    def place_entrance_exit_pillars_potions_pits(dungeon):
        rows, cols = len(dungeon), len(dungeon[0])

        # Placing entrance and exit
        entrance = random.choice(dungeon[0])
        exit_row = random.choice(range(1, rows))
        exit_room = random.choice(dungeon[exit_row])
        entrance.is_entrance = True
        exit.is_exit = True

        # Placing pillars
        pillar_names = ['A', 'E', 'I', 'P']
        pillars = random.sample([room for row in dungeon for room in row
                                 if not room.is_entrance and not room.is_exit], 4)
        for i, pillar in enumerate(pillars):
            pillar.is_pillar = True
            pillar.pillar_name = pillar_names[i]

        # Placing potion rooms
        potion_rooms = random.sample([room for row in dungeon for room in row if not room.is_entrance \
                                      and not room.is_exit and not room.is_pillar], 4)
        for potion_room in potion_rooms:
            potion_room.is_potion = True

        # Placing pit rooms
        pit_rooms = random.sample([room for row in dungeon for room in row if not room.is_entrance \
                                   and not room.is_exit and not room.is_pillar and not room.is_potion], 4)
        for pit_room in pit_rooms:
            pit_room.is_pit = True

        return entrance, exit_room, pillars, potion_rooms, pit_rooms

    @staticmethod
    def dungeon_str(dungeon):
        result = "+***" * len(dungeon[0]) + "+\n"

        for row in dungeon:
            for room in row:
                if room.is_unexplored:
                    result += "| U "
                elif room.is_entrance:
                    result += "| E "
                elif room.is_exit:
                    result += "| X "
                elif room.is_pillar:
                    result += f"| {room.pillar_name} "
                elif room.is_potion:
                    result += "| O "
                elif room.is_pit:
                    result += "| T "
                else:
                    result += "|   " if any(room.doors.values()) else "| * "

                room.is_unexplored = False
            result += "|\n"

            result += "+***" * len(row) + "+\n"

        return result


def main():
    rows, cols = 5, 5
    dungeon = Dungeon.create_dungeon(rows, cols)
    start_room = random.choice(random.choice(dungeon))
    visited = [[False] * cols for _ in range(rows)]

    Dungeon.generate_maze_with_doors(start_room, visited, dead_end_chance=0.2)
    entrance, exit_room, pillars, potion_rooms, pit_rooms = Dungeon.place_entrance_exit_pillars_potions_pits(dungeon)

    # Connect entrance to a neighbor
    if entrance.neighbors:
        connected_room = random.choice(list(entrance.neighbors.values()))
        entrance.connect_rooms_with_door(Dungeon.direction_to_neighbor(entrance, connected_room), connected_room)

    print("Dungeon:")
    print(Dungeon.dungeon_str(dungeon))
    print(f"Entrance: ({entrance.row}, {entrance.col})")
    print(f"Entrance connected to: ({connected_room.row}, {connected_room.col})")
    print(f"Exit: ({exit_room.row}, {exit_room.col})")
    print("Pillars:")
    for pillar in pillars:
        print(f"({pillar.row}, {pillar.col})")
    print("Potion Rooms:")
    for potion_room in potion_rooms:
        print(f"({potion_room.row}, {potion_room.col})")
    print("Pit Rooms:")
    for pit_room in pit_rooms:
        print(f"({pit_room.row}, {pit_room.col})")


if __name__ == "__main__":
    main()

