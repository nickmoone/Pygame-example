import pygame
import glob

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 1200
HEIGHT = 900

""" Creates an animation which is a list of images.
    The animation is made up of all the images at the given path.
"""
def create_animation(path):
    return list(map(pygame.Surface.convert_alpha, list(map(pygame.image.load, glob.glob(path)))))

class Player(pygame.sprite.Sprite):
    def __init__(self, xpos=0, ypos=0, move_keys=[pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]):
        super().__init__()
        
        # Load all player animations.
        self.idle_images = create_animation("idle/*.png")
        self.up_images = create_animation("up/*.png")
        self.down_images = create_animation("down/*.png")
        self.left_images = create_animation("left/*.png")
        self.right_images = create_animation("right/*.png")

        # Set animation interval.
        self.animation_interval = 10
        self.animation_counter = 0

        # Set player image state.
        self.anim_state = 0
        self.cur_images = self.idle_images
        self.image = self.cur_images[self.anim_state]


        self.rect = self.image.get_rect()

        # Set player position.
        self.rect.x = xpos
        self.rect.y = ypos

        # Set movement keys.
        self.move_keys = move_keys


    """ Update player image to next image in animation.
    """
    def animate(self):
        self.animation_counter += 1

        # Go to next step in animation if interval is reached.
        if self.animation_counter >= self.animation_interval:
            self.anim_state += 1
            if self.anim_state >= len(self.cur_images):
                self.anim_state = 0
            self.image = self.cur_images[self.anim_state]

            self.animation_counter = 0

    """ Handle player movement according to button pressed.
    """
    def handle_movement(self, move_dist=10):
        keys = pygame.key.get_pressed()
        if keys[self.move_keys[0]]:
            self.rect.y -= move_dist
            self.cur_images = self.up_images
        elif keys[self.move_keys[1]]:
            self.rect.y += move_dist
            self.cur_images = self.down_images
        elif keys[self.move_keys[2]]:
            self.rect.x -= move_dist
            self.cur_images = self.left_images
        elif keys[self.move_keys[3]]:
            self.rect.x += move_dist
            self.cur_images = self.right_images
        else:
            self.cur_images = self.idle_images

        # Wrap player around screen.
        if self.rect.x > WIDTH:
            self.rect.x = -self.image.get_width()
        elif self.rect.x < 0 - self.image.get_width():
            self.rect.x = WIDTH
        elif self.rect.y > HEIGHT:
            self.rect.y = -self.image.get_height()
        elif self.rect.y < 0 - self.image.get_height():
            self.rect.y = HEIGHT

    def update(self):
        self.handle_movement(10)
        self.animate()

def main():
    # Initialize game.
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sicke game")
    clock = pygame.time.Clock()

    # Initialize player.
    player = Player(0, 0)
    all_sprites = pygame.sprite.Group(player)


    player2 = Player(500, 0, [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d])
    all_sprites.add(player2)

    # Main game loop.
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update()
        player2.update()

        screen.fill(WHITE)
        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()