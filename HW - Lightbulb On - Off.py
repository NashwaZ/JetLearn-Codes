import pygame
import os
pygame.init()

screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

navy_blue = (0, 0, 128)

lightbulb_on = pygame.image.load(os.path.join("C:/Users/User/Desktop/images","on.png")) 
lightbulb_off = pygame.image.load(os.path.join("C:/Users/User/Desktop/images","off.png"))  

show_lightbulb_on = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RCTRL:  
                show_lightbulb_on = True
            elif event.key == pygame.K_LCTRL:  
                show_lightbulb_on = False

   
    screen.fill(navy_blue)

    if show_lightbulb_on:
        screen.blit(lightbulb_on, (200, 200))
    else:
        screen.blit(lightbulb_off, (200, 200))

    pygame.display.flip()

pygame.quit()
