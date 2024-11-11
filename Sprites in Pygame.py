import pygame

pygame.init()

pygame.display.set_caption("Rocket in Space")
width = 700
height = 500
screen = pygame.display.set_mode([width,height])

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/User/Desktop/images/rocket.png")

        self.rect = self.image.get_rect()
    def update(self,pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > width:
            self.rect.right = width

        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom >= height:
            self.rect.bottom = height

sprites = pygame.sprite.Group()
def start_game():
    player = Player()
    sprites.add(player)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        screen.blit(pygame.image.load("C:/Users/User/Desktop/images/bg.png"),(0,0))
        sprites.draw(screen)
        pygame.display.update()

start_game()








            

