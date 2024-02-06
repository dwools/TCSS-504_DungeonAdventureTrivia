# Import packages
import pygame as pg
from pygame.locals import *  # import the pygame modules
import sys

# Import project files

import config as c
import assets as a
import Room
from Dungeon import Maze
from menu import MainMenu

"""
Contains the main logic for playing the game

Introduces the game describing what the game is about and how to play

Creates a Dungeon Object and an Adventurer Object

Obtains the name of the adventurer from the user


Does the following repetitively:

Prints the current room (this is based on the Adventurer's current location)

Determines the Adventurer's options (Move, Use a Potion)

Continues this process until the Adventurer wins or dies

NOTE: Include a hidden menu option for testing that prints out the entire Dungeon -- specify what the menu option
is in your documentation for the DungeonAdventure class

At the conclusion of the game, display the entire Dungeon
"""


class DungeonAdventure(Maze):

    def __init__(self):
        pg.init()
        super().__init__(15, 20)

        # Controls
        self.moving_east, self.moving_west, self.moving_north, self.moving_south = False, False, False, False
        self.interacting, self.left_clicked = False, False
        self.mouse_position = pg.event.get(pg.mouse.get_pos())

        # Game Status
        self.running, self.playing, self.paused = True, False, False
        self.current_menu = MainMenu(self)

        # Window Setup
        self.WIN_WIDTH, self.WIN_HEIGHT = c.WIN_WIDTH, c.WIN_HEIGHT  # 1280w x 960h
        self.WINDOW_SIZE = c.WINDOW_SIZE
        self.display = pg.Surface((640, 480))  # (640w, 480h)
        self.screen = pg.display.set_mode(self.WINDOW_SIZE, 0, 32)

        self.scroll = [0, 0]

        # Config
        self.font = c.dungeon_font
        self.PURPLE = c.PURPLE
        self.BLACK = c.BLACK
        self.WHITE = c.WHITE

    def game_loop(self):
        pg.mixer.pre_init(44100, -16, 2, 512)  # Initializing the audio file to remove its delay
        clock = pg.time.Clock()
        pg.display.set_caption(f"Dungeon Adventure")

        # Player location (need to somehow associate with the Adventurer Class)

        player_image = pg.image.load(a.south_knight)

        player_rect = pg.Rect(25, 25, player_image.get_width(),
                              player_image.get_height())

        # Textures
        bottom_wall_image = pg.image.load(a.bottom_wall)
        upper_wall_image = pg.image.load(a.upper_wall)
        floor_image = pg.image.load(a.floor)
        TILE_SIZE = bottom_wall_image.get_width()

        # Audio
        background_audio = pg.mixer.music.load(a.background_music)  # loading in the audio file
        background_audio = pg.mixer.music.play(-1)  # loops indefinitely
        background_audio = pg.mixer.music.set_volume(0.0)  # scale of 0->1

        # Map 20w x 15h
        def load_map():
            file = open('dungeon.txt', 'r')
            data = file.read()
            file.close()
            data = data.split('\n')
            dungeon_map = []
            for row in data:
                dungeon_map.append((list(row)))
            return dungeon_map

        dungeon_map = load_map()

        def collision_test(rect, tiles):

            hit_list = []
            for tile in tiles:
                if rect.colliderect(tile):
                    hit_list.append(tile)
            return hit_list

        def move(rect, movement, tiles):

            collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
            rect.x += movement[0]
            hit_list = collision_test(rect, tiles)
            for tile in hit_list:

                if movement[0] > 0:
                    rect.right = tile.left
                    collision_types['right'] = True

                elif movement[0] < 0:
                    rect.left = tile.right
                    collision_types['left'] = True

            rect.y += movement[1]
            hit_list = collision_test(rect, tiles)
            for tile in hit_list:
                if movement[1] > 0:
                    rect.bottom = tile.top
                    collision_types['bottom'] = True
                elif movement[1] < 0:
                    rect.top = tile.bottom
                    collision_types['top'] = True
            return rect, collision_types

        while self.running:  # Game Loop

            # Check for player input
            self.check_events()

            # get current Mouse position
            self.mouse_position = pg.mouse.get_pos()

            # Reset the screen Background
            self.display.fill(self.PURPLE)

            # Basically the camera tracking/ following the player sprite
            self.scroll[0] += (player_rect.x - self.scroll[0] - 160)
            self.scroll[1] += (player_rect.y - self.scroll[1] - 120)
            self.scroll[0] += 1
            self.scroll[1] += 1

            # List containing tiles where collisions occur
            tile_rects = []

            y = 0
            for row in dungeon_map:

                x = 0
                for tile in row:

                    if tile == "f":  # floor
                        self.display.blit(floor_image, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))

                    elif tile == "n":  # North Wall (A separate north wall looks better in the GUI)
                        self.display.blit(upper_wall_image,
                                          (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                        tile_rects.append(pg.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

                    elif tile == "w":  # Wall (for east, west, south walls)
                        self.display.blit(bottom_wall_image,
                                          (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                        tile_rects.append(pg.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

                    x += 1
                y += 1

            player_movement = [0, 0]
            if self.moving_east:
                player_movement[0] += 2
                player_image = pg.image.load(a.east_knight)

            if self.moving_west:
                player_movement[0] -= 2
                player_image = pg.image.load(a.west_knight)

            if self.moving_north:
                player_movement[1] -= 2
                player_image = pg.image.load(a.north_knight)

            if self.moving_south:
                player_movement[1] += 2
                player_image = pg.image.load(a.south_knight)

            player_rect, collisions = move(player_rect, player_movement, tile_rects)
            self.display.blit(player_image, (player_rect.x - self.scroll[0], player_rect.y - self.scroll[1]))

            window_surface = pg.transform.scale(self.display, self.WINDOW_SIZE)
            self.screen.blit(window_surface, (0, 0))
            pg.display.update()  # Update the Display
            clock.tick(60)  # set the FPS

    def check_events(self):
        for event in pg.event.get():  # Event Loop

            if event.type == QUIT:  # Check for window quit
                self.running, self.playing = False, False
                self.current_menu.run_display = False

            if event.type == KEYDOWN:

                if event.key == K_w or event.key == K_UP:
                    self.moving_north = True
                    print("Moving North")

                if event.key == K_s or event.key == K_DOWN:
                    self.moving_south = True
                    print("Moving South")

                if event.key == K_a or event.key == K_LEFT:
                    self.moving_west = True
                    print("Moving West")

                if event.key == K_d or event.key == K_RIGHT:
                    self.moving_east = True
                    print("Moving East")

                if event.key == K_e:
                    self.interacting = True
                    print("Interacting!")

                if event.key == K_p:
                    self.paused = True
                    print("The game is paused")
                    # call the pause menu UI here

                if event.key == K_RETURN:
                    self.interacting = True
                    print("option selected")

            if event.type == KEYUP:

                if event.key == K_w or K_UP:
                    self.moving_north = False

                if event.key == K_s or K_DOWN:
                    self.moving_south = False

                if event.key == K_a or K_LEFT:
                    self.moving_west = False

                if event.key == K_d or K_RIGHT:
                    self.moving_east = False

                if event.key == K_e or event.key == K_RETURN:
                    self.interacting = False

    def draw_text(self, text, size, x, y):
        font = pg.font.Font(self.font, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x/2, y/2)
        self.display.blit(text_surface, text_rect)


if __name__ == "__main__":
    main = DungeonAdventure()
    main.game_loop()
