import pygame
from constants import *
from power_ups import *
from player import Player
from asteroids import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from powerupfield import PowerUpField
from text import Score, Lives
from background import Background

def show_game_over_screen(screen):
    font = pygame.font.SysFont("Arial", 30)

    while True:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        gameover = font.render("Press R to Respawn", False, (255, 255, 255))
        rect = gameover.get_rect()
        rect.center = screen.get_rect().center
        screen.fill("black")
        screen.blit(gameover, rect)

        if keys[pygame.K_r]:
            return
        
        pygame.display.flip()

def game_logic(screen):
    score = Score()
    lives = Lives()

    clock = pygame.time.Clock()
    dt = 0

    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    power_ups = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    PowerUpField.containers = (updatable)
    Speed.containers = (updatable, drawable, power_ups)
    Shield.containers = (updatable, drawable, power_ups)
    Shot.containers = (shots, updatable, drawable)
    Score.containers = (updatable)
    Lives.containers = (updatable)

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    powerup_field = PowerUpField(power_ups)
    BackGround = Background("pixel_background.jpg", [0,0])

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                respawn = False
                return respawn

        screen.fill("black")
        screen.blit(BackGround.image, BackGround.rect)

        # Draw all possible drawable objects
        for thing in drawable:
            thing.draw(screen)

        updatable.update(dt)

        # Bullet -> Asteroid hit check
        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collision_check(bullet) is True:
                    asteroid.explosion()
                    bullet.kill()
                    score.update()

        # Power-ups
        for powerup in power_ups:
            if powerup.collision_check(player):
                powerup.is_taken = True
                powerup.power_up(player)

        # Game over (refactored)
        for asteroid in asteroids:
            if not player.collision_check(asteroid):
                continue 
                
            # iframes check
            if player.iframes >= 0:
                continue

            is_dead, was_life_lost = player.take_damage()
            # is dead check
            if was_life_lost:
                lives.update()
            
            if is_dead:
                respawn = True
                font = pygame.font.SysFont("Arial", 30)
                gameover = font.render("Press R to Respawn", False, (255, 255, 255))
                rect = gameover.get_rect()
                rect.center = screen.get_rect().center
                screen.blit(gameover, rect)
                show_game_over_screen(screen)
                return respawn
            
        screen.blit(score.surface, (0,0))
        screen.blit(lives.surface, ((SCREEN_WIDTH-105),0))
        pygame.display.flip()

        dt = clock.tick(60) / 1000

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    respawn = True

    while respawn is True:
        respawn = game_logic(screen)

if __name__ == "__main__":
    main()