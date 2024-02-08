from dungeon_adventure import DungeonAdventure

adventure = DungeonAdventure()

while adventure.running:
    adventure.current_menu.display_menu()
    adventure.game_loop()
