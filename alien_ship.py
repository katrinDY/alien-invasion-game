import pygame

class AlienShip:
  """A class to manage the alien ship"""
  
  def __init__(self, ai_game):
    self.screen = ai_game.screen
    self.settings = ai_game.settings
    self.screen_rect = ai_game.screen.get_rect()
  
    # Load the alien ship and get its rect
    self.image = pygame.image.load('images/alien_ship_damaged.bmp')
    self.rect = self.image.get_rect()
  
    # Start each new ship at the bottom center of the screen
    self.rect.midbottom = self.screen_rect.midbottom

    # Store a decimal value for the ship's horizontal position
    self.x = float(self.rect.x)

    # Movement flag
    self.moving_right = False
    self.moving_left = False
  
  def update(self):
    """Update the ship's position based on movement flags"""
    if self.moving_right and self.rect.right < self.screen_rect.right:
      self.x += self.settings.ship_speed
    elif self.moving_left and self.rect.left > 0:
      self.x -= self.settings.ship_speed

    # Update rectangular objects from self.x
    self.rect.x = self.x

  def blitme(self):
    """Draw the ship at its current location"""
    self.screen.blit(self.image, self.rect)