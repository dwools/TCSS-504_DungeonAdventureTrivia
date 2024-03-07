import assets as a
import config as c
import pygame as pg

from hero_factory import *
from monster_factory import *
import dungeon_character


class Combat:
    def __init__(self, game):  # monster, hero
        self.game = game

        # Window Setup
        self.middle_width, self.middle_height = c.WIN_WIDTH / 2, c.WIN_HEIGHT / 2
        self.run_display = True
        self.screen = pg.display.set_mode(c.WINDOW_SIZE, 0, 32)
        self.state = "Attack"

        # Setting UI Locations
        self.attack_x, self.attack_y = self.middle_width + 175, self.middle_height + 300
        self.open_bag_x, self.open_bag_y = self.middle_width + 225, self.middle_height + 400

        self.monster_name_x, self.monster_name_y = self.middle_width + 300, self.middle_height - 400
        self.monster_pos_x, self.monster_pos_y = self.middle_width + 300, self.middle_height - 400

        self.hero_name_x, self.hero_name_y = self.middle_width + 300, self.middle_height + 125
        self.hero_pos_x, self.hero_pos_y = self.middle_width, self.middle_height + 200

        # Making the little star next to buttons
        self.cursor_rect = pg.Rect(self.attack_x - 85, self.attack_y, 20, 20)
        self.cursor_offset = - 350

        # Monster init
        self.m_factory = MonsterFactory()
        self.monster = self.m_factory.create_skeleton()
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
        self.hero_heal_range = [self.hero.get_minimum_heal_points(), self.hero.get_maximum_heal_points()]

    def draw_cursor(self):
        # Draw the pointer next to the buttons
        self.game.draw_text(c.dungeon_font, '*', 10, self.cursor_rect.x, self.cursor_rect.y, 'green')

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

            self.game.display.fill('darkgrey')
            self.game.font_color = c.BLACK

            # Monster
            self.game.draw_text(c.dungeon_font, f'{self.monster_name}', 15, self.monster_name_x, self.monster_name_y,
                                'darkred')
            self.game.draw_text(c.dungeon_font, f'Health {self.monster_health}', 15, self.monster_name_x,
                                self.monster_name_y + 50,
                                'white')
            pg.draw.ellipse(self.game.display, 'darkred', pg.Rect(375, 90, 210, 50))
            pg.draw.ellipse(self.game.display, 'pink', pg.Rect(380, 95, 200, 40))

            # Monster Sprite

            # Hero
            self.game.draw_text(c.dungeon_font, f'{self.hero_name}', 15, self.hero_name_x, self.hero_name_y,
                                'darkgreen')
            self.game.draw_text(c.dungeon_font, f'Health {self.hero_health}', 15, self.hero_name_x,
                                self.hero_name_y + 50, 'white')

            pg.draw.ellipse(self.game.display, 'darkslategray', pg.Rect(70, 275, 210, 50))
            pg.draw.ellipse(self.game.display, 'lightgreen', pg.Rect(75, 280, 200, 40))

            # In combat actions menu
            pg.draw.rect(self.game.display, 'black', pg.Rect(5, 330, 630, 150))  # outside background
            pg.draw.rect(self.game.display, 'darkslategray', pg.Rect(10, 335, 620, 140))  # inside background

            # Line Seperator
            pg.draw.rect(self.game.display, 'black', pg.Rect(350, 330, 5, 550))

            pg.draw.rect(self.game.display, 'black', pg.Rect(350, 400, 280, 5))

            self.game.draw_text(c.dungeon_font, 'Fight', 15, self.attack_x, self.attack_y, 'white')
            self.game.draw_text(c.dungeon_font, 'Backpack', 15, self.open_bag_x, self.open_bag_y, 'white')

            self.draw_cursor()
            self.blit_screen()
            clock.tick(12)

    def move_cursor(self):
        """ Adjust cursor position to notify user of their current choice / button.
            Does a full loop through the menu allowing north and south traversal.
        """

        if self.game.moving_south:
            if self.state == 'Attack':
                self.cursor_rect.midtop = (self.open_bag_x - 125, self.open_bag_y)
                self.state = 'Open Bag'

            elif self.state == 'Open Bag':
                self.cursor_rect.midtop = (self.attack_x - 75, self.attack_y)
                self.state = 'Attack'

        elif self.game.moving_north:
            if self.state == 'Attack':
                self.cursor_rect.midtop = (self.open_bag_x - 125, self.open_bag_y)
                self.state = 'Open Bag'

            elif self.state == 'Open Bag':
                self.cursor_rect.midtop = (self.attack_x - 75, self.attack_y)
                self.state = 'Attack'

    def check_input(self):
        """ Check which menu the user is selecting based on cursor position. Then if user interacts, 'open' that menu.
        """

        self.move_cursor()  # Read cursor position

        if self.game.interacting:  # If user interacts (enter or E) with the cursor's position enter that menu

            if self.state == 'Attack':
                self.game.current_menu = self.game.attack_menu
                self.run_display = False
            elif self.state == 'Open Bag':
                self.game.current_menu = self.game.inventory_menu
                self.run_display = False

        self.run_display = False


