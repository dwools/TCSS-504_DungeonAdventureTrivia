import os
import textwrap

import pygame as pg
import sys
import pygame.display

from Gameplay import config as c
from Assets import assets as a
from Pillars_and_Trivia.pillar import Pillar
from Pillars_and_Trivia.trivia_factory import TriviaFactory
from Gameplay.save_game import SaveGame

from Characters.hero_factory import HeroFactory
from Room_and_Maze.maze import Maze


class Menu:
    """
    Super class of Menu hierarchy.
    """

    def __init__(self, game):
        self.game = game
        self.middle_width, self.middle_height = c.WIN_WIDTH / 2, c.WIN_HEIGHT / 2
        self.run_display = True
        self.screen = pg.display.set_mode(c.WINDOW_SIZE, 0, 32)

        # Making the little star next to buttons
        self.cursor_rect = pg.Rect(0, 0, 20, 20)
        self.cursor_offset = - 350
        # Mouse Configuration
        self.mouse_position = pg.mouse.get_pos()

    def draw_cursor(self):
        # Draw the pointer next to the buttons
        self.game.draw_text(c.dungeon_font, '*', 15, self.cursor_rect.x, self.cursor_rect.y, 'red')

    def blit_screen(self):
        # draw to / update the GUI
        window_surface = pg.transform.scale(self.game.display, c.WINDOW_SIZE)
        self.screen.blit(window_surface, (0, 0))
        pg.display.update()  # Update the Display


class MainMenu(Menu):
    """
     Main Menu Class.
        Displays the main menu and leads to the other menus
    """

    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start Game"
        self.start_x, self.start_y = self.middle_width, self.middle_height - 100
        self.how_to_play_x, self.how_to_play_y = self.middle_width, self.middle_height
        self.load_game_x, self.load_game_y = self.middle_width, self.middle_height + 100
        self.options_x, self.options_y = self.middle_width, self.middle_height + 200
        self.credits_x, self.credits_y = self.middle_width, self.middle_height + 300
        self.cursor_rect.midtop = (self.start_x + self.cursor_offset, self.start_y)

    def display_menu(self):
        self.run_display = True
        clock = pg.time.Clock()
        while self.run_display:
            self.game.check_events()
            self.check_input()

            self.game.display.fill(c.PURPLE)
            self.game.menu_font_color = c.WHITE

            self.game.draw_text(c.dungeon_font, 'Dungeon Adventure', 20, self.middle_width, self.middle_height - 250,
                                'forestgreen')
            self.game.draw_text(c.dungeon_font, 'Start Game', 20, self.start_x, self.start_y, self.game.menu_font_color)
            self.game.draw_text(c.dungeon_font, 'How To Play', 20, self.how_to_play_x, self.how_to_play_y,
                                self.game.menu_font_color)
            self.game.draw_text(c.dungeon_font, 'Load Save', 20, self.load_game_x, self.load_game_y,
                                self.game.menu_font_color)
            self.game.draw_text(c.dungeon_font, 'Options', 20, self.options_x, self.options_y,
                                self.game.menu_font_color)
            self.game.draw_text(c.dungeon_font, 'Credits', 20, self.credits_x, self.credits_y,
                                self.game.menu_font_color)
            self.draw_cursor()
            self.blit_screen()
            clock.tick(12)

    def move_cursor(self):
        """ Adjust cursor position to notify user of their current choice / button.
            Does a full loop through the menu allowing north and south traversal.
        """

        if self.game.moving_south:
            if self.state == 'Start Game':
                self.cursor_rect.midtop = (self.how_to_play_x + self.cursor_offset, self.how_to_play_y)
                self.state = 'How To Play'

            elif self.state == 'How To Play':
                self.cursor_rect.midtop = (self.load_game_x + self.cursor_offset, self.load_game_y)
                self.state = 'Load Game'

            elif self.state == 'Load Game':
                self.cursor_rect.midtop = (self.options_x + self.cursor_offset, self.options_y)
                self.state = 'Options'

            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.credits_x + self.cursor_offset, self.credits_y)
                self.state = 'Credits'

            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.start_x + self.cursor_offset, self.start_y)
                self.state = 'Start Game'

        elif self.game.moving_north:
            if self.state == 'Start Game':
                self.cursor_rect.midtop = (self.credits_x + self.cursor_offset, self.credits_y)
                self.state = 'Credits'

            elif self.state == 'How To Play':
                self.cursor_rect.midtop = (self.start_x + self.cursor_offset, self.start_y)
                self.state = 'Start Game'

            elif self.state == 'Load Game':
                self.cursor_rect.midtop = (self.how_to_play_x + self.cursor_offset, self.how_to_play_y)
                self.state = 'How To Play'

            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.load_game_x + self.cursor_offset, self.load_game_y)
                self.state = 'Load Game'

            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.options_x + self.cursor_offset, self.options_y)
                self.state = 'Options'

    def check_input(self):
        """
        Check which menu the user is selecting based on cursor position. Then if user interacts, 'open' that menu.
        Selecting 'Start Game' generates a new maze.
        Selecting "How To Play" displays gameplay instructions.
        Selecting "Load Game" sets game's load_game boolean parameter to True to indicate a pickled file of prior saved
        game info should be unpickled and loaded.
        Selecting "Credits" displays the names of the computer-savy herpetologists responsible for the presented marvel
        of entertainment.
        :return:
        """

        self.move_cursor()  # Read cursor position

        if self.game.interacting:  # If user interacts (enter or E) with the cursor's position enter that menu

            if self.state == 'Start Game':
                Maze(15, 20).new_maze()  # create new dungeon.txt file
                self.game.current_menu = self.game.character_select
                # self.game.playing = True

            elif self.state == 'How To Play':
                self.game.current_menu = self.game.how_to_play

            elif self.state == 'Load Game':
                if os.path.isfile('./save_files/attributes_dict.pkl') and os.path.isfile('./save_files/saved_dungeon_map.pkl'):
                    self.game.set_loaded_game(True)
                    self.game.playing = True  # Here is where we enter the saved game
                    # self.run_display = False  # end the current menu screen
                    # self.game.current_menu = self.game.load_games
                else:
                    print("There's no saved map! Time to begin a new herpetology adventure!")
                    Maze(15, 20).new_maze()  # create new dungeon.txt file
                    self.game.current_menu = self.game.character_select

            elif self.state == 'Options':
                self.game.current_menu = self.game.options

            elif self.state == 'Credits':
                self.game.current_menu = self.game.credits

            self.run_display = False


