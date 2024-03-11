import os
import pickle
from dungeon_adventure import DungeonAdventure
from dungeon import Maze


class LoadGame:

    @staticmethod
    def load_game():
        if os.path.exists("dungeon_adventure.pickle"):
            with open("dungeon_adventure.pickle", "rb") as f:
                game_data = pickle.load(f)
            dungeon_adventure = DungeonAdventure()
            dungeon_adventure.player_position = game_data['player_position']
            dungeon_adventure.monsters = game_data['monster']
            dungeon_adventure.items = game_data['items']
            dungeon_adventure.player_rect = game_data['player_rect']
            # dungeon_adventure.dungeon_map = game_data['dungeon_map']  # if anything breaks it's this


            return dungeon_adventure  # returning the loaded game data
