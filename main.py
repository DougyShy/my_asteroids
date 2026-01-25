import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_RADIUS
from logger import log_state
from player import Player

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: " + pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Infinite game loop
    while True:
        # Log current game state
        log_state()

        # Start processing the pygame event queue
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return


        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        clock.tick(60)
        dt = clock.tick() / 1000       


if __name__ == "__main__":
    main()
