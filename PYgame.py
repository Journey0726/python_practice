import sys
import pygame
pygame.init()
#Vinfo = pygame.display.Info()
size = width,height = 400,600

speed = [1,1]
BLACK = 0,0,0
screen=pygame.display.set_mode(size)
turtle = pygame.image.load(r'D:\PYthon\练习\res\cat1.png')
pygame.display.set_caption('哈哈')
position=turtle.get_rect()
fps = 300
fclock=pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type ==pygame.KEYDOWN:
            if event.key ==pygame.K_LEFT:
                speed[0] =speed[0] if speed[0]==0 else (abs(speed[0]-1))*int(speed[0]/abs(speed[0]))
                print('左')
            if event.key == pygame.K_RIGHT:
                speed[0] = speed[0]+ 1 if speed[0] > 0 else speed[0]-1
                print('右')
            if event.key ==pygame.K_UP:
                speed[1] =speed[1]+ 1  if speed[1]> 0  else speed[1]-1
            if event.key ==pygame.K_DOWN:
                speed[1] =speed[1] if speed[1]==0 else (abs(speed[1]-1))*int(speed[1]/abs(speed[1]))
            if event.key ==pygame.K_ESCAPE:
                sys.exit()
        if event.type==pygame.VIDEORESIZE:
            size = width,height =event.size[0],event.size[1]
            screen = pygame .display.set_mode(size,pygame.RESIZABLE)
    if pygame.display.get_active():
        position = position.move(speed)
    if position.left<0 or position.right>width:
        speed[0]=-speed[0]
    if position.top<0 or position.bottom>height:
         speed[1]=-speed[1]
    screen.fill(BLACK)
    screen.blit(turtle,position)
    pygame.display.flip()
    fclock.tick(fps)