class CharacterSelectMenu(Menu):
    """Select the Hero class player character."""

    def __init__(self, game):
        Menu.__init__(self, game)
        # The Knight
        self.state = "Knight"  # Base state
        self.select_knight_x, self.select_knight_y = self.middle_width + 50, self.middle_height + 300
        self.knight_image = pg.image.load(a.south_knight)

        # The Priestess
        self.select_priestess_x, self.select_priestess_y = self.middle_width - 350, self.middle_height + 300
        self.priestess_image = pg.image.load(a.south_priestess)

        # The Rogue
        self.select_rogue_x, self.select_rogue_y = self.middle_width + 400, self.middle_height + 300
        self.rogue_image = pg.image.load(a.south_rogue)  # Change to Roque image

        # Placing the cursor at the Base State
        self.cursor_rect.midtop = (self.select_knight_x - 125, self.select_knight_y)

    def display_menu(self):
        self.run_display = True
        clock = pg.time.Clock()

        while self.run_display:
            self.game.interacting = False
            self.game.display.fill(c.PURPLE)

            self.game.check_events()
            self.check_input()

            # Title
            self.game.draw_text(c.dungeon_font, 'Character Select', 30, self.middle_width, self.middle_height - 300,
                                'forestgreen')

            # Line Separators
            pg.draw.rect(self.screen, 'gray', pg.Rect(self.select_knight_x + 150, self.select_knight_y - 550, 10, 550))
            pg.draw.rect(self.screen, 'gray', pg.Rect(self.select_knight_x - 225, self.select_knight_y - 550, 10, 550))

            # Knight
            self.game.draw_text(c.dungeon_font, 'Knight', 15, self.select_knight_x - 25, self.select_knight_y,
                                self.game.menu_font_color)
            self.knight_image = pg.transform.scale(self.knight_image, (c.WIN_WIDTH / 8, c.WIN_HEIGHT / 4))
            self.screen.blit(self.knight_image, (self.select_knight_x - 100, self.select_knight_y - 500))

            # Abilities
            self.game.draw_text(c.dungeon_font, 'Crushing Blow', 12, self.select_knight_x - 25,
                                self.select_knight_y - 200,
                                'forestgreen')
            self.game.draw_text(c.dungeon_font, '40 percent chance', 10, self.select_knight_x - 25,
                                self.select_knight_y - 125,
                                'yellow')
            self.game.draw_text(c.dungeon_font, 'to do', 10, self.select_knight_x - 25, self.select_knight_y - 100,
                                'yellow')
            self.game.draw_text(c.dungeon_font, 'high damage', 10, self.select_knight_x - 25, self.select_knight_y - 75,
                                'yellow')

            # Priestess
            self.game.draw_text(c.dungeon_font, 'Priestess', 15, self.select_priestess_x, self.select_priestess_y,
                                self.game.menu_font_color)
            self.priestess_image = pg.transform.scale(self.priestess_image, (c.WIN_WIDTH / 8, c.WIN_HEIGHT / 4))
            self.screen.blit(self.priestess_image, (self.select_priestess_x - 75, self.select_priestess_y - 500))

            # Abilities
            self.game.draw_text(c.dungeon_font, 'Divine Blessing', 12, self.select_priestess_x,
                                self.select_priestess_y - 200,
                                'forestgreen')
            self.game.draw_text(c.dungeon_font, 'Heal a', 10, self.select_priestess_x, self.select_priestess_y - 125,
                                'yellow')
            self.game.draw_text(c.dungeon_font, 'random amount', 10, self.select_priestess_x,
                                self.select_priestess_y - 100, 'yellow')

            # Rogue
            self.game.draw_text(c.dungeon_font, 'Rogue', 15, self.select_rogue_x, self.select_rogue_y,
                                self.game.menu_font_color)
            self.rogue_image = pg.transform.scale(self.rogue_image, (c.WIN_WIDTH / 8, c.WIN_HEIGHT / 4))
            self.screen.blit(self.rogue_image, (self.select_rogue_x - 75, self.select_rogue_y - 500))

            # Abilities
            self.game.draw_text(c.dungeon_font, 'Surprise Attack', 12, self.select_rogue_x, self.select_rogue_y - 200,
                                'forestgreen')
            self.game.draw_text(c.dungeon_font, '40 percent chance', 10, self.select_rogue_x, self.select_rogue_y - 125,
                                'yellow')
            self.game.draw_text(c.dungeon_font, 'to do a', 10, self.select_rogue_x, self.select_rogue_y - 100, 'yellow')
            self.game.draw_text(c.dungeon_font, 'second attack', 10, self.select_rogue_x, self.select_rogue_y - 75,
                                'yellow')

            # Return to Main Menu prompt
            self.game.draw_text(c.dungeon_font, 'Press ESCAPE to go to the main menu', 10, self.middle_width,
                                self.middle_height + 400,
                                'yellow')

            self.draw_cursor()
            pygame.display.update()

            window_surface = pg.transform.scale(self.game.display, c.WINDOW_SIZE)
            self.screen.blit(window_surface, (0, 0))
            clock.tick(12)

    def move_cursor(self):

        if self.game.moving_east:
            if self.state == 'Knight':
                self.cursor_rect.midtop = (self.select_rogue_x - 100, self.select_rogue_y)
                self.state = 'Rogue'

            elif self.state == 'Rogue':
                self.cursor_rect.midtop = (self.select_priestess_x - 150, self.select_priestess_y)
                self.state = 'Priestess'

            elif self.state == 'Priestess':
                self.cursor_rect.midtop = (self.select_knight_x - 125, self.select_knight_y)
                self.state = 'Knight'

        elif self.game.moving_west:
            if self.state == 'Knight':
                self.cursor_rect.midtop = (self.select_priestess_x - 150, self.select_priestess_y)
                self.state = 'Priestess'

            elif self.state == 'Priestess':
                self.cursor_rect.midtop = (self.select_rogue_x - 100, self.select_rogue_y)
                self.state = 'Rogue'

            elif self.state == 'Rogue':
                self.cursor_rect.midtop = (self.select_knight_x - 125, self.select_knight_y)
                self.state = 'Knight'

    def check_input(self):
        """
         Check which menu the user is selecting based on cursor position. Then if user interacts, 'open' that menu.
        Instantiate an object of the respective character's class using HeroFactory and assign its appropriate sprites
        and set the player rectangle. Then initiate gameplay.
        :return:
        """

        self.move_cursor()  # Read cursor position

        if self.game.escaping:
            self.game.current_menu = self.game.main_menu
            self.run_display = False

        if self.game.interacting:  # If user interacts (enter or E) with the cursor's position enter that menu

            if self.state == 'Knight':
                self.game.set_player_character(HeroFactory().create_knight())

            elif self.state == 'Priestess':
                self.game.set_player_character(HeroFactory().create_priestess())

            elif self.state == 'Rogue':
                self.game.set_player_character(HeroFactory().create_rogue())

            player = self.game.get_player_character()

            self.game.set_player_images((player.get_sprite_north(), self.game.get_player_img_size()),
                                        (player.get_sprite_east(), self.game.get_player_img_size()),
                                        (player.get_sprite_west(), self.game.get_player_img_size()),
                                        (player.get_sprite_south(), self.game.get_player_img_size())
                                        )
            # self.game.set_player_images(pg.transform.scale(player.get_sprite_north(), self.game.get_player_img_size()),
            #                             pg.transform.scale(player.get_sprite_east(), self.game.get_player_img_size()),
            #                             pg.transform.scale(player.get_sprite_west(), self.game.get_player_img_size()),
            #                             pg.transform.scale(player.get_sprite_south(), self.game.get_player_img_size())
            #                             )
            self.game.set_player_rect()
            self.game.playing = True

            self.run_display = False

    def set_menu_images(self, knight_image, priestess_image, rogue_image):
        """
        Setter for menu images, especially for saving (set to None)
        :param param1:
        :param param2:
        :param param3:
        :return:
        """

        self.knight_image = knight_image
        self.priestess_image = priestess_image
        self.rogue_image = rogue_image

