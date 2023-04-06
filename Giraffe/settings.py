
from app import *

BLACK = (0, 0, 0)


class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def getting_image(self, frame, width, height, scale, colour):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)

        return image

    def animation(self, sprite, steps):
        animation_list = []
        for x in range(steps):
            animation_list.append(self.getting_image(x, 32, 32, 3, BLACK))
        return animation_list


class FPS:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Verdana", 20)
        self.text = self.font.render(str(self.clock.get_fps()), True, (255, 255, 255))

    def render(self, display):
        self.text = self.font.render(str(self.clock.get_fps()), True, (255, 255, 255))
        display.blit(self.text, (725, 3))

    def frame(self):
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame += 1
            last_update = current_time
            if frame >= len(idle_list):
                frame = 0

