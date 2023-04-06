import pygame.display

from settings import *
from rizzle import *

pygame.init()

BG = (64, 64, 64)
# idle image
screen = pygame.display.set_mode((1000, 800))
idle_image = pygame.image.load('player/Owlet_Monster_Idle_4.png').convert_alpha()
idle_sheet = SpriteSheet(idle_image)

# run image
run_image = pygame.image.load('player/Owlet_Monster_Run_6.png').convert_alpha()
run_sheet = SpriteSheet(run_image)

# jump image
jump_image = pygame.image.load('player/Owlet_Monster_Jump_8.png').convert_alpha()
jump_sheet = SpriteSheet(jump_image)

# idle animation setup
animation_idle_list = []
idle_steps = 4


# animation setup
last_update = pygame.time.get_ticks()
animation_cooldown = 200
frame = 0

idle_sheet.animation(idle_image, 4)
idle_list = []
idle_list = idle_sheet.animation(idle_image, 4)

run_list = []
run_list = run_sheet.animation(run_image, 6)

run = True
while run:

    screen.fill(BG)

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(idle_list):
            frame = 0

    # screen.blit(animation_idle_list[frame], (0, 0))

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                run_list = run_sheet.animation(run_image, 6)
                screen.blit(run_list[frame], player_pos)

        if event.type == pygame.KEYUP:
            idle_list = idle_sheet.animation(idle_image, 4)
            screen.blit(idle_list[frame], player_pos)
    screen.blit(idle_list[frame], player_pos)


    clock.tick(60)

    pygame.display.update()

pygame.quit()
