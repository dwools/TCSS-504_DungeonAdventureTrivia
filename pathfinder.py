from monster import  Monster
import pygame as pg
from dungeon_character import DungeonCharacter
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import math
class Pathfinder:
    def __init__(self, matrix):

        # setup
        self.__matrix = matrix
        self.__grid = Grid(matrix=matrix, inverse=True)

        # pathfinding
        self.__path = []

        # Monster
        self.__monster = None

    def empty_path(self):
        self.__path = []

    def set_monster(self, monster):
        self.__monster, self.__path = monster, self.empty_path()

    # def draw_active_cell(self, monster):
    #     target = monster.get_monster_goal()  # coords of player in the overworld
    #     row = target.x // 16
    #     col = target.y // 16

    def create_path(self, monster):
        # start cell
        monster_start = monster.get_character_rect()
        print(f"MONSTER START: {monster_start} \n")
        start_x, start_y = monster_start.x, monster_start.y
        start = self.__grid.node(start_x // 16, start_y // 16)

        # end cell
        target = monster.get_monster_goal()  # coords of player in the overworld
        end_x, end_y = target.x // 16, target.y // 16
        end = self.__grid.node(end_x, end_y)

        # path
        finder = AStarFinder()
        self.__path, empty = finder.find_path(start, end, self.__grid)
        self.__grid.cleanup()
        self.__monster.set_path(self.__path)

    def draw_path(self, screen, scroll):
        if self.__path:
            points = []
            for point in self.__path:
                x = (point.x * 16 - scroll[0]) + 8
                y = (point.y * 16 - scroll[1]) + 8
                points.append((x, y))
            pg.draw.lines(screen, 'red', False, points, 1)
        else:
            pass

    def update(self, monster):
        self.set_monster(monster)
        self.create_path(monster)
        # self.monster.update()
        # print(self.__position)