class AttackMenu(Combat):
    def __init__(self, game):
        Combat.__init__(self, game)

        self.state = 'Special'

        # Lining up attack options
        self.special_x, self.special_y = self.middle_width + 350, self.middle_height + 250
        self.simple_x, self.simple_y = self.middle_width + 350, self.middle_height + 325
        self.go_back_x, self.go_back_y = self.middle_width + 350, self.middle_height + 425

        # prompt txt
        self.main_txt_x, self.main_txt_y = self.middle_width, self.middle_height

        # Little star
        self.cursor_rect = pg.Rect(self.special_x - 85, self.special_y, 20, 20)
        self.cursor_offset = - 50

    def display_menu(self):
        self.run_display = True
        clock = pg.time.Clock()
        while self.run_display:
            self.game.check_events()
            self.check_input()

            self.game.display.fill('darkgrey')
            self.game.font_color = c.BLACK

            # Monster
            self.game.draw_text(c.dungeon_font, f'{self.monster_name}', 15, self.monster_name_x, self.monster_name_y,
                                'darkred')
            self.game.draw_text(c.dungeon_font, f'Health {self.monster_health}', 15, self.monster_name_x,
                                self.monster_name_y + 50,
                                'white')
            pg.draw.ellipse(self.game.display, 'darkred', pg.Rect(375, 90, 210, 50))
            pg.draw.ellipse(self.game.display, 'pink', pg.Rect(380, 95, 200, 40))

            # Monster Sprite

            # Hero
            self.game.draw_text(c.dungeon_font, f'{self.hero_name}', 15, self.hero_name_x, self.hero_name_y,
                                'darkgreen')
            self.game.draw_text(c.dungeon_font, f'Health {self.hero_health}', 15, self.hero_name_x,
                                self.hero_name_y + 50, 'white')

            pg.draw.ellipse(self.game.display, 'darkslategray', pg.Rect(70, 275, 210, 50))
            pg.draw.ellipse(self.game.display, 'lightgreen', pg.Rect(75, 280, 200, 40))

            # In combat actions menu
            pg.draw.rect(self.game.display, 'black', pg.Rect(5, 330, 630, 150))  # outside background
            pg.draw.rect(self.game.display, 'darkslategray', pg.Rect(10, 335, 620, 140))  # inside background

            # Line Seperator
            pg.draw.rect(self.game.display, 'black', pg.Rect(350, 330, 5, 550))  # L T W H

            pg.draw.rect(self.game.display, 'black', pg.Rect(350, 415, 280, 5))

            self.game.draw_text(c.dungeon_font, 'Special Move', 15, self.special_x, self.special_y, 'white')
            self.game.draw_text(c.dungeon_font, 'Simple Attack', 15, self.simple_x, self.simple_y, 'white')
            self.game.draw_text(c.dungeon_font, 'Go Back', 15, self.go_back_x, self.go_back_y, 'yellow')

            self.draw_cursor()
            self.blit_screen()
            clock.tick(12)

    def draw_cursor(self):
        # Draw the pointer next to the buttons
        self.game.draw_text(c.dungeon_font, '*', 10, self.cursor_rect.x, self.cursor_rect.y, 'green')

    def blit_screen(self):
        # draw to / update the GUI
        window_surface = pg.transform.scale(self.game.display, c.WINDOW_SIZE)
        self.screen.blit(window_surface, (0, 0))
        pg.display.update()  # Update the Display

    def move_cursor(self):
        """ Adjust cursor position to notify user of their current choice / button.
            Does a full loop through the menu allowing north and south traversal.
        """

        if self.game.moving_south:
            if self.state == 'Special':
                self.cursor_rect.midtop = (self.simple_x - self.cursor_offset, self.simple_y)
                self.state = 'Simple'

            elif self.state == 'Simple':
                self.cursor_rect.midtop = (self.go_back_x - self.cursor_offset, self.go_back_y)
                self.state = 'Go Back'

            elif self.state == 'Go Back':
                self.cursor_rect.midtop = (self.special_x - self.cursor_offset, self.special_y)
                self.state = 'Special'

        elif self.game.moving_north:
            if self.state == 'Special':
                self.cursor_rect.midtop = (self.go_back_x - self.cursor_offset, self.go_back_y)
                self.state = 'Go Back'

            elif self.state == 'Simple':
                self.cursor_rect.midtop = (self.special_x - self.cursor_offset, self.special_y)
                self.state = 'Special'

            elif self.state == 'Go Back':
                self.cursor_rect.midtop = (self.simple_x - self.cursor_offset, self.simple_y)
                self.state = 'Simple'

    def check_input(self):
        """ Check which menu the user is selecting based on cursor position. Then if user interacts, 'open' that menu.
        """

        self.move_cursor()  # Read cursor position

        if self.game.interacting:  # If user interacts (enter or E) with the cursor's position enter that menu

            if self.state == 'Attack':
                self.game.current_menu = self.game.attack_menu
                self.run_display = False

            elif self.state == 'Simple Attack':
                print("You are making a simple attack")

            elif self.state == 'Special Ability':
                print("You have used your special ability")

            elif self.state == 'Go Back':
                self.game.current_menu = self.game.combat_ui
                self.run_display = False

        if self.game.escaping:
            self.game.current_menu = self.game.combat_ui
            self.run_display = False

        self.run_display = False


class InventoryMenu(Combat):
    def __init__(self, game):
        Combat.__init__(self, game)
