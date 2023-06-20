import pygame 
from Reptile import PlayerReptile
from Scorpion import PlayerScorpion
import threading
from controls import GameControlls
from sounds import unwisely
from collisions import iScollision

pygame.joystick.init()
pygame.init()
width,height = 1200,650#pyautogui.size()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("game")
clock = pygame.time.Clock()
fps = 60


background_img = pygame.image.load("arenas/desert.jpg")
background_img = pygame.transform.scale(background_img, (width, height))

dps_reptile = "dps/reptile.png"
dps_reptile = pygame.image.load(dps_reptile)

versus = "dps/versus.png"
versus = pygame.image.load(versus)
versus = pygame.transform.rotozoom(versus,0,0.5)

dps_scorpion = "dps/scorpion.png"
dps_scorpion = pygame.image.load(dps_scorpion)

player_reptile = PlayerReptile()
player_scorpion = PlayerScorpion()


lifebar = "dps/bar.png"
lifebar = pygame.image.load(lifebar)

#

green_color = (23, 203, 7)
yellow = (203, 228, 32)

controls = GameControlls()

threading.Thread(target=unwisely,).start()

playing = True 
while playing:
    clock.tick(fps)
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    player_reptile.update(width)
    player_scorpion.update(width)

    screen.blit(background_img,(0,0))
    player_reptile.handle_fireball(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False 
    
        controls.load_keyboard_controlls(event,player_reptile)

        controls.joystick_controlls2(event,player_reptile)
        controls.joystick_controlls_player2(event,player_scorpion)
        controls.joyaxis_controlls(event,player_reptile,player_scorpion)



    screen.blit(dps_reptile,(10,50))
    screen.blit(dps_scorpion,(1050,50))
    screen.blit(versus,(550,50))


    screen.blit(lifebar,(150,70))
    screen.blit(lifebar,(800,70))
    pygame.draw.rect(screen, green_color, pygame.Rect(155,74,250, 15))
    pygame.draw.rect(screen, yellow, pygame.Rect(805,74,250, 15))

    collision = iScollision(player_reptile.rect.x, player_scorpion.rect.x, player_reptile.rect.y, player_scorpion.rect.y)

    
    player_reptile.draw_characters(screen)
    player_scorpion.draw_characters(screen)
    player_reptile.brutality_check()

    pygame.display.update()