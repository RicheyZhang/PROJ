import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
font = pygame.font.Font('../Assets/font/Pixeltype.ttf', 50)

# fling animation (snail)
snail_vel_x = 0
snail_vel_y = 0
snail_hit = False

# # fling animation (hit)
# hit_surface_x = 0
# hit_surface_y = 0
# hit_surface_x = False


show_hit_timer = 0

sky_surface = pygame.image.load('../Assets/graphics/Sky.png').convert()
ground_surface = pygame.image.load('../Assets/graphics/ground.png').convert()
text_surface = font.render('', False, 'Black')

snail_surface = pygame.image.load('../Assets/graphics/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomleft = (600, 300)) # builds snail hitbox



player_surf = pygame.image.load('../Assets/graphics/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300)) 
player_gravity = 0

hit_surface = font.render('HIT!', False, 'Red')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (300, 50))
    

    snail_rect.x -= 4
    if snail_rect.x < -100: snail_rect.x = 800
    screen.blit(snail_surface, snail_rect)

    # Player
    if player_rect.right < 0:
        player_rect.left = 800

    player_gravity += 1
    player_rect.y += player_gravity

    if player_rect.bottom >= 300:
        player_rect.bottom = 300
        player_gravity = 0 # reset gravity
    screen.blit(player_surf, player_rect)
    print(player_rect.y)

    # player gravity
    # Character Jump
    keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     player_vel_y = -10 # inital jump 


    #initial fling
    if player_rect.colliderect(snail_rect) and not snail_hit:
        snail_hit = True
        snail_vel_x = 10 # flings right
        snail_vel_y = -13 # flings upward
        show_hit_timer = 30 # shows text for 60 frames
    if show_hit_timer > 0:
        screen.blit(hit_surface, (350, 50))
        show_hit_timer -= 1 # counts down each frame

    # return fling (gravity)
    if snail_hit:
        snail_vel_y += 1 # gravity pulls it down
        snail_rect.x += snail_vel_x
        snail_rect.y += snail_vel_y
    else: 
        snail_rect.x -= 4
        if snail_rect.x < -100:
            snail_rect.x = 800


    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print ("collision")

    

    pygame.display.update()
    clock.tick(60)
