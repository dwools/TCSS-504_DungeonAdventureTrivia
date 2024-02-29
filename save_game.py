import os
import pickle
from dungeon_adventure import DungeonAdventure

class SaveGame:

    @staticmethod
    def pickle(game_data):
        attributes = {}
        attributes['player_position'] = game_data.player_position
        with open('dungeon_adventure.pickle', 'wb') as saved_file:
            pickle.dump(attributes, saved_file)

    @staticmethod
    def load_game():
        if os.path.exists("dungeon_adventure.pickle"):
            with open("dungeon_adventure.pickle", "rb") as f:
                game_data = pickle.load(f)
                dungeon_adventure = DungeonAdventure()
                dungeon_adventure.player_position = game_data['player_position']
                return dungeon_adventure  # returning the loaded game data


# creating an instance of SaveGame
game = SaveGame()
