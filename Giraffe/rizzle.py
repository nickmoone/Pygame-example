from app import *
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = [
            pygame.image.load('player/Owlet_Monster_Idle_4.png').convert_alpha(),
            pygame.image.load('player/Owlet_Monster_Run_6.png').convert_alpha(),
            pygame.image.load('player/Owlet_Monster_Jump_8.png').convert_alpha()
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect()


def movement(player):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player.rect.x += 10
        player.image = player.images[1]
    elif keys[pygame.K_SPACE]:
        player.rect.y -= 5
        player.image = player.images[2]
    else:
        idle_list = idle_sheet.animation(idle_image, 4)
        screen.blit(idle_list[frame], player_pos)


def main():
    pygame.init()

    width = 1000
    height = 900
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Multiverse of Dash')

    player = Player()

    # spawn position
    player.rect.x = 0
    player.rect.y = 800

    all_sprites = pygame.sprite.Group()
    pygame.sprite.Sprite.add(player, all_sprites)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            movement(player)

            screen.fill((64, 64, 64))
            all_sprites.draw(screen)
            pygame.display.update()

            clock.tick(60)
    pygame.quit()


print(main())
