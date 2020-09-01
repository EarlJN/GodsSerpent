import pygame
import time
from pygame.locals import *
import random


pygame.init()

# Game Audio
game_music = pygame.mixer.Sound('Gamefiles/gamesong.ogg')

# Game Sprites
snake_head = pygame.image.load('Gamefiles/SHead00.png')
snake_tail = pygame.image.load('Gamefiles/STail00.png')
game_background = pygame.image.load('Gamefiles/background.png')
game_icon = pygame.image.load('Gamefiles/gameicon.png')
start_background = pygame.image.load('Gamefiles/StartBackground.png')
apple = pygame.image.load('Gamefiles/Holywaterapple.png')

gDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('God\'s Serpent')
FPS = 15
TZ = pygame.time.Clock()

# Colors
white = (255, 255, 255)
red = (255, 000, 000)
light_green = (0, 105, 0)
dark_green = (0, 255, 0)
body_color = (0, 155, 0)
light_gray = (105, 105, 105)
dark_gray = (192, 192, 192)
black = (0, 0, 0)

# Window Size
width = 800
height = 600
blocks = 20

# Text Fonts and Sizes
small_font = pygame.font.Font("Gamefiles/scaryfont.ttf", 25)
medium_font = pygame.font.Font("Gamefiles/scaryfont.ttf", 50)
large_font = pygame.font.Font("Gamefiles/scaryfont.ttf", 150)  # Font Style
play_button = pygame.font.Font("Gamefiles/playgamebutton.otf", 20)

# Directions
direction = "right"


def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        show_message("PAUSED", white, -100, size="large")
        show_message("press c to continue or q to quit", white, 25)

        pygame.display.update()
        TZ.tick(5)


def score(score):
    txt = medium_font.render("Score: " + str(score), True, white)
    gDisplay.blit(txt, [0, 0])


def spawn_apple():
    apple_x = round(random.randrange(0, width - blocks))
    apple_y = round(random.randrange(0, height - blocks))

    return apple_x, apple_y


def start_menu():
    smenu = True

    while smenu:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gDisplay.blit(start_background, [0, 0])
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        pygame.draw.rect(gDisplay, light_gray, (550, 450, 100, 50))
        # The most ghetto way ive ever done in to my code
        if 150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(gDisplay, dark_green, (150, 450, 100, 50))
            if 150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
                if click[0] == 1:
                    start_game()

        else:
            pygame.draw.rect(gDisplay, light_green, (150, 450, 100, 50))

        if 550 + 100 > mouse[0] > 500 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(gDisplay, dark_gray, (550, 450, 100, 50))

            if 550 + 100 > mouse[0] > 500 and 450 + 50 > mouse[1] > 450:
                if click[0] == 1:
                    pygame.quit()
                    quit()

        show_message("Play                                        ", black, y_dis=175, size="mediumButton")
        show_message("                                        Quit", black, y_dis=175, size="mediumButton")

        # pygame.draw.rect(gDisplay , fGray , (550,450,100,50))
        show_message("                                        Quit", black, y_dis=175, size="mediumButton")

        pygame.display.update()
        TZ.tick(15)


def txt_objects(text, color, size):
    if size == "small":
        text_surface = small_font.render(text, True, color)
    elif size == "medium":
        text_surface = medium_font.render(text, True, color)
    elif size == "mediumButton":
        text_surface = play_button.render(text, True, color)
    elif size == "large":
        text_surface = large_font.render(text, True, color)

    return text_surface, text_surface.get_rect()


def show_message(msg, color, y_dis=0, size="small"):
    text_surf, text_rect = txt_objects(msg, color, size)
    text_rect.center = (width / 2), (height / 2) + y_dis
    gDisplay.blit(text_surf, text_rect)


def serpent(block, lists):
    if direction == "right":
        head = pygame.transform.rotate(snake_head, 270)
    if direction == "left":
        head = pygame.transform.rotate(snake_head, 90)
    if direction == "up":
        head = snake_head
    if direction == "down":
        head = pygame.transform.rotate(snake_head, 180)

    gDisplay.blit(head, (lists[-1][0], lists[-1][1]))

    for XY in lists[:-1]:
        pygame.draw.rect(gDisplay, body_color, [XY[0], XY[1], block, block])


def start_game():
    pygame.mixer.Sound.play(game_music)
    game_quit = False
    game_over = False
    global direction
    direction = "right"

    x_line = width / 2

    y_line = height / 2

    x_move = 20

    y_move = 0

    snake_length = []

    starting_length = 1

    apple_x, apple_y = spawn_apple()

    while not game_quit:

        while game_over == True:
            gDisplay.fill(black)
            show_message("You Died", red, -50, size="large")
            show_message("Remember Jesus died for your sin , Try again", red, 50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_quit = True
                    game_over = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_quit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        start_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != "right":
                    direction = "left"
                    x_move = - blocks
                    y_move = 0

                elif event.key == pygame.K_RIGHT and direction != "left":
                    direction = "right"
                    x_move = blocks
                    y_move = 0

                elif event.key == pygame.K_UP and direction != "down":
                    direction = "up"
                    y_move = - blocks
                    x_move = 0

                elif event.key == pygame.K_DOWN and direction != "up":
                    direction = "down"
                    y_move = blocks
                    x_move = 0

                elif event.key == pygame.K_p:
                    pause()

        if x_line >= width or x_line < 0 or y_line >= height or y_line < 0:
            game_over = True

        # Game Structs

        x_line += x_move
        y_line += y_move
        gDisplay.blit(game_background, [0, 0])
        d_Apple_Thickness = 30
        gDisplay.blit(apple, (apple_x, apple_y))
        SHead = []
        SHead.append(x_line)
        SHead.append(y_line)
        snake_length.append(SHead)

        if len(snake_length) > starting_length:
            del snake_length[0]

        for eachPixel in snake_length[:-1]:
            if eachPixel == SHead:
                game_over = True

        serpent(blocks, snake_length)

        score(starting_length - 1)
        pygame.display.update()

        if x_line > apple_x and x_line < apple_x + d_Apple_Thickness or x_line + blocks > apple_x and x_line + blocks < apple_x + d_Apple_Thickness:
            if y_line > apple_y and y_line < apple_y + d_Apple_Thickness or y_line + blocks > apple_y and y_line + blocks < apple_y + d_Apple_Thickness:
                apple_x, apple_y = spawn_apple()
                starting_length += 1

            elif y_line + blocks > apple_y and y_line + blocks < apple_y + d_Apple_Thickness:
                apple_x, apple_y = spawn_apple()
                starting_length += 1

        TZ.tick(FPS)

    pygame.quit()
    game_quit()


def main():
    start_menu()


if __name__ == "__main__":
    main()


