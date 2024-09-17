import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set display dimensions
dis_width = 600
dis_height = 600

# Create the display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

# Set the game clock
clock = pygame.time.Clock()
blockSize = 30
gameSpeed = 5

# Define font styles
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def displaySnake(blockSize, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], blockSize, blockSize])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    gameOpen = True # Is the game app open?
    gameOver = False # Is the player alive?

    # Initial position of the snake head
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Change in position of the snake head each frame (velocity)
    x1_change = 0
    y1_change = 0

    # List to store snake body segments
    snakeList = []
    snakeLength = 1
    snakeDirection = "left"

    foodX = round(random.randrange(0, dis_width - blockSize) / blockSize) * blockSize
    foodY = round(random.randrange(0, dis_height - blockSize) / blockSize) * blockSize

    while gameOpen:

        while gameOver == True:
            dis.fill(blue)
            message("You lost with a score of {}! Press Q-Quit or C-Play Again".format(snakeLength), red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOpen = False
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOpen = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snakeDirection != "right":
                    x1_change = -blockSize
                    y1_change = 0
                    snakeDirection = "left"
                elif event.key == pygame.K_RIGHT and snakeDirection != "left":
                    x1_change = blockSize
                    y1_change = 0
                    snakeDirection = "right"
                elif event.key == pygame.K_UP and snakeDirection != "down":
                    y1_change = -blockSize
                    x1_change = 0
                    snakeDirection = "up"
                elif event.key == pygame.K_DOWN and snakeDirection != "up":
                    y1_change = blockSize
                    x1_change = 0
                    snakeDirection = "down"

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            gameOver = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodX, foodY, blockSize, blockSize])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snakeList.append(snake_Head)

        # Remove the tail of the snake each frame
        if len(snakeList) > snakeLength:
            del snakeList[0]

        # Check if the snake has collided with itself
        for x in snakeList[:-1]:
            if x == snake_Head:
                gameOver = True

        displaySnake(blockSize, snakeList)
        pygame.display.update()

        # Check if the snake has eaten the food
        if x1 == foodX and y1 == foodY:
            foodX = round(random.randrange(0, dis_width - blockSize) / blockSize) * blockSize
            foodY = round(random.randrange(0, dis_height - blockSize) / blockSize) * blockSize
            snakeLength += 1

        clock.tick(gameSpeed)

    pygame.quit()
    quit()

gameLoop()