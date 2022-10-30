import sys
import time
import pygame
import config as cfg
from paddle import Paddle
from ball import Ball
from brick import Brick
from game_menu import *
from pygame.locals import *
import random


pygame.init()
count = 1
score = cfg.SCORE
time_duration_count = cfg.TIME_DURATION_COUNT
font = pygame.font.SysFont(None, 30)

#life = 3

# set window size
size = (cfg.WINDOW_WIDTH, cfg.WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Shoot Astroid Game")
balls = []
bg = pygame.image.load("./images/james.jpg")

# this will be a list that will contain all the sprites we intend
all_sprites_list = pygame.sprite.Group()
all_bricks = pygame.sprite.Group()


def paddle_and_ball_initialization():
    # Create the paddle
    paddle = Paddle(cfg.LIGHTBLUE, 100, 50)
    paddle.rect.x = 350
    paddle.rect.y = 560
    screen.blit(paddle.image, paddle.rect)

    # Create the ball sprite

    ball = Ball(cfg.RED, 10, 10)
    ball.rect.x = 400
    ball.rect.y = 560

    balls.append(ball)
    all_sprites_list.add(paddle)

    return paddle, ball


def brick_design_on_display():

    matrix_show = random.choice(cfg.matrix)
    colors = [cfg.RED, cfg.ORANGE, cfg.YELLOW, cfg.GREEN]
    for i in range(7):
        for j in range(4):
            if(matrix_show[i][j] == 1):
                brick = Brick(colors[j], 80, 30)
                brick.rect.x = 60 + i * 100
                brick.rect.y = 100+j*40 + time_duration_count
                all_sprites_list.add(brick)
                all_bricks.add(brick)

    return all_bricks


def score_and_time_duration_calucation(score, time_duration_count):
    font = pygame.font.Font(None, 34)
    text = font.render("Astroid: "+str(score), 1, cfg.YELLOW)
    screen.blit(text, (20, 10))
    text = font.render("Time Pass: "+str(time_duration_count), 1, cfg.YELLOW)
    screen.blit(text, (610, 10))


def game_win_function(score, time_duration_count):
    font = pygame.font.Font(None, 65)
    text = font.render("Win, Congratulations!", 1, cfg.WHITE)
    screen.blit(text, (200, 200))
    pygame.display.flip()
    player_score_and_time_show_in_display(score, time_duration_count)
    pygame.time.wait(3000)


def player_score_and_time_show_in_display(score, time_duration_count):
    font = pygame.font.Font(None, 45)
    text = font.render('Astroid Destroyed: '+str(score), 1, cfg.YELLOW)
    screen.blit(text, (250, 300))
    pygame.display.flip()

    text = font.render(
        'Total Time: '+str(abs(time_duration_count)), 1, cfg.GREEN)
    screen.blit(text, (250, 350))
    pygame.display.flip()


def game_over_function(score, time_duration_count):
    font = pygame.font.Font(None, 74)
    text = font.render("You Lost", 1, cfg.WHITE)
    screen.blit(text, (250, 150))
    pygame.display.flip()

    player_score_and_time_show_in_display(score, time_duration_count)

    pygame.time.wait(3000)
    # game_on()


def brick_and_ball_collision_detection(ball, brick, score, time_duration_count):
    ball.bounce()
    ball.kill()
    brick.kill()
    balls.remove(ball)

    if len(all_bricks) == 0:
        game_win_function(score, time_duration_count)
        carryOn = False
        return carryOn


def ball_fire_to_bricks_from_paddle(ball, paddle, score, time_duration_count):
    # ball=Ball(WHITE,10,10)
   # print("yes")
    all_sprites_list.add(ball)
    ball.rect.x = paddle.rect.x+50
    ball.rect.y = paddle.rect.y
    balls.append(ball)

    number_list = [-19, 0, 19]
    # random item from list
    # print(random.choice(number_list))
    num = random.choice(number_list)
    for brick in all_bricks:
        brick.rect.x += num
        brick.rect.y += 1

    if brick.rect.y > 550:
        game_over_function(score, time_duration_count)
        carryOn = False
        return carryOn


def game_end_display_function(clock, score, time_duration_count):
    # screen.fill(cfg.DARKBLUE)
    screen.blit(bg, (0, 0))
    pygame.draw.line(screen, cfg.WHITE, [0, 38], [800, 38], 2)
    all_sprites_list.draw(screen)

    score_and_time_duration_calucation(score, time_duration_count)
    pygame.display.flip()
    clock.tick(100)


def aircraft_shooter_game_screen(carryOn, all_sprites_list, all_bricks, paddle, ball, balls, clock, score, time_duration_count):

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            paddle.moveRight(5)
        if keys[pygame.K_DOWN]:
            paddle.moveDown(5)

        if keys[pygame.K_UP]:
            paddle.moveUp(5)

        if keys[pygame.K_SPACE]:
            print("yes")
            game_end = ball_fire_to_bricks_from_paddle(
                ball, paddle, score, time_duration_count)
            if game_end == False:
                carryOn = False

        all_sprites_list.update()
        for ball in balls:
            brick_collision_list = pygame.sprite.spritecollide(
                ball, all_bricks, False)
            for brick in brick_collision_list:
                score += 1
                game_end = brick_and_ball_collision_detection(
                    ball, brick, score, time_duration_count)
                if game_end == False:
                    carryOn = False

        time_duration_count += 1
        game_end_display_function(clock, score, time_duration_count)
    all_sprites_list.empty()
    all_bricks.empty()
    game_loop()


def game_on():
    carryOn = True
    # clock=pygame.time.Clock()
    all_bricks = brick_design_on_display()
    paddle, ball = paddle_and_ball_initialization()
    aircraft_shooter_game_screen(carryOn, all_sprites_list, all_bricks,
                                 paddle, ball, balls, clock, score, time_duration_count)


def game_loop():
    # make a game start menu program
    #clock = pygame.time.Clock()
    bg2 = pygame.image.load("./images/james2.jpg")
    font = pygame.font.SysFont(None, 30)
    screen = pygame.display.set_mode(
        (cfg.WINDOW_WIDTH, cfg.WINDOW_HEIGHT), 0, 32)
    click = False
    while True:
        #screen.fill((0, 190, 255))
        screen.blit(bg2, (0, 0))
        draw_text('Shoot Astroid', pygame.font.SysFont(
            None, 45), (0, 255, 255), screen, 300, 100)
        mx, my = pygame.mouse.get_pos()

        # creating buttons
        button_1 = pygame.Rect(300, 200, 200, 50)
        button_2 = pygame.Rect(300, 300, 200, 50)
        button_3 = pygame.Rect(300, 400, 200, 50)

        # defining functions when a certain button is pressed
        if button_1.collidepoint((mx, my)):
            if click:
                game_on()
        if button_2.collidepoint((mx, my)):
            if click:
                options(screen, font, clock, click)

        if button_3.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        pygame.draw.rect(screen, (255, 0, 0), button_3)

        # writing text on top of button
        draw_text('Play', font, (255, 255, 255), screen, 370, 220)
        draw_text('Game Control', font, (255, 255, 255), screen, 330, 315)
        draw_text('Exit', font, (255, 255, 255), screen, 370, 420)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)


clock = pygame.time.Clock()

if __name__ == "__main__":

    game_loop()
