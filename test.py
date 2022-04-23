import pygame,sys
from pygame.locals import *

WINDOW_SIZE=(1280,720)  #set window size

pygame.init()   #initialize pygame

clock=pygame.time.Clock()    #get clock 

pygame.display.set_caption("Poseidons Dome")   #set window name

screen=pygame.display.set_mode(WINDOW_SIZE)    #create window with window size 

img=pygame.image.load("IMG_20211122_165544.jpg")  #get an image

img_location=(0,0)    # set image location variable

screen.blit(img,img_location)   # add image on the window screen at image location

while True:  # game loop 
    for event in pygame.event.get():  # event loop 
        if event.type==QUIT:    # if window cross is clicked
            pygame.quit()    # quit pygame
            sys.exit()       # end the script
    
    pygame.display.update()   #update window
    clock.tick(60)   # fps controller 