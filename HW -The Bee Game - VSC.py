import pygame
import random
pygame.init()

screen = pygame.display.set_mode((500,600))
score = 0
game_over = False

theif = pygame.image.load("C:/Users/User/Desktop/images/theif.png")
money = pygame.image.load("C:/Users/User/Desktop/images/money.png")
night = pygame.image.load("C:/Users/User/Desktop/images/night.png")

theif_rect = theif.get_rect()
theif_rect.topleft = (100,100)

money_rect = money.get_rect()

def place_money():
    money_rect.x = random.randint(0, 500 - money_rect.width)
    money_rect.y = random.randint(0, 400 - money_rect.height)

place_money()

def draw():
    screen.blit(night,(0,0))
    screen.blit(money, money_rect)
    screen.blit(theif, theif_rect)

    score_text = f'Score is {score}'
    font = pygame.font.SysFont(None,45)
    score_surface = font.render(score_text, True, (255,255,255))
    screen.blit(score_surface, (10,10))

    if game_over:
      screen.fill(0,0,0)
      game_over_text =print(f'You got {score} dollars')
      game_over_surface = font.render(game_over_text, True, (455,455,455))
      screen.blit(game_over_surface)

    pygame.display.flip()

def handle_movement():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        theif_rect.x -=2
    if keys[pygame.K_RIGHT]:
        theif_rect.x +=2
    if keys[pygame.K_DOWN]:
        theif_rect.y +=2
    if keys[pygame.K_UP]:
        theif_rect.y -=2
      
def check_collisions():
    global score
    if theif_rect.colliderect(money_rect):
        score +=10
        place_money()

running = True
pygame.time.set_timer(pygame.USEREVENT, 60000)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            game_over = True

    handle_movement()
    check_collisions()
    draw()


pygame.quit()



    
