import pgzrun

WIDTH = 600
HEIGHT = 800

player = Actor("player")
player.x = WIDTH/2
player.y = HEIGHT - 100

rock = Actor("rock")
whistle = Actor('whistle')


def draw():
    screen.clear()
    player.draw()




pgzrun.go()