import pygame,sys
from pygame.locals import *

WINDOW_SIZE=(1280,720)  #set window size

pygame.init()   #initialize pygame

clock=pygame.time.Clock()    #get clock 

pygame.display.set_caption("Poseidons Dome")   #set window name

screen=pygame.display.set_mode(WINDOW_SIZE)    #create window

img=pygame.image.load("IMG_20211122_165544.jpg")

img_location=(0,0)

screen.blit(img,img_location)

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    clock.tick(60)