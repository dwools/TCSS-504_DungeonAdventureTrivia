import random
from adventurer import Adventurer
from dungeon import Dungeon
from items import Items


class DungeonAdventure:

    def __init__(self):
        pass

    def run(self):
        print("You are a hero that has been teleported into a dungeon, to escape you must find 4 pillars. "
              "The dungeon has pit traps which will cause you to take health damage. "
              "But there are also health potions which will restore health, "
              "as well as vision potions which will allow you to see into the surrounding rooms. "
              "Your task is to retrieve the 4 pillars and make it out of the dungeon without losing all of your HP.\
               Good Luck!")

        # Create the dungeon and adventurer
        rows, cols = 5, 5
        dungeon = Dungeon.create_dungeon(rows, cols)
        start_room = random.choice(random.choice(dungeon))
        visited = [[False] * cols for _ in range(rows)]

        Dungeon.generate_maze_with_doors(start_room, visited, dead_end_chance=0.2)
        entrance, exit_room, pillars, potion_rooms, pit_rooms = Dungeon.place_entrance_exit_pillars_potions_pits\
            (dungeon)

        # Connect the entrance to a neighbor
        if entrance.neighbors:
            connected_room = random.choice(list(entrance.neighbors.values()))
            entrance.connect_rooms_with_door(Dungeon.direction_to_neighbor(entrance, connected_room), connected_room)

        adventurer = Adventurer()

        while True:
            # Display current room and adventurer stats
            print(f"\nCurrent Room:\n{Dungeon.dungeon_str(dungeon)}")
            adventurer.print_stats()

            # Get player/user action
            action = input("What direction would you like to head in? W, A, S, D\n"
                           "Or would you like to use a potion? H, V\n").lower()

            if action in ["w", "a", "s", "d"]:
                # Move the adventurer
                self.move_adventurer(adventurer, dungeon, action)

            elif action in ["h", "v"]:
                # Use potion
                self.use_potion(adventurer, action)

            else:
                print("Invalid input. Please enter W, A, S, D, H, or V.")

            # Check if the adventurer has won or died
            if adventurer.get_obtained_pillars() == 4:
                print(f"Congratulations {adventurer.get_adventurer_name()}! You found all four pillars and escaped\
                 the dungeon.")
                break
            elif adventurer.get_current_health() <= 0:
                print("Unfortunately, your adventure has come to an end. Better luck next time.")
                break

    @staticmethod
    def move_adventurer(adventurer, dungeon, direction):
        current_room = dungeon[adventurer.get_adventurer_position()[0]][adventurer.get_adventurer_position()[1]]
        next_room = current_room.neighbors[direction]

        # Update adventurer position
        adventurer.set_adventurer_position([next_room.row, next_room.col])

        # Check if the room has a potion or pit
        if next_room.is_potion:
            adventurer.add_to_backpack(Items.health_potion)
            next_room.is_potion = False
        elif next_room.is_pit:
            adventurer.update_health(Items.pit_trap)

    @staticmethod
    def use_potion(adventurer, potion_type):
        if potion_type == "h":
            adventurer.remove_from_backpack(Items.health_potion)
            adventurer.update_health(Items.health_potion)
        elif potion_type == "v":
            adventurer.remove_from_backpack(Items.vision_potion)
            adventurer.update_vision(Items.vision_potion)


if __name__ == "__main__":
    dungeon_adventure = DungeonAdventure()
    dungeon_adventure.run()
