import random

from Characters.dungeon_character import DungeonCharacter

from Assets import assets as a
import pygame as pg



class Monster(DungeonCharacter):

    def __init__(self,
                 name,
                 type,
                 hit_points,
                 attack_speed,
                 chance_to_hit,
                 minimum_damage,
                 maximum_damage,
                 chance_to_heal,
                 minimum_heal_points,
                 maximum_heal_points
                 ):
        super().__init__(name, type, hit_points, attack_speed, chance_to_hit, minimum_damage, maximum_damage)
        self.__chance_to_heal = chance_to_heal
        self.__minimum_heal_points = minimum_heal_points
        self.__maximum_heal_points = maximum_heal_points

        self.__speed = 2
        self.__movement = [0, 0]
        self.__direction = pg.math.Vector2(0, 0)
        self.__monster_goal = None
        self.__path = []
        self.__collision_rects = []
        self.__player_scroll = [0, 0]
        
        if self.get_type() == "Gremlin":
            self.__sprite_south = pg.image.load(a.south_gremlin)
            self.__sprite_north = pg.image.load(a.north_gremlin)
            self.__sprite_east = pg.image.load(a.east_gremlin)
            self.__sprite_west = pg.image.load(a.west_gremlin)
            self.__sprite_current = pg.image.load(a.south_gremlin)

        if self.get_type() == "Skeleton":
            self.__sprite_south = pg.image.load(a.south_skelly)
            self.__sprite_north = pg.image.load(a.north_skelly)
            self.__sprite_east = pg.image.load(a.east_skelly)
            self.__sprite_west = pg.image.load(a.west_skelly)
            self.__sprite_current = pg.image.load(a.south_skelly)

        if self.get_type() == "Ogre":
            self.__sprite_south = pg.image.load(a.south_ogre)
            self.__sprite_north = pg.image.load(a.north_ogre)
            self.__sprite_east = pg.image.load(a.east_ogre)
            self.__sprite_west = pg.image.load(a.west_ogre)
            self.__sprite_current = pg.image.load(a.south_ogre)


    def monster_heal(self):  # Heal Monster
        if self.get_current_hit_points() <= self.get_max_hit_points() // 3: #(self.get_monster_health_max() // 3): # change this to chance to heal
            if random.randint(1, 100) <= self.__chance_to_heal:
                heal_points = random.randint(self.__minimum_heal_points, self.__maximum_heal_points)

                if self.get_current_hit_points() + heal_points > self.__maximum_heal_points:
                    heal_points = self.get_max_hit_points() - self.get_current_hit_points()

                self.set_current_hit_points(self.get_current_hit_points() + heal_points)
                print(f"{self.get_name()} increased its health by {heal_points} hit points!")

    def update(self):
        position = self.get_position()
        rectangle = self.get_character_rect()
        self.set_direction()
        position += self.__direction
        self.set_position(position)
        rect_x, rect_y = position
        rectangle.topleft = rect_y, rect_x

        self.check_collisions()

    def set_direction(self):
        if len(self.__path) > 1:
            self.__path.pop(0)
        # if len(self.__path) > 1:        # If monster and player rectangles don't collide, delete this line and un-indent the lines below
            path_x, path_y = self.__path[0]
            start = pg.math.Vector2(self.get_position())
            end = pg.math.Vector2(path_y * 16, path_x * 16)
            self.__direction = (end - start).normalize()
        else:
            self.__direction = pg.math.Vector2(0, 0)
        return self.__direction


    def get_direction(self):
        if self.__collision_rects:
            if len(self.__collision_rects) > 1:
                start = pg.math.Vector2(self.get_position())
                collision_rect_y, collision_rect_x = self.__collision_rects[1].topleft
                end = pg.math.Vector2((collision_rect_x, collision_rect_y))
                self.__direction = (end - start).normalize()

        else:
            self.__direction = pg.math.Vector2(0, 0)
            self.__sprite_current = self.__sprite_south
            self.__path = []
    # Statistics

    def get_chance_to_heal(self):
        return self.__chance_to_heal

    def get_minimum_heal_points(self):
        return self.__minimum_heal_points

    def get_maximum_heal_points(self):
        return self.__maximum_heal_points

    def set_chance_to_heal(self, chance_to_heal):
        self.__chance_to_heal = chance_to_heal

    def set_minimum_heal_points(self, minimum_heal_points):
        self.__minimum_heal_points = minimum_heal_points

    def set_maximum_heal_points(self, maximum_heal_points):
        self.__maximum_heal_points = maximum_heal_points

    # Movement / Direction Getters and Setters

    def set_monster_movement(self, monster_movement):
        self.__movement = monster_movement

    def get_monster_movement(self):
        return self.__movement

    def set_monster_direction(self, monster_direction):
        self.__direction = monster_direction

    def get_monster_direction(self):
        return self.__direction

    def set_monster_goal(self, monster_goal):
        self.__monster_goal = monster_goal

    def get_monster_goal(self):
        return self.__monster_goal



    def set_path(self, path):
        self.__path = path
        self.create_collision_rects()
        self.get_direction()

    def create_collision_rects(self):
        """ Create a rectangle over a tile,
        if the monster collides with that tile.
        Append that collision rect to a list that will be used in the check_collisions method.
        """

        if self.__path:
            self.__collision_rects = []
            for point in self.__path:
                x = (point.x * 16)
                y = (point.y * 16)
                rect = pg.Rect((x, y), (16, 16))
                self.__collision_rects.append(rect)

    def check_collisions(self):
        """ Check for collisions, if monster collides, delete that rect and move to the next rect in the path.
        """

        if self.__collision_rects:
            for rect in self.__collision_rects:
                if rect.collidepoint(self.get_position()):
                    del self.__collision_rects[0]
                    self.get_direction()
        else:
            self.__path = []



    # Sprite Getters / Setters

    def set_sprite_current(self, sprite_path):
        self.__sprite_current = sprite_path

    def get_sprite_current(self):
        return self.__sprite_current

    def get_sprite_south(self):
        return self.__sprite_south

    def set_sprite_south(self, sprite_path):
        self.__sprite_south = sprite_path

    def get_sprite_north(self):
        return self.__sprite_north

    def set_sprite_north(self, sprite):
        self.__sprite_north = sprite

    def get_sprite_east(self):
        return self.__sprite_east

    def set_sprite_east(self, sprite):
        self.__sprite_east = sprite

    def get_sprite_west(self):
        return self.__sprite_west

    def set_sprite_west(self, sprite):
        self.__sprite_west = sprite

    def set_player_scroll(self, scroll):
        self.__player_scroll = scroll

    def simple_attack(self, enemy):
        print(f'{self.get_name()} tries a simple attack...')
        if random.randint(1, 100) <= self.get_chance_to_hit():
            if random.randint(1, 100) <= enemy.get_chance_to_block():
                print(f'but {enemy.get_name()} blocked the attack!')
            else:
                damage = random.randint(self.get_minimum_damage(), self.get_maximum_damage())
                enemy.set_current_hit_points(enemy.get_current_hit_points() - damage)
                print(f'{enemy.get_name()} took {damage} damage! {enemy.get_name()} now has {enemy.get_current_hit_points()} hit points!')
        else:
            print(f"but {self.get_name()}'s attack missed!")

    # def simple_attack2(self, enemy):
    #     print(f'{enemy.get_name()} tries a simple attack...')
    #     if random.randint(1, 100) <= enemy.get_chance_to_hit():
    #         damage = random.randint(enemy.get_minimum_damage(), enemy.get_maximum_damage())
    #         self.set_current_hit_points(self.get_current_hit_points() - damage)
    #         print(f'{self.__name} took {damage} damage! {self.__name} now has {self.get_current_hit_points()} hit points!')
    #     else:
    #         print(f"{enemy.get_name}'s attack missed!")





# Abstract classes are parent classes. We write them to consolidate information for objects that share characteristic
# We do it when there isn't enough information to warrant an instance of a class.


# Any set methods need to ensure the data being passed in looks okay, and if not, raise an exception.
if __name__ == '__main__':
    gremlin = Monster("Gremlin", 70, 70, 5, 80, 15, 30, 40, 20, 40)
    ogre = Monster("Ogre", 200, 200, 2, 60, 30, 60, 10, 30, 60)
    for _ in range(10):
        gremlin.simple_attack(ogre)
    for _ in range(5):
        ogre.monster_heal()