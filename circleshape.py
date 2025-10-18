import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision_check(self, circle2):
        if self.distance_to(circle2) < (self.radius + circle2.radius):
            return True
        else:
            return False

    def distance_to(self, circle2):
        return pygame.math.Vector2.distance_to(self.position, circle2.position)