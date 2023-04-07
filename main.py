import pygame

from datetime import datetime, timedelta

from settings import *
from player import Player
from item import Item


def main():
    # Initialize game.
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sicke game")
    clock = pygame.time.Clock()

    # Initialize players.
    player = Player(0, 0)
    all_sprites = pygame.sprite.Group(player)

    player2 = Player(500, 0, [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d])
    all_sprites.add(player2)

    player3 = Player(0, 500, [pygame.K_i, pygame.K_k, pygame.K_j, pygame.K_l])
    all_sprites.add(player3)

    # Main game loop.
    running = True

    now = datetime.now()
    now_plus_10 = now + timedelta(seconds = 2)

    while running:
        now = datetime.now()

        if now > now_plus_10:
            print("2 seconds have passed")
            now_plus_10 = now + timedelta(seconds = 2)

            apple = Item("item_img/apple.png")
            all_sprites.add(apple)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update()
        player2.update()
        player3.update()

        screen.fill(WHITE)
        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(FRAMERATE)

    pygame.quit()

if __name__ == "__main__":
    main()
