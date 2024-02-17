# Import packages
import pygame as pg  # import pygame
from pygame.locals import *  # import the pygame modules
import sys
import textwrap

# Import project files

import config as c
import assets as a
import room
import initialize_databases
from dungeon import Maze
from menu import *

"""
Contains the main logic for playing the game

"""


class DungeonAdventure(Maze):
    """
    Class Dungeon Adventure:
    Holds main gameplay loop and generates the GUI.
    Reads and adapts to player input.
    """

    def __init__(self):
        pg.init()
        super().__init__(15, 20)

        # Controls
        self.moving_east, self.moving_west, self.moving_north, self.moving_south = False, False, False, False
        self.interacting, self.left_clicked, self.escaping = False, False, False

        # Game Status
        self.running, self.playing, self.paused = True, False, False

        # Menu Status
        self.main_menu = MainMenu(self)
        self.character_select = CharacterSelectMenu(self)
        self.options = OptionsMenu(self)
        self.how_to_play = HowToPlayMenu(self)  # need 2 build
        self.load_games = LoadSaveGamesMenu(self)
        self.credits = CreditsMenu(self)
        self.pause_menu = PauseMenu(self)
        self.trivia_ui = TriviaUI(self)
        self.game_over = GameOver(self)
        self.current_menu = self.trivia_ui  # Default menu is the main menu

        # Window Setup
        self.WIN_WIDTH, self.WIN_HEIGHT = c.WIN_WIDTH, c.WIN_HEIGHT  # 1280w x 960h
        self.WINDOW_SIZE = c.WINDOW_SIZE
        self.display = pg.Surface((640, 480))  # (640w, 480h)
        self.screen = pg.display.set_mode(self.WINDOW_SIZE, 0, 32)

        # Player sprite setup, camera scrolling setup
        self.player_movement = [0, 0]
        self.camera_scroll = [0, 0]

        self.player_image = pg.image.load(a.south_knight)
        self.player_rect = pg.Rect(16, 16, self.player_image.get_width(),
                                   self.player_image.get_height())
        self.camera_scroll = [0, 0]

        # Config
        self.font = c.dungeon_font
        self.font_color = c.WHITE
        self.PURPLE = c.PURPLE
        self.BLACK = c.BLACK
        self.WHITE = c.WHITE

    def game_loop(self):
        """
        Main Gameplay Loop, runs the Main Game GUI and updates screen based on user input.
        :return:
        """

        pg.mixer.pre_init(44100, -16, 2, 512)  # Initializing the audio file to remove its delay
        clock = pg.time.Clock()
        pg.display.set_caption(f"Dungeon Adventure")

        # Loading Map/ Tile Textures
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
            """ Reading-in the tilemap from the dungeon.txt map file.
            """

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
            """ Testing whether the player collides with n tile. """

            hit_list = []
            for tile in tiles:
                if rect.colliderect(tile):
                    hit_list.append(tile)
            return hit_list

        def move(rect, movement, tiles):
            """ Adjusts player position based on collision with n tile. """

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

        while self.playing and not self.paused:  # Game Loop
            """ Dungeon Adventure Gui runs while: game is not paused, game is 'playing'. """

            # Check for player input
            self.check_events()

            # Reset the screen Background
            self.display.fill(self.PURPLE)

            # Basically the camera tracking/ following the player sprite
            self.camera_scroll[0] += (self.player_rect.x - self.camera_scroll[0] - 160)
            self.camera_scroll[1] += (self.player_rect.y - self.camera_scroll[1] - 120)
            self.camera_scroll[0] += 1
            self.camera_scroll[1] += 1

            ###

            # List containing tiles where collisions occur
            tile_rects = []

            # Assign image sprites to the dungeon map txt values. Depending on the sprite add it to the collisions list.

            y = 0
            for row in dungeon_map:

                x = 0
                for tile in row:

                    if tile == "f":  # floor
                        self.display.blit(floor_image, (x * TILE_SIZE - self.camera_scroll[0], y * TILE_SIZE - self.camera_scroll[1]))

                    elif tile == "n":  # North Wall (A separate north wall looks better in the GUI)
                        self.display.blit(upper_wall_image,
                                          (x * TILE_SIZE - self.camera_scroll[0], y * TILE_SIZE - self.camera_scroll[1]))
                        tile_rects.append(pg.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

                    elif tile == "w":  # Wall (for east, west, south walls)
                        self.display.blit(bottom_wall_image,
                                          (x * TILE_SIZE - self.camera_scroll[0], y * TILE_SIZE - self.camera_scroll[1]))
                        tile_rects.append(pg.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

                    x += 1
                y += 1

            # set players position to 0,0
            # update player position based on user input

            self.player_movement = [0, 0]
            if self.moving_east:
                self.player_movement[0] += 2
                self.player_image = pg.image.load(a.east_knight)

            if self.moving_west:
                self.player_movement[0] -= 2
                self.player_image = pg.image.load(a.west_knight)

            if self.moving_north:
                self.player_movement[1] -= 2
                self.player_image = pg.image.load(a.north_knight)

            if self.moving_south:
                self.player_movement[1] += 2
                self.player_image = pg.image.load(a.south_knight)

            # adjust player position based on collision with n tiles

            self.player_rect, collisions = move(self.player_rect, self.player_movement, tile_rects)
            self.display.blit(self.player_image, (self.player_rect.x - self.camera_scroll[0], self.player_rect.y - self.camera_scroll[1]))

            # Draw the Gui to the screen, update it

            window_surface = pg.transform.scale(self.display, self.WINDOW_SIZE)
            self.screen.blit(window_surface, (0, 0))
            pg.display.update()  # Update the Display
            clock.tick(60)  # set the FPS

    def check_events(self):
        """ Receive user input from Mouse x Keyboard. """

        for event in pg.event.get():  # Event Loop

            if event.type == QUIT:  # Check for window quit
                self.running, self.playing, self.paused = False, False, False
                self.current_menu.run_display = False

            if event.type == MOUSEBUTTONDOWN:
                self.left_clicked = True

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
                    self.current_menu = self.pause_menu

                if event.key == K_t:
                    self.paused = True
                    self.current_menu = self.trivia_ui

                if event.key == K_RETURN:
                    self.interacting = True
                    print("option selected")

                if event.key == K_ESCAPE or event.key == K_BACKSPACE:
                    self.escaping = True

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

                if event.key == K_ESCAPE or event.key == K_BACKSPACE:
                    self.escaping = False

    def draw_text(self, text, size, x, y, font_color):
        """ Simple helper-function used to write text to the GUI. """

        font = pg.font.Font(self.font, size)
        text_surface = font.render(text, True, font_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x / 2, y / 2)
        self.display.blit(text_surface, text_rect)


if __name__ == "__main__":
    databases = initialize_databases.main()
    main = DungeonAdventure()
    main.game_loop()
