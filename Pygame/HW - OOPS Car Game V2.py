import pygame
import random

pygame.init()

pygame.display.set_caption("Coin Car")
width = 800
height = 600
screen = pygame.display.set_mode([width, height])
fps = 60
total_game_time = 60
initial_score = 0
initial_lives = 3

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

car_imgs = [
    pygame.image.load("C:/Users/User/Desktop/images/car.png"),
    pygame.image.load("C:/Users/User/Desktop/images/car2.png"),
    pygame.image.load("C:/Users/User/Desktop/images/car3.png"),
]
coin_img = pygame.image.load("C:/Users/User/Desktop/images/coin.png")
fire_img = pygame.image.load("C:/Users/User/Desktop/images/fire.png")
bg_imgs = [
    pygame.image.load("C:/Users/User/Desktop/images/road.jpg"),
    pygame.image.load("C:/Users/User/Desktop/images/road2.jpg"),
    pygame.image.load("C:/Users/User/Desktop/images/road3.jpg"),
]
powerup_img = pygame.image.load("C:/Users/User/Desktop/images/petrol.png")

font = pygame.font.SysFont("verdana", 36)


class Car(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        self.image = car_imgs[0]
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height - 80)
        self.base_speed = 7

    def reset_position(self):
        self.rect.center = (width // 2, height - 80)

    def update(self, pressed_keys):
        if pressed_keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.base_speed
        if pressed_keys[pygame.K_RIGHT] and self.rect.right < width:
            self.rect.x += self.base_speed
        if pressed_keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.base_speed
        if pressed_keys[pygame.K_DOWN] and self.rect.bottom < height:
            self.rect.y += self.base_speed


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - self.rect.width)
        self.rect.y = random.randint(-100, -40)

    def update(self):
        self.rect.y += 3
        if self.rect.top > height:
            self.rect.y = random.randint(-100, -40)
            self.rect.x = random.randint(0, width - self.rect.width)


class Fire(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = fire_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - self.rect.width)
        self.rect.y = random.randint(-150, -50)
        self.speed = 5

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > height:
            self.rect.y = random.randint(-150, -50)
            self.rect.x = random.randint(0, width - self.rect.width)


class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = powerup_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - self.rect.width)
        self.rect.y = random.randint(-200, -100)

    def update(self):
        self.rect.y += 3
        if self.rect.top > height:
            self.rect.y = random.randint(-200, -100)
            self.rect.x = random.randint(0, width - self.rect.width)


def display_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


def start_game():
    score = initial_score
    lives = initial_lives
    running = True
    clock = pygame.time.Clock()
    level = 1
    elapsed_time = 0
    current_bg = pygame.transform.scale(bg_imgs[0], (width, height))

    car = Car(level)
    sprites = pygame.sprite.Group(car)
    coins = pygame.sprite.Group(Coin() for _ in range(4))
    fires = pygame.sprite.Group(Fire() for _ in range(5))
    powerups = pygame.sprite.Group(PowerUp() for _ in range(1))

    while running:
        dt = clock.tick(fps) / 1000
        elapsed_time += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pressed_keys = pygame.key.get_pressed()
        car.update(pressed_keys)
        coins.update()
        fires.update()
        powerups.update()

        coins_collided = pygame.sprite.spritecollide(car, coins, False)
        if coins_collided:
            score += 5 * len(coins_collided)
            for coin in coins_collided:
                coin.rect.y = random.randint(-100, -40)
                coin.rect.x = random.randint(0, width - coin.rect.width)

        fires_collided = pygame.sprite.spritecollide(car, fires, True)
        if fires_collided:
            lives -= 1
            if lives == 0:
                screen.fill(black)
                display_text("Game Over", red, width // 2, height // 2)
                pygame.display.flip()
                pygame.time.wait(2000)
                running = False

        powerups_collided = pygame.sprite.spritecollide(car, powerups, True)
        if powerups_collided:
            lives += len(powerups_collided)
            powerups.add(PowerUp())

        if score >= 50 and level == 1:
            level = 2
            current_bg = pygame.transform.scale(bg_imgs[1], (width, height))
            car.image = car_imgs[1]
            car.reset_position()
            for fire in fires:
                fire.speed += 1
            screen.fill(black)
            display_text(f"Level {level}", white, width // 2, height // 2)
            pygame.display.flip()
            pygame.time.wait(1000)

        elif score >= 100 and level == 2:
            level = 3
            current_bg = pygame.transform.scale(bg_imgs[2], (width, height))
            car.image = car_imgs[2]
            car.reset_position()
            fires = pygame.sprite.Group(Fire() for _ in range(7))
            for fire in fires:
                fire.speed += 2
            screen.fill(black)
            display_text(f"Level {level}", white, width // 2, height // 2)
            pygame.display.flip()
            pygame.time.wait(1000)

        if elapsed_time >= total_game_time:
            screen.fill(black)
            if level < 3:
                display_text("Game Over", red, width // 2, height // 2)
            else:
                display_text("You WON!", white, width // 2, height // 2)
            pygame.display.flip()
            pygame.time.wait(1000)
            running = False

        screen.blit(current_bg, (0, 0))
        sprites.draw(screen)
        coins.draw(screen)
        fires.draw(screen)
        powerups.draw(screen)

        display_text(f"Lives: {lives}", white, 100, 30)
        display_text(f"Score: {score}", white, 100, 70)
        display_text(f"Time: {int(total_game_time - elapsed_time)}s", white, 100, 110)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    start_game()
