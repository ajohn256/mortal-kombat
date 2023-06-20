import pygame 
import threading
from sounds import come_here

class GameControlls:
    def __init__(self):
        pass

    def load_keyboard_controlls(self,event,player_reptile):
        # for event in pygame.event.get():
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_reptile.FLIP_KEY = True
                
            if event.key == pygame.K_DOWN:
                player_reptile.FLIP_KEY_RIGHT = True

            if event.key == pygame.K_LEFT:
                player_reptile.LEFT_KEY,player_reptile.FACING_LEFT = True,True
                # bg.let_background_moveRight = True


            if event.key == pygame.K_RIGHT:
                player_reptile.RIGHT_KEY,player_reptile.FACING_LEFT = True,False
                # bg.let_background_moveLeft = True
            
            if event.key == pygame.K_q:
                player_reptile.SIDE_KICK_LEFT_KEY = True
            
            if event.key == pygame.K_SPACE:
                player_reptile.ESCAPE_KEY = True
                
            if event.key == pygame.K_r:
                player_reptile.SIDE_KICK_RIGHT_KEY = True
                
            if event.key == pygame.K_z:
                player_reptile.STING_VENOM_KEY_LEFT = True
            
            if event.key == pygame.K_x:
                player_reptile.STING_VENOM_KEY_RIGHT = True
            
            if event.key == pygame.K_v:
                player_reptile.LOW_KICK_KEY_RIGHT = True
            
            if event.key == pygame.K_c:
                player_reptile.LOW_KICK_KEY_LEFT = True
            
            if event.key == pygame.K_k:
                player_reptile.FPUNCH_KEY_LEFT = True
            
            if event.key == pygame.K_l:
                player_reptile.FPUNCH_KEY_RIGHT = True
            
            if event.key == pygame.K_RSHIFT:
                player_reptile.swing_KEY_RIGHT = True
            
            if event.key == pygame.K_LSHIFT:
                player_reptile.swing_KEY_LEFT = True
        

    def joystick_controlls2(self,event,player_reptile):
        if event.type == pygame.JOYBUTTONDOWN:
            if pygame.joystick.Joystick(1).get_button(0):#up
                player_reptile.FLIP_KEY_RIGHT = True
                
            if pygame.joystick.Joystick(1).get_button(1):#right
                player_reptile.RIGHT_KEY,player_reptile.FACING_LEFT = True,False
            
            if pygame.joystick.Joystick(1).get_button(2):#down
                player_reptile.FLIP_KEY = True
                
            if pygame.joystick.Joystick(1).get_button(3):#left
                player_reptile.LEFT_KEY,player_reptile.FACING_LEFT = True,True


            if pygame.joystick.Joystick(1).get_button(4):
                if player_reptile.FACING_LEFT:
                    player_reptile.FPUNCH_KEY_LEFT = True
                else:
                    player_reptile.FPUNCH_KEY_RIGHT = True
                
            if pygame.joystick.Joystick(1).get_button(5):
                if player_reptile.FACING_LEFT:
                    player_reptile.swing_KEY_LEFT = True
                else:
                    player_reptile.swing_KEY_RIGHT = True
            
            if pygame.joystick.Joystick(1).get_button(6):#down
                if player_reptile.FACING_LEFT:
                    player_reptile.defend_KEY_LEFT = True
                    
                else:
                    player_reptile.defend_KEY_RIGHT = True
            
            if pygame.joystick.Joystick(1).get_button(7):#left
                if player_reptile.FACING_LEFT:
                    player_reptile.SIDE_KICK_LEFT_KEY = True
                else:
                    player_reptile.SIDE_KICK_RIGHT_KEY = True

    def joystick_controlls_player2(self,event,player_scorpion):        
        if event.type == pygame.JOYBUTTONDOWN:
            if pygame.joystick.Joystick(0).get_button(0):#up
                player_scorpion.flip_KEY_RIGHT = True
                
            if pygame.joystick.Joystick(0).get_button(1):#right
                player_scorpion.RIGHT_KEY,player_scorpion.FACING_LEFT = True,False
            
            if pygame.joystick.Joystick(0).get_button(2):#down
                player_scorpion.flip_KEY_LEFT = True
                
            if pygame.joystick.Joystick(0).get_button(3):#left
                player_scorpion.FACING_LEFT,player_scorpion.LEFT_KEY = True,True


            if pygame.joystick.Joystick(0).get_button(4):
                if player_scorpion.FACING_LEFT:
                    player_scorpion.punch_KEY_LEFT = True
                else:
                    player_scorpion.punch_KEY_RIGHT = True
                
            if pygame.joystick.Joystick(0).get_button(5):
                if player_scorpion.FACING_LEFT:
                    player_scorpion.knife_KEY_LEFT = True
                else:
                    player_scorpion.knife_KEY_RIGHT = True
            
            if pygame.joystick.Joystick(0).get_button(6):#down
                if player_scorpion.FACING_LEFT:
                    player_scorpion.come_KEY_LEFT = True
                    threading.Thread(target=come_here,).start()
                else:
                    player_scorpion.come_KEY_RIGHT = True
                    threading.Thread(target=come_here,).start()


            
            if pygame.joystick.Joystick(0).get_button(7):#left
                if player_scorpion.FACING_LEFT:
                    player_scorpion.kick_KEY_LEFT = True
                else:
                    player_scorpion.kick_KEY_RIGHT = True
            
            if pygame.joystick.Joystick(0).get_button(8):#left
                player_scorpion.explosion_KEY = True
        

        
    def joyaxis_controlls(self,event,player_reptile,player_scorpion):
        if event.type == pygame.JOYAXISMOTION:
            val = event.value
            joy = event.joy
            

            if joy == 1:
                if event.axis == 0:
                
                    if abs(val) >= 1:
                        if player_reptile.FACING_LEFT:
                            player_reptile.STING_VENOM_KEY_LEFT = True
                        
                        else:
                            player_reptile.STING_VENOM_KEY_RIGHT = True
                    else:
                        player_reptile.STING_VENOM_KEY_LEFT = False
                        player_reptile.STING_VENOM_KEY_RIGHT = False
                
                if event.axis == 1:
                    if abs(val) >= 1:
                        if player_reptile.FACING_LEFT:
                            player_reptile.FLAW_KEY_LEFT = True
                        
                        else:
                            player_reptile.FLAW_KEY_RIGHT = True
                            player_reptile.SHOOT_FIREBALL = True

                    else:
                        player_reptile.FLAW_KEY_LEFT = False
                        player_reptile.FLAW_KEY_RIGHT = False
                    
                            
                    
            elif joy == 0:
                if event.axis == 0:
                
                    if abs(val) >= 1:
                        player_scorpion.explosion_KEY = True
                    
                    else:
                        player_scorpion.explosion_KEY = False
                
                if event.axis == 1:
                    if abs(val) >= 1:
                        # player_scorpion.baby_KEY = True
                        pass

                    else:
                        # player_scorpion.baby_KEY = False
                        pass

        
        
        if event.type == pygame.KEYUP:
            player_reptile.RIGHT_KEY = False 
            player_reptile.LEFT_KEY = False
            player_reptile.FLIP_KEY = False
            player_reptile.FLIP_KEY_RIGHT = False
            player_reptile.SIDE_KICK_LEFT_KEY = False
            player_reptile.SIDE_KICK_RIGHT_KEY = False
            player_reptile.STING_VENOM_KEY_LEFT = False
            player_reptile.STING_VENOM_KEY_RIGHT = False
            player_reptile.LOW_KICK_KEY_RIGHT = False
            player_reptile.LOW_KICK_KEY_LEFT = False
            player_reptile.FPUNCH_KEY_RIGHT = False
            player_reptile.FPUNCH_KEY_LEFT = False
            player_reptile.swing_KEY_RIGHT = False
            player_reptile.swing_KEY_LEFT = False
            player_reptile.defend_KEY_LEFT = False
            player_reptile.defend_KEY_RIGHT = False
            player_reptile.ESCAPE_KEY = False

            ################################
            ##PLAYER 2
            player_scorpion.punch_KEY_LEFT = False
            player_scorpion.punch_KEY_RIGHT = False
            player_scorpion.knife_KEY_LEFT = False
            player_scorpion.knife_KEY_RIGHT = False
            player_scorpion.specialKick_KEY_LEFT = False
            player_scorpion.specialKick_KEY_RIGHT = False
            player_scorpion.kick_KEY_LEFT = False
            player_scorpion.kick_KEY_RIGHT = False

            player_scorpion.flip_KEY_RIGHT = False
            player_scorpion.RIGHT_KEY = False
            if player_scorpion.FACING_LEFT:
                player_scorpion.FACING_LEFT = True
            else:
                player_scorpion.FACING_LEFT = False

            player_scorpion.flip_KEY_LEFT = False
            player_scorpion.LEFT_KEY = False

            player_scorpion.come_KEY_LEFT = False
            player_scorpion.come_KEY_RIGHT = False
            player_scorpion.explosion_KEY = False

            ###############################


        if event.type == pygame.JOYBUTTONUP:
            player_reptile.RIGHT_KEY = False 
            player_reptile.LEFT_KEY = False
            player_reptile.FLIP_KEY = False
            player_reptile.FLIP_KEY_RIGHT = False
            player_reptile.SIDE_KICK_LEFT_KEY = False
            player_reptile.SIDE_KICK_RIGHT_KEY = False
            player_reptile.STING_VENOM_KEY_LEFT = False
            player_reptile.STING_VENOM_KEY_RIGHT = False
            player_reptile.LOW_KICK_KEY_RIGHT = False
            player_reptile.LOW_KICK_KEY_LEFT = False
            player_reptile.FPUNCH_KEY_RIGHT = False
            player_reptile.FPUNCH_KEY_LEFT = False
            player_reptile.swing_KEY_RIGHT = False
            player_reptile.swing_KEY_LEFT = False
            player_reptile.defend_KEY_LEFT = False
            player_reptile.defend_KEY_RIGHT = False
            player_reptile.ESCAPE_KEY = False

            ################################
            ##PLAYER 2
            player_scorpion.punch_KEY_LEFT = False
            player_scorpion.punch_KEY_RIGHT = False
            player_scorpion.knife_KEY_LEFT = False
            player_scorpion.knife_KEY_RIGHT = False
            player_scorpion.specialKick_KEY_LEFT = False
            player_scorpion.specialKick_KEY_RIGHT = False
            player_scorpion.kick_KEY_LEFT = False
            player_scorpion.kick_KEY_RIGHT = False

            player_scorpion.flip_KEY_RIGHT = False
            player_scorpion.RIGHT_KEY = False
            if player_scorpion.FACING_LEFT:
                player_scorpion.FACING_LEFT = True
            else:
                player_scorpion.FACING_LEFT = False

            player_scorpion.flip_KEY_LEFT = False
            player_scorpion.LEFT_KEY = False

            player_scorpion.come_KEY_LEFT = False
            player_scorpion.come_KEY_RIGHT = False
            player_scorpion.explosion_KEY = False

