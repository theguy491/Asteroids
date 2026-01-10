import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_RADIUS
from logger import log_state
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    #x = SCREEN_WIDTH/2
    #y = SCREEN_HEIGHT/2
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        clock.tick(60)
        dt = clock.tick(60)
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        player.update(dt)


if __name__ == "__main__":
    main()
