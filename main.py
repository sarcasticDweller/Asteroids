#!venv/bin/python3
# python libraries
import pygame
# project libraries
from constants import *

def io():
    pass

def update():
    pass

def draw(screen):
    screen.fill((0, 0, 0))
    screen.flip()

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        # make the window's close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        screen.flip()


if __name__ == "__main__":
    main()