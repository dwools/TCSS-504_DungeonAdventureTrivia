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
            self.__south_monster_sprite = pg.image.load(a.south_gremlin)
            self.__north_monster_sprite = pg.image.load(a.north_gremlin)
            self.__east_monster_sprite = pg.image.load(a.east_gremlin)
            self.__west_monster_sprite = pg.image.load(a.west_gremlin)
            self.__current_sprite = pg.image.load(a.south_gremlin)
        
        if self.get_type() == "Skeleton":
            self.__south_monster_sprite = pg.image.load(a.south_skelly)
            self.__north_monster_sprite = pg.image.load(a.north_skelly)
            self.__east_monster_sprite = pg.image.load(a.east_skelly)
            self.__west_monster_sprite = pg.image.load(a.west_skelly)
            self.__current_sprite = pg.image.load(a.south_skelly)
        
        if self.get_type() == "Ogre":
            self.__south_monster_sprite = pg.image.load(a.south_ogre)
            self.__north_monster_sprite = pg.image.load(a.north_ogre)
            self.__east_monster_sprite = pg.image.load(a.east_ogre)
            self.__west_monster_sprite = pg.image.load(a.west_ogre)
            self.__current_sprite = pg.image.load(a.south_ogre)
            

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
            self.__current_sprite = self.__south_monster_sprite
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

    def set_current_sprite(self, sprite_path):
        self.__current_sprite = sprite_path

    def get_current_sprite(self):
        return self.__current_sprite

    def get_south_monster_sprite(self):
        return self.__south_monster_sprite

    def set_south_monster_sprite(self, sprite_path):
        self.__south_monster_sprite = sprite_path

    def get_north_monster_sprite(self):
        return self.__north_monster_sprite

    def set_north_monster_sprite(self, sprite):
        self.__north_monster_sprite = sprite

    def get_east_monster_sprite(self):
        return self.__east_monster_sprite

    def set_east_monster_sprite(self, sprite):
        self.__east_monster_sprite = sprite

    def get_west_monster_sprite(self):
        return self.__west_monster_sprite

    def set_west_monster_sprite(self, sprite):
        self.__west_monster_sprite = sprite

    def set_player_scroll(self, scroll):
        self.__player_scroll = scroll

    def monster_heal(self):  # Heal Monster
        if random.randint(1, 100) <= self.__chance_to_heal:
            heal_points = random.randint(self.__minimum_heal_points, self.__maximum_heal_points)

            if self.get_current_hit_points() + heal_points > self.__maximum_heal_points:
                heal_points = self.get_max_hit_points() - self.get_current_hit_points()

            self.set_current_hit_points(self.get_current_hit_points() + heal_points)
            print(f"{self.get_name()} increased its health by {heal_points} hit points!")





# Abstract classes are parent classes. We write them to consolidate information for objects that share characteristic
# We do it when there isn't enough information to warrant an instance of a class.


# Any set methods need to ensure the data being passed in looks okay, and if not, raise an exception.
