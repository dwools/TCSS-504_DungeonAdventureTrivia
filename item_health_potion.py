from item import Item
from dungeon_character import DungeonCharacter


class HealthPotion(Item):
    def __init__(self, health_change_value):
        # self.__location = location
        super().__init__(health_change_value)

        self.__healthpotion_sprite = None
        # self.__collision_rects = []
        self.__player_scroll = [0, 0]


    def change_health(self):
        hit_points = DungeonCharacter.get_hit_points()
        hit_points += self.__health_change_value
        DungeonCharacter.set_hit_points(hit_points)



    def add_to_backpack(self):
        """We need to be able to pick up potions and put them in our backpack/inventory
        """

    def get_healpotion_sprite(self):
        return self.__healthpotion_sprite
    def set_healthpotion_sprite(self, sprite_path):
        self.__healthpotion_sprite = sprite_path

    # def create_collision_rects(self):
    #     """ Create a rectangle over a tile,
    #     if the monster collides with that tile.
    #     Append that collision rect to a list that will be used in the check_collisions method.
    #     """
    #
    #     if self.__path:
    #         self.__collision_rects = []
    #         for point in self.__path:
    #             x = (point.x * 16)
    #             y = (point.y * 16)
    #             rect = pg.Rect((x, y), (16, 16))
    #             self.__collision_rects.append(rect)
    #
    # def check_collisions(self):
    #     """ Check for collisions, if monster collides, delete that rect and move to the next rect in the path.
    #     """
    #
    #     if self.__collision_rects:
    #         for rect in self.__collision_rects:
    #             if rect.collidepoint(self.get_position()):
    #                 del self.__collision_rects[0]
    #                 self.get_direction()
    #     else:
    #         self.__path = []