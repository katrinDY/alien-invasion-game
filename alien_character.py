import pygame

class AlienCharacter:
  """A class dedicated to the alien character"""
  
  def __init__(self, ai_game):
    self.screen = ai_game.screen
    self.screen_rect = ai_game.screen.get_rect()
    
    # Load alien character and its rect
    self.image = pygame.image.load('images/alien_character.bmp')
    self.rect = self.image.get_rect()
    
    # Add character to the bottom left corner of the screen
    self.rect.bottomleft = self.screen_rect.bottomleft
    
  def blitme(self):
    """Add the character to the desired position"""
    self.screen.blit(self.image, self.rect)