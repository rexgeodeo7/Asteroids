import pygame
from squareshape import SquareShape
from constants import MIN_SPAWN_TIME, POWERUP_SPEED_MULTIPLIER

class Speed(SquareShape):
    def __init__(self, width, height, x, y):
        super().__init__(width, height, x, y)
        self.is_taken = False

    def draw(self, screen):
        power_up = pygame.draw.rect(screen, "white", (self.position.x - (self.width / 2), self.position.y - (self.height / 2), self.width, self.height), 0)

    def update(self, dt):
        if self.is_taken:
            self.kill()

    def power_up(self, player):
        player.speed_powerup_multiplier = POWERUP_SPEED_MULTIPLIER
        player.speed_powerup_timer = MIN_SPAWN_TIME