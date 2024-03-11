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
            dungeon_adventure.monster = game_data['monster']
            dungeon_adventure.monster_rect = game_data['monster_rect']
            dungeon_adventure.items = game_data['items']
            dungeon_adventure.item_rects = game_data['item_rects']
            dungeon_adventure.player_rect = game_data['player_rect']
            dungeon_adventure.dungeon_map = game_data['dungeon_map']  # if anything breaks it's this

            with open('dungeon.txt','r') as file:
                text_content = file.read()

            with open('dungeon.txt.pkl','wb') as pkl_file:
                pickle.dump(text_content, pkl_file)

            return dungeon_adventure  # returning the loaded game data