class HowToPlayMenu(Menu):

    def __init__(self, game):
        Menu.__init__(self, game)
        self.how_to_play_x, self.how_to_play_y = self.middle_width, self.middle_height - 200
        self.text_x, self.text_y = self.middle_width, self.middle_height

    def display_menu(self):
        self.run_display = True
        clock = pg.time.Clock()

        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.text_y = self.middle_height - 150

            self.game.display.fill(c.PURPLE)
            self.game.draw_text(c.dungeon_font, 'How To Play', 20, self.middle_width, self.middle_height - 250,
                                'forestgreen')

            text = 'Use WASD or Arrow keys to move your character and navigate menus. \nPress H to use a health potion. Press P to pause the game. \nPick up all four pillars to win the game. Avoid monsters and fire.'
            wrapped_text = textwrap.wrap(text, 35)

            for line in wrapped_text:
                self.draw_wrapped_text(line, 20, self.text_x, self.text_y, c.WHITE)
                self.text_y += 50

            self.game.draw_text(c.dungeon_font, 'Press ESCAPE to go to the main menu', 10, self.middle_width,
                                self.middle_height + 250,
                                'yellow')

            self.blit_screen()
            clock.tick(12)

    def draw_wrapped_text(self, text, size, x, y, font_color):
        """
         Simple helper-function used to write text to the GUI.
        :param text:
        :param size:
        :param x:
        :param y:
        :param font_color:
        :return:
        """
        # pg.font.init()
        font = pg.font.Font(c.system_font, size)
        text_surface = font.render(text, True, font_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x / 2, y / 2)
        self.game.display.blit(text_surface, text_rect)

    def check_input(self):

        if self.game.escaping:
            self.game.current_menu = self.game.main_menu
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

        self.state = 'Volume'
        self.volume_x, self.volume_y = self.middle_width, self.middle_height + 20
        self.difficulty_x, self.difficulty_y = self.middle_width, self.middle_height + 120

        self.cursor_rect.midtop = (self.volume_x + self.cursor_offset, self.volume_y)

    def display_menu(self):
        clock = pg.time.Clock()
        self.run_display = True

        while self.run_display:
            self.game.check_events()
            self.check_input()

            self.game.display.fill(c.PURPLE)
            self.game.draw_text(c.dungeon_font, 'Options', 30, self.middle_width, self.middle_height - 120,
                                'forestgreen')
            self.game.draw_text(c.dungeon_font, 'Volume', 20, self.volume_x, self.volume_y, self.game.menu_font_color)
            self.game.draw_text(c.system_font, f'{self.game.get_volume()}', 12, self.volume_x, self.volume_y + 50,
                                self.game.menu_font_color)

            self.game.draw_text(c.dungeon_font, 'Difficulty', 20, self.difficulty_x, self.difficulty_y,
                                self.game.menu_font_color)
            self.game.draw_text(c.system_font, f'Monster Count: {self.game.get_monster_count()}', 12, self.difficulty_x,
                                self.difficulty_y + 50,
                                self.game.menu_font_color)
            self.game.draw_text(c.system_font, 'difficulty settings are non-functional', 10, self.difficulty_x,
                                self.difficulty_y + 300,
                                'yellow')

            self.game.draw_text(c.dungeon_font, 'Press ESCAPE to go to the main menu', 10, self.middle_width,
                                self.middle_height + 250,
                                'yellow')
            self.draw_cursor()

            self.blit_screen()

            clock.tick(12)

    def check_input(self):

        self.move_cursor()

        if self.game.paused:
            if self.game.escaping:
                self.game.current_menu = self.game.pause_menu
                self.run_display = False

        if self.game.escaping and not self.game.paused:
            self.game.current_menu = self.game.main_menu
            self.run_display = False

        if self.state == 'Volume':  # Volume
            if self.game.moving_east:
                self.game.set_volume(self.game.get_volume() + 0.1)
                if self.game.get_volume() > 1.0:
                    self.game.set_volume(1.0)
            elif self.game.moving_west:
                self.game.set_volume(self.game.get_volume() - 0.1)
                if self.game.get_volume() < 0.0:
                    self.game.set_volume(0.0)

        if self.state == 'Difficulty':  # Difficulty
            if self.game.moving_east:
                self.game.set_monster_count(self.game.get_monster_count() + 1)
                if self.game.get_monster_count() > 25:
                    self.game.set_monster_count(25)
            elif self.game.moving_west:
                self.game.set_monster_count(self.game.get_monster_count() - 1)
                if self.game.get_monster_count() < 0:
                    self.game.set_monster_count(0)

    def move_cursor(self):
        """
        Adjust cursor position to notify user of their current choice / button.
            Does a full loop through the menu allowing north and south traversal.
        :return:
        """

        if self.game.moving_south:
            if self.state == 'Volume':
                self.cursor_rect.midtop = (self.difficulty_x + self.cursor_offset, self.difficulty_y)
                self.state = 'Difficulty'

            elif self.state == 'Difficulty':
                self.cursor_rect.midtop = (self.volume_x + self.cursor_offset, self.volume_y)
                self.state = 'Volume'

        elif self.game.moving_north:
            if self.state == 'Volume':
                self.cursor_rect.midtop = (self.difficulty_x + self.cursor_offset, self.difficulty_y)
                self.state = 'Difficulty'

            elif self.state == 'Difficulty':
                self.cursor_rect.midtop = (self.volume_x + self.cursor_offset, self.volume_y)
                self.state = 'Volume'


