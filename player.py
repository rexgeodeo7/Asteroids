import pygame
import sys
from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer =  0 # rate limit
        self.lives = PLAYER_LIVES
        self.iframes = 0
        self.multiplier = 1
        self.speed_powerup_multiplier = 1
        self.speed_powerup_timer = 0
        self.shield_invincibility  = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

        # draw shield if active
        if self.shield_invincibility > 0:
            pygame.draw.circle(screen, "blue", self.position, self.radius + 10, 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        self.timer -= dt
        self.iframes -= dt

        if self.speed_powerup_timer > 0:
            self.speed_powerup_timer -= dt
            if self.speed_powerup_timer <= 0:
                self.speed_powerup_multiplier = 1  # reset when timer expires

        if self.timer <= 0:
            if keys[pygame.K_SPACE]:
                self.shoot()

    def move(self, dt):
        self.multiplier = 1        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LSHIFT]:
            self.multiplier = 2

        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        next_position = self.position + forward * PLAYER_SPEED * dt * self.multiplier * self.speed_powerup_multiplier

        if next_position.x - self.radius < 0: # left border check
            return
        
        if next_position.x + self.radius > SCREEN_WIDTH: # right border check
            return
        
        if next_position.y - self.radius < 0: # top border check
            return
        
        if next_position.y + self.radius > SCREEN_HEIGHT: # bottom border check
            return

        self.position += forward * PLAYER_SPEED * dt * self.multiplier * self.speed_powerup_multiplier # if none of the border cases pop up, this will execute

    def shoot(self):
            velocity = (pygame.Vector2(0, 1).rotate(self.rotation)) * PLAYER_SHOOT_SPEED
            shot = Shot(self.position.x, self.position.y, velocity)
            self.timer = PLAYER_SHOT_COOLDOWN

    def take_damage(self): 
        if self.shield_invincibility <= 0:
            self.lives -= 1
            was_life_lost = True
        else:
            self.shield_invincibility -= 1
            was_life_lost = False

        self.iframes = PLAYER_IFRAMES
        return self.is_dead(), was_life_lost
    
    def is_dead(self):
        if self.lives <= 0:
            return True
        else:
            return False