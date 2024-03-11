import textwrap

import pygame as pg
import sys
import pygame.display

import config as c
import assets as a
from pillar import Pillar
# from pillar import Pillar
from trivia_factory import TriviaFactory
from save_game import SaveGame
# from load_game import LoadGame
from hero import Hero
from hero_priestess import Priestess
from hero_knight import Knight
from hero_rogue import Rogue
from hero_factory import HeroFactory
from dungeon import Maze



class Menu:

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
    """ Main Menu Class.
        Displays the main menu and leads to the other menus"""

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
            self.game.font_color = c.WHITE

            self.game.draw_text(c.dungeon_font, 'Dungeon Adventure', 20, self.middle_width, self.middle_height - 250,
                                'forestgreen')
            self.game.draw_text(c.dungeon_font, 'Start Game', 20, self.start_x, self.start_y, self.game.font_color)
            self.game.draw_text(c.dungeon_font, 'How To Play', 20, self.how_to_play_x, self.how_to_play_y,
                                self.game.font_color)
            self.game.draw_text(c.dungeon_font, 'Load Save', 20, self.load_game_x, self.load_game_y,
                                self.game.font_color)
            self.game.draw_text(c.dungeon_font, 'Options', 20, self.options_x, self.options_y, self.game.font_color)
            self.game.draw_text(c.dungeon_font, 'Credits', 20, self.credits_x, self.credits_y, self.game.font_color)
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
        """ Check which menu the user is selecting based on cursor position. Then if user interacts, 'open' that menu.
        """

        self.move_cursor()  # Read cursor position

        if self.game.interacting:  # If user interacts (enter or E) with the cursor's position enter that menu

            if self.state == 'Start Game':
                self.game.set_maze(Maze(15, 20).new_maze())
                self.game.current_menu = self.game.character_select
                # self.game.playing = True

            elif self.state == 'How To Play':
                self.game.current_menu = self.game.how_to_play

            elif self.state == 'Load Game':
                self.game.current_menu = self.game.load_games

            elif self.state == 'Options':
                self.game.current_menu = self.game.options

            elif self.state == 'Credits':
                self.game.current_menu = self.game.credits

            self.run_display = False


class CharacterSelectMenu(Menu):

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
                                self.game.font_color)
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
                                self.game.font_color)
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
                                self.game.font_color)
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
        """ Check which menu the user is selecting based on cursor position. Then if user interacts, 'open' that menu.
        """

        self.move_cursor()  # Read cursor position

        if self.game.escaping:
            self.game.current_menu = self.game.main_menu
            self.run_display = False

        if self.game.interacting:  # If user interacts (enter or E) with the cursor's position enter that menu
            if self.state == 'Knight':
                self.game.set_player_character(HeroFactory().create_knight())
                self.game.playing = True

            elif self.state == 'Priestess':
                self.game.set_player_character(HeroFactory().create_priestess())
                self.game.playing = True

            elif self.state == 'Rogue':
                self.game.set_player_character(HeroFactory().create_rogue())
                self.game.playing = True

            self.run_display = False


class HowToPlayMenu(Menu):

    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "First Slide"
        self.how_to_play_x, self.how_to_play_y = self.middle_width, self.middle_height - 200

    def display_menu(self):
        self.run_display = True
        clock = pg.time.Clock()
        while self.run_display:
            self.game.check_events()
            self.check_input()

            self.game.display.fill(c.PURPLE)
            self.game.draw_text(c.dungeon_font, 'How To Play', 20, self.middle_width, self.middle_height - 250,
                                'forestgreen')
            self.game.draw_text(c.dungeon_font, 'Press ESCAPE to go to the main menu', 10, self.middle_width,
                                self.middle_height + 250,
                                self.game.font_color)

            self.draw_cursor()
            self.blit_screen()
            clock.tick(12)

    def check_input(self):

        if self.game.escaping:
            self.game.current_menu = self.game.main_menu
            self.run_display = False

        elif self.game.moving_east:
            if self.state == 'First Slide':  # thinking seperate screens for each set of directions? Navigate with east/west keys
                pass


class LoadSaveGamesMenu(Menu):  # WIP
    def __init__(self, game):
        Menu.__init__(self, game)

        self.saved_games = [1, 2]  # Populate this from somewhere somehow?

        if len(self.saved_games) != 0:  # if there are one or more saves
            self.state = "Save One"
            self.save_x, self.save_y = self.middle_width, self.middle_height
            self.save_rect = None
            self.saved_rects = []

        else:
            self.state = "No Saved Games"

    def display_menu(self):
        clock = pg.time.Clock()
        self.run_display = True

        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.mouse_position = pg.mouse.get_pos()

            self.game.display.fill(c.PURPLE)

            self.game.draw_text(c.dungeon_font, f'Load A Saved Game', 25, self.middle_width, self.middle_height - 200,
                                'forestgreen')

            self.game.draw_text(c.dungeon_font, f'Left Click on a save to start that save', 10, self.middle_width,
                                self.middle_height - 150, 'yellow')

            if len(self.saved_games) != 0:
                self.save_y = self.middle_height - 60

                for save in self.saved_games:
                    self.save_rect = pg.Rect(self.save_x - 100, self.save_y - 50, 200, 50)

                    if self.save_rect.collidepoint(self.mouse_position):

                        self.game.font_color = 'teal'  # changes the color of the text (applying to the next, but we want it to apply to current

                        if self.game.left_clicked:
                            self.game.load_game()

                            self.game.set_maze(Maze(15, 20))
                            self.game.playing = True  # Here is where we enter the saved game
                            self.run_display = False  # end the current menu screen

                        self.game.left_clicked = False

                    else:
                        self.game.font_color = c.WHITE

                    self.game.draw_text(c.dungeon_font, f'Save {self.saved_games[save - 1]}', 20, self.save_x,
                                        self.save_y,
                                        self.game.font_color)

                    self.saved_rects.append(self.save_rect)
                    self.save_y += 70

            else:
                self.game.draw_text(c.dungeon_font, f'No Saves Found', 15, self.middle_width, self.middle_height,
                                    self.game.font_color)

            self.game.draw_text(c.dungeon_font, 'Press ESCAPE to go to the main menu', 10, self.middle_width,
                                self.middle_height + 250,
                                c.WHITE)

            self.blit_screen()

            clock.tick(12)

    def check_input(self):

        if self.game.escaping:
            self.game.current_menu = self.game.main_menu
            self.run_display = False


