#!venv/bin/python3
# python libraries
import pygame, sys, os
# project libraries
from constants import *
import player, asteroid, asteroidfield

def update(dt, things):
    for thing in things:
        thing.update(dt)

def collide(player, things):
    for thing in things:
        if player.collide(thing):
            return True
            # else, continue

def draw(screen, sprites):
    screen.fill(BLACK)
    for sprite in sprites:
        sprite.draw(screen)
    pygame.display.flip()

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # delta time
    fps = 60 # frames per second

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)
    player_one = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid.Asteroid.containers = (updatable, drawable, asteroids)
    asteroidfield.AsteroidField.containers = (updatable)
    asteroidfield.AsteroidField()

    while True:
        # make the window's close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(fps) / 1000 # convert to seconds
        update(dt, updatable)
        if collide(player_one, asteroids):
            print("Game over!")
            sys.exit(0)
        draw(screen, drawable)




if __name__ == "__main__":
    main()