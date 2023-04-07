import pygame

from datetime import datetime, timedelta

from settings import *
from player import Player
from item import Item


""" Create n_players and add to all_sprites container.
"""
def add_players(all_sprites, n_players=1):
    players = pygame.sprite.Group()

    if n_players >= 1:
        player = Player(500, 0)
        all_sprites.add(player)
        players.add(player)

    if n_players >= 2:
        player2 = Player(0, 0, [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d])
        all_sprites.add(player2)
        players.add(player2)

    if n_players >= 3:
        player3 = Player(200, 0, [pygame.K_i, pygame.K_k, pygame.K_j, pygame.K_l])
        all_sprites.add(player3)
        players.add(player3)

    return players


def init_gameboard():
    # Initialize game.
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sicke game")
    clock = pygame.time.Clock()

    # Create container that holds sprites and add players.
    all_sprites = pygame.sprite.Group()

    player_sprites = add_players(all_sprites, 3)
    apple_sprites = pygame.sprite.Group()

    # Main game loop.
    running = True
    clock_timer = None
    while running:
        # Stop if quit event is received.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()

        # Check for collisions.
        for player in player_sprites:
            for apple in apple_sprites:
                if pygame.sprite.collide_rect_ratio(0.6)(player, apple):
                    apple_sprites.remove(apple)
                    all_sprites.remove(apple)

        clock_now = datetime.now()

        # Add apple every few seconds.
        if clock_timer is None or clock_now >= clock_timer:
            apple = Item("item_img/apple.png")
            all_sprites.add(apple)
            apple_sprites.add(apple)

            clock_timer = clock_now + timedelta(seconds = 8)

        # Redraw / update screen.
        screen.fill(WHITE)
        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(FRAMERATE)

    pygame.quit()

if __name__ == "__main__":
    init_gameboard()
