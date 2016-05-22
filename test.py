import pygame, sys
from pygame.locals import *
from Sprite import Sprite
from random import randrange

running = True
resolution = (640, 980)
player_speed = 4
score        = 0
pipes_speed  = 2
fall_speed   = 3
range_grow   = 150
up = False
dead = False
timer = 0

pygame.init()
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()

background      = pygame.image.load("bg.jpg").convert()
player_image    = pygame.image.load("player.png").convert_alpha()

pipe_down_image = pygame.image.load("Pipe_Down.png").convert_alpha()
pipe_up_image   = pygame.image.load("Pipe_Up.png").convert_alpha()

player_down = pygame.transform.rotate(player_image, -30)
player_dead = pygame.transform.rotate(player_image, -90)

player    = Sprite(player_image, (100, 100))
player.set_gravity(True, fall_speed)


pipe_down = Sprite(pygame.transform.scale(pipe_down_image, (pipe_down_image.get_width(), pipe_down_image.get_height() + randrange(50, range_grow))), (400, 0))
pipe_up   = Sprite(pygame.transform.scale(pipe_up_image, (pipe_up_image.get_width(), pipe_up_image.get_height() - 50)), (400, 520))


pipe_down1 = Sprite(pygame.transform.scale(pipe_down_image, (pipe_down_image.get_width(), pipe_down_image.get_height() + randrange(50, range_grow))), (600, 0))
pipe_up1   = Sprite(pygame.transform.scale(pipe_up_image, (pipe_up_image.get_width(), pipe_up_image.get_height() - 50)), (600, 520))


pipe_down2 = Sprite(pygame.transform.scale(pipe_down_image, (pipe_down_image.get_width(), pipe_down_image.get_height() + randrange(50, range_grow))), (800, 0))
pipe_up2   = Sprite(pygame.transform.scale(pipe_up_image, (pipe_up_image.get_width(), pipe_up_image.get_height() - 50)), (800, 520))

pipe_down3 = Sprite(pygame.transform.scale(pipe_down_image, (pipe_down_image.get_width(), pipe_down_image.get_height() + randrange(50, range_grow))), (1000, 0))
pipe_up3   = Sprite(pygame.transform.scale(pipe_up_image, (pipe_up_image.get_width(), pipe_up_image.get_height() - 50)), (1000, 520))


pipes      = [pipe_down, pipe_up, pipe_down1, pipe_up1, pipe_down2, pipe_up2, pipe_down3, pipe_up3]
pipes_down = [pipe_down, pipe_down1, pipe_down2, pipe_down3]
pipes_up   = [pipe_up, pipe_up1, pipe_up2, pipe_up3]


font = pygame.font.Font("Chango-Regular.ttf", 30)


def pipe_logic():

    for pipe in pipes_down:
        x, y = pipe.get_pos()
        
        if (x < (-pipe_up.get_width()+20) ):

            pipe.set_pos((1000, 0))    
            pipe.set_image(pygame.transform.scale(pipe_down_image, (pipe_down_image.get_width(), pipe_down_image.get_height() + randrange(50, range_grow))))

    for pipe in pipes_up:
        x, y = pipe.get_pos()
        
        if (x < -pipe_up.get_width() + 10):
            pipe.set_pos((1000, 520))



def player_animations():

    if (not dead):
        if (not up):
            player.set_image(player_down)

        else:
            player.set_image(player_image)




def borders():
    global up

    x, y = player.get_pos()

    if (y < 0):
        up = False


    elif (y > 700):
        die()




def die():
    global player_speed, pipes_speed, up, dead

    dead = True

    player_speed = 0
    pipes_speed  = 0
    up = False
    player.set_gravity(True, fall_speed)

    player.set_image(player_dead)
    
        
        
    


while running:

    for event in pygame.event.get():

        if event.type == QUIT:
            running = False
            break

        elif event.type == KEYDOWN:
            if event.key == K_UP:
                up = True

        elif event.type == KEYUP:
            if event.key == K_UP:
                up = False


    screen.blit(background, (0,0) )

    if (not dead):
        player.move(player_speed, up = up)
    
    player.render(screen, not up)


    for pipe in pipes:
        x, y = player.get_pos()
        x1,y1= pipe.get_pos()
        
        if (player.get_collision(pipe)):
            die()

        elif (x > x1 and x < x1+pipe.get_width() and timer > 40):
            score += 1
            timer = 0

        elif (x > x1 and x < x1+pipe.get_width() and timer <= 40):
            timer += 1
            
        if (not dead):
            pipe.move(pipes_speed, left = True)

        pipe.render(screen)

    if (dead):
        die()

    pipe_logic()
    player_animations()
    borders()

    screen.blit(font.render(str(score), True, (255,0,0)), (300,300))

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
sys.exit()
