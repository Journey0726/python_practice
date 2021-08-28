import pygame
import sys

pygame.init()

size = width, height =1800,1000
speed =[0,-5]
bg= (255,200,255)

screen =pygame.display.set_mode(size)

pygame.display.set_caption('I love you ')

turtle = pygame.image.load(r'D:\PYthon\练习\res\cat1.png')
turtle = pygame.transform.rotate(turtle,-90)
turtle=pygame.transform.flip(turtle,False,True)
position =turtle.get_rect()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

    position =position.move(speed)

    if position.left<0 :
        turtle = pygame.transform.rotate(turtle, -90)
        position=turtle_rect=turtle.get_rect()
        position.top=height-turtle_rect.height
        speed=[0,-5]
        

    if position.right>width:
        turtle = pygame.transform.rotate(turtle, -90)
        position=turtle_rect=turtle.get_rect()
        position.left=width-turtle_rect.width
        speed=[0,5]
    
    if position.top<0 :
        turtle = pygame.transform.rotate(turtle, -90)
        position=turtle_rect=turtle.get_rect()
        speed=[5,0]
    if position.bottom>height:
        turtle = pygame.transform.rotate(turtle,-90)
        position=turtle_rect=turtle.get_rect()
        position.left=width-turtle_rect.width
        position.top=height-turtle_rect.height
        speed=[-5,0]


        

    screen.fill(bg)
    screen.blit(turtle,position)
    pygame.display.flip()
    pygame.time.delay(5)


