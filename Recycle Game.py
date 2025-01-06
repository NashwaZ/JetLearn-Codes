import pygame
import random
import time
from pygame.locals import *

def change_bg(img):
    background = pygame.image.load(img)
    bg = pygame.transform.scale(background,(screen_width,screen_height))
    screen.blit(bg,(0,0))

pygame.init()
pygame.display.caption("Recycle Game")
screen_width = 900
screen_height = 700
screen = pygame.display.set_mode([screen_width,screen_height])

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bin.png")
        self.image = pygame.transform.scale(self.image,(40,60))
        self.rect = pygame.image.get_rect()

class recyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = pygame.image.get_rect()
    
class not_recyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("plastic.png")
        self.image = pygame.transform.scale(self.image,(40,40))
        self.rect = pygame.image.get_rect()

images = ["item1.png","item2.png","item3.png"]
item_list = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
plastic_list = pygame.sprite.Group()

for i in range(50):
    item = recyclable(random.choice(images))
    item.rect.x = random.randrange(screen_width)
    item.rect.y = random.randrange(screen_height)
    item_list.add(item)
    all_sprites.add(item)
for i in range(20):
    plastic = not_recyclable()
    plastic.rect.x,y = random.randrange(screen_width,screen_height)
    #plastic.rect.y = random.randrange(screen_height)
    plastic_list.add(plastic)
    all_sprites.add(plastic)

bin = Bin()
all_sprites.add(bin)

white = (255,255,255)
red = (255,0,0)
playing = True
score = 0
clock = pygame.time.Clock()
start_time = time.time()
myFont = pygame.font.SysFont("Times new roman", 22)
timingFont = pygame.font.SysFont("Times new roman", 22)
text = myFont.render("score = " + str(0),True, white)

while playing:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    time_elapsed = time.time() - start_time
    if time_elapsed >= 60:
        if score > 50:
            text = myFont.render("Bin Loot successful", True, red)
            change_bg("winscreen.jpg")
        else:
            change_bg("losescreen.png")
            
        screen.blit(text,(250,40))
    else:
        change_bg("background.png")
        countdown = timingFont.render("time left" +str(60-int(time_elapsed)), True, white)
        screen.blit(countdown,(20,10))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if bin.rect.y > 0:
                bin.rect.y -=5
        if keys[pygame.K_DOWN]:
            if bin.rect.y < 630:
                bin.rect.y += 5
        if keys[pygame.K_RIGHT]:
            if bin.rect.x < 850:
                bin.rect.x += 5
        if keys[pygame.K_LEFT]:
            if bin.rect.x > 0:
                bin.rect.x -= 5      






