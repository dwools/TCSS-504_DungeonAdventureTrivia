import unittest
import pygame
import main

class MyTestCase(unittest.TestCase):


    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_setUp(self):
        # Initialize Pygame (required for testing)
        pygame.init()

    def test_tearDown(self):
        # Clean up Pygame resources
        pygame.quit()

    def test_testdraw_rectangle(self):
        # Create a Pygame screen (you can adjust the dimensions as needed)
        screen = pygame.display.set_mode((800, 600))

        # Call your draw_rectangle function (replace with actual parameters)
        self.draw_rectangle(screen, (255, 0, 0), (100, 100, 200, 150))

        # Update the display
        pygame.display.flip()

        # Wait for a moment (adjust as needed)
        pygame.time.delay(1000)

        # Check if the rectangle was drawn (you can add more specific checks)
        self.assertTrue(pygame.surfarray.array_colorkey(screen).any())


    # Check that character can't walk thorugh walls
    def test_player_sprite_clipping(self):
        '''
        A player spawns at [0, 0], aka [16, 16] pixels, the northwest corner. There are walls to the north and west. If the player moves north or west, its coordinates will not change.
        '''
        self.main()

        # player starts at 0, 0 (16, 16)
        # player moves north
        # player's rect coordinates don't change
        # exit game
    def main(self):
        main.main()
        main.DungeonAdventure.playing = True





if __name__ == '__main__':
    unittest.main()
