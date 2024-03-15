import os
import pickle


# from combat import Combat


class SaveGame:

    @staticmethod
    def pickle(game_data):
        attributes = {}
        for monster in game_data.get_monsters_list():
            monster.set_monster_sprite_current(None)
            monster.set_sprite_east(None)
            monster.set_sprite_west(None)
            monster.set_sprite_north(None)
            monster.set_sprite_south(None)
        for pillar in game_data.get_pillars_list():
            pillar.set_abstraction_sprite(None)
            pillar.set_encapsulation_sprite(None)
            pillar.set_inheritance_sprite(None)
            pillar.set_polymorphism_sprite(None)
        for item in game_data.get_items_list():
            item.set_health_potion_sprite(None)
            item.set_fire_trap_sprite(None)
        for item in game_data.get_player_character().get_player_health_potions():
            item.set_health_potion_sprite(None)
            item.set_fire_trap_sprite(None)
        for pillar in game_data.get_player_character().get_player_pillars():
            pillar.set_abstraction_sprite(None)
            pillar.set_encapsulation_sprite(None)
            pillar.set_inheritance_sprite(None)
            pillar.set_polymorphism_sprite(None)
        attributes['player_images'] = game_data.set_player_images(None, None, None, None)
        attributes['player_position'] = game_data.player_position
        attributes['player_rect'] = game_data.player_rect
        attributes['player_character'] = game_data.get_player_character()
        attributes['monsters'] = game_data.get_monsters_list()
        attributes['pillars'] = game_data.get_pillars_list()
        attributes['items'] = game_data.get_items_list()


        with open('dungeon.txt', 'r') as file:
            text_content = file.read()
        with open('dungeon_adventure.pickle', 'wb') as saved_file:
            pickle.dump([attributes, text_content], saved_file)

        # with open('dungeon.txt.pickle', 'wb') as saved_file:
        #     pickle.dump(text_content, saved_file)

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


