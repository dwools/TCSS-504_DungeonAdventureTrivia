from Adventurer import Adventurer
from HealingPotion import *
from dungeon import Dungeon
import random
from DungeonASCII import *

art = Ascii()

INTRO = ("\n'Deep in this dungeon, four pillars are hidden...'"
         "\n  'A for Abstraction'"
         "\n  'E for Encapsulation'"
         "\n  'I for Inheritance'"
         "\n  'P for Polymorphism'"
         "\n\n'Collect them and you'll gain incredible power.'"
         "\n\n'But be warned; once you enter, you cannot leave until you have found all four!'")

class DungeonAdventure:
    """
    Dungeon adventure game logic, creates a Dungeon object and an adventurer object, names the adventurer
    with the users input. Allows the user to navigate the dungeon, collect and use potions, collect pillars,
    and fall into pits! Once all 4 pillars are collected the exit is unlocked.
    HIDDEN MAP OPTION: enter 'ADVENTURE' during the game.
    """
    def __init__(self):
        self.dungeon = self.create_dungeon()
        print(art.get_message('welcome'))
        self.adventurer = self.create_adventurer()
        self.user_quit = False
        self.playing = True

    def create_dungeon(self):
        """
        uses user input to change the dungeon size
        """
        difficulty = input("\nEnter 'HARD' for a harder dungeon, or any other key to continue: ").strip().upper()
        if difficulty == "HARD":
            print("Prepare for a challenge...")
            return Dungeon(8, 8)
        else:
            print("This is a standard adventure...")
            return Dungeon(5, 5)

    def create_adventurer(self):
        """
        Creates a new adventurer object with the users input for name
        """
        name = input("'Who dares enter the Dungeon?! Tell me your name, adventurer...:' ")
        if not name:
            name = "Finn"  # default
            print(f"\n'Shy one are you? Very well, I'll just call you {name}.'")
        return Adventurer(name)

    def display_current_room(self):  # shows the user what room in the dungeon they're in\
        """
        Helper for displaying the current room to the player
        """
        row, col = self.adventurer.location
        current_room = self.dungeon.get_room(row, col)
        print("\n_______________________________________________")
        print(f"\nYou look around at your current room...\n\n{current_room}\n")

    def get_user_input(self):
        """
        Helper for gathering player input for moves as they play the game
        """
        print("\nWhat do you want to do?: Move (N/S/E/W), Health Potion (H), Vision Potion (V), Check Status (C), Quit (Q)\n")
        user_input = input("Please choose an action: ").strip().upper()  # store input, stripping out spaces, forcing upper
        # handle inputs other than valid options
        accepted_inputs = ["N", "S", "E", "W", "H", "V", "C", "Q", "ADVENTURE"]  # 'adventure' is our Easter egg option
        while user_input not in accepted_inputs:
            print("Sorry, that's not one of the provided options. Please try again.")
            return self.get_user_input()
        return user_input

    def process_movement(self, direction):
        """
        Takes movement inputs and updates adventurers location accordingly, moving them through the dungeon
        """
        row, col = self.adventurer.location
        current_room = self.dungeon.get_room(row, col)
        # print(f"New adventurer location: {self.adventurer.location}")
        if direction == "N" and current_room.has_north_door():
            self.adventurer.location = (row - 1, col)
            print(f"\nYou move north to the next room")
        elif direction == "S" and current_room.has_south_door():
            self.adventurer.location = (row + 1, col)
            print(f"\nYou move south to the next room")
        elif direction == "E" and current_room.has_east_door():
            self.adventurer.location = (row, col + 1)
            print(f"\nYou move east to the next room")
        elif direction == "W" and current_room.has_west_door():
            self.adventurer.location = (row, col - 1)
            print(f"\nYou move west to the next room")
        else:
            print("\nYou walked right into a wall... "
                  "\nLook around more carefully and try a different direction.")

    def process_pitfall(self, damage):
        """
        Helper method for handling pits
        """
        print(f"\nLook out! You fell in a pit and took {damage} damage!")
        self.adventurer.hit_points -= damage
        print(f"\nYou climb out of the pit with {self.adventurer.hit_points} hit points!")

    def process_potion(self, potion):
        """
        Helper method for handling potions when processing user input
        """
        if potion == "H":
            self.adventurer.take_healing_potion()
        if potion == "V":
            player_row, player_col = self.adventurer.location
            if self.adventurer.vision_potions >= 1:
                self.adventurer.take_vision_potion()
                self.dungeon.vision_potion_print(player_row, player_col)
                print(f"\nYou were blind, now you see! You can see all the rooms surrounding your current location.")
            else:
                print(f"\nYou don't have any vision potions right now.")
        else:
            pass

    def process_user_input(self, user_input):
        """
        processes the actions chosen by the user
        """
        if user_input in ["N", "S", "E", "W"]:  # movement input
            self.process_movement(user_input)  # process movement helper
        elif user_input in ["H", "V"]:  # potion input
            self.process_potion(user_input)
        elif user_input == "C":  # check character status input
            print(self.adventurer)
        elif user_input == "Q":  # quit input
            self.user_quit = True
        elif user_input == "ADVENTURE":
            print("\nYou found the secret Dungeon map!\n\n")
            self.dungeon.draw()
        else:
            print("This shouldn't be happening - should have accounted for this earlier")
            pass

    def update_game(self):
        """
        Checks the contents of the room as the player navigates the dungeon to handle encounters with
        pillars, potions, and pits
        """
        row, col = self.adventurer.location
        current_room = self.dungeon.get_room(row, col)

        if current_room.has_pillars():  # check for a pillar in the room
            self.display_current_room()
            pillar_type = self.dungeon.get_room_pillar(row, col)
            print(f"Finally! This room has a pillar! This '{pillar_type}' is coming along with you.")
            self.adventurer.pillar_found(pillar_type)
            current_room.clear_item("pillar")

        if current_room.has_multiple_items():  # check for multiple items in the room
            self.display_current_room()
            print("This room has a healing potion AND a vision potion in it! Jackpot! "
                  "\bYou put the items in your backpack for later.")
            potion = HealingPotion()
            self.adventurer.find_healing_potion(potion)
            self.adventurer.find_vision_potion()
            current_room.clear_item("multiple")

        if current_room.has_healing_potion():  # check for a healing potion in the room
            self.display_current_room()
            print("Nice! You found a healing potion in here. You're going to need it! "
                  "\bYou put it in your backpack for later.")
            potion = HealingPotion()
            self.adventurer.find_healing_potion(potion)  # we find a healing potion and add to the adventurer
            current_room.clear_item("healing")  # remove the healing potion from the room

        if current_room.has_vision_potion():  # check for a vision potion in the room
            self.display_current_room()
            self.adventurer.find_vision_potion()
            current_room.clear_item("vision")
            print("Wow! This room had a Vision Potion in it! Use it to see through walls! "
                  "\bYou put it in your backpack for later.")

        if current_room.has_pit():
            damage = random.randint(10, 30)
            self.process_pitfall(damage)


    def check_game_over(self):
        """
        Evaluates conditions that could end the game and passes on the outcome (win, lose, quit)
        """
        current_room = self.dungeon.get_room(*self.adventurer.location)
        if self.adventurer.hit_points <= 0:  # lose due to health dropping to zero
            return True, "lose"
        elif current_room.is_exit():  # reaching exit could mean game ends
            if 4 == len(self.adventurer.pillar_pieces_found):
                return True, "win"
            if 4 > len(self.adventurer.pillar_pieces_found):
                missing_pieces = 4 - len(self.adventurer.pillar_pieces_found)
                print(f"\nYou have reached the exit, but you can't leave yet.")
                print(f"\nYou need {missing_pieces} more Pillar piece{'s' if missing_pieces > 1 else ''} to unlock the exit.")
                return False, None
        elif self.user_quit:  # quit condition
            return True, "quit"
        else:
            return False, None

    def end_game(self, outcome):
        """
        Receives outcome of a game ending condition and returns the related message
        """
        if outcome == "win":
            print(art.get_message('win'))
            print(f"\nAmazing! You escaped the Dungeon with all four Pillars and {self.adventurer.hit_points} Hit Points remaining.")
        elif outcome == "lose":
            missing_pieces = 4 - len(self.adventurer.pillar_pieces_found)
            print(art.get_message('lose'))
            print(f"\nYour Adventurer has been defeated by the Dungeon..."
                  f"\n\n{self.adventurer.name} collected {4 - missing_pieces} Pillar piece{'s' if missing_pieces != 1 else ''} before dying.")
        elif outcome == "quit":
            print("Game quit. See you next time!")

    def game_intro(self):
        """
        introduces the game concept
        """
        name = self.adventurer.name
        print(f"\n'Hello, {name}! You must be here to find the legendary 'Pillars of Ooh''.\n "
              f"{INTRO}")
        print(input("\n   --PRESS ENTER TO BEGIN--"))
        print(f"{name} opens the door and finds themself in the first room of the dungeon."
              f"\nThere is nowhere to go but forward."
              f"\n\n'Good luck, {name}... I hope you make it out alive...'")

    def play_game(self):
        """
        Core game loop: receives and evaluates input, checks the game state until a game ending condition
        is found and the loop ends
        """
        self.game_intro()
        while self.playing:  # while the game is being played
            self.display_current_room()  # show the current room to the user
            user_input = self.get_user_input()  # get input from the user on what they'd like to do
            self.process_user_input(user_input)  # processes the input from the user
            self.update_game()  # check to see what the game state is following the users input
            game_over, outcome = self.check_game_over() # evaluates if the game is over
            if game_over:
                self.end_game(outcome)
                self.dungeon.draw()
                self.playing = False


if __name__ == "__main__":
    game = DungeonAdventure()
    game.play_game()
