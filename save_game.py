import os
import pickle
from dungeon_adventure import DungeonAdventure
# from combat import Combat


class SaveGame:

    @staticmethod
    def pickle(game_data):
        attributes = {}
        attributes['player_position'] = game_data.player_position
        attributes['self.monster'] = game_data.self.monster
        attributes['self.monster_rect'] = game_data.self.monster_rect
        attributes['self.items'] = game_data.self.items
        attributes['self.item_rects'] = game_data.self.item_rects
        attributes['self.player_rect'] = game_data.self.player_rect
        with open('dungeon_adventure.pickle', 'wb') as saved_file:
            pickle.dump(attributes, saved_file)

    @staticmethod
    def load_game():
        if os.path.exists("dungeon_adventure.pickle"):
            with open("dungeon_adventure.pickle", "rb") as f:
                game_data = pickle.load(f)
                dungeon_adventure = DungeonAdventure()
                dungeon_adventure.player_position = game_data['player_position']
                dungeon_adventure.self.monster = game_data['self.monster']
                dungeon_adventure.self.monster_rect = game_data['self.monster_rect']
                dungeon_adventure.self.items = game_data['self.items']
                dungeon_adventure.self.item_rects = game_data['self.item_rects']
                dungeon_adventure.self.player_rect = game_data['self.player_rect']

                return dungeon_adventure  # returning the loaded game data


# creating an instance of SaveGame
game = SaveGame()



# import os
# import pickle
# from dungeon_adventure import DungeonAdventure
#
# class SaveGame:
#
#     @staticmethod
#     def pickle(game_data):
#         attributes = {}
#         attributes['player_position'] = game_data.player_position
#         with open('dungeon_adventure.pickle', 'wb') as saved_file:
#             pickle.dump(attributes, saved_file)
#
#     @staticmethod
#     def load_game():
#         if os.path.exists("dungeon_adventure.pickle"):
#             with open("dungeon_adventure.pickle", "rb") as f:
#                 game_data = pickle.load(f)
#                 dungeon_adventure = DungeonAdventure()
#                 dungeon_adventure.player_position = game_data['player_position']
#                 return dungeon_adventure  # returning the loaded game data
#
#
# # creating an instance of SaveGame
# game = SaveGame()
