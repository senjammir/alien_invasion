import sys  # functionality to make the game. Used to exit game when user quits

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """ Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()   # Initialize background settings to run game
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # Screen dimensions in self.screen for all methods in the class
        self.screen = pygame.display.set_mode((1200, 800))
        # display.set_mode represents the entire game window
        pygame.display.set_caption("Alien Invasion")  # Game title

        # gives ship access to the game's resources, such as the screen object
        self.ship = Ship(self)

        # Set the background color
        self.bg_color = (230, 230, 230)  # RGB colors that create a light grey

    def run_game(self):
        """Start the main loop for the game."""
        while True:     # While loop to run the game continually
            # Watch for keyboard and mouse events (keystroke or mouse movement)
            self._check_events()
            self._update_screen()
            # Redraw the screen during each pass through the loop

            pygame.display.flip()


def _check_events(self):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:    # Quits the game if user selects quit
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                # Move the shiip to the right
                self.ship.rect.x += 1


def _update_screen(self):
    """Update images on the screen, and flip to the new screen"""
    self.screen.fill(
        self.settings.bg_color)    # fill method fills the screen and takes only one argument 'color
    # shows the ship on top of the grey screen. Make the most recently drawn screen visible.
    self.ship.blitme()
    # Deletes old screen and updates new screen with new positions depending on events
    pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