class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

        self.state = 'Volume'
        self.volume_x, self.volume_y = self.middle_width, self.middle_height + 20
        self.cursor_rect.midtop = (self.volume_x + self.cursor_offset, self.volume_y)

    def display_menu(self):
        clock = pg.time.Clock()
        self.run_display = True

        while self.run_display:
            self.game.check_events()
            self.check_input()

            self.game.display.fill(c.PURPLE)
            self.game.draw_text(c.dungeon_font, 'Options', 30, self.middle_width, self.middle_height - 100,
                                'forestgreen')
            self.game.draw_text(c.dungeon_font, 'Volume', 20, self.volume_x, self.volume_y, self.game.font_color)
            self.game.draw_text(c.dungeon_font, 'Press ESCAPE to go to the main menu', 10, self.middle_width,
                                self.middle_height + 250,
                                self.game.font_color)
            self.draw_cursor()

            self.blit_screen()

            clock.tick(12)

    def check_input(self):

        if self.game.paused:
            if self.game.escaping:
                self.game.current_menu = self.game.pause_menu
                self.run_display = False

        if self.game.escaping and not self.game.paused:
            self.game.current_menu = self.game.main_menu
            self.run_display = False

        elif self.game.interacting:
            if self.state == 'Volume':  # Create a volume control menu
                self.game.current_menu = self.game.volume_menu


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
                                self.game.font_color)
            self.game.draw_text(c.dungeon_font, 'Sanya Sinha', 15, self.middle_width, self.middle_height + 50, 'teal')
            self.game.draw_text(c.dungeon_font, 'David Woolston', 15, self.middle_width, self.middle_height + 100,
                                'blue')
            self.game.draw_text(c.dungeon_font, 'Jackson Davis', 15, self.middle_width, self.middle_height + 150,
                                'royalblue')
            self.game.draw_text(c.dungeon_font, 'Press ESCAPE to go to the main menu', 10, self.middle_width,
                                self.middle_height + 300,
                                self.game.font_color)

            self.blit_screen()

            clock.tick(12)


class PauseMenu(Menu):
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
                                self.game.font_color)
            self.game.draw_text(c.dungeon_font, 'Main Menu', 15, self.main_x, self.main_y, self.game.font_color)
            self.game.draw_text(c.dungeon_font, 'Options', 15, self.options_x, self.options_y, self.game.font_color)
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

        self.move_cursor()

        if self.game.interacting:

            if self.state == 'Save The Game':
                print("SAVING GAME!")
                # self.set_save_game(True)
                SaveGame.pickle(self.game)
                self.game.interacting = False

            if self.state == 'Main Menu':
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
                self.draw_question(line, 20, self.question_x, self.question_y, self.game.font_color)
                self.question_y += 50

            self.game.draw_text(c.dungeon_font, "True", 15, self.true_x, self.true_y, 'forestgreen')
            self.game.draw_text(c.dungeon_font, "False", 15, self.false_x, self.false_y, 'darkred')

            self.draw_cursor()

            self.blit_screen()

            clock.tick(12)

    def draw_question(self, text, size, x, y, font_color):
        """ Simple helper-function used to write text to the GUI. """
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

    def check_input(self):
        """ Check which menu the user is selecting based on cursor position. Then if user interacts, 'open' that menu.
        """

        self.move_cursor()  # Read cursor position

        if self.game.interacting:  # If user interacts (enter or E) with the cursor's position enter that menu

            if self.state == 'TRUE':
                print('you have selected true')

            elif self.state == 'FALSE':
                print('you have selected false')

            # if answer == true, add pillar to backpack || else: relocate pillar
            if self.answer == self.state:
                print('You have chosen correctly')  # add pillar to backpack
                self.game.add_to_backpack(Pillar(self.__pillar))
                self.game.remove_pillar(self.__pillar)
            else:
                print('you failed')  # relocate pillar
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


class GameOver(Menu):
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
                                self.game.font_color)
            self.game.draw_text(c.dungeon_font, "Exit Game", 20, self.exit_game_x, self.exit_game_y,
                                self.game.font_color)

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
                self.game.current_menu = MainMenu(self.game)
                self.game.paused = False
                self.game.playing = False
                self.run_display = False
                print("Going to main menu")
                self.game.interacting = False

            if self.state == 'Exit Game':
                pg.quit()
                sys.exit()
