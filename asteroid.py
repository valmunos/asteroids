import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen, 
            color='white',
            center=self.position,
            radius=self.radius,
            width=2
        )

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            vec1 = self.velocity.rotate(angle)
            vec2 = self.velocity.rotate(-angle)
            r_prime = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(x=self.position.x, y=self.position.y, radius=r_prime)
            a1.velocity = vec1 * 1.2
            a2 = Asteroid(x=self.position.x, y=self.position.y, radius=r_prime)
            a2.velocity = vec2 * 1.2
