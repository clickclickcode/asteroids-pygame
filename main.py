import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    # initializing pygame
    pygame.init()

    clock = pygame.time.Clock()

    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    

    # groups for sprites
    updatable = pygame.sprite.Group()

    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    shots = pygame.sprite.Group()

    # adding instances of the player class to the groups
    Player.containers = (updatable, drawable)

    Asteroid.containers = (updatable, drawable, asteroids)

    AsteroidField.containers = (updatable)

    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid_field = AsteroidField()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0, 0, 0))

        for sprite in updatable:
            sprite.update(dt)

        for sprite in asteroids:
            if player.collision_check(sprite):
                print("Game over!")
                sys.exit()

        for sprite in asteroids:
            for shot in shots:
                if shot.collision_check(sprite):
                    sprite.split()
                    shot.kill()

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        dt_ms = clock.tick(60)

        dt = dt_ms / 1000

if __name__ == "__main__":
    main()