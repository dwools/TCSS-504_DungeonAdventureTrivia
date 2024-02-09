import pygame as pg
import config as c


class Menu():

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
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y, 'red')

    def blit_screen(self):
        window_surface = pg.transform.scale(self.game.display, c.WINDOW_SIZE)
        self.screen.blit(window_surface, (0, 0))
        pg.display.update()  # Update the Display


class MainMenu(Menu):
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
            self.game.draw_text('Dungeon Adventure', 20, self.middle_width, self.middle_height - 250, 'forestgreen')
            self.game.draw_text('Start Game', 20, self.start_x, self.start_y, self.game.font_color)
            self.game.draw_text('How To Play', 20, self.how_to_play_x, self.how_to_play_y, self.game.font_color)
            self.game.draw_text('Load Save', 20, self.load_game_x, self.load_game_y, self.game.font_color)
            self.game.draw_text('Options', 20, self.options_x, self.options_y, self.game.font_color)
            self.game.draw_text('Credits', 20, self.credits_x, self.credits_y, self.game.font_color)
            self.draw_cursor()
            self.blit_screen()
            clock.tick(12)

    def move_cursor(self):
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

        self.move_cursor()

        if self.game.interacting:

            if self.state == 'Start Game':
                self.game.playing = True

            elif self.state == 'How To Play':
                self.game.current_menu = self.game.how_to_play

            elif self.state == 'Load Game':
                self.game.current_menu = self.game.load_games

            elif self.state == 'Options':
                self.game.current_menu = self.game.options

            elif self.state == 'Credits':
                self.game.current_menu = self.game.credits

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
            self.game.draw_text('How To Play', 20, self.middle_width, self.middle_height - 250, 'forestgreen')
            self.game.draw_text('Press ESCAPE to go to the main menu', 10, self.middle_width, self.middle_height + 250,
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

            self.game.draw_text(f'{self.mouse_position}', 15, self.middle_width - 500, self.middle_height - 200,
                                'yellow')

            self.game.draw_text(f'Load A Saved Game', 25, self.middle_width, self.middle_height - 200, 'forestgreen')

            self.game.draw_text(f'Left Click on a save to start that save', 10, self.middle_width,
                                self.middle_height - 150, 'yellow')

            if len(self.saved_games) != 0:
                self.save_y = self.middle_height - 60

                for save in self.saved_games:
                    self.save_rect = pg.Rect(self.save_x - 100, self.save_y - 25, 200, 50)

                    self.game.draw_text(f'Save {self.saved_games[save - 1]}', 20, self.save_x, self.save_y,
                                        self.game.font_color)

                    self.saved_rects.append(self.save_rect)
                    self.save_y += 70

                    self.game.font_color = c.WHITE

                    if self.save_rect.collidepoint(self.mouse_position):

                        self.game.font_color = 'teal'  # changes the color of the text (applying to the next, but we want it to apply to current

                        if self.game.left_clicked:
                            self.game.playing = True  # Here is where we enter the saved game
                            self.run_display = False  # end the current menu screen

                        self.game.left_clicked = False

                    else:
                        self.game.font_color = c.WHITE



            else:
                self.game.draw_text(f'No Saves Found', 15, self.middle_width, self.middle_height, self.game.font_color)

            self.game.draw_text('Press ESCAPE to go to the main menu', 10, self.middle_width, self.middle_height + 250,
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
            self.game.draw_text('Options', 30, self.middle_width, self.middle_height - 100, 'forestgreen')
            self.game.draw_text('Volume', 20, self.volume_x, self.volume_y, self.game.font_color)
            self.game.draw_text('Press ESCAPE to go to the main menu', 10, self.middle_width, self.middle_height + 250,
                                self.game.font_color)
            self.draw_cursor()

            self.blit_screen()

            clock.tick(12)

    def check_input(self):

        if self.game.escaping:
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

            if self.game.escaping or self.game.interacting:
                self.game.current_menu = self.game.main_menu
                self.run_display = False

            self.game.display.fill(c.PURPLE)
            self.game.draw_text('Credits', 30, self.middle_width, self.middle_height - 200, 'forestgreen')
            self.game.draw_text('Made by', 20, self.middle_width, self.middle_height - 50, self.game.font_color)
            self.game.draw_text('Sanya Sinha', 15, self.middle_width, self.middle_height + 50, 'teal')
            self.game.draw_text('David Woolston', 15, self.middle_width, self.middle_height + 100, 'blue')
            self.game.draw_text('Jackson Davis', 15, self.middle_width, self.middle_height + 150, 'royalblue')
            self.game.draw_text('Press ESCAPE to go to the main menu', 10, self.middle_width, self.middle_height + 300,
                                self.game.font_color)

            self.blit_screen()

            clock.tick(12)
