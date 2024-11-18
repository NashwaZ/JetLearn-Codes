import pygame
import random
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
fps = 60
screen_width = 864
screen_height = 936
screen = pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption("Flappy Bird")
font = pygame.font.SysFont('Arial',60)
white = (255,255,255)
ground_scroll = 0
scroll_speed = 4
flying = False
game_over = False
pipe_gap = 150
pip_frequency = 1500
last_pipe = pygame.time.get_ticks() - pip_frequency
scroll = 0
pass_pipe = False

background = pygame.image.load("C:/Users/User/Desktop/images/bg.png")
ground = pygame.image.load("C:/Users/User/Desktop/images/ground.png")
restart_button = pygame.image.load("C:/Users/User/Desktop/images/restart.png")

