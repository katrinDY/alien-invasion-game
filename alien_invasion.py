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
    # Create an alien and find the number of aliens in a row
    # Spacing between each alien is equal to one alien width
    alien_ship = AlienShip(self)
    alien_width, alien_height = alien_ship.rect.size
    alien_width = alien_ship.rect.width
    available_space_x = self.settings.screen_width - (2 * alien_width)
    number_of_aliens_x = available_space_x // (2 * alien_width)
    
    # Determine the number of rows of aliens that fit on the screen
    ship_height = self.astronaut_ship.rect.height
    available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
    number_of_rows = available_space_y // (2 * alien_height)

    # Create the full fleet of aliens
    for row_number in range(number_of_rows):
      for alien_number in range(number_of_aliens_x):
        self._create_alien(alien_number, row_number)

  def _create_alien(self, alien_number, row_number):
    """Create an alien and place it in a row"""
    alien_ship = AlienShip(self)
    alien_width, alien_height = alien_ship.rect.size
    alien_width = alien_ship.rect.width
    alien_ship.x = alien_width + 2.3 * alien_width * alien_number
    alien_ship.rect.x = alien_ship.x
    alien_ship.rect.y = alien_ship.rect.height + 2 * alien_ship.rect.height * row_number
    self.aliens.add(alien_ship)

  def run_game(self):
    """Start the main loop for the game"""
    while True:
      self._check_events()
      self.astronaut_ship.update()
      self.bullets.update()
      self._update_bullets()
      self._update_aliens()
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

  def _update_aliens(self):
    """Update the positions of all aliens in the fleet"""
    self.aliens.update()

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