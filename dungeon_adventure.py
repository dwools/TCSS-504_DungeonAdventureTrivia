# Import packages
import os
import pickle

from pygame.locals import *  # import the pygame modules

# Import project files

from Items import item_factory
from Items.item import Item

from Characters import monster_factory

from Databases import initialize_databases
from Gameplay.object_coordinates_generator import ValidCoordsGenerator
from menu import *
from Gameplay.combat import *
from Gameplay.pathfinder import Pathfinder

# from save_game import SaveGame

"""
Contains the main logic for playing the game

"""


class DungeonAdventure():
    """
    Class Dungeon Adventure:
    Holds main gameplay loop and generates the GUI.
    Reads and adapts to player input.
    """

    def __init__(self):
        # Maze set in MainMenu upon "Start Game" or "Load Saved Game" interaction
        self.__dungeon_map = None
        self.__loaded_game = None

        # Menu Status
        self.main_menu = MainMenu(self)
        self.character_select = CharacterSelectMenu(self)
        self.options = OptionsMenu(self)
        self.how_to_play = HowToPlayMenu(self)
        self.trivia_ui = None
        self.credits = CreditsMenu(self)
        self.pause_menu = PauseMenu(self)
        self.game_over = GameOver(self)
        self.victory_screen = VictoryScreen(self)
        self.current_menu = self.main_menu  # Default menu is the main menu


        # Window Setup
        self.WIN_WIDTH, self.WIN_HEIGHT = c.WIN_WIDTH, c.WIN_HEIGHT  # 1280w x 960h
        self.WINDOW_SIZE = c.WINDOW_SIZE
        self.display = pg.Surface((640, 480))  # (640w, 480h)
        self.screen = pg.display.set_mode(self.WINDOW_SIZE, 0, 32)


        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Config
        self.dungeon_font = c.dungeon_font
        self.normal_cont = c.system_font
        self.menu_font_color = c.WHITE
        self.combat_font_color = c.BLACK
        self.PURPLE = c.PURPLE
        self.BLACK = c.BLACK
        self.WHITE = c.WHITE
        self.volume = 0.5

        # Player setup
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

        self.player_image_current = None  # pg.transform.scale(pg.image.load(a.south_priestess), self.player_img_size)
        self.player_image_north = None
        self.player_image_south = None
        self.player_image_east = None
        self.player_image_west = None

        self.player_rect = None  # pg.Rect(self.player_x, self.player_y, self.player_image_current.get_width(),
        #      self.player_image_current.get_height())  # start at 16, add 48 x or y for good position

        # Monster setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.__monsters = []
        self.__monster_count = 5

        # Place/spawn monsters
        for _ in range(self.get_monster_count()):
            self.place_monsters()

        # Item setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.__health_potion = Item("Health Potion")
        self.__fire_trap = Item("Fire Trap")
        self.i_factory = item_factory.ItemFactory()
        self.__items = []
        self.__item_count = 10

        # Place/spawn items
        for item in range(self.__item_count):
            item = self.i_factory.choose_item()
            self.place_items(item)

        # Pillar setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.__abstraction_pillar = Pillar("Abstraction")
        self.__encapsulation_pillar = Pillar("Encapsulation")
        self.__inheritance_pillar = Pillar("Inheritance")
        self.__polymorphism_pillar = Pillar("Polymorphism")
        self.__pillars = [self.__abstraction_pillar, self.__encapsulation_pillar, self.__inheritance_pillar,
                          self.__polymorphism_pillar]

        # Place/spawn pillars
        for pillar in self.__pillars:
            self.place_pillar(pillar)

        # PNG objects to ignore
        # self.snake = 'snake.png'
        # self.south_knight = 'south_knight.png'
        # self.north_knight = 'north_knight.png'
        # self.west_knight = 'west_knight.png'
        # self.east_knight = 'east_knight.png'
        # self.south_priestess = 'south_priestess.png'
        # self.north_priestess = 'north_priestess.png'
        # self.west_priestess = 'west_priestess.png'
        # self.east_priestess = 'east_priestess.png'
        # self.south_rogue = 'south_rogue.png'
        # self.north_rogue = 'north_rogue.png'
        # self.west_rogue = 'west_rogue.png'
        # self.east_rogue = 'east_rogue.png'
        # self.south_gremlin = 'south_gremlin.png'
        # self.north_gremlin = 'north_gremlin.png'
        # self.west_gremlin = 'west_gremlin.png'
        # self.east_gremlin = 'east_gremlin.png'
        # self.south_ogre = 'south_ogre.png'
        # self.north_ogre = 'north_ogre.png'
        # self.west_ogre = 'west_ogre.png'
        # self.east_ogre = 'east_ogre.png'
        # self.south_skelly = 'south_skelly.png'
        # self.north_skelly = 'north_skelly.png'
        # self.west_skelly = 'west_skelly.png'
        # self.east_skelly = 'east_skelly.png'
        # self.background_music = 'theme_forest.mp3'
        # self.bottom_wall = 'bottom_wall.png'
        # self.upper_wall = 'upper_wall.png'
        # self.floor = 'floor1.png'
        # self.health_potion = 'HealthPotion.png'
        # self.fire_trap = 'FireTrap.png'
        # self.abstraction_pillar = 'AstronomyPillar.png'
        # self.encapsulation_pillar = 'ElapidPillar.png'
        # self.inheritance_pillar = 'InternationalPillar.png'
        # self.polymorphism_pillar = 'PokemonPillar.png'

        # Controls
        self.moving_east, self.moving_west, self.moving_north, self.moving_south = False, False, False, False
        self.interacting, self.left_clicked, self.escaping = False, False, False

        # Game Status
        self.running, self.playing, self.paused = True, False, False

    def set_player_rect(self):
        self.player_rect = pg.Rect(self.player_y, self.player_x, self.player_image_south.get_width(),
                                   self.player_image_south.get_height())

    def get_player_img_size(self):
        return self.player_img_size

    def set_volume(self, volume):
        self.volume = volume

    def get_volume(self):
        return self.volume

    def set_player_images(self, north_image, east_image, west_image, south_image):
        self.player_image_north = pg.transform.scale(pg.image.load(north_image[0]), north_image[1])
        self.player_image_east = pg.transform.scale(pg.image.load(east_image[0]), east_image[1])
        self.player_image_west = pg.transform.scale(pg.image.load(west_image[0]), west_image[1])
        self.player_image_south = pg.transform.scale(pg.image.load(south_image[0]), south_image[1])
        self.player_image_current = pg.transform.scale(pg.image.load(south_image[0]), south_image[1])

    def place_items(self, item):
        item.set_item_position(self.coords_generator.get_random_coords())
        item_x, item_y = item.get_item_position()
        if item.get_item_name() == "Health Potion":
            item.set_item_rect(item_x + 4, item_y + 4)
        else:
            item.set_item_rect(item_x, item_y)
        self.__items.append(item)

    def remove_pillar(self, pillar):
        if pillar.get_pillar_name() == 'Abstraction':
            self.__pillars.remove(self.__abstraction_pillar)
        elif pillar.get_pillar_name() == 'Encapsulation':
            self.__pillars.remove(self.__encapsulation_pillar)
        elif pillar.get_pillar_name() == 'Inheritance':
            self.__pillars.remove(self.__inheritance_pillar)
        elif pillar.get_pillar_name() == 'Polymorphism':
            self.__pillars.remove(self.__polymorphism_pillar)

    def get_pillar(self, pillar):
        if pillar == 'Abstraction':
            return self.__abstraction_pillar
        elif pillar == 'Encapsulation':
            return self.__encapsulation_pillar
        elif pillar == 'Inheritance':
            return self.__inheritance_pillar
        elif pillar == 'Polymorphism':
            return self.__polymorphism_pillar

    def get_abstraction_pillar(self):
        return self.__abstraction_pillar

    def get_encapsulation_pillar(self):
        return self.__encapsulation_pillar

    def get_inheritance_pillar(self):
        return self.__inheritance_pillar

    def get_polymorphism_pillar(self):
        return self.__polymorphism_pillar

    def get_pillars_list(self):
        return self.__pillars

    def place_pillar(self, pillar):
        pillar.set_pillar_position(self.coords_generator.get_random_coords())
        pillar_x, pillar_y = pillar.get_pillar_position()
        pillar.set_pillar_rect(pillar_x + 4, pillar_y + 4)

    def get_player_character(self):
        return self.__player_character

    def set_player_character(self, player_character):
        self.__player_character = player_character

    def game_loop(self):
        """
        Main Gameplay Loop, runs the Main Game GUI and updates screen based on user input.
        :return:
        """
        if self.__loaded_game is True:

            self.set_dungeon_map(self.load_saved_map())  #
            self.load_game()
        else:
            self.set_dungeon_map(self.load_new_map())  # load_new_map() reads in new dungeon.txt file


        pg.mixer.pre_init(44100, -16, 2, 512)  # Initializing the audio file to remove its delay
        clock = pg.time.Clock()
        pg.display.set_caption(f"Dungeon Adventure")

        # Loading Map/ Tile Textures
        bottom_wall_image = pg.image.load(a.bottom_wall)
        upper_wall_image = pg.image.load(a.upper_wall)
        floor_image = pg.image.load(a.floor)
        TILE_SIZE = bottom_wall_image.get_width()

        # # Audio
        # background_audio = pg.mixer.music.load(a.background_music)  # loading in the audio file
        # background_audio = pg.mixer.music.play(-1)  # loops indefinitely
        # background_audio = pg.mixer.music.set_volume(self.volume)  # scale of 0->1

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # Set up map for new game, test game, or loaded game

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
            """
             Adjusts player position based on collision with n tile.
            :param rect:
            :param movement:
            :param tiles:
            :return:
            """

            tile_collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
            rect.x += movement[0]
            self.player_x = rect.x
            self.player_position[0] = rect.x
            hit_list = tile_collision_test(rect, tiles)
            for tile in hit_list:

                if movement[0] > 0:
                    rect.right = tile.left
                    tile_collision_types['right'] = True

                elif movement[0] < 0:
                    rect.left = tile.right
                    tile_collision_types['left'] = True

            rect.y += movement[1]
            self.player_y = rect.y
            self.player_position[1] = rect.y
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
            #####  Dungeon Adventure Gui runs while: game is not paused, game is 'playing'.  #####

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

            # Item collisions
            for item in self.__items:
                if self.player_rect.colliderect(item.get_item_rect()):
                    if item.get_item_name() == "Fire Trap":
                        self.__player_character.damage(1)
                    else:
                        self.__player_character.add_to_backpack(item)
                        self.__items.remove(item)

            # Pillar collision. When player collides with pillar, the Trivia UI opens with the corresponding category of question..=
            for pillar in self.__pillars:
                pillar_rect = pillar.get_pillar_rect()
                if self.player_rect.colliderect(pillar_rect):
                    if pillar == self.__abstraction_pillar:
                        # prompt Astronomy trivia
                        self.trivia_ui = TriviaUI(self, "Abstraction")
                    elif pillar == self.__encapsulation_pillar:
                        # prompt Elapid trivia
                        self.trivia_ui = TriviaUI(self, "Encapsulation")
                    elif pillar == self.__inheritance_pillar:
                        # prompt International trivia
                        self.trivia_ui = TriviaUI(self, "Inheritance")
                    elif pillar == self.__polymorphism_pillar:
                        # prompt Pokemon trivia
                        self.trivia_ui = TriviaUI(self, "Polymorphism")
                    self.paused = True
                    self.current_menu = self.trivia_ui

            # If players' hit points hit 0, game pauses and opens "game over" menu. This can go here or in the item collision loop upon collision with the fire trap..
            if self.__player_character.get_death() == True:
                self.paused = True
                self.current_menu = self.game_over

            # Update Sprites for Player

            # set players movement to 0,0
            # update player movement based on user input

            self.player_movement = [0, 0]
            if self.moving_east:
                self.player_movement[0] += 2

                self.player_image_current = self.player_image_east
                # self.player_image_current = pg.transform.scale(pg.image.load(a.east_priestess), self.player_img_size)  # self.player_image_east

            if self.moving_west:
                self.player_movement[0] -= 2
                self.player_image_current = self.player_image_west # self.player_image_west  #

            if self.moving_north:
                self.player_movement[1] -= 2
                self.player_image_current = self.player_image_north  # pg.transform.scale(pg.image.load(a.north_priestess), self.player_img_size)

            if self.moving_south:
                self.player_movement[1] += 2
                self.player_image_current = self.player_image_south  # pg.transform.scale(pg.image.load(a.south_priestess), self.player_img_size)

            # adjust player position based on collision with n tiles

            self.player_rect, collisions = move(self.player_rect, self.player_movement, tile_rects)

            self.display.blit(self.player_image_current,
                              (self.player_rect.x - self.camera_scroll[0], self.player_rect.y - self.camera_scroll[1]))

            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

            # Update the sprites for the monsters

            for monster in self.__monsters:
                ##### For monster in list of monsters, get monster rect, get monster position, calculate monster's
                # path to the player, update monster position based on path to the player. #####
                if monster.get_death() is True:
                    self.__monsters.remove(monster)
                monster.set_monster_goal(self.player_rect)  # Setting monsters goal to player position
                monster.set_player_scroll(self.camera_scroll)  # adjusting for camera scroll
                # pathfinder.draw_path(self.display, self.camera_scroll)  # Drawing the path visually, not necessary in gameplay
                pathfinder.update(monster)  # Updating the monster's path based on player position
                rect = monster.get_character_rect()  # Get the monster's rect to move
                monster.update()  # Update the monsters position based on the above path

                if self.player_rect.colliderect(monster.get_character_rect()):
                    self.paused = True
                    self.set_monster(monster)
                    self.__combat_ui = Combat(self)
                    self.attack_menu = AttackMenu(self)
                    self.current_menu = self.__combat_ui

                self.display.blit(pg.image.load(monster.get_sprite_current()), (
                    rect.x - self.camera_scroll[0], rect.y - self.camera_scroll[1]))  # Draws monster to screen

            for item in self.__items:
                item.set_player_scroll(self.camera_scroll)
                rect = item.get_item_rect()
                if item.get_item_name() == "Health Potion":
                    self.display.blit(pg.image.load(item.get_health_potion_sprite()),
                                      (rect.x - self.camera_scroll[0], rect.y - self.camera_scroll[1]))
                elif item.get_item_name() == "Fire Trap":
                    self.display.blit(pg.image.load(item.get_fire_trap_sprite()),
                                      (rect.x - self.camera_scroll[0], rect.y - self.camera_scroll[1]))

            for pillar in self.__pillars:
                pillar.set_player_scroll(self.camera_scroll)
                rect = pillar.get_pillar_rect()
                if pillar == self.__abstraction_pillar:
                    self.display.blit(pillar.get_abstraction_sprite(),
                                      (rect.x - self.camera_scroll[0], rect.y - self.camera_scroll[1]))
                elif pillar == self.__encapsulation_pillar:
                    self.display.blit(pillar.get_encapsulation_sprite(),
                                      (rect.x - self.camera_scroll[0], rect.y - self.camera_scroll[1]))
                elif pillar == self.__inheritance_pillar:
                    self.display.blit(pillar.get_inheritance_sprite(),
                                      (rect.x - self.camera_scroll[0], rect.y - self.camera_scroll[1]))
                elif pillar == self.__polymorphism_pillar:
                    self.display.blit(pillar.get_polymorphism_sprite(),
                                      (rect.x - self.camera_scroll[0], rect.y - self.camera_scroll[1]))

            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

            # Create the Heads-up Display, draw it to the screen, update it with player stats dynamically

            # test health for HUD

            # Drawing the HUDisplay
            pg.draw.rect(self.display, 'black', pg.Rect(0, 0, 140, 90))  # outside background
            pg.draw.rect(self.display, 'darkslategray', pg.Rect(5, 5, 130, 80))  # inside background

            # Setup Health
            self.draw_text(c.system_font, f'Health: ', 10, 55, 30, c.BLACK)
            self.draw_text(c.system_font, f'{self.__player_character.get_current_hit_points()}', 10, 120, 30, 'red')

            # Setup Pillars
            self.draw_text(c.system_font, f'Pillars: {len(self.__player_character.get_player_pillars())}', 10, 55, 60,
                           c.BLACK)

            # Winning condition
            if len(self.__player_character.get_player_pillars()) == 4:
                self.current_menu = self.victory_screen
                self.paused = True

            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

            # Draw the Gui to the screen, update it
            window_surface = pg.transform.scale(self.display, self.WINDOW_SIZE)
            self.screen.blit(window_surface, (0, 0))

            pg.display.update()  # Update the Display
            clock.tick(60)  # set the FPS

    def check_events(self):
        """
         Receive user input from Mouse x Keyboard.
        :return:
        """

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
                    # print("Interacting!")

                if event.key == K_p:
                    self.paused = True
                    # print("The game is paused")
                    self.current_menu = self.pause_menu

                if event.key == K_h:
                    self.__player_character.drink_health_potion()

                if event.key == K_RETURN:
                    self.interacting = True
                    # print("option selected")

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
        """
         Simple helper-function used to write text to the GUI.
        :param font:
        :param text:
        :param size:
        :param x:
        :param y:
        :param font_color:
        :return:
        """

        pg.font.init()
        font = pg.font.Font(font, size)
        text_surface = font.render(text, True, font_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x / 2, y / 2)
        self.display.blit(text_surface, text_rect)

        # Create the map for visuals, create the matrix for monsters
        # Map 20w x 15h

        # self.__dungeon_map = load_new_map()



    def load_game(self):
        """
        Pickling cannot pickle png objects. So character sprites must be re-loaded.
        :return:
        """
        if os.path.isfile("./save_files/attributes_dict.pkl"):

            with open('./save_files/attributes_dict.pkl', 'rb') as f:
                attributes = pickle.load(f)

            self.trivia_ui = attributes['trivia_ui']
            self.player_position = attributes['player_position']
            self.player_rect = attributes['player_rect']
            self.__player_character = attributes['player_character']
            self.set_player_images((self.__player_character.get_sprite_north(), self.get_player_img_size()),
                                                              (self.__player_character.get_sprite_east(), self.get_player_img_size()),
                                                              (self.__player_character.get_sprite_west(), self.get_player_img_size()),
                                                              (self.__player_character.get_sprite_south(), self.get_player_img_size()))

            self.__pillars = attributes['pillars']
            self.__items = attributes['items']
            self.__monsters = attributes['monsters']



        # if os.path.exists("dungeon_adventure.pickle"):
        #     with open("dungeon_adventure.pickle", "rb") as f:
        #         game_data = pickle.load(f)[0]
        #     self.__player_character = game_data["player_character"]
        #     self.player_position = game_data['player_position']
        #     self.player_rect = game_data['player_rect']
        #     self.__monsters = game_data['monsters']
        #     self.__items = game_data['items']
        #     self.__pillars = game_data['pillars']
        #     for monster in self.__monsters:
        #         if monster.get_type() == "Gremlin":
        #             monster.set_sprite_south(pg.image.load(a.south_gremlin))
        #             monster.set_sprite_north(pg.image.load(a.north_gremlin))
        #             monster.set_sprite_east(pg.image.load(a.east_gremlin))
        #             monster.set_sprite_west(pg.image.load(a.west_gremlin))
        #             monster.set_sprite_current(pg.image.load(a.south_gremlin))
        #
        #         elif monster.get_type() == "Skeleton":
        #             monster.set_sprite_south(pg.image.load(a.south_skelly))
        #             monster.set_sprite_north(pg.image.load(a.north_skelly))
        #             monster.set_sprite_east(pg.image.load(a.east_skelly))
        #             monster.set_sprite_west(pg.image.load(a.west_skelly))
        #             monster.set_sprite_current(pg.image.load(a.south_skelly))
        #
        #         elif monster.get_type() == "Ogre":
        #             monster.set_sprite_south(pg.image.load(a.south_ogre))
        #             monster.set_sprite_north(pg.image.load(a.north_ogre))
        #             monster.set_sprite_east(pg.image.load(a.east_ogre))
        #             monster.set_sprite_west(pg.image.load(a.west_ogre))
        #             monster.set_sprite_current(pg.image.load(a.south_ogre))
        #
        #     for pillar in self.__pillars:
        #         if pillar.get_pillar_name() == "Abstraction":
        #             pillar.set_abstraction_sprite(pg.image.load(a.abstraction_pillar))
        #         elif pillar.get_pillar_name() == "Encapsulation":
        #             pillar.set_encapsulation_sprite(pg.image.load(a.encapsulation_pillar))
        #         elif pillar.get_pillar_name() == "Inheritance":
        #             pillar.set_inheritance_sprite(pg.image.load(a.inheritance_pillar))
        #         elif pillar.get_pillar_name() == "Polymorphism":
        #             pillar.set_polymorphism_sprite(pg.image.load(a.polymorphism_pillar))
        #
        #     for item in self.__items:
        #         if item.get_item_name() == "Health Potion":
        #             item.set_health_potion_sprite(pg.image.load(a.health_potion))
        #         elif item.get_item_name() == "Fire Trap":
        #             item.set_fire_trap_sprite(pg.image.load(a.fire_trap))
        #
        #     if isinstance(self.__player_character, Knight):
        #         self.__player_character.set_character_sprites(a.north_knight,
        #                                                       a.east_knight,
        #                                                       a.west_knight,
        #                                                       a.south_knight)
        #             # pg.image.load(a.north_knight),
        #             # pg.image.load(a.east_knight),
        #             # pg.image.load(a.west_knight),
        #             # pg.image.load(a.south_knight)
        #         # )
        #     elif isinstance(self.__player_character, Priestess):
        #         self.__player_character.set_character_sprites((a.north_priestess,
        #                                                       a.east_priestess,
        #                                                       a.west_priestess,
        #                                                       a.south_priestess)
        #             # pg.image.load(a.north_priestess),
        #             # pg.image.load(a.east_priestess),
        #             # pg.image.load(a.west_priestess),
        #             # pg.image.load(a.south_priestess)
        #         )
        #     elif isinstance(self.__player_character, Rogue):
        #         self.__player_character.set_character_sprites((a.north_rogue,
        #                                                       a.east_rogue,
        #                                                       a.west_rogue,
        #                                                       a.south_rogue)
        #             # pg.image.load(a.north_rogue),
        #             # pg.image.load(a.east_rogue),
        #             # pg.image.load(a.west_rogue),
        #             # pg.image.load(a.south_rogue)
        #         )
        #     self.set_player_images((self.__player_character.get_sprite_north(), self.get_player_img_size()),
        #                            (self.__player_character.get_sprite_east(), self.get_player_img_size()),
        #                            (self.__player_character.get_sprite_west(), self.get_player_img_size()),
        #                            (self.__player_character.get_sprite_south(), self.get_player_img_size())
        #                            )
        #     # # self.set_item_sprites(self.__health_potion.get_health_potion_sprite(), self.__fire_trap.get_fire_trap_sprite())
        #     # self.set_pillar_sprites(self.__abstraction_pillar.get_abstraction_sprite(),
        #     #                         self.__encapsulation_pillar.get_encapsulation_sprite(),
        #     #                         self.__inheritance_pillar.get_inheritance_sprite(),
        #     #                         self.__polymorphism_pillar.get_polymorphism_sprite())
        #     # self.character_select.set_menu_images(pg.transform.scale(self.character_select.knight_image, (c.WIN_WIDTH / 8, c.WIN_HEIGHT / 4)),
        #     #                                       pg.transform.scale(self.character_select.priestess_image, (c.WIN_WIDTH / 8, c.WIN_HEIGHT / 4)),
        #     #                                       pg.transform.scale(self.character_select.rogue_image, (c.WIN_WIDTH / 8, c.WIN_HEIGHT / 4)))
        #     # self.trivia_ui = TriviaUI(self, self.__player_character.get_player_pillars()[-1])
        #     # self.trivia_ui.set_trivia_ui_images(Pillar("Abstraction").get_abstraction_sprite(),
        #     #                                     Pillar("Encapsulation").get_encapsulation_sprite(),
        #     #                                     Pillar("Inheritance").get_inheritance_sprite(),
        #     #                                     Pillar("Polymorphism").get_polymorphism_sprite())



    @staticmethod
    def load_new_map():
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


    @staticmethod
    def load_saved_map():
        saved_maze = pickle.load(open('./save_files/saved_dungeon_map.pkl', 'rb'))
        saved_maze = saved_maze.split('\n')
        dungeon_map = []
        for row in saved_maze:
            dungeon_map.append((list(row)))
        return dungeon_map

    def set_dungeon_map(self, dungeon_map):
        self.__dungeon_map = dungeon_map

    def get_dungeon_map(self):
        return self.__dungeon_map

    # def testing_game(self):
    #     self.__dungeon_map = open('test_maze.txt', 'r')

    def set_loaded_game(self, value):
        self.__loaded_game = value

    def place_monsters(self):
        monster = MonsterFactory().choose_monster()
        monster.set_position(
            self.coords_generator.get_random_coords())  # Set monster initial position to random coords
        monster_x, monster_y = monster.get_position()
        monster.set_character_rect(monster_x, monster_y)
        self.__monsters.append(monster)

    def get_items_list(self):
        return self.__items

    def add_to_backpack(self, object):
        self.__player_character.add_to_backpack(object)

    def set_monster(self, monster):
        self.__monster = monster

    def get_monster(self):
        return self.__monster

    def get_monster_count(self):
        return self.__monster_count

    def set_monster_count(self, count):
        self.__monster_count = count

    def get_monsters_list(self):
        return self.__monsters

    def get_combat_ui(self):
        return self.__combat_ui

    def reset_game(self):
        self.__dungeon_map = None
        self.__loaded_game = None

        # Player setup
        # Player sprite setup, camera scrolling setup
        self.__player_character = None
        self.player_movement = [0, 0]
        self.camera_scroll = [0, 0]
        self.player_direction = 0

        self.coords_generator = ValidCoordsGenerator()
        self.coords_generator.generate_coords()

        self.player_position = [16, 16]  # self.coords_generator.get_random_coords()
        self.player_x, self.player_y = self.player_position

        self.player_img_size = (14, 14)

        self.player_image_current = None  # pg.transform.scale(pg.image.load(a.south_priestess), self.player_img_size)
        self.player_image_north = None
        self.player_image_south = None
        self.player_image_east = None
        self.player_image_west = None

        self.player_rect = None  # pg.Rect(self.player_x, self.player_y, self.player_image_current.get_width(),
        #      self.player_image_current.get_height())  # start at 16, add 48 x or y for good position

        # Monster setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.__monsters = []
        self.__monster_count = 5

        # Place/spawn monsters
        for _ in range(self.get_monster_count()):
            self.place_monsters()

        # Item setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.__health_potion = Item("Health Potion")
        self.__fire_trap = Item("Fire Trap")
        self.i_factory = item_factory.ItemFactory()
        self.__items = []
        self.__item_count = 10

        # Place/spawn items
        for item in range(self.__item_count):
            item = self.i_factory.choose_item()
            self.place_items(item)

        # Pillar setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.__abstraction_pillar = Pillar("Abstraction")
        self.__encapsulation_pillar = Pillar("Encapsulation")
        self.__inheritance_pillar = Pillar("Inheritance")
        self.__polymorphism_pillar = Pillar("Polymorphism")
        self.__pillars = [self.__abstraction_pillar, self.__encapsulation_pillar, self.__inheritance_pillar,
                          self.__polymorphism_pillar]

        # Place/spawn pillars
        for pillar in self.__pillars:
            self.place_pillar(pillar)

        # Controls
        self.moving_east, self.moving_west, self.moving_north, self.moving_south = False, False, False, False
        self.interacting, self.left_clicked, self.escaping = False, False, False

        # Game Status
        self.running, self.playing, self.paused = True, False, False

    def set_player_position(self, position):
        self.player_position = position
        self.player_x, self.player_y = position
        self.set_player_rect()

    def get_player_rect(self):
        return self.player_rect

    def set_item_sprites(self, param1, param2):
        """
        Setter for item sprites, especially for saving (set to None) and loading (set to pg.image.load(a.<image>))
        :param param1:
        :param param2:
        :return:
        """

        Item("Health Potion").set_health_potion_sprite(param1)
        Item("Fire Trap").set_fire_trap_sprite(param2)
        self.__health_potion.set_health_potion_sprite(param1)
        self.__fire_trap.set_fire_trap_sprite(param2)

    def set_pillar_sprites(self, param1, param2, param3, param4):
        """
        Setter for pillar sprites, especially for saving (set to None) and loading (set to pg.image.load(a.<image>))
        :param param1:
        :param param2:
        :param param3:
        :param param4:
        :return:
        """

        self.__abstraction_pillar.set_abstraction_sprite(param1)
        self.__encapsulation_pillar.set_encapsulation_sprite(param2)
        self.__inheritance_pillar.set_inheritance_sprite(param3)
        self.__polymorphism_pillar.set_polymorphism_sprite(param4)




if __name__ == "__main__":
    databases = initialize_databases.main()
    main = DungeonAdventure()
    main.game_loop()
    SaveGame.pickle(main)
