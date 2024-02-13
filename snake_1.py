import pygame
import time
pygame.init()

screen = pygame.display.set_mode((1000, 720))
game_icon = pygame.image.load('snake.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption('Snake')

# Colours for use in game
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 155, 0)

# Fonts for the game
score_font = pygame.font.SysFont("arialblack", 25)
exit_font = pygame.font.Font("freesansbold.ttf", 30)

clock = pygame.time.Clock()  # control the frame rate of the game,
# which will be used to control the speed of the snake

quit_game = False

# snake will be 20x20 pixels
snake_x = 490   # Centre point horizontally is (1000-20)/2 = 490
snake_y = 350   # Centre point vertically is (720-2)/2 = 350

snake_x_change = 0  # holds the value of changes in the x-coordinate
snake_y_change = 0  # holds the value of changes in the y-coordinate

while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -20
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = 20
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = 0
                snake_x_change = -20
            elif event.key == pygame.K_DOWN:
                snake_y_change = 0
                snake_x_change = 20



    snake_x += snake_x_change
    snake_y += snake_y_change

    screen.fill(green)  # changes screen (surface) from the default black to green

    # create rectangle for snake
    pygame.draw.rect(screen, red, [snake_x, snake_y, 20, 20])
    pygame.display.update()

    clock.tick(5)  # 5 frames per second

pygame.quit()
quit()