class CreditsMenu(Menu):
    # Needs to be able to go back to main menu
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):

        self.run_display = True

        while self.run_display:

            clock = pg.time.Clock()

            self.game.check_events()

            if self.game.escaping:
                self.game.current_menu = self.game.main_menu
                self.run_display = False

            self.game.display.fill(c.PURPLE)
            self.game.draw_text(c.dungeon_font, 'Credits', 30, self.middle_width, self.middle_height - 200,
                                'forestgreen')
            self.game.draw_text(c.dungeon_font, 'Made by', 20, self.middle_width, self.middle_height - 50,
                                self.game.menu_font_color)
            self.game.draw_text(c.dungeon_font, 'Sanya Sinha', 15, self.middle_width, self.middle_height + 50, 'teal')
            self.game.draw_text(c.dungeon_font, 'David Woolston', 15, self.middle_width, self.middle_height + 100,
                                'blue')
            self.game.draw_text(c.dungeon_font, 'Jackson Davis', 15, self.middle_width, self.middle_height + 150,
                                'royalblue')
            self.game.draw_text(c.dungeon_font, 'Press ESCAPE to go to the main menu', 10, self.middle_width,
                                self.middle_height + 300,
                                self.game.menu_font_color)

            self.blit_screen()

            clock.tick(12)


