import pygame
from constants import SHOT_SCORE_ADD

pygame.font.init()
font = pygame.font.SysFont("Arial", 30)

class Score:
    def __init__(self):
        self.score = 1000
        self.surface = font.render(f"Score: {self.score}", True, "white")

    def update(self):
        self.score += SHOT_SCORE_ADD
        self.surface = font.render(f"Score: {self.score}", True, "white")

class Lives:
    def __init__(self):
        self.lives = 3
        self.surface = font.render(f"Lives: {self.lives}", True, "white")

    def update(self):
        self.lives -= 1
        self.surface = font.render(f"Lives: {self.lives}", True, "white")