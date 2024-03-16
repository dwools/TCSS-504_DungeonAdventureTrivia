import os
import pickle


# from combat import Combat


class SaveGame:

    @staticmethod
    def pickle(game_data):
        """
        Save the current state of the game
        :param game_data:
        :return:
        """

        attributes = {}
        for monster in game_data.get_monsters_list():
            monster.set_character_sprites(None, None, None, None)
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
        game_data.get_player_character().set_character_sprites(None, None, None, None)
        game_data.set_item_sprites(None)
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


if __name__ == '__main__':
    game = SaveGame()