class PauseMenu(Menu):
    """
    Pause menu opened during gameplay with options "Save The Game", "Main Menu", "Options", and "Exit Game"
    """
    # Needs to be able to resume game time
    def __init__(self, game):
        Menu.__init__(self, game)
        self.mouse_position = pg.mouse.get_pos()

        self.state = "Save The Game"

        self.save_game_x, self.save_game_y = self.middle_width, self.middle_height - 50

        self.main_x, self.main_y = self.middle_width, self.middle_height + 50

        self.options_x, self.options_y = self.middle_width, self.middle_height + 150

        self.exit_game_x, self.exit_game_y = self.middle_width, self.middle_height + 250

        # create cursor and set position to save_game
        self.cursor_rect.midtop = (self.save_game_x + self.cursor_offset, self.save_game_y)

    def display_menu(self):

        self.game.paused = True
        self.run_display = True

        while self.game.paused and self.run_display:
            clock = pg.time.Clock()

            self.game.check_events()
            self.check_input()

            self.game.display.fill(c.PURPLE)  # will fill in background

            self.game.draw_text(c.dungeon_font, 'Pause Menu', 30, self.middle_width, self.middle_height - 200,
                                'forestgreen')

            self.game.draw_text(c.dungeon_font, 'Save The Game', 15, self.save_game_x, self.save_game_y,
                                self.game.menu_font_color)
            self.game.draw_text(c.dungeon_font, 'Main Menu', 15, self.main_x, self.main_y, self.game.menu_font_color)
            self.game.draw_text(c.dungeon_font, 'Options', 15, self.options_x, self.options_y,
                                self.game.menu_font_color)
            self.game.draw_text(c.dungeon_font, 'Exit Game', 20, self.exit_game_x, self.exit_game_y, 'red')

            self.game.draw_text(c.dungeon_font, 'Press ESCAPE to resume your game', 10, self.middle_width,
                                self.middle_height + 350,
                                'yellow')

            self.draw_cursor()
            self.blit_screen()

            clock.tick(12)

    def move_cursor(self):

        if self.game.moving_south or self.game.moving_east:
            if self.state == 'Save The Game':
                self.cursor_rect.midtop = (self.main_x + self.cursor_offset, self.main_y)
                self.state = 'Main Menu'

            elif self.state == 'Main Menu':
                self.cursor_rect.midtop = (self.options_x + self.cursor_offset, self.options_y)
                self.state = 'Options'

            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.exit_game_x + self.cursor_offset, self.exit_game_y)
                self.state = 'Exit Game'

            elif self.state == 'Exit Game':
                self.cursor_rect.midtop = (self.save_game_x + self.cursor_offset, self.save_game_y)
                self.state = 'Save The Game'

        elif self.game.moving_north or self.game.moving_west:
            if self.state == 'Save The Game':
                self.cursor_rect.midtop = (self.exit_game_x + self.cursor_offset, self.exit_game_y)
                self.state = 'Exit Game'

            elif self.state == 'Main Menu':
                self.cursor_rect.midtop = (self.save_game_x + self.cursor_offset, self.save_game_y)
                self.state = 'Save The Game'

            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.main_x + self.cursor_offset, self.main_y)
                self.state = 'Main Menu'

            elif self.state == 'Exit Game':
                self.cursor_rect.midtop = (self.options_x + self.cursor_offset, self.options_y)
                self.state = 'Options'

    def check_input(self):
        """
        If "Save the Game" is selected: execute SaveGame()'s save_game() method to pickle dungeon data.
        If "Main Menu" is selected: return to Main Menu.
        If "Options is selected: open Options menu.
        IF "Exit Game" is selected: exit game using pg.quit() and sys.exit().
        :return:
        """

        self.move_cursor()

        if self.game.interacting:

            if self.state == 'Save The Game':
                print("SAVING GAME!")
                # self.set_save_game(True)
                # SaveGame.pickle(self.game)
                SaveGame.save_helper(self.game)
                self.game.interacting = False

            if self.state == 'Main Menu':
                self.game.reset_game()
                self.game.current_menu = MainMenu(self.game)
                self.game.paused = False
                self.game.playing = False
                self.run_display = False
                print("Going to main menu")
                self.game.interacting = False

            if self.state == 'Options':
                self.game.current_menu = OptionsMenu(self.game)
                self.run_display = False
                print("Going to Options Menu")
                self.game.interacting = False

            if self.state == 'Exit Game':
                pg.quit()
                sys.exit()

        if self.game.escaping:
            self.game.paused = False
            self.run_display = False


