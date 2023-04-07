import pygame

from datetime import datetime, timedelta

from settings import *
from player import Player
from item import Item
from platformbar import PlatformBar


""" Create n_players and add to all_sprites container.
"""
def add_players(all_sprites, n_players=1):
    players = pygame.sprite.Group()

    if n_players >= 1:
        player = Player(500, 0, player_name="Nick")
        all_sprites.add(player)
        players.add(player)

    if n_players >= 2:
        player2 = Player(0, 0, move_keys=[pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d], player_name="Xavier")
        all_sprites.add(player2)
        players.add(player2)

    if n_players >= 3:
        player3 = Player(200, 0, move_keys=[pygame.K_i, pygame.K_k, pygame.K_j, pygame.K_l], player_name="Eke")
        all_sprites.add(player3)
        players.add(player3)

    return players

def add_platformbars(all_sprites):
    platformbars = pygame.sprite.Group()

    locations = [(0, 200), (0, 500), (0, 800), (734, 200), (734, 500), (734, 800)]

    for location in locations:
        platformbar = PlatformBar("platform_img/black_bar.png", location[0], location[1])
        all_sprites.add(platformbar)
        platformbars.add(platformbar)

    return platformbars


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

    # Add black bar sprite to middle of screen.
    platformbar_sprites = add_platformbars(all_sprites)

    # Main game loop.
    running = True
    clock_timer = None
    while running:
        # Stop if quit event is received.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen.
        screen.fill(WHITE)

        # Update all sprite animations/movement.
        all_sprites.update()

        # Make player fall to bottom of screen.
        for player in player_sprites:
            player.rect.y += GRAVITY
            # Stop falling at platformbar.
            for platformbar in platformbar_sprites:
                # Make sprite that is a pixel at the bottom of the player position.
                player_bottom = pygame.sprite.Sprite()
                player_bottom.image = pygame.Surface((1, 1))
                player_bottom.rect = player_bottom.image.get_rect()
                player_bottom.rect.x = player.rect.x + player.rect.width/2
                player_bottom.rect.y = player.rect.y + player.rect.height

                # Check if player_bottom collides with platformbar, and stop falling.
                if pygame.sprite.collide_rect(player_bottom, platformbar):
                    player.rect.y = platformbar.rect.y - player.rect.height

            # Stop falling at bottom.
            if player.rect.y >= HEIGHT - player.rect.height:
                player.rect.y = HEIGHT - player.rect.height

        # Check for collisions.
        for player in player_sprites:
            for apple in apple_sprites:
                if pygame.sprite.collide_rect_ratio(0.6)(player, apple):
                    player.score += 1

                    apple_sprites.remove(apple)
                    all_sprites.remove(apple)

        # Add player name above player.
        for player in player_sprites:
            font = pygame.font.SysFont('arial', 16)
            text = font.render(player.name + " ["+str(player.score)+"]", True, BLACK)
            text_rect = text.get_rect()
            text_rect.center = (player.rect.x+40, player.rect.y - 5)
            screen.blit(text, text_rect)

        clock_now = datetime.now()
        # Add apple every few seconds.
        if clock_timer is None or clock_now >= clock_timer:
            apple = Item("item_img/apple.png")
            all_sprites.add(apple)
            apple_sprites.add(apple)

            clock_timer = clock_now + timedelta(seconds = 8)

        # Redraw/update screen.
        all_sprites.draw(screen)
        pygame.display.flip()

        # Clear terminal and write score to terminal.
        print("\033c", end="")
        for player in player_sprites:
            print(player.name, player.score)

        clock.tick(FRAMERATE)

    pygame.quit()

if __name__ == "__main__":
    init_gameboard()
