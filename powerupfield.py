import pygame
import random
from power_ups import *
from constants import MIN_SPAWN_TIME, MAX_SPAWN_TIME, POWER_UP_WIDTH, POWER_UP_HEIGHT, SCREEN_HEIGHT, SCREEN_WIDTH

class PowerUpField(pygame.sprite.Sprite):
    def __init__(self, power_ups_group):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer_interval = random.uniform(MIN_SPAWN_TIME, MAX_SPAWN_TIME)
        self.group = power_ups_group 
        
    def spawn(self, width, height):
        # Generate random coordinates
        x = random.uniform(0, SCREEN_WIDTH)
        y = random.uniform(0, SCREEN_HEIGHT)


        # randomize powerups
        power_up_random_choice = random.choice([Speed, Shield])
        power_up = power_up_random_choice(width, height, x, y)
        # randomizes spawn timer interval again after it hits 0 (aka. spawns a new powerup)
        self.spawn_timer_interval = random.uniform(MIN_SPAWN_TIME, MAX_SPAWN_TIME)

    def update(self, dt):
        if len(self.group) > 0:
            return
        
        self.spawn_timer_interval -= dt

        if self.spawn_timer_interval <= 0:
            self.spawn(POWER_UP_WIDTH, POWER_UP_HEIGHT)