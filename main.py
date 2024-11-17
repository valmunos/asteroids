# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print('Starting asteroids!')
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # start writing code
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    field = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0

    # main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill('black')

        for item in updatable:
            item.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print('Game over!')
                sys.exit(0)
            
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()
        
        for item in drawable:
            item.draw(screen)
      
        pygame.display.flip()
        # pygame.display.update()
        dt = clock.tick(60) / 1000


if __name__ == '__main__':
    main()
