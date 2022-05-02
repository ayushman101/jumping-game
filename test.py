from msilib.schema import Class
import pygame
from sys import exit
from pygame.locals import* 

class Player (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk1=pygame.image.load('player_walk_1.png')
        player_walk2=pygame.image.load('player_walk_2.png')
        
        self.player_walk=[player_walk1,player_walk2]

        self.player_walk_index=0

        self.image=self.player_walk[self.player_walk_index]
        self.rect=self.image.get_rect(midbottom=(40,300))
        self.player_jump=pygame.image.load('jump.png')
        self.gravity=0

    def player_input(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >=300 :
            self.gravity= -20
    
    def apply_gravity(self):
        self.rect.y+=self.gravity
        self.gravity+=1
        if self.rect.bottom>=300 :
            self.rect.bottom=300

    def animation(self):
        if self.rect.bottom < 300 :
            self.image=self.player_jump
        else:
            self.player_walk_index+=0.1
            if self.player_walk_index > len(self.player_walk):
                self.player_walk_index=0
            self.image=self.player_walk[int(self.player_walk_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation()

class obstacle(pygame.sprite.Sprite):
    def __init__(self,type):                      # type argument tells us type of obstacle , fly or a snail 
        super().__init__()
        if type=='fly':
            fly1=pygame.image.load('fly1.png')
            fly2=pygame.image.load('fly2.png')
            self.frames=[fly1,fly2]
            y_pos=210
        else:
            snail1=pygame.image.load('snail1.png')
            snail2=pygame.image.load('snail2.png')
            self.frames=[snail1,snail2]
            y_pos=300
        self.frames_index=0
        self.image=self.frames[self.frames_index]
        self.rect=self.image.get_rect(midbottom=(900,y_pos))

    def animation(self):
        self.frames_index+=0.1
        if self.frames_index > len(self.frames) :
            self.frames_index=0
        self.image=self.frames[int(self.frames_index)]

    def update(self):
        self.animation()



pygame.init()

clock=pygame.time.Clock()

screen=pygame.display.set_mode((800,400))

pygame.display.set_caption('My Game')

sky_surface=pygame.image.load('Sky.png').convert()
ground_surf=pygame.image.load('ground.png').convert()

text=pygame.font.Font('Pixeltype.ttf',50)

#text_surf=text.render('MY GAME',False,'white')
#text_rect=text_surf.get_rect(center=(400,50))

#player group --> single group
player=pygame.sprite.GroupSingle()
player.add(Player())

#obstacle group
obstacle_group=pygame.sprite.Group()


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

        player.update()
        player.draw(screen)

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
        player_gravity=0
        player_rect.bottom=300

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
