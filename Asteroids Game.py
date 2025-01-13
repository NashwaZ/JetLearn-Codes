import pygame
import random

pygame.init()

pygame.display.set_caption("Asteroid Game")
width = 800
height = 600
screen = pygame.display.set_mode([width, height])
initial_lives = 5
score = 0
total_time = 20000

black = (0, 0, 0)
white = (255, 255, 255)
font = pygame.font.SysFont('Verdana', 36)

ship_image = pygame.image.load("C:/Users/User/Desktop/images/alienShip.png")
asteroid_images = [
    pygame.image.load("C:/Users/User/Desktop/images/asteroid50.png"),
    pygame.image.load("C:/Users/User/Desktop/images/asteroid100.png"),
    pygame.image.load("C:/Users/User/Desktop/images/asteroid150.png"),
]
star_image = pygame.image.load("C:/Users/User/Desktop/images/star.png")
bg_image = pygame.transform.scale(pygame.image.load("C:/Users/User/Desktop/images/starbg.png"), (width, height))

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ship_image
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height - 80)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < width:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < height:
            self.rect.y += self.speed

class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice(asteroid_images)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - self.rect.width)
        self.rect.y = random.randint(-100, -40)

    def update(self):
        self.rect.y += 3
        if self.rect.top > height:
            self.rect.x = random.randint(0, width - self.rect.width)
            self.rect.y = random.randint(-100, -40)

class Star(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = star_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - self.rect.width)
        self.rect.y = random.randint(-150, -100)

    def update(self):
        self.rect.y += 2
        if self.rect.top > height:
            self.rect.x = random.randint(0, width - self.rect.width)
            self.rect.y = random.randint(-150, -100)

def start_game():
    score = 0
    lives = initial_lives
    running = True
    start_ticks = pygame.time.get_ticks()

    ship = Ship()
    asteroids = pygame.sprite.Group(Asteroid() for _ in range(5))
    stars = pygame.sprite.Group(Star() for _ in range(3))
    sprites = pygame.sprite.Group(ship, asteroids, stars)

    while running:
        screen.fill(black)
        screen.blit(bg_image, (0, 0))

        elapsed_time = pygame.time.get_ticks() - start_ticks
        time = (total_time - elapsed_time) // 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        sprites.update()

        if pygame.sprite.spritecollide(ship, asteroids, True):
            lives -= 1
            asteroids.add(Asteroid())
            if lives <= 0:
                message = f"Game Over! Your final score was: {score}"
                pygame.time.wait(500)
                screen.fill(black)
                text_surface = font.render(message, True, white)
                text_rect = text_surface.get_rect(center=(width // 2, height // 2))
                screen.blit(text_surface, text_rect)
                pygame.display.flip()
                pygame.time.wait(2000)
                break
            if elapsed_time <= 0:
                message = f"You WON! Your final score was: {score}"
                pygame.time.wait(500)
                screen.fill(white)
                text_surface = font.render(message, True, black)
                text_rect = text_surface.get_rect(center=(width // 2, height // 2))
                screen.blit(text_surface, text_rect)
                pygame.display.flip()
                pygame.time.wait(2000)
                break                

        if pygame.sprite.spritecollide(ship, stars, True):
            score += 10
            stars.add(Star())

        sprites.draw(screen)
        screen.blit(font.render(f"Score: {score}", True, white), (10, 10))
        screen.blit(font.render(f"Lives: {lives}", True, white), (10, 50))
        screen.blit(font.render(f"Time Left: {time}s", True, white), (10, 100))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    start_game()
