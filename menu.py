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
        self.cursor_offset = - 300

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        window_surface = pg.transform.scale(self.game.display, c.WINDOW_SIZE)
        self.screen.blit(window_surface, (0, 0))
        pg.display.update()  # Update the Display


class MainMenu(Menu):
    def __init__(self, game):
        '''

        :param game:
        '''
        Menu.__init__(self, game)
        self.state = "Start Game"
        self.start_x, self.start_y = self.middle_width, self.middle_height
        self.how_to_play_x, self.how_to_play_y = self.middle_width, self.middle_height + 100
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
            self.game.draw_text('Main Menu', 20, self.middle_width, self.middle_height - 250)
            self.game.draw_text('Start Game', 20, self.start_x, self.start_y)
            self.game.draw_text('How To Play', 20, self.how_to_play_x, self.how_to_play_y)
            self.game.draw_text('Options', 20, self.options_x, self.options_y)
            self.game.draw_text('Credits', 20, self.credits_x, self.credits_y)
            self.draw_cursor()
            self.blit_screen()
            clock.tick(13)

    def move_cursor(self):
        if self.game.moving_south:
            if self.state == 'Start Game':
                self.cursor_rect.midtop = (self.how_to_play_x + self.cursor_offset, self.how_to_play_y)
                self.state = 'How To Play'

            elif self.state == 'How To Play':
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

            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.how_to_play_x + self.cursor_offset, self.how_to_play_y)
                self.state = 'How To Play'

            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.options_x + self.cursor_offset, self.options_y)
                self.state = 'Options'

    def check_input(self):

        self.move_cursor()

        if self.game.interacting:
            if self.state == 'Start Game':
                self.game.playing = True
                self.run_display = False
                print("starting game")

            elif self.state == 'How To Play':
                print("How to Play")

            elif self.state == 'Options':
                print("Options")

            elif self.state == 'Credits':
                print("Credits")

