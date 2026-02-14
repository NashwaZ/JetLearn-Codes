import pygame
import random

pygame.init()

pygame.display.set_caption("Sprite Catch")
width = 639
height = 360
screen = pygame.display.set_mode([width, height])

background_image = pygame.image.load("C:/Users/User/Desktop/images/clouds.jpg")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/User/Desktop/images/ninja.png")
        self.rect = self.image.get_rect()
        self.speed = 0.1

    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -1)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(1, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom >= height:
            self.rect.bottom = height

class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice(fruit_images)
        self.rect = self.image.get_rect()
        self.place_randomly()

    def place_randomly(self):
        self.rect.x = random.randint(0, width - self.rect.width)
        self.rect.y = random.randint(0, height - self.rect.height)

fruit_images = [
    pygame.image.load("C:/Users/User/Desktop/images/apple.png"),
    pygame.image.load("C:/Users/User/Desktop/images/fig.png"),
    pygame.image.load("C:/Users/User/Desktop/images/kumquat.png"),
    pygame.image.load("C:/Users/User/Desktop/images/papaya.png"),
    pygame.image.load("C:/Users/User/Desktop/images/coconut.png"),
    pygame.image.load("C:/Users/User/Desktop/images/apricot.png")
]

player = Player()
sprites = pygame.sprite.Group()
sprites.add(player)

fruit = Fruit()
fruits = pygame.sprite.Group()
fruits.add(fruit)

score = 0
font = pygame.font.SysFont(None, 36)

def start_game():
    global score
    running = True
    while running:
        screen.blit(background_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        if pygame.sprite.spritecollide(player, fruits, True):
            score += 1
            new_fruit = Fruit()
            fruits.add(new_fruit)

        sprites.draw(screen)
        fruits.draw(screen)

        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

    pygame.quit()

start_game()
