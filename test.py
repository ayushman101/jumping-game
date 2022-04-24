import pygame,sys
from pygame.locals import *

WINDOW_SIZE=(1280,720)  #set window size

pygame.init()   #initialize pygame

clock=pygame.time.Clock()    #get clock 

pygame.display.set_caption("Poseidons Dome")   #set window name

screen=pygame.display.set_mode(WINDOW_SIZE)    #create window with window size 

img=pygame.image.load("6b7e7e672f4a3c82b564aaf6850f6579-boy-with-boombox-pixel-art.png")  #get an image

img_location=[0,0]    # set image location variable

move_right=False
move_left=False

while True:  # game loop
    
    screen.fill((0,0,0))  #fill screen with black colour
    
    screen.blit(img,img_location)   # add image on the window screen at image location

    if move_left==True:   # change x point of location
        img_location[0]-=4   
    if move_right==True:    #change y point of location
        img_location[0]+=4

    
    for event in pygame.event.get():  # event loop 
        if event.type==QUIT:    # if window cross is clicked
            pygame.quit()    # quit pygame
            sys.exit()       # end the script
        
        if event.type==KEYDOWN:   #if a keyboard button was pressed down
            if event.key==K_LEFT:  # check if button was left arrow
                move_left=True
            if event.key==K_RIGHT:  # check if button was right arrow
                move_right=True
        
        if event.type==KEYUP:    # if the keyboard button which was pressed came back up 
            if event.key==K_LEFT:  # check if button was left arrow 
                move_left=False
            if event.key==K_RIGHT:  # if button was right arrow 
                move_right=False
        
    
    pygame.display.update()   #update window
    clock.tick(60)   # fps controller 