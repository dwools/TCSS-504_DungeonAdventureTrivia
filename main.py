from Databases import initialize_databases
from dungeon_adventure import DungeonAdventure
import pygame as pg


def main():
    pg.init()

    initialize_databases.main()
    adventure = DungeonAdventure()

    while adventure.running:
        initialize_databases.main()
        adventure.current_menu.display_menu()
        adventure.game_loop()


if __name__ == '__main__':
    main()
