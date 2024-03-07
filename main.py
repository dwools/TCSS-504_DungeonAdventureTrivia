import initialize_databases
from dungeon_adventure import DungeonAdventure
from save_game import SaveGame
import pygame as pg

pg.init()



adventure = DungeonAdventure()

while adventure.running:
    initialize_databases.main()
    adventure.current_menu.display_menu()
    adventure.game_loop()

