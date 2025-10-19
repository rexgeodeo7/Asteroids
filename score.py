import pygame
from constants import SHOT_SCORE_ADD
from circleshape import CircleShape

pygame.font.init()
font = pygame.font.SysFont("Arial", 40)

class Score:
    def __init__(self):
        self.score = 1000
        self.surface = font.render(f"Score: {self.score}", True, "white")

    def update(self):
        self.score += SHOT_SCORE_ADD
        self.surface = font.render(f"Score: {self.score}", True, "white")