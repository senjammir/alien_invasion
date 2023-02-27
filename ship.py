
import pygame


class Ship:
    """A class to manage the ship"""

    # ai_game parameter to give ship access to all the game resources defined in AlienInvasion
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # to place the ship in the correct locaiton on the screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')   # to load image
        self.rect = self.image.get_rect()   # position of ship in the shape of a rectangle
        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):       # draws the image to the game screen as speciied by self.rect method
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
