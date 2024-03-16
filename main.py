from Databases import initialize_databases
from dungeon_adventure import DungeonAdventure
import pygame as pg


def main():
    """
    Game's overall constructor. It initializes and builds the databases to be queried in the game, instantiates the
    game's view and gameplay controller (and part of the model system) loop, and opens and displays the game's
    Main Menu to begin gameplay.
    :return:
    """
    pg.init()

    initialize_databases.main()
    adventure = DungeonAdventure()

    while adventure.running:
        initialize_databases.main()
        adventure.current_menu.display_menu()
        adventure.game_loop()


if __name__ == '__main__':
    main()