class TriviaUI(Menu):
    """
    Displays trivia question corresponding to the theme of the given pillar.
    """
    def __init__(self, game, pillar):
        Menu.__init__(self, game)
        self.__pillar = self.game.get_pillar(pillar)
        self.state = 'TRUE'
        self.question_font = c.system_font

        self.trivia = TriviaFactory(self.__pillar).create_question()

        self.given_question = textwrap.wrap(self.trivia.get_question(), 55)
        self.answer = self.trivia.get_answer()

        self.title_x, self.title_y = self.middle_width, self.middle_height - 250
        self.question_x, self.question_y = self.middle_width, self.middle_height - 150

        self.true_x, self.true_y = self.middle_width - 150, self.middle_height + 100
        self.false_x, self.false_y = self.middle_width + 150, self.middle_height + 100

        self.cursor_rect.midtop = (self.true_x - 100, self.true_y)

    def display_menu(self):
        self.run_display = True

        while self.run_display:
            self.question_y = self.middle_height - 150
            clock = pg.time.Clock()

            self.game.check_events()
            self.check_input()

            self.game.display.fill(c.PURPLE)

            self.game.draw_text(c.dungeon_font, "Trivia Question", 15, self.title_x, self.title_y, 'teal')

            for line in self.given_question:
                self.draw_question(line, 20, self.question_x, self.question_y, self.game.menu_font_color)
                self.question_y += 50

            self.game.draw_text(c.dungeon_font, "True", 15, self.true_x, self.true_y, 'forestgreen')
            self.game.draw_text(c.dungeon_font, "False", 15, self.false_x, self.false_y, 'darkred')

            self.draw_cursor()

            self.blit_screen()

            clock.tick(12)

    def draw_question(self, text, size, x, y, font_color):
        """
        Simple helper-function used to write text to the GUI.
        :param text:
        :param size:
        :param x:
        :param y:
        :param font_color:
        :return:
        """
        # pg.font.init()
        font = pg.font.Font(self.question_font, size)
        text_surface = font.render(text, True, font_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x / 2, y / 2)
        self.game.display.blit(text_surface, text_rect)

    def move_cursor(self):

        if self.game.moving_east:
            if self.state == 'TRUE':
                self.cursor_rect.midtop = (self.false_x - 100, self.false_y)
                self.state = 'FALSE'

            elif self.state == 'TRUE':
                self.cursor_rect.midtop = (self.true_x - 100, self.true_y)
                self.state = 'FALSE'

        elif self.game.moving_west:
            if self.state == 'TRUE':
                self.cursor_rect.midtop = (self.false_x - 100, self.false_y)
                self.state = 'FALSE'

            elif self.state == 'FALSE':
                self.cursor_rect.midtop = (self.true_x - 100, self.true_y)
                self.state = 'TRUE'

    def set_trivia_ui_images(self, abstraction, encapsulation, inheritance, polymorphism):
        """
        Setter for TriviaUI pillar attribute images, especially for saving (set to None) and loading.
        :param param1:
        :param param2:
        :param param3:
        :param param4:
        :return:
        """
        self.__pillar.set_abstraction_sprite(abstraction)
        self.__pillar.set_encapsulation_sprite(encapsulation)
        self.__pillar.set_inheritance_sprite(inheritance)
        self.__pillar.set_polymorphism_sprite(polymorphism)



    def check_input(self):
        """
         Select "TRUE" or "FALSE" to guess answer to trivia question. If correct, the given pillar is added to
         player's pillar inventory. If incorrect, the pillar relocates to a random position in the maze.
        :return:
        """

        self.move_cursor()  # Read cursor position

        if self.game.interacting:  # If user interacts (enter or E) with the cursor's position enter that menu

            if self.state == 'TRUE':
                print('You have selected True')

            elif self.state == 'FALSE':
                print('You have selected False')

            # if answer == true, add pillar to backpack || else: relocate pillar
            if self.answer == self.state:
                print('You have chosen correctly')  # add pillar to backpack
                self.game.add_to_backpack(Pillar(self.__pillar))
                self.game.remove_pillar(self.__pillar)
            else:
                print(f'You failed! The {self.__pillar.get_pillar_name()} pillar has vanished and appeared elsewhere!')  # relocate pillar
                self.game.place_pillar(self.__pillar)

            self.run_display = False
            self.game.paused = False

            # # if answer == false, add pillar to backpack || else: relocate pillar
            # if self.answer == self.state:
            #     print('You have chosen correctly')  # add pillar to backpack
            # else:
            #     print('you failed')  # relocate pillar
            #
            # self.run_display = False
            # self.game.paused = False

    def get_trivia_category(self):
        return self.__pillar

