# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    clk = pygame.time.Clock()
    dt = 0.0
    Player.containers = (updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid = pygame.sprite.Group()
    Asteroid.containers = (asteroid, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()
    

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return



        screen.fill((0, 0, 0))
        
        for obj in updatable:
            obj.update(dt)

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clk.tick(60) / 1000
        



if __name__ == "__main__":
    main()
