import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500,500))

alien = pygame.image.load("C:/Users/User/Desktop/images/rock.png")
background = pygame.image.load("C:/Users/User/Desktop/images/bg.png")

alien_rect = alien.get_rect()
alien_rect.x = 150
alien_rect.y = 150

message = ""
font = pygame.font.Font(None,30)



def draw():
    screen.blit(background,(0,0))
    screen.blit(alien, alien_rect)
    text_surface = font.render(message, True, (255,255,255))
    screen.blit(text_surface,(200,10))
    pygame.display.flip()

def place_alien():
    alien_rect.x = random.randint(50,450)
    alien_rect.y = random.randint(50,450)

place_alien()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if alien_rect.collidepoint(pos):
                message = "Got em'"
                place_alien()
            else:
                message = "So close, yet so far."

    draw()

pygame.quit()

    
