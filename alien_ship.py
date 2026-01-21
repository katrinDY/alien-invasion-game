import pygame

from pygame.sprite import Sprite

class AlienShip(Sprite):
    """A class to represent a single alien ship in the alien invasion game."""
    
    def __init__(self, ai_game):
      """Initialize the alien ship and set its starting position."""
      super().__init__()
      self.screen = ai_game.screen
      
      # Load the alien ship image and set its rect attribute
      self.image = pygame.image.load('images/alien_ship.bmp')
      self.rect = self.image.get_rect()
      
      # Start each new alien ship near the top left of the screen
      self.rect.x = self.rect.width
      self.rect.y = self.rect.height
      
      # Store the alien ship's exact horizontal position
      self.x = float(self.rect.x)