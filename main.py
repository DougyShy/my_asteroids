import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_RADIUS
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: " + pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    # AsteroidField only updates logic — no drawing
    AsteroidField.containers = (updatable,)


    player = Player(SCREEN_WIDTH / 2.0, SCREEN_HEIGHT / 2.0)

    field = AsteroidField()

    # Infinite game loop
    while True:
        # Log current game state
        log_state()

        # Start processing the pygame event queue
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return
            # I added this but not sure if this is the best escape option for quitting the game. There has to be a better way.
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        dt = clock.tick(60) / 1000 # ← ONE call, at the top or bottom

        screen.fill("black")
        
        for sprite in drawable:
            sprite.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        # player.draw(screen)
        pygame.display.flip()   


if __name__ == "__main__":
    main()
