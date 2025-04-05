# python libraries
import pygame, random
# project libraries
import circleshape
from constants import *

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, 2)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return # asteroid too small to split
        random_angle = random.uniform(20, 50)
        new_asteroid_1_velocity = self.velocity.rotate(random_angle)
        new_asteroid_2_velocity = self.velocity.rotate(-random_angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(*self.position, radius)
        new_asteroid_1.velocity = new_asteroid_1_velocity * 1.2
        new_asteroid_2 = Asteroid(*self.position, radius)
        new_asteroid_2.velocity = new_asteroid_2_velocity * 1.2
