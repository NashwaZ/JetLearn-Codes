import pgzrun
import random

WIDTH = 600
HEIGHT = 800


player = Actor("player")
player.x = WIDTH/2
player.y = HEIGHT - 100



obstacles = []
obstacle_types = ["rock", "offside", "slide"]
game_over = False

bg_y = -700
lives = 3

def update():
    global game_over, bg_y, lives
    
    if game_over:
        return
    else:
        if keyboard.left and player.left > 0:
            player.x -= 6
        if keyboard.right and player.right < WIDTH:
            player.x += 6

        if random.randint(0, 50) == 0:
            new_obs = Actor(random.choice(obstacle_types))
            new_obs.x = random.randint(50, WIDTH - 50)
            new_obs.y = -50
            obstacles.append(new_obs)

        for obstacle in obstacles:
            obstacle.y += 10
            if player.colliderect(obstacle):
                lives -=1
                obstacles.remove(obstacle)
            if obstacle.top > HEIGHT:
                obstacles.remove(obstacle)

        if lives == 0:
            game_over = True
        
        if bg_y < 0:
            bg_y +=5
        else:
            bg_y = -700



    


def draw():
    global game_over, bg_y
    screen.clear()
    screen.blit('bg4', (0,bg_y))
    
    player.draw()

    for obstacle in obstacles:
        obstacle.draw()
        
    screen.draw.text(f"LIVES: {lives}", (15,15), color = 'red', fontsize= 30)
    if game_over:
        screen.draw.text("GAME OVER", center=(WIDTH/2, HEIGHT/2), color="red", fontsize=80)


pgzrun.go()