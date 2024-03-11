import os
import pickle


# from combat import Combat


class SaveGame:

    @staticmethod
    def pickle(game_data):
        attributes = {}
        attributes['player_position'] = game_data.player_position
        for monster in game_data.monsters:
            monster.set_monster_sprite(None)
            monster.set_east_monster_sprite(None)
            monster.set_west_monster_sprite(None)
            monster.set_north_monster_sprite(None)
            monster.set_south_monster_sprite(None)
        # for item in game_data.items:
        #     item.set_health_potion_sprite(None)
        #     item.set_fire_trap_sprite(None)
        # for items in game_data.items:
        # game_data.set_health_potion_sprite(None)
        # game_data.set_fire_trap_sprite(None)
        attributes['monsters'] = game_data.monsters
        # attributes['monster_rects'] = game_data.monster_rects
        # attributes['items'] = game_data.items
        # for item in game_data.items:
        #     item.set_item_sprite(None)
        # attributes['item_rects'] = game_data.item_rects
        attributes['player_rect'] = game_data.player_rect
        attributes['dungeon_map'] = game_data.dungeon_map
        # attributes['maze'] = game_data.maze
        with open('dungeon_adventure.pickle', 'wb') as saved_file:
            pickle.dump(attributes, saved_file)

        with open('dungeon.txt', 'r') as file:
            text_content = file.read()

        with open('dungeon.txt.pickle', 'wb') as saved_file:
            pickle.dump(text_content, saved_file)

    # @staticmethod
    # def load_game():
    #     if os.path.exists("dungeon_adventure.pickle"):
    #         with open("dungeon_adventure.pickle", "rb") as f:
    #             game_data = pickle.load(f)
    #             dungeon_adventure = DungeonAdventure()
    #             dungeon_adventure.player_position = game_data['player_position']
    #             dungeon_adventure.monster = game_data['self.monster']
    #             dungeon_adventure.monster_rect = game_data['self.monster_rect']
    #             dungeon_adventure.items = game_data['self.items']
    #             dungeon_adventure.item_rects = game_data['self.item_rects']
    #             dungeon_adventure.player_rect = game_data['self.player_rect']
    #
    #             return dungeon_adventure  # returning the loaded game data
    #

# creating an instance of SaveGame
if __name__ == '__main__':
    game = SaveGame()


