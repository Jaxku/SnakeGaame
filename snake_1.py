import pygame
import time
import random
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
yellow = (255, 255, 0)

# Fonts for the game
score_font = pygame.font.SysFont("arialblack", 25)
exit_font = pygame.font.Font("freesansbold.ttf", 30)
msg_font = pygame.font.SysFont("arialblack", 20)

clock = pygame.time.Clock()  # control the frame rate of the game,
# which will be used to control the speed of the snake


# Function to display message on screen
def message(msg, txt_colour, bkgd_colour):
    txt = msg_font.render(msg, True, txt_colour, bkgd_colour)

    # Center rectangle: 1000/2 = 500, 720/2 = 360
    text_box = txt.get_rect(center=(500, 360))
    screen.blit(txt, text_box)


# function to run the main game loop
def game_loop():
    quit_game = False
    game_over = False

    # snake will be 20x20 pixels
    snake_x = 490   # Centre point horizontally is (1000-20)/2 = 490
    snake_y = 350   # Centre point vertically is (720-2)/2 = 350

    snake_x_change = 0  # holds the value of changes in the x-coordinate
    snake_y_change = 0  # holds the value of changes in the y-coordinate

    # Setting a random position for the food - start
    food_x = round(random.randrange(0, 1000 - 20) / 20) * 20
    food_y = round(random.randrange(0, 720 - 20) / 20) * 20

    while not quit_game:
        # gives user the option to quit or play again when they die
        while game_over:
            screen.fill(white)
            message("You Died! Game Over, "
                    "Press 'Q' or Quit or 'A' to play again"
                    , black, white)
            pygame.display.update()

            # Check if user wants to quit or play again
            for even in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit_game = True
                        game_over = False
                    if event.key == pygame.K_a:
                        game_loop()  # restart the main game loop

        # Original set-up for arrow keys to move the snake
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

        if snake_x >= 1000 or snake_x < 0 or snake_y >= 720 or snake_y < 0:
            game_over = True

        snake_x += snake_x_change
        snake_y += snake_y_change

        screen.fill(green)  # changes screen (surface) from the default black to green

        # create rectangle for snake
        pygame.draw.rect(screen, red, [snake_x, snake_y, 20, 20])
        pygame.display.update()

        # create circle for food
        pygame.draw.circle(screen, yellow, [food_x, food_y], 10)
        pygame.display.update()

        # Collison detection (test if snake touches food)
        if snake_x == food_x and snake_y == food_y - 10:
            # Set new random position for food in snake touches it
            food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
            food_y = round(random.randrange(20, 720 - 20) / 20) * 20

        clock.tick(5)  # 5 frames per second


pygame.quit()
quit()

# Main routine
game_loop()
