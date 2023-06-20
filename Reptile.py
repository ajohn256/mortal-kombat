import pygame 
import random

#file paths
path = "PlayerReptile/stance/"
flip = "PlayerReptile/flips/"
side_kick = "PlayerReptile/kicks/"
venom = "PlayerReptile/venom/"
low_kicks = "PlayerReptile/low_kicks/"
punches = "PlayerReptile/punches/"
swing_kick = "PlayerReptile/swing/"
defend = "PlayerReptile/defend/"
flaws = "PlayerReptile/flaw/"
escape = "PlayerReptile/escape/"
fire_ball = "PlayerReptile/flaw/"
knock_out = "PlayerReptile/knock_out/"
hits = "PlayerReptile/hits/"
brutality = "PlayerReptile/brutality/"

class PlayerReptile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.LEFT_KEY,self.RIGHT_KEY,self.FACING_LEFT = False,False,True
        self.FLIP_KEY,self.FLIP_KEY_RIGHT = False,False
        self.SIDE_KICK_LEFT_KEY,self.SIDE_KICK_RIGHT_KEY = False,False
        self.POSITION = (800,550)
        self.fireball = fire_ball+"fireball.png"
        self.SHOOT_FIREBALL = False
        self.fireball_coordinates = (200,420)
        

        self.STING_VENOM_KEY_LEFT,self.STING_VENOM_KEY_RIGHT = False,False
        self.venom_frame = 0
        self.venom_left = 0
        self.venom_right = 0

        self.ESCAPE_KEY = False
        self.escape_frame = 0
        self.escape_arena = 0

        self.FLAW_KEY_LEFT,self.FLAW_KEY_RIGHT = False,False
        self.flaw_frame = 0
        self.flaw_left = 0
        self.flaw_right = 0

        self.LOW_KICK_KEY_LEFT,self.LOW_KICK_KEY_RIGHT = False,False
        self.lowkick_frame = 0
        self.lowkick_left = 0
        self.lowkick_right = 0
        self.down_velocity = 0

        self.swing_KEY_LEFT,self.swing_KEY_RIGHT = False,False
        self.swing_frame = 0
        self.swing_left = 0
        self.swing_right = 0

        self.defend_KEY_LEFT,self.defend_KEY_RIGHT = False,False
        self.defend_frame = 0
        self.defend_left = 0
        self.defend_right = 0

        self.FPUNCH_KEY_LEFT,self.FPUNCH_KEY_RIGHT = False,False
        self.fpunch_frame = 0
        self.fpunch_left = 0
        self.fpunch_right = 0
        self.upper_cut_frame = 0

        self.load_frames()
        self.rect = self.standing_idle_right[0].get_rect()
        self.rect.midbottom = self.POSITION
        self.current_frame = 0
        self.walk_frame = 0
        self.flipping_frame = 0
        self.kicking_frame = 0
        self.flipping_to_right = 0
        self.side_kick_left = 0
        self.side_kick_right = 0
        self.last_updated = 0
        self.velocity = 0
        self.flipping = 0
        self.state = "idle"
        self.current_image = self.standing_idle_right[0]

        self.fireball_vel = 0
        self.posx = (self.rect.x-35)
        self.posy = (self.rect.y+35)
        self.fball = ""
        self.fball = pygame.image.load(self.fireball)
        self.fball = pygame.transform.rotozoom(self.fball,0,2)
        self.ball_state = "reset"

        self.KNOCK_OUT = False
        self.knock_out_frame = 0
        self.knock_out_side = 0
        self.ko_updated = 0

        self.GETTING_HIT = False
        self.hit_frame = 0
        self.hit_side = 0

        self.BRUTALITY = False
        self.brutality_frame = 0
        self.brutality_pos = 0
        self.brutality_count = 0
        self.brutalityImg = pygame.image.load(brutality+"tear_8.png")
        self.brutalityImg = pygame.transform.rotozoom(self.brutalityImg,0,2)
        self.brutality_state = "finished"
        
    
    
    def draw_characters(self,screen):
        screen.blit(self.current_image,self.rect)


    
    def handle_fireball(self,screen):
        if self.SHOOT_FIREBALL:
            screen.blit(self.fball,(self.posx,self.posy))
        
        
        self.posx += self.fireball_vel



    
    def update(self,width):
        self.velocity = 0
        self.down_velocity = 0
        self.flipping = 0
        self.flipping_to_right = 0
        self.side_kick_left = 0
        self.lowkick_right = 0
        self.lowkick_left = 0
        self.fpunch_right = 0
        self.fpunch_left = 0
        self.swing_left = 0
        self.swing_right = 0
        self.defend_left = 0
        self.defend_right = 0
        self.flaw_right = 0
        self.flaw_left = 0
        self.escape_arena = 0
        self.knock_out_side = 0
        self.hit_side = 0
        self.brutality_pos = 0

        if self.LEFT_KEY:
            self.velocity = -2
           
        elif self.RIGHT_KEY:
            self.velocity = 2
        
        elif self.FLIP_KEY:
            self.flipping = 1
            self.velocity = -4
        
        elif self.FLIP_KEY_RIGHT:
            self.flipping_to_right = 1
            self.velocity = 4
        
        elif self.SIDE_KICK_LEFT_KEY:
            self.side_kick_left = 1
            self.velocity = -0.00001
        
        elif self.SIDE_KICK_RIGHT_KEY:
            self.side_kick_right = 1
            self.velocity = 0.00001
        
        elif self.STING_VENOM_KEY_LEFT:
            self.venom_left = 1
            self.velocity = -0.005
        
        elif self.STING_VENOM_KEY_RIGHT:
            self.venom_right = 1
            self.velocity = 0.005
        
        elif self.LOW_KICK_KEY_RIGHT:
            self.lowkick_right = 1
        
        elif self.LOW_KICK_KEY_LEFT:
            self.lowkick_left = 1
        
        elif self.FPUNCH_KEY_RIGHT:
            self.fpunch_right = 1
        
        elif self.FPUNCH_KEY_LEFT:
            self.fpunch_left = 1
        
        elif self.swing_KEY_RIGHT:
            self.swing_right = 1
        
        elif self.swing_KEY_LEFT:
            self.swing_left = 1
        
        elif self.defend_KEY_RIGHT:
            self.defend_right = 1
        
        elif self.defend_KEY_LEFT:
            self.defend_left = 1
        
        elif self.FLAW_KEY_LEFT:
            self.flaw_left = 1
        
        elif self.FLAW_KEY_RIGHT:
            self.flaw_right = 1
            self.ball_state = "fire"
            self.fireball_vel = 7

        
        elif self.ESCAPE_KEY:
            self.escape_arena = 1
        
        elif self.KNOCK_OUT:
            self.knock_out_side = 1
        
        elif self.GETTING_HIT:
            self.hit_side = 1
            self.velocity = -1
        
        elif self.BRUTALITY:
            self.brutality_pos = 1

       

        
        else:
            self.flipping = 0
            self.brutality_pos = 0
            self.hit_side = 0
            self.knock_out_side = 0
            self.flipping_to_right = 0
            self.side_kick_left = 0
            self.side_kick_right = 0
            self.venom_left = 0
            self.venom_right = 0
            self.lowkick_right = 0
            self.lowkick_left = 0
            self.fpunch_right = 0
            self.fpunch_left = 0
            self.swing_left = 0
            self.swing_right = 0
            self.defend_left = 0
            self.defend_right = 0
            self.flaw_right = 0
            self.flaw_left = 0
            self.escape_arena = 0
        

        if self.rect.x <= 0:
            self.rect.x = 0
        
        elif self.rect.x >= width-100:
            self.rect.x = width-100
        
        elif self.posx >= width:
            self.posx = self.rect.x-35
            self.ball_state = "reset"
            self.SHOOT_FIREBALL = False
            

       
        self.rect.x += self.velocity
        

        self.set_state()
        self.animate()
        
    
    def set_state(self):
        self.state = 'idle'
        if self.velocity > 0:
            self.state = 'moving_right'
        
        elif self.velocity < 0:
            self.state = 'moving_left'
        
        #dont add an else statement here coz i got bugs and issues with movement L/R
        
        if self.flipping == 1:
            self.state = 'flipping_left'
            self.FACING_LEFT = True
        
        elif self.flipping_to_right == 1:
            self.state = "flipping_right"
            self.FACING_LEFT = False
        
        elif self.side_kick_left == 1:
            self.state = "side_kick_left"
        
        elif self.side_kick_right == 1:
            self.state = "side_kick_right"
        
        elif self.venom_left == 1:
            self.state = "sting_left"
        
        elif self.venom_right == 1:
            self.state = "sting_right"
        
        elif self.lowkick_right == 1:
            self.state = "low_kick_right"
        
        elif self.lowkick_left == 1:
            self.state = "low_kick_left"
        
        elif self.fpunch_right == 1:
            self.state = "fpunch_right"
        
        elif self.fpunch_left == 1:
            self.state = "fpunch_left"

        elif self.swing_right == 1:
            self.state = "swing_right"
        
        elif self.swing_left == 1:
            self.state = "swing_left"
        
        elif self.defend_left == 1:
            self.state = "defend_left"
        
        elif self.defend_right == 1:
            self.state = "defend_right"
        
        elif self.flaw_right == 1:
            self.state = "flaw_right"
        
        elif self.flaw_left == 1:
            self.state = "flaw_left"
        
        elif self.escape_arena == 1:
            self.state = "escape_arena"
        
        elif self.knock_out_side == 1:
            self.state = "KO"
        
        elif self.hit_side == 1:
            self.state = "getting_hit"
        
        
        elif self.brutality_pos == 1:
            self.state = "tear_brutality"
        
        
              
    
    def brutality_check(self):
        timer = pygame.time.get_ticks()

        if (timer - self.brutality_count) > 100:
            self.brutality_count = timer
            self.brutality_frame = (self.current_frame + 1) % len(self.brutalityHit)

            if self.state == "tear_brutality":
                self.current_image = self.brutalityHit[self.brutality_frame]
            
            

    def animate(self):
        now = pygame.time.get_ticks()
        
        if self.state == "idle":
            if (now - self.last_updated) > 100:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.standing_idle_right)

                if self.FACING_LEFT:
                    self.current_image = self.standing_idle_left[self.current_frame]
                
                elif not self.FACING_LEFT:
                    self.current_image = self.standing_idle_right[self.current_frame]
                
                
        else:

            if (now - self.last_updated) > 60:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.walking_right)
                self.flipping_frame = (self.current_frame + 1) % len(self.frontflip_left)
                self.kicking_frame = (self.current_frame + 1) % len(self.leftSideKick)
                self.venom_frame = (self.current_frame + 1) % len(self.leftVenomSting)
                self.lowkick_frame = (self.current_frame + 1) % len(self.rightLowKick)
                self.fpunch_frame = (self.current_frame + 1) % len(self.punchRight)
                self.upper_cut_frame = (self.current_frame + 1) % len(self.punch_two_Right)
                self.swing_frame = (self.current_frame + 1) % len(self.swingKickRight)
                self.defend_frame = (self.current_frame + 1) % len(self.defendRight)
                self.flaw_frame = (self.current_frame + 1) % len(self.flawRight)
                self.escape_frame = (self.current_frame + 1) % len(self.escapeArena)
                self.knock_out_frame = (self.current_frame + 1) % len(self.knockOut)
                self.hit_frame = (self.current_frame + 1) % len(self.gettingHit)
                # self.brutality_frame = (self.current_frame + 1) % len(self.brutalityHit)


                if self.state == "moving_left":
                    self.current_image = self.walking_left[self.current_frame]
                
                elif self.state == "moving_right":
                    self.current_image = self.walking_right[self.current_frame]
            
                elif self.state == "flipping_left":
                    self.current_image = self.frontflip_left[self.flipping_frame]
                
                elif self.state == "flipping_right":
                    self.current_image = self.frontflip_right[self.flipping_frame]
                
                elif self.state == "side_kick_left":
                    self.current_image = self.leftSideKick[self.kicking_frame]
                
                elif self.state == "side_kick_right":
                    self.current_image = self.rightSideKick[self.kicking_frame]
                
                elif self.state == "sting_left":
                    self.current_image = self.leftVenomSting[self.venom_frame]
                
                elif self.state == "sting_right":
                    self.current_image = self.rightVenomSting[self.venom_frame]
                
                elif self.state == "low_kick_right":
                    self.current_image = self.rightLowKick[self.lowkick_frame]
                
                elif self.state == "low_kick_left":
                    self.current_image = self.leftLowKick[self.lowkick_frame]
                

                elif self.state == "fpunch_right":
                    punch_list = [self.punch_two_Right,self.punchRight]
                    selected_option = random.choice(punch_list)

                    if selected_option == self.punch_two_Right:
                        #self.current_image = self.punch_two_Right[self.upper_cut_frame]
                        self.current_image = self.punchRight[self.fpunch_frame]
                    
                    else:
                        self.current_image = self.punchRight[self.fpunch_frame]
                
                elif self.state == "fpunch_left":
                    punchlft_list = [self.punch_two_Left,self.punchLeft]
                    selected_option = random.choice(punchlft_list)

                    if selected_option == self.punch_two_Left:
                        #self.current_image = self.punch_two_Left[self.upper_cut_frame]
                        self.current_image = self.punchLeft[self.fpunch_frame]
                    
                    else:
                        self.current_image = self.punchLeft[self.fpunch_frame]
                    
                elif self.state == "swing_right":
                    self.current_image = self.swingKickRight[self.swing_frame]
                
                elif self.state == "swing_left":
                    self.current_image = self.swingKickLeft[self.swing_frame]
            
                elif self.state == "defend_right":
                    self.current_image = self.defendRight[0]
                
                elif self.state == "defend_left":
                    self.current_image = self.defendLeft[0]
                
                elif self.state == "flaw_left":
                    self.current_image = self.flawLeft[self.flaw_frame]
                    # self.fireball_vel = -1.5

                
                elif self.state == "flaw_right":
                    self.current_image = self.flawRight[self.flaw_frame]
                    # self.fireball_vel = 1.5
                
                elif self.state == "escape_arena":
                    self.current_image = self.escapeArena[self.escape_frame]
                    if self.current_image == self.escapeArena[-1]:
                        if self.rect.x <= 600:
                            self.rect.x = 1000
                            self.FACING_LEFT = True

                        else:
                            self.rect.x = 100
                            self.FACING_LEFT = False
                
                elif self.state == "KO":
                    self.current_image = self.knockOut[self.knock_out_frame]
            
                elif self.state == "getting_hit":
                    self.current_image = self.gettingHit[self.hit_frame]
                
                

            
                        
                
                
               
    def load_frames(self):
        self.standing_idle_right = []
        for i in range(8,14):
            stand_img = pygame.image.load(path+f"stance_{i}.png")#.convert()
            nonflipped_right = pygame.transform.flip(stand_img,False,False)
            self.standing_idle_right.append(pygame.transform.rotozoom(nonflipped_right,0,2))
        
        #standing idle left
        self.standing_idle_left = []
        for i in range(8,14):
            img0 = pygame.image.load(path+f"stance_{i}.png")
            flipped_left = pygame.transform.flip(img0,True,False)
            self.standing_idle_left.append(pygame.transform.rotozoom(flipped_left,0,2))

        
        #walking right
        self.walking_right = []
        for j in range(1,7):
            walk_right = pygame.image.load(path+f"walk_{j}.png")#.convert()
            self.walking_right.append(pygame.transform.rotozoom(walk_right,0,2))
        

        #walking left
        self.walking_left = []
        for p in range(1,7):
            img_left = pygame.image.load(path+f"walk_{p}.png")
            walk_left = pygame.transform.flip(img_left,True,False)
            self.walking_left.append(pygame.transform.rotozoom(walk_left,0,2))
            

        #front flip facing left
        self.frontflip_left = []
        for x in range(2,16):
            img_flip = pygame.image.load(flip+f"flip_{x}.png")         
            flip_front_left = pygame.transform.flip(img_flip,True,False)
            self.frontflip_left.append(pygame.transform.rotozoom(flip_front_left,0,2))
        

        #front flip facing right
        self.frontflip_right = []
        for x in range(2,16):
            img_flip1 = pygame.image.load(flip+f"flip_{x}.png")         
            flip_front_right = pygame.transform.flip(img_flip1,False,False)
            self.frontflip_right.append(pygame.transform.rotozoom(flip_front_right,0,2))
        

        #side kick facing left
        self.leftSideKick = []
        for x in range(7,10):
            img_kick = pygame.image.load(side_kick+f"sk_{x}.png")         
            kick_side_left = pygame.transform.flip(img_kick,True,False)
            self.leftSideKick.append(pygame.transform.rotozoom(kick_side_left,0,2))
        

        #side kick facing right
        self.rightSideKick = []
        for x in range(7,10):
            img_kick = pygame.image.load(side_kick+f"sk_{x}.png")         
            kick_side_left = pygame.transform.flip(img_kick,False,False)
            self.rightSideKick.append(pygame.transform.rotozoom(kick_side_left,0,2))
        

        #venom sting facing left
        self.leftVenomSting = []
        for x in range(1,16):
            sting_left = pygame.image.load(venom+f"venom_{x}.png")         
            sting_side_left = pygame.transform.flip(sting_left,True,False)
            self.leftVenomSting.append(pygame.transform.rotozoom(sting_side_left,0,2))
        

        #venom sting facing right
        self.rightVenomSting = []
        for x in range(1,16):
            sting_right = pygame.image.load(venom+f"venom_{x}.png")         
            sting_side_right = pygame.transform.flip(sting_right,False,False)
            self.rightVenomSting.append(pygame.transform.rotozoom(sting_side_right,0,2))
        

        #low kick facing right
        self.rightLowKick = []
        for x in range(1,6):
            low_kick_right = pygame.image.load(low_kicks+f"lk_{x}.png")         
            low_kick_right = pygame.transform.flip(low_kick_right,False,False)
            self.rightLowKick.append(pygame.transform.rotozoom(low_kick_right,0,2))
        

        #low kick facing left
        self.leftLowKick = []
        for j in range(1,6):
            low_kick_left = pygame.image.load(low_kicks+f"lk_{j}.png")         
            low_kick_left = pygame.transform.flip(low_kick_left,True,False)
            self.leftLowKick.append(pygame.transform.rotozoom(low_kick_left,0,2))
        

        #sweep kicks
        self.rightSweepKick = []
        for x in range(1,6):
            sweep_kick_right = pygame.image.load(low_kicks+f"sweep{x}.png")         
            sweep_kick_right = pygame.transform.flip(sweep_kick_right,False,False)
            self.rightSweepKick.append(pygame.transform.rotozoom(sweep_kick_right,0,2))
        

        #sweep kick facing left
        self.leftSweepKick = []
        for x in range(1,6):
            sweep_kick_left = pygame.image.load(low_kicks+f"sweep{x}.png")         
            sweep_kick_left = pygame.transform.flip(sweep_kick_left,True,False)
            self.leftSweepKick.append(pygame.transform.rotozoom(sweep_kick_left,0,2))
        

        #punches right
        self.punchRight = []
        for x in range(1,9):
            punch_right = pygame.image.load(punches+f"fpunch{x}.png")         
            punch_right = pygame.transform.flip(punch_right,False,False)
            self.punchRight.append(pygame.transform.rotozoom(punch_right,0,2))
        

        #punches left
        self.punchLeft = []
        for x in range(1,9):
            punch_left = pygame.image.load(punches+f"fpunch{x}.png")         
            punch_left = pygame.transform.flip(punch_left,True,False)
            self.punchLeft.append(pygame.transform.rotozoom(punch_left,0,2))
        
        #punches2 right
        self.punch_two_Right = []
        for x in range(1,7):
            punch_right = pygame.image.load(punches+f"cut{x}.png")         
            punch_right = pygame.transform.flip(punch_right,False,False)
            self.punch_two_Right.append(pygame.transform.rotozoom(punch_right,0,1.9))
        

        #punches2 left
        self.punch_two_Left = []
        for x in range(1,7):
            punch2_left = pygame.image.load(punches+f"cut{x}.png")         
            punch2_left = pygame.transform.flip(punch2_left,True,False)
            self.punch_two_Left.append(pygame.transform.rotozoom(punch2_left,0,1.9))
        

        #swing kick to right
        self.swingKickRight = []
        for x in range(1,7):
            swing_right = pygame.image.load(swing_kick+f"swing{x}.png")         
            swing_right = pygame.transform.flip(swing_right,False,False)
            self.swingKickRight.append(pygame.transform.rotozoom(swing_right,0,2))
        

        #swing kick to left
        self.swingKickLeft = []
        for x in range(1,7):
            swing_left = pygame.image.load(swing_kick+f"swing{x}.png")         
            swing_left = pygame.transform.flip(swing_left,True,False)
            self.swingKickLeft.append(pygame.transform.rotozoom(swing_left,0,2))
        

        #defending
        self.defendRight = []
        for i in range(1,3):
            defend_right = pygame.image.load(defend+f"defend{i}.png")         
            defend_right = pygame.transform.flip(defend_right,False,False)
            self.defendRight.append(pygame.transform.rotozoom(defend_right,0,2))
        

        self.defendLeft = []
        for i in range(1,3):
            defend_left = pygame.image.load(defend+f"defend{i}.png")         
            defend_left = pygame.transform.flip(defend_left,True,False)
            self.defendLeft.append(pygame.transform.rotozoom(defend_left,0,2))
        

        #fireball skill
        self.flawRight = []
        for j in range(1,7):
            flaw_right = pygame.image.load(flaws+f"flaw{j}.png")         
            flaw_right = pygame.transform.flip(flaw_right,False,False)
            self.flawRight.append(pygame.transform.rotozoom(flaw_right,0,2))
        

        self.flawLeft = []
        for j in range(1,7):
            flaw_left = pygame.image.load(flaws+f"flaw{j}.png")         
            flaw_left = pygame.transform.flip(flaw_left,True,False)
            self.flawLeft.append(pygame.transform.rotozoom(flaw_left,0,2))
        


        #escape from arena
        self.escapeArena = []
        for q in range(1,7):
            escape_arr = pygame.image.load(escape+f"blast{q}.png")         
            escape_arr = pygame.transform.flip(escape_arr,False,False)
            self.escapeArena.append(pygame.transform.rotozoom(escape_arr,0,2))
        

            
        #knock out fatlity frames
        self.knockOut = []
        for x in range(1,6):
            ko = pygame.image.load(knock_out+f"ko_{x}.png")         
            ko = pygame.transform.flip(ko,False,False)
            self.knockOut.append(pygame.transform.rotozoom(ko,0,2))
        


        #getting hit frames
        self.gettingHit = []
        for p in range(1,10):
            hit = pygame.image.load(hits+f"hit_{p}.png")         
            hit = pygame.transform.flip(hit,False,False)
            self.gettingHit.append(pygame.transform.rotozoom(hit,0,2))
        

        #BRUTALITY FLICKS
        #tears
        self.brutalityHit = []
        for y in range(1,9):
            brut = pygame.image.load(brutality+f"tear_{y}.png")         
            brut = pygame.transform.flip(brut,False,False)
            self.brutalityHit.append(pygame.transform.rotozoom(brut,0,2))
        
        
        
        
        

        

        
