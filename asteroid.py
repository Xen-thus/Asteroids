import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        width = 2
        pygame.draw.circle(screen, "red", self.position, self.radius, width)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            x, y = self.position
            angle = random.uniform(20, 50)
            vector_a = self.velocity.rotate(angle)
            vector_b = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(x, y, new_radius)
            new_asteroid_1.velocity = vector_a * 1.2
            new_asteroid_2 = Asteroid(x, y, new_radius)
            new_asteroid_2.velocity = vector_b * 1.2