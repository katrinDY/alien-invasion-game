import pygame

class Astronaut:
  """A class dedicated to the astronaut character (the player) in the game."""
  
  def __init__(self, ai_game):
    self.screen = ai_game.screen
    self.screen_rect = ai_game.screen.get_rect()
    
    # Load astronaut character and its rect
    self.image = pygame.image.load('images/astronaut.bmp')
    self.rect = self.image.get_rect()
    
    # Add character to the bottom left corner of the screen
    self.rect.bottomleft = self.screen_rect.bottomleft
    
  def blitme(self):
    """Add the character to the desired position"""
    self.screen.blit(self.image, self.rect)