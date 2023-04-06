import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 1200
HEIGHT = 900

FRAMERATE = 100


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

class Player(pygame.sprite.Sprite):
    def __init__(self, xpos=0, ypos=0, move_keys=[pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]):
        super().__init__()
        
        # Load all player animations.
        self.idle_images = create_animation("player_img/Owlet_Monster_Idle_4.png", 4, 32, 32, 3)
        self.up_images = create_animation("player_img/Owlet_Monster_Jump_8.png", 8, 32, 32, 3)
        self.down_images = self.idle_images
        self.right_images = create_animation("player_img/Owlet_Monster_Run_6.png", 6, 32, 32, 3)

        self.left_images = []
        for image in self.right_images:
            self.left_images.append(pygame.transform.flip(image, True, False))

        # Set animation interval.
        self.animation_interval = 100
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
    def handle_movement(self, move_dist=2):
        keys = pygame.key.get_pressed()
        if keys[self.move_keys[0]]:  # Up
            self.rect.y -= move_dist
            self.cur_images = self.up_images
            self.animation_interval = 0.1*FRAMERATE
        elif keys[self.move_keys[1]]:  # Down
            self.rect.y += move_dist
            self.cur_images = self.down_images
            self.animation_interval = 0.05*FRAMERATE
        elif keys[self.move_keys[2]]:  # Left
            self.rect.x -= move_dist
            self.cur_images = self.left_images
            self.animation_interval = 0.05*FRAMERATE
        elif keys[self.move_keys[3]]:  # Right
            self.rect.x += move_dist
            self.cur_images = self.right_images
            self.animation_interval = 0.05*FRAMERATE
        else:
            self.cur_images = self.idle_images
            self.animation_interval = 0.15*FRAMERATE

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
        self.handle_movement()
        self.animate()

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
    while running:
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
