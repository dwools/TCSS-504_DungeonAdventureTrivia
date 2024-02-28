import os
import pickle


class SaveGame:

    @staticmethod
    def pickle(game_data):
        with open('dungeon_adventure.pickle', 'wb') as saved_file:
            pickle.dump(game_data, saved_file)

    @staticmethod
    def load_game():
        if os.path.exists("dungeon_adventure.pickle"):
            with open("dungeon_adventure.pickle", "rb") as f:
                game_data = pickle.load(f)
                return game_data  # returning the loaded game data


# creating an instance of SaveGame
game = SaveGame()
