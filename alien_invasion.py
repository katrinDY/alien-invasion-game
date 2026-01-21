import sys
import pygame
from settings import Settings
from astronaut_ship import AstronautShip
from astronaut import Astronaut
from alien_ship import AlienShip
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
    self.astronaut = Astronaut(self)
    self.astronaut_ship = AstronautShip(self)
    self.bullets = pygame.sprite.Group()
    self.aliens = pygame.sprite.Group()
    
    self._create_fleet()
    pygame.display.set_caption("Alien Invasion")
    # Set the background color
    self.bg_color = (230, 230, 230)

  def _create_fleet(self):
    """Create a fleet of aliens"""
    # Make an alien.
    alien_ship = AlienShip(self)
    self.aliens.add(alien_ship)

  def run_game(self):
    """Start the main loop for the game"""
    while True:
      self._check_events()
      self.astronaut_ship.update()
      self.bullets.update()
      self._update_bullets()
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
      self.astronaut_ship.moving_right = True
    elif event.key == pygame.K_LEFT:
      # Move the ship to the left
      self.astronaut_ship.moving_left = True
    elif event.key == pygame.K_UP:
      # Move the ship up
      self.astronaut_ship.moving_up = True
    elif event.key == pygame.K_DOWN:
      # Move the ship down
      self.astronaut_ship.moving_down = True
    elif event.key == pygame.K_SPACE:
      self._fire_bullet()
    elif event.key == pygame.K_q:
      sys.exit()

  def _check_keyup_events(self, event):
    """Respond to key release"""
    if event.key == pygame.K_RIGHT:
      self.astronaut_ship.moving_right = False
    elif event.key == pygame.K_LEFT:
      self.astronaut_ship.moving_left = False
    elif event.key == pygame.K_UP:
      self.astronaut_ship.moving_up = False
    elif event.key == pygame.K_DOWN:
      self.astronaut_ship.moving_down = False

  def _fire_bullet(self):
    """Create a new bullet and add it to the bullet group"""
    if len(self.bullets) < self.settings.bullets_allowed:
      new_bullet = Bullet(self)
      self.bullets.add(new_bullet)

  def _update_bullets(self):
    """Update position of bullets and get rid of old bullets"""
    # Update bullet position
    self.bullets.update()

    # Get rid of bullets that have disappeared
    for bullet in self.bullets.copy():
      if bullet.rect.bottom <= 0:
        self.bullets.remove(bullet)

  def update_screen(self):
    # Redraw the screen during each pass through the loop
    self.screen.fill(self.settings.bg_color)
    # Add astronaut ship
    self.astronaut_ship.blitme()
    # Add astronaut character
    self.astronaut.blitme()

    for bullet in self.bullets.sprites():
      bullet.draw_bullet()

    self.aliens.draw(self.screen)

    # Make the most recently drawn screen visible
    pygame.display.flip()

if __name__ == '__main__':
  # Make a game instance and run the game.
  ai = AlienInvasion()
  ai.run_game()