class GameOver(Menu):
    """
    Menu displayed when player's current_hit_points drops to <= 0.
    """
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Main Menu"
        self.game_over_x, self.game_over_y = self.middle_width, self.middle_height - 200
        self.main_menu_x, self.main_menu_y = self.middle_width, self.middle_height
        self.exit_game_x, self.exit_game_y = self.middle_width, self.middle_height + 100

        self.cursor_rect.midtop = (self.main_menu_x + self.cursor_offset, self.main_menu_y)

    def display_menu(self):
        self.run_display = True

        while self.run_display:
            clock = pg.time.Clock()
            self.check_input()
            self.game.check_events()

            self.game.display.fill(c.PURPLE)
            self.draw_cursor()

            self.game.draw_text(c.dungeon_font, "Game Over", 40, self.game_over_x, self.game_over_y, 'red')
            self.game.draw_text(c.dungeon_font, "Main Menu", 20, self.main_menu_x, self.main_menu_y,
                                self.game.menu_font_color)
            self.game.draw_text(c.dungeon_font, "Exit Game", 20, self.exit_game_x, self.exit_game_y,
                                self.game.menu_font_color)

            self.blit_screen()

            clock.tick(12)

    def move_cursor(self):

        if self.game.moving_south:
            if self.state == 'Main Menu':
                self.cursor_rect.midtop = (self.exit_game_x + self.cursor_offset, self.exit_game_y)
                self.state = 'Exit Game'

            elif self.state == 'Exit Game':
                self.cursor_rect.midtop = (self.main_menu_x + self.cursor_offset, self.main_menu_y)
                self.state = 'Main Menu'

        elif self.game.moving_north:
            if self.state == 'Main Menu':
                self.cursor_rect.midtop = (self.exit_game_x + self.cursor_offset, self.exit_game_y)
                self.state = 'Exit Game'

            elif self.state == 'Exit Game':
                self.cursor_rect.midtop = (self.main_menu_x + self.cursor_offset, self.main_menu_y)
                self.state = 'Main Menu'

    def check_input(self):

        self.move_cursor()

        if self.game.interacting:

            if self.state == 'Main Menu':
                self.game.reset_game()
                self.game.current_menu = MainMenu(self.game)
                self.game.paused = False
                self.game.playing = False
                self.run_display = False
                print("Going to main menu")
                self.game.interacting = False

            if self.state == 'Exit Game':
                pg.quit()
                sys.exit()


