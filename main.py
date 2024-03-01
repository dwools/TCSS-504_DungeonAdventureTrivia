from dungeon_adventure import DungeonAdventure
from save_game import SaveGame
import pygame as pg

pg.init()
pg.font.init()



adventure = DungeonAdventure()

while adventure.running:
    adventure.current_menu.display_menu()
    adventure.game_loop()
# SaveGame.pickle(adventure)
