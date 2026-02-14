import pgzrun
import random

WIDTH = 800
HEIGHT = 600


gravity = 2000


class Ball():
    def __init__(self,intial_x,intial_y):
        self.x = intial_x
        self.y = intial_y

        self.vx = random.randint(100,200)
        self.vy = 0
        self.radius = random.randint(20,90)
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    def draw(self):
        pos = (self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,self.color)
    def update(self,dt):
        self.vy += gravity*dt
        self.y += self.vy*dt
        if self.y > HEIGHT-self.radius:
            self.y = HEIGHT-self.radius
            self.vy = -self.vy*0.7
        self.x += self.vx*dt
        if self.x > WIDTH-self.radius or self.x < self.radius:
            self.vx = -self.vx

ball1 = Ball(100,100)
ball2 = Ball(200,200)
ball3 = Ball(400,100)

def draw():
    screen.clear()
    ball1.draw()
    ball2.draw()
    ball3.draw()

def update(dt):
    ball1.update(dt)
    ball2.update(dt)
    ball3.update(dt)

def on_key_down(key):
    if key == keys.SPACE:
        ball1.vy = -1000
        ball2.vy = -500
        ball3.vy = -1500
pgzrun.go()    




    