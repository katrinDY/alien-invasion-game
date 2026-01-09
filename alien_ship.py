import pygame

class AlienShip:
  """A class to manage the alien ship"""
  
  def __init__(self, ai_game):
    self.screen = ai_game.screen
    self.screen_rect = ai_game.screen.get_rect()
  
    # Load the alien ship and get its rect
    self.image = pygame.image.load('images/alien_ship_damaged.bmp')
    self.rect = self.image.get_rect()
  
    # Start each new ship at the bottom center of the screen
    self.rect.midbottom = self.screen_rect.midbottom
  
  def blitme(self):
    """Draw the ship at its current location"""
    self.screen.blit(self.image, self.rect)