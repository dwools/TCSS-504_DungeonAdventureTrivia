import os
import pickle
from dungeon_adventure import DungeonAdventure
# from combat import Combat


class LoadGame:

    @staticmethod
    def load_game():
        if os.path.exists("dungeon_adventure.pickle"):
            with open("dungeon_adventure.pickle", "rb") as f:
                game_data = pickle.load(f)
                dungeon_adventure = DungeonAdventure()
                dungeon_adventure.player_position = game_data['player_position']
                dungeon_adventure.monster = game_data['self.monster']
                dungeon_adventure.monster_rect = game_data['self.monster_rect']
                dungeon_adventure.items = game_data['self.items']
                dungeon_adventure.item_rects = game_data['self.item_rects']
                dungeon_adventure.player_rect = game_data['self.player_rect']

                return dungeon_adventure  # returning the loaded game data
