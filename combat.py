import textwrap
import assets as a
import config as c
import pygame as pg

from hero_factory import *
from monster_factory import *
import dungeon_character


class Combat:
    def __init__(self, game):  # monster, hero
        self.__game = game

        # Window Setup
        self.__middle_width, self.__middle_height = c.WIN_WIDTH / 2, c.WIN_HEIGHT / 2
        self.__run_display = True
        self.__screen = pg.display.set_mode(c.WINDOW_SIZE, 0, 32)
        self.__state = "Attack"

        # Setting UI Locations
        self.__attack_x, self.__attack_y = self.__middle_width + 175, self.__middle_height + 300
        self.__open_bag_x, self.__open_bag_y = self.__middle_width + 225, self.__middle_height + 400

        self.__monster_name_x, self.__monster_name_y = self.__middle_width + 300, self.__middle_height - 400
        self.__monster_pos_x, self.__monster_pos_y = self.__middle_width + 300, self.__middle_height - 400

        self.__hero_name_x, self.__hero_name_y = self.__middle_width + 300, self.__middle_height + 125
        self.__hero_pos_x, self.__hero_pos_y = self.__middle_width, self.__middle_height + 200

        self.__main_text_box_x, self.__main_text_box_y = self.__middle_width, self.__middle_height + 200

        # Making the little star next to buttons
        self.__cursor_rect = pg.Rect(self.__attack_x - 85, self.__attack_y, 20, 20)
        self.__cursor_offset = - 350

        # Monster init
        self.__m_factory = MonsterFactory()
        self.__monster = self.__m_factory.create_skeleton()
        self.__monster_health = self.__monster.get_hit_points()
        self.__monster_attack_speed = self.__monster.get_attack_speed()
        self.__monster_name = self.__monster.get_name()
        self.__monster_damage_range = [self.__monster.get_minimum_damage(), self.__monster.get_maximum_damage()]
        self.__monster_chance_to_hit = self.__monster.get_chance_to_hit()
        self.__monster_chance_to_heal = self.__monster.get_chance_to_heal()
        self.__monster_heal_range = [self.__monster.get_minimum_heal_points(), self.__monster.get_maximum_heal_points()]

        # Hero init
        self.__h_factory = HeroFactory()
        self.__hero = self.__h_factory.create_rogue()
        self.__hero_health = self.__hero.get_hit_points()
        self.__hero_attack_speed = self.__hero.get_attack_speed()
        self.__hero_name = self.__hero.get_name()
        self.__hero_damage_range = [self.__hero.get_minimum_damage(), self.__hero.get_maximum_damage()]
        self.__hero_chance_to_block = self.__hero.get_chance_to_block()
        self.__hero_chance_to_hit = self.__hero.get_chance_to_hit()
        self.__hero_heal_range = [self.__hero.get_minimum_heal_points(), self.__hero.get_maximum_heal_points()]

    def get_monster_health(self):
        return self.__monster_health

    def set_monster_health(self, value):
        self.__monster_health = value
        return self.__monster_health

    def get_hero_heal_range(self):
        return self.__hero_heal_range

    def get_hero_health(self):
        return self.__hero_health

    def set_hero_health(self, value):
        self.__hero_health = value
        return self.__hero_health

    def get_monster(self):
        return self.__monster

    def get_hero_attack_speed(self):
        return self.__hero_attack_speed

    def get_monster_chance_to_hit(self):
        return self.__monster_chance_to_hit

    def get_hero_damage_range(self):
        return self.__hero_damage_range

    def get_hero(self):
        return self.__hero

    def set_hero(self, value):
        self.__hero = value

    def get_monster_attack_speed(self):
        return self.__monster_attack_speed

    def get_monster_damage_range(self):
        return self.__monster_damage_range

    def get_hero_chance_to_block(self):
        return self.__hero_chance_to_block

    def get_screen(self):
        return self.__screen

    def get_hero_chance_to_hit(self):
        return self.__hero_chance_to_hit

    def get_monster_name(self):
        return self.__monster_name

    def get_monster_pos_y(self):
        return self.__monster_pos_y

    def get_monster_pos_x(self):
        return self.__monster_pos_x

    def get_monster_name_x(self):
        return self.__monster_name_x

    def get_hero_name_x(self):
        return self.__hero_name_x

    def get_hero_name(self):
        return self.__hero_name

    def get_hero_name_y(self):
        return self.__hero_name_y

    def get_monster_name_y(self):
        return self.__monster_name_y

    def get_main_text_box_y(self):
        return self.__main_text_box_y

    def middle_height(self):
        return self.__middle_height

    def main_text_box_x(self):
        return self.__main_text_box_x

    def get_main_text_box_x(self, value):
        self.__main_text_box_x = value

    def get_hero_health(self):
        return self.__hero_health

    def set_hero_health(self, value):
        self.__hero_health = value
        return self.__hero_health

    def get_monster_health(self):
        return self.__monster_health

    def set_monster_health(self, value):
        self.__monster_health = value
        return self.__monster_health

    def draw_cursor(self):
        # Draw the pointer next to the buttons
        self.__game.draw_text(c.dungeon_font, '*', 10, self.__cursor_rect.x, self.__cursor_rect.y, 'green')

    def blit_screen(self):
        # draw to / update the GUI
        window_surface = pg.transform.scale(self.__game.display, c.WINDOW_SIZE)
        self.__screen.blit(window_surface, (0, 0))
        pg.display.update()  # Update the Display

    def write_main_text_box(self, text):
        """ Simple helper-function used to write text to the GUI. """
        text_to_write = textwrap.wrap(text, 20)
        vertical_offset = 0

        for line in text_to_write:
            font = pg.font.Font(c.system_font, 20)
            text_surface = font.render(line, True, c.WHITE)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (180, 365 + vertical_offset)
            vertical_offset += text_rect.height + 5
            self.__game.display.blit(text_surface, text_rect)
        pg.display.flip()

    def display_menu(self):
        self.__run_display = True
        clock = pg.time.Clock()
        while self.__run_display:
            self.__game.check_events()
            self.check_input()

            self.__game.display.fill('darkgrey')
            self.__game.font_color = c.BLACK

            # Monster
            self.__game.draw_text(c.dungeon_font, f'{self.__monster_name}', 15, self.__monster_name_x,
                                  self.__monster_name_y,
                                  'darkred')
            self.__game.draw_text(c.dungeon_font, f'HP {self.__monster_health}', 15, self.__monster_name_x,
                                  self.__monster_name_y + 50,
                                  'white')
            pg.draw.ellipse(self.__game.display, 'darkred', pg.Rect(375, 90, 210, 50))
            pg.draw.ellipse(self.__game.display, 'pink', pg.Rect(380, 95, 200, 40))

            # Monster Sprite

            # Hero
            self.__game.draw_text(c.dungeon_font, f'{self.__hero_name}', 15, self.__hero_name_x, self.__hero_name_y,
                                  'darkgreen')
            self.__game.draw_text(c.dungeon_font, f'HP {self.__hero_health}', 15, self.__hero_name_x,
                                  self.__hero_name_y + 50, 'white')

            pg.draw.ellipse(self.__game.display, 'darkslategray', pg.Rect(70, 275, 210, 50))
            pg.draw.ellipse(self.__game.display, 'lightgreen', pg.Rect(75, 280, 200, 40))

            # In combat actions menu
            pg.draw.rect(self.__game.display, 'black', pg.Rect(5, 330, 630, 150))  # outside background
            pg.draw.rect(self.__game.display, 'darkslategray', pg.Rect(10, 335, 620, 140))  # inside background

            # Line Seperator
            pg.draw.rect(self.__game.display, 'black', pg.Rect(350, 330, 5, 550))

            pg.draw.rect(self.__game.display, 'black', pg.Rect(350, 400, 280, 5))

            self.__game.draw_text(c.dungeon_font, 'Fight', 15, self.__attack_x, self.__attack_y, 'white')
            self.__game.draw_text(c.dungeon_font, 'Backpack', 15, self.__open_bag_x, self.__open_bag_y, 'white')
            self.write_main_text_box(text='What would you like to do?')

            self.draw_cursor()
            self.blit_screen()
            clock.tick(12)

    def move_cursor(self):
        """ Adjust cursor position to notify user of their current choice / button.
            Does a full loop through the menu allowing north and south traversal.
        """

        if self.__game.moving_south:
            if self.__state == 'Attack':
                self.__cursor_rect.midtop = (self.__open_bag_x - 125, self.__open_bag_y)
                self.__state = 'Open Bag'

            elif self.__state == 'Open Bag':
                self.__cursor_rect.midtop = (self.__attack_x - 75, self.__attack_y)
                self.__state = 'Attack'

        elif self.__game.moving_north:
            if self.__state == 'Attack':
                self.__cursor_rect.midtop = (self.__open_bag_x - 125, self.__open_bag_y)
                self.__state = 'Open Bag'

            elif self.__state == 'Open Bag':
                self.__cursor_rect.midtop = (self.__attack_x - 75, self.__attack_y)
                self.__state = 'Attack'

    def check_input(self):
        """ Check which menu the user is selecting based on cursor position. Then if user interacts, 'open' that menu.
        """

        self.move_cursor()  # Read cursor position

        if self.__game.interacting:  # If user interacts (enter or E) with the cursor's position enter that menu

            if self.__state == 'Attack':
                self.__game.current_menu = self.__game.attack_menu
            elif self.__state == 'Open Bag':
                self.__game.current_menu = self.__game.inventory_menu

        self.__run_display = False


