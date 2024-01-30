import HealingPotion
import random

"""Creates the room class with constructors self, healing, vision, pit"""
class Room:
    """init function includes all features a room could have"""
    def __init__(self, content, doors, row, column):
        self._row = row
        self._column = column
        self._northdoor = 'N' in doors
        self._eastdoor = 'E' in doors
        self._westdoor = 'W' in doors
        self._southdoor = 'S' in doors
        self._entrance = 'i' in content
        self._exit = 'O' in content
        self._blocked = 'B' in content
        self._entered = 'e' in content
        self._empty_room = ' ' in content
        self._multiple_items = 'M' in content
        self._pit = 'X' in content
        self._healing = 'H' in content
        self._vision = 'V' in content
        self._pillars = False
        self._pillar_type = None
        # self._items = []
        self._healing_points = random.randint(5, 15) if self._healing else 0


    def __str__(self):
        """
        String function to create 2D visual of the rooms. Multiple items will likely happen in here.
        """
        room_design = ""
        if self._northdoor:
            room_design += "* _ *"
        else:
            room_design += "*****"
        room_design += ("\n")
        if self._westdoor:
            room_design += "| "
        else:
            room_design += "* "
        if self._pit:
            room_design += "X"
        elif self._entrance:
            room_design += "i"
        elif self._exit:
            room_design += "o"
        elif self._pillars:
            room_design += self._pillar_type
        elif self._vision:
            room_design += "V"
        elif self._healing:
            room_design += "H"
        elif self._multiple_items:
            room_design += "M"
        else:
            room_design += " "

        if self._eastdoor:
            room_design += " |"
        else:
            room_design += " *"
        room_design += ("\n")

        if self._southdoor:
            room_design += "* _ *"
        else:
            room_design += "*****"
        return room_design

    # def __repr__(self):
    #     return self.__str__()



    # def draw_top(self):
    #     if self._northdoor:
    #         print("*   *", end="")
    #     else:
    #         print("*****", end="")
    #
    # def draw_bottom(self):
    #     if self._southdoor:
    #         print("*   *", end="")
    #     else:
    #         print("*****", end="")
    #
    # def draw_middle(self, is_current = False):
    #     if self._westdoor:
    #         print(" ", end="")
    #     else:
    #         print("*", end="")
    #
    #     print(" ", end="")
    #     if is_current:
    #         print("#", end="")
    #     else:
    #         item_count = len(self._items)
    #         if item_count == 0:
    #             print(" ", end="")
    #         elif item_count == 1:
    #             print(self._items[0], end="")
    #         else:
    #             print("M", end="")
    #             self._multiple_items = True
    #     print(" ", end="")
    #
    #     if self._eastdoor:
    #         print(" ", end="")
    #     else:
    #         print("*", end="")

    # def __str__(self):
    #     item_count = 0;
    #     if self._healing:
    #         item_count += 1
    #     if self._vision:
    #         item_count += 1
    #
    #     if item_count > 1:
    #         return "M"
    #     return "Health potion: " + str(self._healing) + "\n" \
    #         + "Vision potion: " + str(self._vision) + "\n" \
    #         + "Pillar: " + str(self._pillars) + "\n" \
    #         + "Pit: " + str(self._pit) + "\n" \
    #         + "Blocked: " + str(self._blocked) + "\n" \
    #         + "Entrance: " + str(self._entrance) + "\n" \
    #         + "Exit: " + str(self._exit) + "\n\n"

    # def place_item(self, item):
    #     self._items.append(item)
    #
    # def remove_item(self, item):
    #     self._items.remove(item)

    def draw_top(self):
        if self._northdoor:
            print("*   *", end="")
        else:
            print("*****", end="")

    def draw_bottom(self):
        if self._southdoor:
            print("*   *", end="")
        else:
            print("*****", end="")

    def draw_middle(self):
        if self._westdoor:
            print(" ", end="")
        else:
            print("*", end="")

        print(" ", end="")
        # if is_current:
        #     print("#", end="")
        # else:

        if self._entrance:
            print('i', end='')
        elif self._exit:
            print('o', end='')
        elif self._pillars:
            print(f'{self._pillar_type}', end='')
        elif self._multiple_items:
            print('M', end='')
        elif self._pit:
            print('X', end='')
        elif self._vision:
            print('V', end='')
        elif self._healing:
            print('H', end='')

        else:
            print(' ', end='')
            # item_count = len(content)
            # if item_count == 0:
            #     print(" ", end="")
            # elif item_count == 1:
            #     print(self._items[0], end="")
            # else:
            #     print("M", end="")
            #     self._multiple_items = True
        print(" ", end="")

        if self._eastdoor:
            print(" ", end="")
        else:
            print("*", end="")

    """Sets healing to be adding a potion"""
    def set_healing(self):
        self._healing = True

    def get_healing_points(self):
        return self._healing_points

    """Sets vision to be adding a vision potion"""
    def set_vision(self, add_vision_potion):
        self._vision = add_vision_potion

    """Sets if can enter a room"""
    def can_enter(self):
        return not self._blocked and not self._entered

    """Sets if is an exit"""
    def is_exit(self):
        return self._exit

    """Sets if an entrance"""
    def is_entrance(self):
        return self._entrance

    """Sets if empty"""
    def is_empty(self):
        if not (self._healing or self._vision or self._pillars or self._multiple_items or self._entrance or self._exit):
            return True
        else:
            return False

    """Sets if blocked"""
    def is_blocked(self):
        return self._blocked

    """Sets if not blocked"""
    def is_not_blocked(self):
        return not self._blocked

    """Sets if the room was entered already"""
    def set_entered(self, entered):
        self._entered = entered

    """Sets the pillars of OO"""
    def set_pillars(self, pillar):
        self._pillars = True
        self._pillar_type = pillar

    """Getter for pillar type"""
    def get_pillar(self):
        if self._pillars:
            return self._pillar_type
        return None

# changes in the room


    # def get_health_chance(self):
    #     return self._healthChance
    #
    # def get_vision_chance(self):
    #     return self._visionChance
    #
    # def get_pillars_chance(self):
    #     return self._pillarsChance


# DUNGEON ADVENTURE PUBLIC METHODS
    """public method for checking for a door on the north end of the room"""
    def has_north_door(self):
        return self._northdoor

    """public method for checking for a door on the east end of the room"""
    def has_east_door(self):
        return self._eastdoor

    """public method for checking for a door on the west end of the room"""
    def has_west_door(self):
        return self._westdoor

    """public method for checking for a door on the south end of the room"""
    def has_south_door(self):
        return self._southdoor

    """public method for checking if a room has a healing potion in it"""
    def has_healing_potion(self):
        return self._healing

    """public method for checking if a room has a vision potion in it"""
    def has_vision_potion(self):
        return self._vision

    """public method for checking if a room has a pillars in it"""
    def has_pillars(self):
        return self._pillars

    """public method for checking if a room has a pit in it"""
    def has_pit(self):
        return self._pit

    """public method for checking if a room has a multiple items in it"""
    def has_multiple_items(self):
        return self._multiple_items

    """Helper method for checking if a room has a pit in it"""
    def clear_item(self, item):
        if item == "healing":
            self._healing = False
        elif item == "vision":
            self._vision = False
        elif item == "pillar":
            self._pillars = False
        elif item == "multiple":
            self._multiple_items = False



if __name__ == "__main__":
    room = RoomFactory.create_room(1, 2)
    print(room)









