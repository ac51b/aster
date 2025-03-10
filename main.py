# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    clk = pygame.time.Clock()
    dt = 0.0

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()
    
    Shot.containers = (shots, updatable, drawable)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return



        screen.fill((0, 0, 0))
        
        for obj in updatable:
            obj.update(dt)

        for obj in asteroids:
            for shot in shots:
                if obj.collide(shot):
                    obj.split()
                    shot.kill()
            if obj.collide(player):
                print("Game over!")
                exit()

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clk.tick(60) / 1000
        



if __name__ == "__main__":
    main()
