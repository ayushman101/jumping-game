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

#text_surf=text.render('MY GAME',False,'white')
#text_rect=text_surf.get_rect(center=(400,50))

snail_surf=pygame.transform.rotozoom(pygame.image.load('snail1.png').convert_alpha(),0,0.75)
snail_rect=snail_surf.get_rect(midbottom=(700,300))

player_surf=pygame.image.load('player_stand.png').convert_alpha()
player_rect=player_surf.get_rect(bottomleft=(10,300))

player_stand=pygame.transform.rotozoom(pygame.image.load('player_stand.png').convert_alpha(),0,2)
player_stand_rect=player_stand.get_rect(center=(400,200))

screen_message=text.render('Jumper Game',False,'White')
screen_message_rect=screen_message.get_rect(center=(400,50))

screen_message2=text.render('Press Space to Jump',False,'#ffffff')
screen_message2_rect=screen_message2.get_rect(center=(400,350))       

snail_x=[700,270]

game_score=0


game_active=0


player_gravity=0

while True:

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if game_active:    
            if event.type==KEYDOWN:
                if event.key==K_SPACE:
                    if player_rect.bottom > 270:
                        player_gravity=-20
            
    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surf,(0,300))
        #pygame.draw.rect(screen,'pink',text_rect,5)
    
        #pygame.draw.rect(screen,'pink',text_rect)
        #screen.blit(text_surf,text_rect)
        
        snail_rect.left -=4
        if snail_rect.right< 0:
            snail_rect.left=800

        if player_rect.colliderect(snail_rect):
            snail_rect.left=800
            game_active=0



        screen.blit(snail_surf,snail_rect)

        player_rect.y+=player_gravity
        player_gravity+=1

        if player_rect.bottom>=300:
            player_rect.bottom=300
        screen.blit(player_surf,player_rect)

        game_score+=1
        current_score=(int)(game_score/60)
        score_text=text.render(f'Score: {current_score}',False,'#000000')
        score_rect=score_text.get_rect(center=(400,50))

        screen.blit(score_text,score_rect)

    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        screen.blit(screen_message,screen_message_rect)

        if game_score:
            score_text=text.render(f'Score: {current_score}',False,'#ffffff')
            score_rect=score_text.get_rect(center=(400,350))
            screen.blit(score_text,score_rect)
        else:
            screen.blit(screen_message2,screen_message2_rect)
       
        keys=pygame.key.get_pressed()

        if keys[pygame.K_SPACE] :
            game_active=1
            game_score=0

    pygame.display.update()
    clock.tick(60)
