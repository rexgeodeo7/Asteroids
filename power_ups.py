import pygame
from squareshape import SquareShape 
from constants import MIN_SPAWN_TIME, POWERUP_SPEED_MULTIPLIER, POWERUP_SHIELD_HITS, POWER_UP_HEIGHT, POWER_UP_WIDTH

class Speed(SquareShape):
    def __init__(self, width, height, x, y):
        super().__init__(width, height, x, y)
        self.is_taken = False

    def draw(self, screen):
        power_up = pygame.draw.rect(screen, "white", (self.position.x - (POWER_UP_WIDTH / 2), self.position.y - (POWER_UP_HEIGHT / 2), POWER_UP_WIDTH, POWER_UP_HEIGHT), 0)

    def update(self, dt):
        if self.is_taken:
            self.kill()

    def power_up(self, player):
        player.speed_powerup_multiplier = POWERUP_SPEED_MULTIPLIER
        player.speed_powerup_timer = MIN_SPAWN_TIME

class Shield(SquareShape):
    def __init__(self, width, height, x, y):
        super().__init__(width, height, x, y)
        self.is_taken = False

    def draw(self, screen):
        power_up = pygame.draw.rect(screen, "blue", (self.position.x - (POWER_UP_WIDTH / 2), self.position.y - (POWER_UP_HEIGHT / 2), POWER_UP_WIDTH, POWER_UP_HEIGHT), 0)

    def update(self, dt):
        if self.is_taken:
            self.kill()

    def power_up(self, player):
        player.shield_invincibility = POWERUP_SHIELD_HITS
