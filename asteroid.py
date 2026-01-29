import pygame
import random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event
import colors

class Asteroid(CircleShape):
  def __init__(self, x, y, radius, color="white"):
    super().__init__(x, y, radius)
    self.rotation = 0
    self.color = color

  def draw(self, screen):
    pygame.draw.circle(screen, self.color, self.position, self.radius, LINE_WIDTH)

  def update(self, dt):
    self.position += self.velocity * dt

  # Divides each asteroid into 2 chunks
  '''
  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    
    log_event("asteroid_split")
    random_angle = random.uniform(20, 50)

    new_vector1 = self.velocity.rotate(random_angle)
    new_vector2 = self.velocity.rotate(-random_angle)
    
    new_radius = self.radius - ASTEROID_MIN_RADIUS

    new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius, colors.random_color())
    new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius, colors.random_color())

    new_asteroid1.velocity = new_vector1 * 1.2
    new_asteroid2.velocity = new_vector2 * 1.2
  '''
  # Divides asteroids into 2 - 4 chunks randomly
  '''
  def split(self):
      self.kill()
      if self.radius <= ASTEROID_MIN_RADIUS:
          return

      log_event("asteroid_split")

      # Random number of child asteroids
      num_children = random.randint(2, 4)

      new_radius = self.radius - ASTEROID_MIN_RADIUS

      # Spread angles evenly around the original direction
      angle_step = 360 / num_children
      start_angle = random.uniform(0, 360)

      for i in range(num_children):
          angle = start_angle + i * angle_step
          new_velocity = self.velocity.rotate(angle) * 1.2

          new_asteroid = Asteroid(
              self.position.x,
              self.position.y,
              new_radius,
              colors.random_color()
          )

          new_asteroid.velocity = new_velocity
  '''