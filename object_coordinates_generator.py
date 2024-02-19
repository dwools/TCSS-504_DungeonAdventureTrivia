import random


# min = 16, 64 or 64, 16
# max = 928, 688
class ValidCoordsGenerator:
    """ Generate a valid set of coordinates where a monster or object can be placed.
    Valid meaning: any square that cannot be populated by a collision tile (wall) or another object.
    """

    def __init__(self):

        self.start_x, self.start_y = 16, 16
        self.increment = 48
        self.max_x = 928
        self.max_y = 688

        self.coords = []

    def generate_coords(self):
        """ Calculates all valid coords for objects to be placed in the Dungeon.
        These coords must be free of walls, always.
        """

        x = self.start_x
        while x <= self.max_x:
            row = []
            y = self.start_y
            while y <= self.max_y:
                row.append([x, y])
                y += self.increment
            self.coords.append(row)
            x += self.increment

        return self.coords

    def get_random_coords(self):
        """ Method to get a set of random coordinates from the above valid coordinates.
        When a set is chosen, it is removed from the list of valid coords.
        If the random coords are [16, 16], it is recursively ran to generate a new random coord.
        [16,16] is the character's tile.
        """

        row_index = random.randint(0, len(self.coords) - 1)
        col_index = random.randint(0, len(self.coords[row_index]) - 1)
        random_coord = self.coords[row_index].pop(col_index)

        if not self.coords[row_index]:
            self.coords.pop(row_index)

        if random_coord == [16, 16]:
            random_coord = self.get_random_coords()

        return random_coord


if __name__ == '__main__':
    u = ValidCoordsGenerator()
    u.generate_coords()
    random_coords = u.get_random_coords()
