import pygame
import random

pygame.init()

pygame.display.set_caption("Dodge the Rock")
width = 800
height = 400
screen = pygame.display.set_mode([width,height])
fps = 60
intial_lives = 5

white = (255,255,255)
black = (0,0,0)

standing_img = pygame.image.load("C:/Users/User/Desktop/images/stand.png")
right_run_img = pygame.image.load("C:/Users/User/Desktop/images/right.png")
left_run_img = pygame.image.load("C:/Users/User/Desktop/images/left.png")
rock_img = pygame.image.load("C:/Users/User/Desktop/images/rock.png")
bg_img = pygame.image.load("C:/Users/User/Desktop/images/volc.png")

font = pygame.font.SysFont('Times new roman',36)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = [standing_img, right_run_img, left_run_img]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (width//2, height-50)
        self.speed = 5
        self.direction = 0
    
    def update(self, pressed_keys):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if self.rect.right < width:
                self.rect.x += self.speed
            self.image = self.images[1]
            self.direction = 1
        elif keys[pygame.K_LEFT]:
            if self.rect.left > 0:
                self.rect.x -= self.speed
            self.image = self.images[2]
            self.direction = 2
        else:
            self.image = self.images[0]
            self.direction = 0
        
class Rock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = rock_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width -40)
        self.rect.y = random.randint(-100,-30)
        self.speed = random.randint(3,8)
        self.gravity = 1
        self.fall_speed = self.speed

    def update(self):
        self.fall_speed += self.gravity
        self.rect.y = self.fall_speed
        if self.rect.top > height:
            self.rect.y = random.randint(-100,-30)
            self.rect.x = random.randint(0, width-40)
            self.fall_speed = self.speed

def start_game():
    lives = intial_lives
    running = True
    clock = pygame.time.Clock()

    player = Player()
    sprites = pygame.sprite.Group(player)
    rocks = pygame.sprite.Group()

    pygame.time.set_timer(pygame.USEREVENT, 30000)

    while running:
        clock.tick(fps)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT:
                display_text("You beat the ROCKS", white, width//2, height//2)
                pygame.display.flip()
                pygame.time.wait(3000)
                running = False
            
        if random.random() < 0.01:
            new_rock = Rock()
            rocks.add(new_rock)

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
            
        rocks.update()
        if pygame.sprite.spritecollide(player, rocks, True):
            lives -= 1
            if lives == 0:
                screen.fill(black)
                pygame.display.flip()
                pygame.time.wait(1000)
                display_text("You have been annilihated by the rocks.", white, width//2, height//2)
                pygame.display.flip()
                pygame.time.wait(3000)
                running = False

        screen.blit(bg_img,(0,0))
        sprites.draw(screen)
        rocks.draw(screen)

        lives_text = font.render(f"Lives: {lives}", True, white)
        screen.blit(lives_text,(10,10))

        pygame.display.flip()
    
    pygame.quit()

def display_text(text,color,x,y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x,y))
    screen = pygame.display.set_mode([width, height])
    screen.blit(text_surface, text_rect)

start_game()


        
        

            








