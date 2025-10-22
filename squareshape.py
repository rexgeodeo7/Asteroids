import pygame

# Base class for power-ups
class SquareShape(pygame.sprite.Sprite):
    def __init__(self, width, height):
            if hasattr(self, "containers"):
                super().__init__(self.containers)
            else:
                super().__init__()
            
            self.width = width
            self.height = height
            self.position = pygame.Vector2(self.width/2, self.height/2) # center coordinates
            self.radius =  (self.width - (self.width/2)) # a work-around around circle radius but with squares for square-circle hitbox collision


    def draw(self, screen):
        # overwriten by children
        pass

    def update(self, dt):
        # overwriten by children
        pass

    def collision_check(self, object2):
        if self.distance_to(object2) < ((self.radius) + (object2.radius)):
            return True
        else:
            return False

    def distance_to(self, object2):
        return pygame.math.Vector2.distance_to(self.position, object2.position)