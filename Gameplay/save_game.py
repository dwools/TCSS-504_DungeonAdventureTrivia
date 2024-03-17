import os
import pickle

import pygame
from pygame import Surface


class SaveGame:


    @staticmethod
    def save_helper(game_data):
        """
        Save the current state of the game
        :param game_data:
        :return:
        """
        if not os.path.exists('./save_files'): os.mkdir('./save_files')

        def exclude_surface(value):
            if isinstance(value, Surface):
                return None
            return value
    #
        attributes = {}
        attributes['trivia_ui'] = game_data.trivia_ui
        attributes['player_position'] = game_data.player_position
        attributes['player_rect'] = game_data.player_rect
        attributes['player_character'] = game_data.get_player_character()
        attributes['monsters'] = game_data.get_monsters_list()
        attributes['pillars'] = game_data.get_pillars_list()
        attributes['items'] = game_data.get_items_list()

        with open('dungeon.txt', 'r') as file:
            dungeon_map = file.read()

        with open('./save_files/saved_dungeon_map.pkl', 'wb') as f:
            pickle.dump(dungeon_map, f, pickle.HIGHEST_PROTOCOL)

        with open("./save_files/attributes_dict.pkl", "wb") as f:
            pickle.dump(attributes, f, pickle.HIGHEST_PROTOCOL)





    # def filter_non_png_files(attributes):
    #     return [filename for filename in attributes if not filename.lower().endswith(".png")]
#
#     @staticmethod
#     def pickle(game_data):
#         """
#         Save the current state of the game
#         :param game_data:
#         :return:
#         """

        # attributes = {}
        # for monster in game_data.get_monsters_list():
        #     monster.set_character_sprites(None, None, None, None)
        # for pillar in game_data.get_pillars_list():
        #     pillar.set_abstraction_sprite(None)
        #     pillar.set_encapsulation_sprite(None)
        #     pillar.set_inheritance_sprite(None)
        #     pillar.set_polymorphism_sprite(None)
        # for item in game_data.get_items_list():
        #     item.set_health_potion_sprite(None)
        #     item.set_fire_trap_sprite(None)
        # for item in game_data.get_player_character().get_player_health_potions():
        #     item.set_health_potion_sprite(None)
        #     item.set_fire_trap_sprite(None)
        # for pillar in game_data.get_player_character().get_player_pillars():
        #     pillar.set_abstraction_sprite(None)
        #     pillar.set_encapsulation_sprite(None)
        #     pillar.set_inheritance_sprite(None)
        #     pillar.set_polymorphism_sprite(None)
        # game_data.get_player_character().set_character_sprites(None, None, None, None)
        # game_data.set_item_sprites(None, None)
        # game_data.set_pillar_sprites(None, None, None, None)
        # game_data.character_select.set_menu_images(None, None, None)
        # attributes['trivia_ui'] = game_data.trivia_ui
        # if game_data.trivia_ui:
        #     game_data.trivia_ui.set_trivia_ui_images(None, None, None, None)
        # attributes['player_images'] = game_data.set_player_images(None, None, None, None)
        # attributes['player_position'] = game_data.player_position
        # attributes['player_rect'] = game_data.player_rect
        # attributes['player_character'] = game_data.get_player_character()
        # attributes['monsters'] = game_data.get_monsters_list()
        # attributes['pillars'] = game_data.get_pillars_list()
        # attributes['items'] = game_data.get_items_list()
#
#
#         with open('dungeon.txt', 'r') as file:
#             text_content = file.read()
#         with open('dungeon_adventure.pickle', 'wb') as saved_file:
#            pickle.dump([attributes, text_content], saved_file)
#
#
# if __name__ == '__main__':
#     game = SaveGame()
#
#
#
#
