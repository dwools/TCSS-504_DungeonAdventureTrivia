from abc import ABC, abstractmethod
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
                 maximum_heal_points,
                 ):
        super().__init__(name, type, hit_points, attack_speed, chance_to_hit, minimum_damage, maximum_damage)

        self.__movement = [0, 0]
        self.__direction = pg.math.Vector2(0, 0)
        self.__monster_goal = None
        self.__path = []

        self.__chance_to_heal = chance_to_heal
        self.__minimum_heal_points = minimum_heal_points
        self.__maximum_heal_points = maximum_heal_points

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

    def draw_active_cell(self, monster):
        target = monster.get_monster_goal()  # coords of player in the overworld
        row = target.x // 16
        col = target.y // 16

    def create_path(self, monster):
        # start cell
        monster_start = monster.get_character_rect()
        start_x, start_y = monster_start.x, monster_start.y
        start = self.grid.node(start_x // 16, start_y // 16)

        # end cell
        target = monster.get_monster_goal()  # coords of player in the overworld
        end_x, end_y = target.x // 16, target.y // 16
        end = self.grid.node(end_x, end_y)

        # path
        finder = AStarFinder()
        self.path, empty = finder.find_path(start, end, self.grid)
        print(target)
        self.grid.cleanup()

    def draw_path(self, screen, scroll):
        if self.path:
            points = []
            for point in self.path:
                x = (point.x * 16 - scroll[0]) + 8
                y = (point.y * 16 - scroll[1]) + 8
                points.append((x, y))
            pg.draw.lines(screen, 'red', False, points, 3)

    def update(self, monster):
        self.create_path(monster)
        self.draw_active_cell(monster)
