import pygame

""" Convert a spritesheet to a single frame image.
"""
def get_spritesheet_frame(sheet, frame_nr, width, height, scale):
    image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
    image.blit(sheet, (0,0), (frame_nr*width, 0, width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    return image


""" Create an animation which is a list of images.
"""
def create_animation(path, n_steps, width, height, scale):
    sheet = pygame.image.load(path).convert_alpha()

    # Convert sheet to animation.
    animation_list = []
    for frame_nr in range(n_steps):
        animation_list.append(get_spritesheet_frame(sheet, frame_nr, width, height, scale))

    return animation_list