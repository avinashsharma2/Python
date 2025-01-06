import random
import math
import pygame as pg  # importing pygame as pg
from pygame import mixer

# High score
with open("highscore.txt") as f:
    highscore = int(f.read())

# Creating display
pg.init()
screen = pg.display.set_mode((800, 600))

# Background
background = pg.image.load("background.png")

# Title and Icon
pg.display.set_caption("Space Shooters")
icon = pg.image.load("icon.png")
pg.display.set_icon(icon)

# Player
playerImg = pg.image.load("player.png")
playerX = 368  # player's x_co-ordinate
playerY = 480  # player's y_co-ordinate
playerX_change = 0  # change in x co-ordinates when kenemyY is pressed

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pg.image.load("enemy.png"))
    enemyX.append(random.randint(0, 736))  # Enemy's x_co-ordinate
    enemyY.append(random.randint(40, 140))  # Enemy's y_co-ordinate
    enemyX_change.append(random.choice([3, -3]))  # change in x co-ordinates of enemy
    enemyY_change.append(40)  # change in y co-ordinates when kenemyY is pressed

# Bullet
# ready -- we can't see the bullet
# fire -- the bullet is moving
bulletImg = pg.image.load("bullet.png")
bulletX = 0 
bulletY = 480
bulletY_change = 20
bullet_state = "ready"


# creates player
def player(x, y):
    screen.blit(playerImg, (x, y))


# creates enemy
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

# Background music
mixer.music.load("background.mp3")
mixer.music.play(-1)

# draw bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

# Collision detection
def isCollision(bx, bulletY, enemyX, enemyY):
    distance = math.sqrt(math.pow(enemyX-bx,2) + math.pow(enemyY-bulletY,2))
    if distance < 27:
        return True
    else:
        return False
    
# Score of the player
score_value = 0
font = pg.font.Font("jokerman.ttf", 32)
scoreX = 10
scoreY = 10
def show_score(x,y):
    score = font.render("Score : "+str(score_value), True, (255,180,178))
    screen.blit(score, (x, y))
    
# Sounds 
kill_sound = mixer.Sound("explosion.mp3")
bullet_sound = mixer.Sound("laser.mp3")

font_big = pg.font.Font("jokerman.ttf", 72) # changing size for game over
# Game over 
def game_over():
    game_over = font_big.render("GAME OVER", True, (255,180,178))
    screen.blit(game_over, (170, 264))

# Highscore printing
def print_highscore():
    high_score = font.render("Highscore: "+str(highscore), True, (255,180,178))
    screen.blit(high_score, (250, 375))
# Game loop so game window does not close
running = True
while running:

    # background colour
    # screen.fill((51, 0, 102))

    # Background
    screen.blit(background, (0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        # Action for pressing a kenemyY
        if event.type == pg.KEYDOWN:
            # When right arrow kenemyY is pressed
            if event.key == pg.K_RIGHT:
                playerX_change = 5
            # When left arrow kenemyY is pressed
            if event.key == pg.K_LEFT:
                playerX_change = -5
            if bullet_state == "ready":
                if event.key == pg.K_SPACE:
                    bullet_sound.play()
                    fire_bullet(bulletX:= playerX, bulletY)

        # Action when kenemyY is released
        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT or event.key == pg.K_LEFT:
                playerX_change = 0
    
    # For 6 enemies
    for i in range(num_of_enemies):
        
        # Game over 
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over()
            print_highscore()
            if highscore < score_value:
                highscore = score_value
                with open("highscore.txt",'w') as f:
                    f.write(str(highscore))
            break
            
        
        # displaying enemy's position
        enemyX[i] += enemyX_change[i]
        
        # lowering enemy's position everytime it hit the boundary
        if enemyX[i] < 0:
            enemyX[i] = 0
            enemyX_change[i] = 3
            enemyY[i] += 64
        elif enemyX[i] > 736:
            enemyX[i] = 736
            enemyX_change[i] = -3
            enemyY[i] += 64
        
        # displaying enemy's current position
        enemy(enemyX[i], enemyY[i],i)
            
        # Collision
        collision = isCollision(bulletX, bulletY, enemyX[i], enemyY[i])
        if collision:
            kill_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736) 
            enemyY[i] = random.randint(40, 140)
        
    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # x co-ordinate boundary
    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736
    player(playerX, playerY)


    # resetting bullet
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    # displaying player's position
    playerX += playerX_change  
    
    # Score 
    show_score(scoreX, scoreY)

    pg.display.update()  # must have to update for every action