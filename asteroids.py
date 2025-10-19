import pygame, random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, EXPLOSION_GROWTH_RATE

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.current_explosion_radius = 0
        self.is_exploding = False

    def draw(self, screen):
        if self.is_exploding:
            pygame.draw.circle(screen, "white", self.position, self.current_explosion_radius, 0)
        else:
            pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity*dt)

        if self.is_exploding:
            self.current_explosion_radius += EXPLOSION_GROWTH_RATE * dt
            if self.current_explosion_radius >= self.radius:
                self.split()
                self.kill()

    def split(self):            
        spawn_angle = random.uniform(20, 50)

        velocity1 = self.velocity.rotate(spawn_angle)
        velocity2 = self.velocity.rotate(-spawn_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        new_asteroid1.velocity = velocity1 * 1.2
        new_asteroid2.velocity = velocity2 * 1.2

    def explosion(self):
        self.is_exploding = True