# Import packages
import pygame as pg
from pygame.locals import *  # import the pygame modules
import sys

# Import project files
import adventurer
import rooms
from dungeon import Dungeon

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


class DungeonAdventure:
    WINDOW_SIZE = [1280, 960]

    def __init__(self):
        super().__init__()

    def run(self):
        pg.mixer.pre_init(44100, -16, 2, 512)  # Initializing the audio file to remove it's delay
        pg.init()
        clock = pg.time.Clock()
        pg.display.set_caption(f"Dungeon Adventure")

        screen = pg.display.set_mode(self.WINDOW_SIZE, 0, 32)

        scroll = [0, 0]

        display = pg.Surface((640, 480))  # (640, 480)

        # Player location (need to somehow associate with the Adventurer Class)

        player_image = pg.image.load('assets/char_sprites/south_knight.png')

        player_rect = pg.Rect(150, 150, player_image.get_width(),
                              player_image.get_height())

        # Textures
        bottom_wall_image = pg.image.load('assets/Environment/Dungeon Prison/Assets/bottom_wall.png')
        upper_wall_image = pg.image.load('assets/Environment/Dungeon Prison/Assets/upper_wall.png')
        floor1_image = pg.image.load('assets/Environment/Dungeon Prison/Assets/floor1.png')
        north_left_door_image = pg.image.load('assets/Environment/Dungeon Prison/Assets/upper_left_door.png')
        north_right_door_image = pg.image.load('assets/Environment/Dungeon Prison/Assets/upper_right_door.png')
        TILE_SIZE = bottom_wall_image.get_width()

        # Audio
        pg.mixer.music.load('assets/audio/theme_foret.mp3')  # loading in the audio file
        pg.mixer.music.play(-1)  # loops indefinitely
        pg.mixer.music.set_volume(0.4)  # scale of 0->1

        # Map 20w x 15h
        def load_map(path):
            f = open(path + '.txt', 'r')
            data = f.read()
            f.close()
            data = data.split('\n')
            room_map = []
            for row in data:
                room_map.append((list(row)))
            return room_map

        room_map = load_map(rooms.Room.entrance_room(self))  # c.game_map

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

        moving_east = False
        moving_west = False
        moving_north = False
        moving_south = False

        display_map = False

        interacting = False

        paused = False

        while True:  # Game Loop

            # display.fill(c.PURPLE)  # Screen Background
            #
            # scroll[0] += (player_rect.x - scroll[0] - 160)
            # scroll[1] += (player_rect.y - scroll[1] - 120)
            #
            # scroll[0] += 1
            # scroll[1] += 1
            #
            # # List containing tiles where collisions occur
            # tile_rects = []
            #
            # y = 0
            # for row in room_map:
            #
            #     x = 0
            #     for tile in row:
            #
            #         if tile == "1":  # floor
            #             display.blit(floor1_image, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
            #
            #         elif tile == "2":  # Bottom Wall
            #             display.blit(bottom_wall_image, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
            #             tile_rects.append(pg.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            #
            #         elif tile == "3":  # Upper Wall
            #             display.blit(upper_wall_image, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
            #             tile_rects.append(pg.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            #
            #         elif tile == "4":  # North Left Door
            #             display.blit(north_left_door_image, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
            #             tile_rects.append(pg.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            #
            #         elif tile == "5":  # North Right Door
            #             display.blit(north_right_door_image, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
            #             tile_rects.append(pg.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            #
            #         x += 1
            #     y += 1

            # player_movement = [0, 0]
            # if moving_east:
            #     player_movement[0] += 2
            #     player_image = pg.image.load('assets/char_sprites/east_knight.png')
            #
            # if moving_west:
            #     player_movement[0] -= 2
            #     player_image = pg.image.load('assets/char_sprites/west_knight.png')
            #
            # if moving_north:
            #     player_movement[1] -= 2
            #     player_image = pg.image.load('assets/char_sprites/north_knight.png')
            #
            # if moving_south:
            #     player_movement[1] += 2
            #     player_image = pg.image.load('assets/char_sprites/south_knight.png')
            #
            # player_rect, collisions = move(player_rect, player_movement, tile_rects)
            # display.blit(player_image, (player_rect.x - scroll[0], player_rect.y - scroll[1]))

            for event in pg.event.get():  # Event Loop

                if event.type == QUIT:  # Check for window quit
                    pg.quit()  # Stop pygame
                    sys.exit()  # Stop running

                if event.type == KEYDOWN:

                    if event.key == K_w or event.key == K_UP:
                        moving_north = True
                        print("Moving North")

                    if event.key == K_s or event.key == K_DOWN:
                        moving_south = True
                        print("Moving South")

                    if event.key == K_a or event.key == K_LEFT:
                        moving_west = True
                        print("Moving West")

                    if event.key == K_d or event.key == K_RIGHT:
                        moving_east = True
                        print("Moving East")

                    if event.key == K_e:
                        interacting = True
                        print("Interacting!")

                    if event.key == K_m:
                        display_map = True
                        print(f"map={room_map}")

                    if event.key == K_p:
                        paused = True
                        print(f"The game is paused")

                if event.type == KEYUP:

                    if event.key == K_w or K_UP:
                        moving_north = False

                    if event.key == K_s or K_DOWN:
                        moving_south = False

                    if event.key == K_a or K_LEFT:
                        moving_west = False

                    if event.key == K_d or K_RIGHT:
                        moving_east = False

                    if event.key == K_e:
                        interacting = False

                    if event.key == K_m:
                        display_map = False
                        print("Hiding the map")

                    if event.key == K_p:
                        paused = False
                        print("Resuming the game!")

            # surf = pg.transform.scale(display, c.WINDOW_SIZE)
            # screen.blit(surf, (0, 0))
            # pg.display.update()  # Update the Display
            # clock.tick(60)  # set the FPS


if __name__ == "__main__":
    main = DungeonAdventure()
    main.run()
