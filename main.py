import config
import initialize_databases
from dungeon_adventure import DungeonAdventure
from save_game import SaveGame
import pygame as pg

def main():
    pg.init()

    adventure = DungeonAdventure()

    while adventure.running:
        initialize_databases.main()
        adventure.current_menu.display_menu()
        adventure.game_loop()

if __name__ == '__main__':
    main()
