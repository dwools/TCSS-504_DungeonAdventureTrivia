import assets as a
import config as c
import pygame as pg

from hero_factory import *
from monster_factory import *


class Combat:
    def __init__(self,  game):  # monster, hero,
        self.game = game
        self.middle_width, self.middle_height = c.WIN_WIDTH / 2, c.WIN_HEIGHT / 2
        self.run_display = True
        self.screen = pg.display.set_mode(c.WINDOW_SIZE, 0, 32)

        # Making the little star next to buttons
        self.cursor_rect = pg.Rect(0, 0, 20, 20)
        self.cursor_offset = - 350
        self.bg_image = pg.image.load(a.main_menu_bg)

        # Monster init
        self.m_factory = MonsterFactory()
        self.monster = self.m_factory.create_gremlin()
        self.monster_health = self.monster.get_hit_points()
        self.monster_attack_speed = self.monster.get_attack_speed()
        self.monster_name = self.monster.get_name()
        self.monster_damage_range = [self.monster.get_minimum_damage(), self.monster.get_maximum_damage()]
        self.monster_chance_to_hit = self.monster.get_chance_to_hit()
        self.monster_chance_to_heal = self.monster.get_chance_to_heal()
        self.monster_heal_range = [self.monster.get_minimum_heal_points(), self.monster.get_maximum_heal_points()]

        # Hero init
        self.h_factory = HeroFactory()
        self.hero = self.h_factory.create_rogue()
        self.hero_health = self.hero.get_hit_points()
        self.hero_attack_speed = self.hero.get_attack_speed()
        self.hero_name = self.hero.get_name()
        self.hero_damage_range = [self.hero.get_minimum_damage(), self.hero.get_maximum_damage()]
        self.hero_chance_to_block = self.hero.get_chance_to_block()
        self.hero_chance_to_hit = self.hero.get_chance_to_hit()
        self.hero_chance_to_heal = self.hero.get_chance_to_heal()
        self.hero_heal_range = [self.hero.get_minimum_heal_points(), self.hero.get_maximum_heal_points()]

    def draw_cursor(self):
        # Draw the pointer next to the buttons
        self.game.draw_text(c.dungeon_font, '*', 15, self.cursor_rect.x, self.cursor_rect.y, 'red')

    def blit_screen(self):
        # draw to / update the GUI
        window_surface = pg.transform.scale(self.game.display, c.WINDOW_SIZE)
        self.screen.blit(window_surface, (0, 0))
        pg.display.update()  # Update the Display

    def display_menu(self):
        self.run_display = True
        clock = pg.time.Clock()
        while self.run_display:
            self.game.check_events()
            self.check_input()

            self.game.display.fill(c.PURPLE)
            self.game.font_color = c.WHITE

            self.game.draw_text(c.dungeon_font, f'{self.monster_name}', 20, self.middle_width, self.middle_height - 250,
                                'forestgreen')

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