# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
import player, circleshape

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clk = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player1 = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        dt = clk.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        player1.draw(screen)
        pygame.display.flip()
        


if __name__ == "__main__":
    main()
