# Import packages
import os
import pickle
import random

import sys
import textwrap

import pygame as pg  # import pygame
from pygame.locals import *  # import the pygame modules
from pygame.font import Font
# Import project files

import config as c
import assets as a
import item_factory
import monster_gremlin
import monster_ogre
from monster import *

import monster_factory

import room
import initialize_databases
from object_coordinates_generator import ValidCoordsGenerator
from dungeon import Maze
from menu import *
from combat import Combat
from monster_ogre import Ogre
from monster_skeleton import Skeleton
from monster_gremlin import Gremlin
from pathfinder import Pathfinder
# from save_game import SaveGame

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
        # pg.init()
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
        self.combat_ui = Combat(self)
        self.game_over = GameOver(self)
        self.current_menu = self.main_menu  # Default menu is the main menu

        # Window Setup
        self.WIN_WIDTH, self.WIN_HEIGHT = c.WIN_WIDTH, c.WIN_HEIGHT  # 1280w x 960h
        self.WINDOW_SIZE = c.WINDOW_SIZE
        self.display = pg.Surface((640, 480))  # (640w, 480h)
        self.screen = pg.display.set_mode(self.WINDOW_SIZE, 0, 32)

        # Player sprite setup, camera scrolling setup
        self.__player_character = None
        self.player_movement = [0, 0]
        self.camera_scroll = [0, 0]
        self.player_direction = 0

        self.coords_generator = ValidCoordsGenerator()
        self.coords_generator.generate_coords()

        self.player_position = [16, 16]
        self.player_x, self.player_y = self.player_position

        self.player_img_size = (14, 14)
        self.player_image = pg.transform.scale(pg.image.load(a.south_priestess), self.player_img_size)
        self.player_rect = pg.Rect(self.player_y, self.player_x, self.player_image.get_width(),
                                   self.player_image.get_height())  # start at 16, add 48 x or y for good position
        self.camera_scroll = [0, 0]

        # Monster setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.m_factory = monster_factory.MonsterFactory()

        self.monsters = []
        self.monster_rects = []

        # Place/spawn monsters
        for _ in range(2):
            creature = self.m_factory.choose_monster()
            creature_position = self.coords_generator.get_random_coords()
            creature.set_position(creature_position)  # Set monster initial position to random coords
            creature_x, creature_y = creature.get_position()
            creature_rect = creature.set_character_rect(creature_x, creature_y)  # Use random coords to create a rect at coords
            self.monster_rects.append(creature_rect)
            self.monsters.append(creature)


        # Item setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.i_factory = item_factory.ItemFactory()

        self.items = []
        self.item_rects = []

        # Place/spawn items
        for _ in range(1):
            item = self.i_factory.choose_item()
            item_position = self.coords_generator.get_random_coords()
            item.set_item_position(item_position)
            item_x, item_y = item.get_item_position()
            item_rect = item.set_item_rect(item_x, item_y)
            self.item_rects.append(item_rect)
            self.items.append(item_position)



        # Load up base images
        self.gremlin_image = pg.image.load(a.south_gremlin)
        self.skelly_image = pg.image.load(a.south_skelly)
        self.ogre_image = pg.image.load(a.south_rogue)  # to be replaced with Ogre sprite
        # self.potion_image = pg.image.load(health_potion)
        # self.pittrap_image = pg.image.load(pittrap)

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Config
        self.dungeon_font = c.dungeon_font
        self.normal_cont = c.system_font
        self.font_color = c.WHITE
        self.PURPLE = c.PURPLE
        self.BLACK = c.BLACK
        self.WHITE = c.WHITE

    # How can we set our character player while avoiding circular imports?
    # def get_save_status(self):
    #     if self.pause_menu.get_save_game() == True:
    #         SaveGame.pickle(DungeonAdventure)
    #         self.pause_menu.set_save_game(False)

    def get_player_character(self):
        return self.__player_character

    def set_player_character(self, player_character):
        self.__player_character = player_character

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

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # Create the map for visuals, create the matrix for monsters
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

        self.__dungeon_map = load_map()

        def create_matrix(tile_set):
            # Creating a map underneath the visual map that monsters will use in the pathfinding algorithm
            # 0 is navigable space, 1 is obstacle / walls
            tile_map = []

            for row in tile_set:
                # Check if the row is not empty
                if row:
                    row_tiles = []
                    for tile in row:
                        if tile == "f":  # floor
                            row_tiles.append(0)
                        elif tile == "n":  # North Wall (A separate north wall looks better in the GUI)
                            row_tiles.append(1)
                        elif tile == "w":  # Wall (for east, west, south walls)
                            row_tiles.append(1)
                    tile_map.append(row_tiles)

            return tile_map

        pathfinder = Pathfinder(create_matrix(self.__dungeon_map))

        def tile_collision_test(rect, tiles):
            """ Testing whether a character collides with n tile. """

            hit_list = []
            for tile in tiles:
                if rect.colliderect(tile):
                    hit_list.append(tile)
            return hit_list

        def move(rect, movement, tiles):
            """ Adjusts player position based on collision with n tile. """

            tile_collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
            rect.x += movement[0]
            hit_list = tile_collision_test(rect, tiles)
            for tile in hit_list:

                if movement[0] > 0:
                    rect.right = tile.left
                    tile_collision_types['right'] = True

                elif movement[0] < 0:
                    rect.left = tile.right
                    tile_collision_types['left'] = True

            rect.y += movement[1]
            hit_list = tile_collision_test(rect, tiles)
            for tile in hit_list:

                if movement[1] > 0:
                    rect.bottom = tile.top
                    tile_collision_types['bottom'] = True

                elif movement[1] < 0:
                    rect.top = tile.bottom
                    tile_collision_types['top'] = True

            return rect, tile_collision_types

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

            # List containing tiles where collisions occur
            tile_rects = []

            # Assign image sprites to the dungeon map txt values. Depending on the sprite add it to the collisions list.

            y = 0
            for row in self.__dungeon_map:

                x = 0
                for tile in row:

                    if tile == "f":  # floor
                        self.display.blit(floor_image, (
                            x * TILE_SIZE - self.camera_scroll[0], y * TILE_SIZE - self.camera_scroll[1]))

                    elif tile == "n":  # North Wall (A separate north wall looks better in the GUI)
                        self.display.blit(upper_wall_image,
                                          (
                                              x * TILE_SIZE - self.camera_scroll[0],
                                              y * TILE_SIZE - self.camera_scroll[1]))
                        tile_rects.append(pg.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

                    elif tile == "w":  # Wall (for east, west, south walls)
                        self.display.blit(bottom_wall_image,
                                          (
                                              x * TILE_SIZE - self.camera_scroll[0],
                                              y * TILE_SIZE - self.camera_scroll[1]))
                        tile_rects.append(pg.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

                    x += 1
                y += 1

            # if self.player_rect.colliderect():
            #     self.
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

            # Update Sprites for Player

            # set players movement to 0,0
            # update player movement based on user input

            self.player_movement = [0, 0]
            if self.moving_east:
                self.player_movement[0] += 2
                self.player_image = pg.transform.scale(pg.image.load(a.east_priestess), self.player_img_size)

            if self.moving_west:
                self.player_movement[0] -= 2
                self.player_image = pg.transform.scale(pg.image.load(a.west_priestess), self.player_img_size)

            if self.moving_north:
                self.player_movement[1] -= 2
                self.player_image = pg.transform.scale(pg.image.load(a.north_priestess), self.player_img_size)

            if self.moving_south:
                self.player_movement[1] += 2
                self.player_image = pg.transform.scale(pg.image.load(a.south_priestess), self.player_img_size)

            # adjust player position based on collision with n tiles

            self.player_rect, collisions = move(self.player_rect, self.player_movement, tile_rects)
            self.display.blit(self.player_image,
                              (self.player_rect.x - self.camera_scroll[0], self.player_rect.y - self.camera_scroll[1]))

            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

            # Update the sprites for the monsters

            for monster in self.monsters:
                """ For monster in list of monsters, get monster rect, get monster position, 
                calculate monster's path to the player, update monster position based on path to the player.
                """

                monster.set_monster_goal(self.player_rect)  # Setting monsters goal to player position
                monster.set_player_scroll(self.camera_scroll)  # adjusting for camera scroll
                # pathfinder.draw_path(self.display, self.camera_scroll)  # Drawing the path visually, not necessary in gameplay
                pathfinder.update(monster)  # Updating the monster's path based on player position
                rect = monster.get_character_rect()  # Get the monster's rect to move
                monster.update()  # Update the monsters position based on the above path

                if isinstance(monster, Gremlin):
                    monster.set_south_monster_sprite(pg.image.load(a.south_gremlin))
                    monster.set_north_monster_sprite(pg.image.load(a.north_gremlin))
                    monster.set_east_monster_sprite(pg.image.load(a.east_gremlin))
                    monster.set_west_monster_sprite(pg.image.load(a.west_gremlin))

                    monster.set_monster_sprite(monster.get_south_monster_sprite())

                    self.gremlin_image = monster.get_monster_sprite()
                    self.display.blit(self.gremlin_image, (
                        rect.x - self.camera_scroll[0], rect.y - self.camera_scroll[1]))  # Draws monster to screen
                    print("Gameloop rect.x: ", rect.x)  # Rect x is the position where the monster is being drawn
                    print("Gameloop rect.y: ", rect.y)  # same for y

                if isinstance(monster, Skeleton):
                    monster.set_south_monster_sprite(pg.image.load(a.south_skelly))
                    monster.set_north_monster_sprite(pg.image.load(a.north_skelly))
                    monster.set_east_monster_sprite(pg.image.load(a.east_skelly))
                    monster.set_west_monster_sprite(pg.image.load(a.west_skelly))
                    # monster.set_monster_sprite(pg.image.load(a.south_skelly))

                    monster.set_monster_sprite(monster.get_south_monster_sprite())

                    self.skelly_image = monster.get_monster_sprite()
                    self.display.blit(self.skelly_image, (
                        rect.x - self.camera_scroll[0], rect.y - self.camera_scroll[1]))
                    print("Gameloop rect.x: ", rect.x)
                    print("Gameloop rect.y: ", rect.y)

                if isinstance(monster, Ogre):
                    monster.set_south_monster_sprite(pg.image.load(a.south_rogue))
                    monster.set_north_monster_sprite(pg.image.load(a.north_rogue))
                    monster.set_east_monster_sprite(pg.image.load(a.east_rogue))
                    monster.set_west_monster_sprite(pg.image.load(a.west_rogue))

                    monster.set_monster_sprite(monster.get_south_monster_sprite())

                    self.ogre_image = monster.get_monster_sprite()
                    self.display.blit(self.ogre_image, (
                        rect.x - self.camera_scroll[0], rect.y - self.camera_scroll[1]))
                    print("Gameloop rect.x: ", rect.x)
                    print("Gameloop rect.y: ", rect.y)

            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

            # Create the Heads Up Display, draw it to the screen, update it with player stats dynamically

            # test health for hud

            # Drawing the HUDisplay
            pg.draw.rect(self.display, 'black', pg.Rect(0, 0, 140, 90))  # outside background
            pg.draw.rect(self.display, 'darkslategray', pg.Rect(5, 5, 130, 80))  # inside background

            # Setup Health
            self.draw_text(c.system_font, f'Health: ', 10, 55, 30, c.BLACK)
            # self.draw_text(c.system_font, f'{current_health} ', 12, 120, 30, c.BLACK)
            # self.draw_text(c.system_font, f'/{max_health}', 12, 150, 30, c.BLACK)

            # Setup Pillars
            self.draw_text(c.system_font, f'Pillars: ', 10, 55, 60, c.BLACK)

            # Setup Lives
            self.draw_text(c.system_font, f'Lives: ', 10, 50, 90, c.BLACK)

            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

                if event.key == K_w or event.key == K_UP:  # 0,1,2,3 == S,N,E,W
                    self.moving_north = True
                    self.player_direction = 1
                    # print("Moving North")

                if event.key == K_s or event.key == K_DOWN:
                    self.moving_south = True
                    self.player_direction = 0
                    # print("Moving South")

                if event.key == K_a or event.key == K_LEFT:
                    self.moving_west = True
                    self.player_direction = 3
                    # print("Moving West")

                if event.key == K_d or event.key == K_RIGHT:
                    self.moving_east = True
                    self.player_direction = 2

                    # print("Moving East")

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

                if event.key == K_c:
                    self.paused = True
                    self.current_menu = self.combat_ui

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

    def draw_text(self, font, text, size, x, y, font_color):
        """ Simple helper-function used to write text to the GUI. """
        pg.font.init()
        font = pg.font.Font(font, size)
        text_surface = font.render(text, True, font_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x / 2, y / 2)
        self.display.blit(text_surface, text_rect)


    def load_game(self):
        if os.path.exists("dungeon_adventure.pickle"):
            with open("dungeon_adventure.pickle", "rb") as f:
                game_data = pickle.load(f)
            self.player_position = game_data['player_position']
            self.monsters = game_data['monsters']
            self.monster_rects = game_data['monster_rects']
            self.items = game_data['items']
            self.item_rects = game_data['item_rects']
            self.player_rect = game_data['player_rect']
            self.__dungeon_map = game_data['dungeon_map']



if __name__ == "__main__":
    databases = initialize_databases.main()
    main = DungeonAdventure()
    main.game_loop()
    SaveGame.pickle(main)
