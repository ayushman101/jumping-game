import pygame
from sys import exit
from pygame.locals import* 

pygame.init()

clock=pygame.time.Clock()

screen=pygame.display.set_mode((800,400))

pygame.display.set_caption('My Game')

sky_surface=pygame.image.load('Sky.png').convert()
ground_surf=pygame.image.load('ground.png').convert()

text=pygame.font.Font('Pixeltype.ttf',50)

text_surf=text.render('MY GAME',False,'black')

snail_surf=pygame.image.load('snail1.png').convert_alpha()
snail_rect=snail_surf.get_rect(midbottom=(700,300))

player_surf=pygame.image.load('player_stand.png').convert_alpha()
player_rect=player_surf.get_rect(bottomleft=(10,300))

snail_x=[700,270]

while True:

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surf,(0,300))
    screen.blit(text_surf,(350,50))

    
    snail_rect.left -=4

    if snail_rect.right< 0:
        snail_rect.left=800

    if player_rect.colliderect(snail_rect):
        print('collision')

    screen.blit(snail_surf,snail_rect)
    screen.blit(player_surf,player_rect)



    pygame.display.update()
    clock.tick(60)
