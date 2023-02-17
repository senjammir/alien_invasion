import sys  # functionality to make the game. Used to exit game when user quits

import pygame


class AlienInvasion:
    """ Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()   # Initialize background settings to run game

        # Screen dimensions in self.screen for all methods in the class
        self.screen = pygame.display.set_mode((1200, 800))
        # display.set_mode represents the entire game window
        pygame.display.set_caption("Alien Invasion")  # Game title

    def run_game(self):
        """Start the main loop for the game."""
        while True:     # While loop to run the game continually
            # Watch for keyboard and mouse events (keystroke or mouse movement)
            for even in pygame.event.get():
                if even.type == pygame.QUIT:    # Quits the game if user selects quit
                    sys.exit()

            # Make the most recently drawn screen visible.
            # Deletes old screen and updates new screen with new positions depending on events
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
