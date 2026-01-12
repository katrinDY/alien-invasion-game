import sys
import pygame
from settings import Settings
from alien_ship import AlienShip
from alien_character import AlienCharacter
from bullet import Bullet

class AlienInvasion:
  """Overall class to manage game assets and behavior"""
  
  def __init__(self):
    """Initialize the game and create game resources"""
    pygame.init()
    self.settings = Settings()
    self.screen = pygame.display.set_mode(
      (self.settings.screen_width, self.settings.screen_height)
    )
    self.alien_ship = AlienShip(self)
    self.bullets = pygame.sprite.Group()
    self.alien_character = AlienCharacter(self)
    pygame.display.set_caption("Alien Invasion")
    # Set the background color
    self.bg_color = (230, 230, 230)

  def run_game(self):
    """Start the main loop for the game"""
    while True:
      self._check_events()
      self.alien_ship.update()
      self.bullets.update()

      # Get rid of bullets that are no longer visible on the screen
      for bullet in self.bullets.copy():
        if bullet.rect.bottom <= 0:
          self.bullets.remove(bullet)

      self.update_screen()

  def _check_events(self):
    # Respond to keypress and mouse events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        self._check_keydown_events(event)
      elif event.type == pygame.KEYUP:
        self._check_keyup_events(event)

  def _check_keydown_events(self, event):
    """Respond to key press"""
    if event.key == pygame.K_RIGHT:
      # Move the ship to the right
      self.alien_ship.moving_right = True
    elif event.key == pygame.K_LEFT:
      # Move the ship to the left
      self.alien_ship.moving_left = True
    elif event.key == pygame.K_UP:
      # Move the ship up
      self.alien_ship.moving_up = True
    elif event.key == pygame.K_DOWN:
      # Move the ship down
      self.alien_ship.moving_down = True
    elif event.key == pygame.K_SPACE:
      self._fire_bullet()
    elif event.key == pygame.K_q:
      sys.exit()

  def _check_keyup_events(self, event):
    """Respond to key release"""
    if event.key == pygame.K_RIGHT:
      self.alien_ship.moving_right = False
    elif event.key == pygame.K_LEFT:
      self.alien_ship.moving_left = False
    elif event.key == pygame.K_UP:
      self.alien_ship.moving_up = False
    elif event.key == pygame.K_DOWN:
      self.alien_ship.moving_down = False

  def _fire_bullet(self):
    """Create a new bullet and add it to the bullet group"""
    if len(self.bullets) < self.settings.bullets_allowed:
      new_bullet = Bullet(self)
      self.bullets.add(new_bullet)

  def update_screen(self):
    # Redraw the screen during each pass through the loop
    self.screen.fill(self.settings.bg_color)
    # Add alien ship
    self.alien_ship.blitme()
    # Add alien character
    self.alien_character.blitme()

    for bullet in self.bullets.sprites():
      bullet.draw_bullet()

    # Make the most recently drawn screen visible
    pygame.display.flip()

if __name__ == '__main__':
  # Make a game instance and run the game.
  ai = AlienInvasion()
  ai.run_game()