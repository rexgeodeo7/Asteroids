import pygame
import sys
from constants import *
from player import Player
from asteroids import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from circleshape import CircleShape


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        # Draw all possible drawable objects
        for thing in drawable:
            thing.draw(screen)

        updatable.update(dt)

        # Bullet -> Asteroid hit check
        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collision_check(bullet) is True:
                    asteroid.kill()
                    bullet.kill()

        # Game over check
        for asteroid in asteroids:
            if player.collision_check(asteroid) is True:
                print("Game Over!")
                sys.exit()

        pygame.display.flip()

        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()
