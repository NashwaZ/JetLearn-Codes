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
bg_img1 = pygame.image.load("C:/Users/User/Desktop/images/volc.png")
bg_img2 = pygame.image.load("C:/Users/User/Desktop/images/volc2.png")
bg_img3 = pygame.image.load("C:/Users/User/Desktop/images/volc3.png")

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
    level = 1
    rock_chance = 0.007
    game_timer = 0
    current_bg = bg_img1

    player = Player()
    sprites = pygame.sprite.Group(player)
    rocks = pygame.sprite.Group()

    while running:
        clock.tick(fps)
        game_timer +=1
        elapsed_time = game_timer // fps

        if elapsed_time == 15 and level == 1:
            level = 2
            rock_chance += 0.002
            current_bg = bg_img2
            for rock in rocks:
                rock.speed +=0.5
                display_text(f"Level {level}", white, width//2, height //2)
                pygame.display.flip()
                pygame.time.wait(100)
        elif elapsed_time == 30 and level == 2:
            level = 3
            rock_chance += 0.002
            current_bg = bg_img3
            for rock in rocks:
                rock.speed +=0.5
                display_text(f"Level {level}", white, width//2, height //2)
                pygame.display.flip()
                pygame.time.wait(100)
        if elapsed_time == 45:
            display_text("You Beat all the ROCKS!", white, width//2, height //2)
            pygame.display.flip()
            pygame.time.wait(1000)
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        if random.random() < rock_chance:
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
                display_text("You have annilihated by the rocks.", white, width//2, height//2)
                pygame.display.flip()
                pygame.time.wait(1000)
                running = False

        screen.blit(current_bg,(0,0))
        sprites.draw(screen)
        rocks.draw(screen)

        lives_text = font.render(f"Lives: {lives}", True, white)
        level_text = font.render(f"Level {level}", True, white)
        time_text = font.render(f"{elapsed_time}", True, white)
        screen.blit(lives_text,(10,10))
        screen.blit(level_text,(10,50))
        screen.blit(time_text,(10,90))


        pygame.display.flip()
    
    pygame.quit()

def display_text(text,color,x,y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x,y))
    screen = pygame.display.set_mode([width, height])
    screen.blit(text_surface, text_rect)

start_game()


        
        

            








