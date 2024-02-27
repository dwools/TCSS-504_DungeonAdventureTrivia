from abc import ABC, abstractmethod
import assets as a
from dungeon_character import DungeonCharacter
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

import pygame as pg
import math


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

        self.__speed = 2
        self.__movement = [0, 0]
        self.__direction = pg.math.Vector2(0, 0)
        self.__monster_goal = None
        self.__path = []
        self.__collision_rects = []

        self.__chance_to_heal = chance_to_heal
        self.__minimum_heal_points = minimum_heal_points
        self.__maximum_heal_points = maximum_heal_points
        # self.__rect = self.get_character_rect()
        # self.__position = self.__rect.center
        self.__player_scroll = [0, 0]

        self.__south_monster_sprite = None
        self.__north_monster_sprite = None
        self.__east_monster_sprite = None
        self.__west_monster_sprite = None
        self.__current_sprite = self.__south_monster_sprite

    def update(self):  # Update the monsters position
        position = self.get_position()
        rectangle = self.get_character_rect()
        print("Before Update - Position:", self.get_position())  # position before movement
        print("Before Update - Direction:", self.__direction)  # monster's current direction (moving towards player, following the path)
        print("Before Update - Speed:", self.__speed)  # Monster's speed
        print("Before Update - Movement: ", self.__movement)
        print("Before Update - Coordinates: ", self.get_coordinate())
        position += self.__direction * self.__speed
        # if self.__path:  # if self.__path [] is not empty:
        #     position = self.__path[0]
        #     x = position.x * 16  #  x attribute of the GridNode object in the Path. Path is a list of GridNode objects, each with their own x and y coordinate. We set our position to these coordinates specifically, here.
        #     y = position.y * 16  # likewise for y.
        #     self.set_position([y, x])  # Pop the first "step" toward player and set position to that "step"
        #     rectangle.center = [x, y]
        self.set_position(position)
        x, y = position
        rectangle.center = y, x
        # self.__rect.center = self.__position  # assign the position of the monster to the monster's rect center

        self.check_collisions()  # Checks if  monster collides with a wall

        # self.__position = self.get_position_from_coordinate(self.__rect.center)
        # print("After Conversion - Position:", self.__position)
        #
        # self.set_monster_position(self.__position)
        # print("Monster Position set to: ", self.__position)
        #
        # self.set_monster_rect(self.__rect)
        #
        print(f"After Update - Position: {self.get_position()}")  # position after movement
        print(f"After Update - Direction: {self.__direction}")
        print("After Update - Movement:", self.__movement)
        print(f"After Update - Coordinates: {self.get_coordinate()}")
        # Update __movement based on __direction
        if self.__direction.x > 0:
            self.__movement = [self.__speed, 0]
        elif self.__direction.x < 0:
            self.__movement = [-self.__speed, 0]
        elif self.__direction.y > 0:
            self.__movement = [0, self.__speed]
        elif self.__direction.y < 0:
            self.__movement = [0, -self.__speed]

    def get_direction(self):
        if self.__collision_rects:
            start = pg.math.Vector2(self.get_position())
            end = pg.math.Vector2(self.__collision_rects[0].center)
            self.__direction = (end - start).normalize()

            # if self.__direction == pg.math.Vector2(0, 1):
            #     self.__current_sprite = self.__south_monster_sprite
            #
            # if self.__direction == pg.math.Vector2(1, 1):
            #     self.__current_sprite = self.__north_monster_sprite
            #
            # if self.__direction == pg.math.Vector2(0, 0):
            #     self.__current_sprite = self.__east_monster_sprite
            #
            # if self.__direction == pg.math.Vector2(1, 0):
            #     self.__current_sprite = self.__west_monster_sprite

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
                x = (point.x * 16) + 8
                y = (point.y * 16) + 8
                rect = pg.Rect((x - 2, y - 2), (4, 4))
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

    def set_monster_sprite(self, sprite):
        self.__current_sprite = sprite

    def get_monster_sprite(self):
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




# Abstract classes are parent classes. We write them to consolidate information for objects that share characteristic
# We do it when there isn't enough information to warrant an instance of a class.


# Any set methods need to ensure the data being passed in looks okay, and if not, raise an exception.
class Pathfinder:
    def __init__(self, matrix):

        # setup
        self.matrix = matrix
        self.grid = Grid(matrix=matrix, inverse=True)

        # pathfinding
        self.path = []

        # Monster
        self.monster = None

    def empty_path(self):
        self.path = []

    def set_monster(self, monster):
        self.monster, self.path = monster, self.empty_path()

    # def draw_active_cell(self, monster):
    #     target = monster.get_monster_goal()  # coords of player in the overworld
    #     row = target.x // 16
    #     col = target.y // 16

    def create_path(self, monster):
        # start cell
        monster_start = monster.get_character_rect()
        print(f"MONSTER START: {monster_start} \n")
        start_x, start_y = monster_start.x, monster_start.y
        start = self.grid.node(start_x // 16, start_y // 16)

        # end cell
        target = monster.get_monster_goal()  # coords of player in the overworld
        end_x, end_y = target.x // 16, target.y // 16
        end = self.grid.node(end_x, end_y)

        # path
        finder = AStarFinder()
        self.path, empty = finder.find_path(start, end, self.grid)
        self.grid.cleanup()
        self.monster.set_path(self.path)

    def draw_path(self, screen, scroll):
        if self.path:
            points = []
            for point in self.path:
                x = (point.x * 16 - scroll[0]) + 8
                y = (point.y * 16 - scroll[1]) + 8
                points.append((x, y))
            pg.draw.lines(screen, 'red', False, points, 3)

    def update(self, monster):
        self.set_monster(monster)
        self.create_path(monster)
        # self.monster.update()
        # print(self.__position)