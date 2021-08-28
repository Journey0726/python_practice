import pygame
import sys
from pygame.locals import * 
pygame.init()

size = width, height =1500,900
speed =[2,1]

bg= (255,255,255)
fullscreen =False
screen =pygame.display.set_mode(size)

pygame.display.set_caption('I love you ')

turtle = pygame.image.load(r'D:\PYthon\练习\res\cat1.png')
position =turtle.get_rect()
l_head=turtle
r_head=turtle = pygame.transform.flip(turtle, True, False)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key ==K_LEFT:
                turtle=r_head
                speed=[-1,0]
            if event.key ==K_RIGHT:
                turtle=l_head
                speed=[1,0]
            if event.key ==K_UP:
                speed=[0,-1]
            if event.key ==K_DOWN:
                speed=[0,1]
            if event.key == K_F11:
                fullscreen = not fullscreen
                if fullscreen :
                    size=width,height=1920,1080
                    screen =pygame. display.set_mode((size),FULLSCREEN|HWSURFACE)
                else:
                    size=width,height=1500,900
                    screen=pygame.display.set_mode(size)
    position =position.move(speed)
    
    if position.left<0 or position.right >width:
        turtle = pygame.transform.flip(turtle, True, False)
        speed[0]=-speed[0]

    if position.top<0 or position.bottom >height:
        speed[1]=-speed[1]


    screen.fill(bg)
    screen.blit(turtle,position)
    pygame.display.flip()
    pygame.time.delay(5)


