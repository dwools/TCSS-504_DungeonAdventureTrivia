from DungeonAdventureGUI import DungeonAdventure

adventure = DungeonAdventure()

while adventure.running:
    adventure.playing = True
    adventure.game_loop()

