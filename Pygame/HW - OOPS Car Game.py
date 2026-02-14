import pygame
import random

pygame.init()

pygame.display.set_caption("Coin Car")
width = 800
height = 600
screen = pygame.display.set_mode([width, height])
fps = 60
initial_score = 0

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

car_img = pygame.image.load("C:/Users/User/Desktop/images/car.png")
coin_img = pygame.image.load("C:/Users/User/Desktop/images/coin.png")
fire_img = pygame.image.load("C:/Users/User/Desktop/images/fire.png")
bg_img = pygame.image.load("C:/Users/User/Desktop/images/road.jpg")

font = pygame.font.SysFont('Veranda', 36)

class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = car_img
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height - 80)
        self.speed = 7

    def update(self, pressed_keys):
        if pressed_keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if pressed_keys[pygame.K_RIGHT] and self.rect.right < width:
            self.rect.x += self.speed
        if pressed_keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if pressed_keys[pygame.K_DOWN] and self.rect.bottom < height:
            self.rect.y += self.speed

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - 40)
        self.rect.y = random.randint(-100, -40)

    def update(self):
        self.rect.y += 3
        if self.rect.top > height:
            self.rect.y = random.randint(-100, -40)
            self.rect.x = random.randint(0, width - 40)

class Fire(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = fire_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - 40)
        self.rect.y = random.randint(-150, -50)

    def update(self):
        self.rect.y += 5
        if self.rect.top > height:
            self.rect.y = random.randint(-150, -50)
            self.rect.x = random.randint(0, width - 40)

def display_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def start_game():
    score = initial_score
    running = True
    clock = pygame.time.Clock()
    bg_y = 0

    car = Car()
    sprites = pygame.sprite.Group(car)
    coins = pygame.sprite.Group(Coin() for _ in range(4))
    fires = pygame.sprite.Group(Fire() for _ in range(5))

    timer = 30000

    while running:
        clock.tick(fps)
        bg_y = (bg_y + 5) % height

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        timer -= clock.get_time()

        if timer <= 0 or score == 250:
            screen.fill(black)
            display_text("You Won!", green, width // 2, height // 2)
            pygame.display.flip()
            pygame.time.wait(2000)
            running = False

        pressed_keys = pygame.key.get_pressed()
        car.update(pressed_keys)
        coins.update()
        fires.update()

        for coin in coins:
            for other_coin in coins:
                if coin != other_coin and coin.rect.colliderect(other_coin.rect):
                    coin.rect.y -= 50

        for fire in fires:
            for other_fire in fires:
                if fire != other_fire and fire.rect.colliderect(other_fire.rect):
                    fire.rect.y -= 50

        if pygame.sprite.spritecollide(car, coins, True):
            score += 5
            coins.add(Coin())

        if pygame.sprite.spritecollide(car, fires, False):
            screen.fill(black)
            display_text("Game Over", red, width // 2, height // 2)
            pygame.display.flip()
            pygame.time.wait(2000)
            running = False

        screen.blit(bg_img, (0, bg_y - height))
        screen.blit(bg_img, (0, bg_y))
        sprites.draw(screen)
        coins.draw(screen)
        fires.draw(screen)

        score_text = font.render(f"Score: {score}", True, white)
        screen.blit(score_text, (10, 10))

        timer_text = font.render(f"Time: {int(timer / 1000)}s", True, white)
        screen.blit(timer_text, (width - 150, 10))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    start_game()