class VictoryScreen(Menu):
    """
    Menu displayed when player picks up all four pillars.
    """
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Main Menu"
        self.victory_x, self.victory_y = self.middle_width, self.middle_height - 200
        self.main_menu_x, self.main_menu_y = self.middle_width, self.middle_height
        self.exit_game_x, self.exit_game_y = self.middle_width, self.middle_height + 100

        self.cursor_rect.midtop = (self.main_menu_x - 200, self.main_menu_y)

    def display_menu(self):
        self.run_display = True

        while self.run_display:
            clock = pg.time.Clock()
            self.check_input()
            self.game.check_events()

            self.game.display.fill(c.PURPLE)
            self.draw_cursor()

            bg_image = pg.transform.scale(pg.image.load(a.victory_bg), (700, 500))
            self.game.display.blit(bg_image, (0, 0))

            self.game.draw_text(c.dungeon_font, "V", 40, self.victory_x - 225, self.victory_y, 'red')
            self.game.draw_text(c.dungeon_font, "I", 40, self.victory_x - 150, self.victory_y, 'orange')
            self.game.draw_text(c.dungeon_font, "C", 40, self.victory_x - 75, self.victory_y, 'yellow')
            self.game.draw_text(c.dungeon_font, "T", 40, self.victory_x, self.victory_y, 'green')
            self.game.draw_text(c.dungeon_font, "O", 40, self.victory_x + 75, self.victory_y, 'blue')
            self.game.draw_text(c.dungeon_font, "R", 40, self.victory_x + 150, self.victory_y, 'purple')
            self.game.draw_text(c.dungeon_font, "Y", 40, self.victory_x + 225, self.victory_y, 'violet')

            self.game.draw_text(c.dungeon_font, "Main Menu", 20, self.main_menu_x, self.main_menu_y,
                                'green')
            self.game.draw_text(c.dungeon_font, "Exit Game", 20, self.exit_game_x, self.exit_game_y,
                                'red')

            self.blit_screen()

            clock.tick(12)

    def move_cursor(self):

        if self.game.moving_south:
            if self.state == 'Main Menu':
                self.cursor_rect.midtop = (self.exit_game_x - 200, self.exit_game_y)
                self.state = 'Exit Game'

            elif self.state == 'Exit Game':
                self.cursor_rect.midtop = (self.main_menu_x - 200, self.main_menu_y)
                self.state = 'Main Menu'

        elif self.game.moving_north:
            if self.state == 'Main Menu':
                self.cursor_rect.midtop = (self.exit_game_x - 200, self.exit_game_y)
                self.state = 'Exit Game'

            elif self.state == 'Exit Game':
                self.cursor_rect.midtop = (self.main_menu_x - 200, self.main_menu_y)
                self.state = 'Main Menu'

    def check_input(self):

        self.move_cursor()

        if self.game.interacting:

            if self.state == 'Main Menu':
                self.game.reset_game()
                self.game.current_menu = MainMenu(self.game)
                self.game.paused = False
                self.game.playing = False
                self.run_display = False
                print("Going to main menu")
                self.game.interacting = False

            if self.state == 'Exit Game':
                pg.quit()
                sys.exit()