class AttackMenu(Combat):
    def __init__(self, game):
        Combat.__init__(self, game)
        self.__game = game

        # Window init
        self.__screen = self.get_screen()
        self.__middle_width, self.__middle_height = c.WIN_WIDTH / 2, c.WIN_HEIGHT / 2

        # Monster init
        self.__monster_name = self.get_monster_name()
        self.__monster_health = self.get_monster_health()
        self.__monster_name_x, self.__monster_name_y = self.get_monster_name_x(), self.get_monster_name_y()

        # Hero init
        self.__hero_name = self.get_hero_name()
        self.__hero_name_x, self.__hero_name_y = self.get_hero_name_x(), self.get_hero_name_y()
        self.__hero_health = self.get_hero_health()

        self.__state = 'Special'

        # Lining up attack options

        self.__special_x, self.__special_y = self.__middle_width + 350, self.__middle_height + 250
        self.__simple_x, self.__simple_y = self.__middle_width + 350, self.__middle_height + 325
        self.__go_back_x, self.__go_back_y = self.__middle_width + 350, self.__middle_height + 425

        # Little star
        self.__cursor_rect = pg.Rect(self.__special_x - 225, self.__special_y, 20, 20)
        self.__cursor_offset = 225

    def display_menu(self):
        self.__run_display = True
        clock = pg.time.Clock()
        while self.__run_display:
            self.__game.check_events()
            self.check_input()

            self.__game.display.fill('darkgrey')
            self.__game.font_color = c.BLACK

            # Monster
            self.__game.draw_text(c.dungeon_font, f'{self.__monster_name}', 15, self.__monster_name_x,
                                  self.__monster_name_y,
                                  'darkred')
            self.__game.draw_text(c.dungeon_font, f'HP {self.__monster_health}', 15, self.__monster_name_x,
                                  self.__monster_name_y + 50,
                                  'white')
            pg.draw.ellipse(self.__game.display, 'darkred', pg.Rect(375, 90, 210, 50))
            pg.draw.ellipse(self.__game.display, 'pink', pg.Rect(380, 95, 200, 40))

            # Monster Sprite

            # Hero
            self.__game.draw_text(c.dungeon_font, f'{self.__hero_name}', 15, self.__hero_name_x, self.__hero_name_y,
                                  'darkgreen')
            self.__game.draw_text(c.dungeon_font, f'HP {self.__hero_health}', 15, self.__hero_name_x,
                                  self.__hero_name_y + 50, 'white')

            pg.draw.ellipse(self.__game.display, 'darkslategray', pg.Rect(70, 275, 210, 50))
            pg.draw.ellipse(self.__game.display, 'lightgreen', pg.Rect(75, 280, 200, 40))

            # In combat actions menu
            pg.draw.rect(self.__game.display, 'black', pg.Rect(5, 330, 630, 150))  # outside background
            pg.draw.rect(self.__game.display, 'darkslategray', pg.Rect(10, 335, 620, 140))  # inside background

            # Line Seperator
            pg.draw.rect(self.__game.display, 'black', pg.Rect(350, 330, 5, 550))  # L T W H

            pg.draw.rect(self.__game.display, 'black', pg.Rect(350, 415, 280, 5))

            self.__game.draw_text(c.dungeon_font, 'Special Move', 15, self.__special_x, self.__special_y, 'white')
            self.__game.draw_text(c.dungeon_font, 'Simple Attack', 15, self.__simple_x, self.__simple_y, 'white')
            self.__game.draw_text(c.dungeon_font, 'Go Back', 15, self.__go_back_x, self.__go_back_y, 'yellow')

            self.write_main_text_box('Choose your Attack! or go back...')

            self.draw_cursor()
            self.blit_screen()
            clock.tick(60)

    def draw_cursor(self):
        # Draw the pointer next to the buttons
        self.__game.draw_text(c.dungeon_font, '*', 10, self.__cursor_rect.x, self.__cursor_rect.y, 'green')

    def blit_screen(self):
        # draw to / update the GUI
        window_surface = pg.transform.scale(self.__game.display, c.WINDOW_SIZE)
        self.__screen.blit(window_surface, (0, 0))
        pg.display.update()  # Update the Display

    def move_cursor(self):
        """ Adjust cursor position to notify user of their current choice / button.
            Does a full loop through the menu allowing north and south traversal.
        """

        if self.__game.moving_south:
            if self.__state == 'Special':
                self.__cursor_rect.midtop = (self.__simple_x - self.__cursor_offset, self.__simple_y)
                self.__state = 'Simple'

            elif self.__state == 'Simple':
                self.__cursor_rect.midtop = (self.__go_back_x - self.__cursor_offset, self.__go_back_y)
                self.__state = 'Go Back'

            elif self.__state == 'Go Back':
                self.__cursor_rect.midtop = (self.__special_x - self.__cursor_offset, self.__special_y)
                self.__state = 'Special'

        elif self.__game.moving_north:
            if self.__state == 'Special':
                self.__cursor_rect.midtop = (self.__go_back_x - self.__cursor_offset, self.__go_back_y)
                self.__state = 'Go Back'

            elif self.__state == 'Simple':
                self.__cursor_rect.midtop = (self.__special_x - self.__cursor_offset, self.__special_y)
                self.__state = 'Special'

            elif self.__state == 'Go Back':
                self.__cursor_rect.midtop = (self.__simple_x - self.__cursor_offset, self.__simple_y)
                self.__state = 'Simple'

    def check_input(self):
        """ Check which menu the user is selecting based on cursor position. Then if user interacts, 'open' that menu.
        """

        self.move_cursor()  # Read cursor position

        if self.__game.interacting:  # If user interacts (enter or E) with the cursor's position enter that menu

            if self.__state == 'Simple':
                print("You are making a simple attack")
                self.write_main_text_box('Go Simple ATTACK!!!')

            elif self.__state == 'Special':
                print("You have used your special ability")

            elif self.__state == 'Go Back':
                self.__game.current_menu = self.__game.combat_ui
                self.__run_display = False

        if self.__game.escaping:
            self.__game.current_menu = self.__game.combat_ui
            self.__run_display = False

        self.__run_display = False


class InventoryMenu(Combat):
    def __init__(self, game):
        Combat.__init__(self, game)
