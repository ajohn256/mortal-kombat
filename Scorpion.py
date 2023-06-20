import pygame
import random


path = "PlayerScorpion/"

standing = path+"standing/"
walking = path+"walking/"
knife_attack = path+"knife_attack/"
punches = path+"punches/"
kicks = path+"kicks/"
explosion = path+"explosion/"
hit = path+"hit/"
special_kick = path+"special_kick/"
baby_fatality = path+"to_baby/"
brutal_fatality = path+"fatal/"
flips=path+"flips/"
come_here = path+"come_here/"



class PlayerScorpion:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.LEFT_KEY,self.RIGHT_KEY,self.FACING_LEFT = False,False,False
        self.FLIP_KEY,self.FLIP_KEY_RIGHT = False,False
        self.SIDE_KICK_LEFT_KEY,self.SIDE_KICK_RIGHT_KEY = False,False
        self.POSITION = (200,550)
        self.verticalVelocity = 0
        

        self.load_frames()
        self.rect = self.standingLeft[0].get_rect()
        self.rect.midbottom = self.POSITION
        self.current_frame = 0
        self.walk_frame = 0

        self.knife_KEY_LEFT,self.knife_KEY_RIGHT = False,False
        self.knife_left = 0
        self.knife_right = 0

        self.come_KEY_LEFT,self.come_KEY_RIGHT = False,False
        self.come_left = 0
        self.come_right = 0
        
        self.punch_KEY_LEFT,self.punch_KEY_RIGHT = False,False
        self.punch_left = 0
        self.punch_right = 0
        
        self.kick_KEY_LEFT,self.kick_KEY_RIGHT = False,False
        self.kick_left = 0
        self.kick_right = 0

        self.specialKick_KEY_LEFT,self.specialKick_KEY_RIGHT = False,False
        self.specialKick_left = 0
        self.specialKick_right = 0

        self.hit_KEY_LEFT,self.hit_KEY_RIGHT = False,False
        self.hit_left = 0
        self.hit_right = 0

        self.flip_KEY_LEFT,self.flip_KEY_RIGHT = False,False
        self.flip_left = 0
        self.flip_right = 0
        
        self.explosion_KEY = False
        self.explode = 0

        self.baby_KEY = False
        self.isBaby = False
        self.to_baby = 0
        self.isbaby = 0
        self.baby_img = pygame.image.load(baby_fatality+"baby7.png").convert_alpha()
        self.baby_img = pygame.transform.rotozoom(self.baby_img,0,2)

        self.brutal_KEY = False
        self.complete_shrinkBrutality = False
        self.to_brutalshrink = 0
        self.isbrutal = 0
        self.brutal_img = pygame.image.load(brutal_fatality+"f13.png").convert_alpha()
        self.brutal_img = pygame.transform.rotozoom(self.brutal_img,0,2)
       
        
        self.last_updated = 0
        self.velocity = 0
        self.state = "idle"
        self.current_image = self.standingRight[0]

        self.standing_frame = 0
    
    def draw_characters(self,screen):
        if self.state == "baby":
            self.current_image = self.baby_img
            screen.blit(self.current_image,self.rect)
        
        elif self.state == "doneshrinking":
            self.current_image = self.brutal_img
            screen.blit(self.current_image,self.rect)
 
        else:
            screen.blit(self.current_image,self.rect)

    def update(self,width):
        self.velocity = 0
        self.flip_left = 0
        self.flip_right = 0
        self.verticalVelocity = 0
        self.to_brutalshrink = 0
        self.isbrutal = 0
        self.tobaby = 0
        self.specialKick_left = 0
        self.specialKick_right = 0
        self.knife_left = 0
        self.knife_right = 0
        self.hit_left = 0
        self.hit_right = 0
        self.punch_left = 0
        self.punch_right = 0
        self.explode = 0
        self.knife_left = 0
        self.knife_right = 0
        self.kick_left = 0
        self.kick_right = 0
        self.explode = 0
        self.to_baby = 0
        self.come_left = 0
        self.come_right = 0
        
        

        if self.LEFT_KEY:
            self.velocity = -2
            
        elif self.RIGHT_KEY:
            self.velocity = 2
        
        elif self.knife_KEY_LEFT:
            self.knife_left = 1
        
        elif self.knife_KEY_RIGHT:
            self.knife_right = 1
        
        elif self.punch_KEY_RIGHT:
            self.punch_right = 1
        
        elif self.punch_KEY_LEFT:
            self.punch_left = 1
            
        elif self.kick_KEY_RIGHT:
            self.kick_right = 1
        
        elif self.kick_KEY_LEFT:
            self.kick_left = 1
        
        elif self.explosion_KEY:
            self.explode = 1
        
        ##############################
        elif self.hit_KEY_RIGHT:
            self.hit_right = 1
        
        elif self.hit_KEY_LEFT:
            self.hit_left = 1
        
        ##############################
        elif self.specialKick_KEY_RIGHT:
            self.specialKick_right = 1
        
        elif self.specialKick_KEY_LEFT:
            self.specialKick_left = 1
        
        ###############################
        elif self.baby_KEY:
            self.to_baby = 1
        
        elif self.isBaby:
            self.tobaby = 1
        
        ###################################
        elif self.brutal_KEY:
            self.isbrutal = 1
            self.verticalVelocity = -0.5
            if self.rect.y <= 200:
                self.verticalVelocity = 2
        
        ################################3
        elif self.complete_shrinkBrutality:
            self.to_brutalshrink = 1
            
        ###############################3
        elif self.flip_KEY_LEFT:
            self.flip_left = 1
            self.velocity = -4
            
        elif self.flip_KEY_RIGHT:
            self.flip_right = 1  
            self.velocity = 4   
        
        elif self.come_KEY_LEFT:
            self.come_left = 1
            # self.rect.x = 300

        
        elif self.come_KEY_RIGHT:
            self.come_right = 1
            
        else:
            self.velocity = 0
            self.flip_left = 0
            self.flip_right = 0
            self.verticalVelocity = 0
            self.to_brutalshrink = 0
            self.isbrutal = 0
            self.tobaby = 0
            self.specialKick_left = 0
            self.specialKick_right = 0
            self.knife_left = 0
            self.knife_right = 0
            self.hit_left = 0
            self.hit_right = 0
            self.punch_left = 0
            self.punch_right = 0
            self.explode = 0
            self.knife_left = 0
            self.knife_right = 0
            self.kick_left = 0
            self.kick_right = 0
            self.explode = 0
            self.to_baby = 0
            self.come_left = 0
            self.come_right = 0
           

        

        self.rect.x += self.velocity
        self.rect.y += self.verticalVelocity

        if self.rect.x <= 0:
            self.rect.x = 0
            self.FACING_LEFT = False 
            # self.RIGHT_KEY = True 
            # self.LEFT_KEY = False
            # self.flip_KEY_LEFT = False
            # self.flip_KEY_RIGHT = True
        
        elif self.rect.x >= width-100:
            self.rect.x = width-100
            self.FACING_LEFT = True 
            # self.RIGHT_KEY = False 
            # self.LEFT_KEY = True
            # self.flip_KEY_LEFT = True
            # self.flip_KEY_RIGHT = False

        

        self.set_state()
        self.animate()
    
    def set_state(self):
        self.state = 'idle'

        if self.velocity > 0:
            self.state = 'moving_right'
        
        elif self.velocity < 0:
            self.state = 'moving_left'
        
        elif self.knife_right == 1:
            self.state = "knife_right"

        elif self.knife_left == 1:
            self.state = "knife_left"
        

        elif self.punch_left == 1:
            self.state = "punch_left"

        elif self.punch_right == 1:
            self.state = "punch_right"
        
        ############################
        elif self.kick_left == 1:
            self.state = "kick_left"

        elif self.kick_right == 1:
            self.state = "kick_right"

        ###########################
        
        elif self.explode == 1:
            self.state = "explode"
        
        ##############################
        elif self.hit_left == 1:
            self.state = "hit_left"

        elif self.hit_right == 1:
            self.state = "hit_right"
        
        ############################
        elif self.specialKick_left == 1:
            self.state = "specialKick_left"

        elif self.specialKick_right == 1:
            self.state = "specialKick_right"
        
        ###################
        elif self.to_baby == 1:
            self.state = 'to_baby'
        
        #######################
        elif self.isbaby == 1:
            self.state = "baby"
        
        elif self.isbrutal == 1:
            self.state = "brutality_shrink"
        
        ############################
        elif self.to_brutalshrink == 1:
            self.state = "doneshrinking"
        
        elif self.come_right == 1:
            self.state = "come_right"

        elif self.come_left == 1:
            self.state = "come_left"
        #################################
        if self.flip_right == 1:
            self.state = "flip_right"
            
        elif self.flip_left == 1:
            self.state = "flip_left"
            
        
    def animate(self):
        now = pygame.time.get_ticks()

        if self.state == "idle":
            if (now - self.last_updated) > 100:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.standingRight)

                if self.FACING_LEFT:
                    self.current_image = self.standingLeft[self.current_frame]
                
                elif not self.FACING_LEFT:
                    self.current_image = self.standingRight[self.current_frame]
                   
        elif self.state == "moving_left":
            if (now - self.last_updated) > 70:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.walking_left)
                self.current_image = self.walking_left[self.current_frame]


                    
        elif self.state == "moving_right":
            if (now - self.last_updated) > 70:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.walking_left)
                self.current_image = self.walking_right[self.current_frame]
        
        elif self.state == "knife_right":
            if (now - self.last_updated) > 70:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.cuttingKnifeRight)
                self.current_image = self.cuttingKnifeRight[self.current_frame]
            
            
        elif self.state == "knife_left":
            if (now - self.last_updated) > 70:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.cuttingKnifeLeft)
                self.current_image = self.cuttingKnifeLeft[self.current_frame]
            

        elif self.state == "punch_left":
            if (now - self.last_updated) > 65:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.punchLeft)
                self.current_image = self.punchLeft[self.current_frame]
            

        elif self.state == "punch_right":
            if (now - self.last_updated) > 50:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.punchRight)
                self.current_image = self.punchRight[self.current_frame]    

        ############################################
        elif self.state == "kick_left":
            if (now - self.last_updated) > 60:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.kickLeft)
                self.current_image = self.kickLeft[self.current_frame]
            

        elif self.state == "kick_right":
            if (now - self.last_updated) > 50:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.kickRight)
                self.current_image = self.kickRight[self.current_frame]    

        ################################################
        elif self.state == "explode":
            if (now - self.last_updated) > 80:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.Explosion)
                self.current_image = self.Explosion[self.current_frame]   

                if self.current_image == self.Explosion[-1]:
                    if self.rect.x <= 600:
                        self.rect.x = random.randint(200,1000)
                        self.state = 'idle'

                        self.FACING_LEFT = True
                        self.explosion_KEY = False
                        
                    else:
                        self.rect.x = random.randint(0,800)
                        self.state = 'idle'

                        self.FACING_LEFT = False 
                        self.explosion_KEY = False
                        
        

        ############################################
        elif self.state == "hit_left":
            if (now - self.last_updated) > 60:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.hitLeft)
                self.current_image = self.hitLeft[self.current_frame]
            

        elif self.state == "hit_right":
            if (now - self.last_updated) > 60:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.hitRight)
                self.current_image = self.hitRight[self.current_frame]   
        
        ############################################
        elif self.state == "specialKick_left":
            if (now - self.last_updated) > 120:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.specialKickLeft)
                self.current_image = self.specialKickLeft[self.current_frame]

                if self.current_image == self.specialKickLeft[-1]:
                    self.state = "idle"
                    self.specialKick_KEY_LEFT = False
                    self.FACING_LEFT = True
              
            

        elif self.state == "specialKick_right":
            if (now - self.last_updated) > 100:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.specialKickRight)
                self.current_image = self.specialKickRight[self.current_frame]  

                if self.current_image == self.specialKickRight[-1]:
                    self.state = "idle"
                    self.specialKick_KEY_RIGHT = False
                    self.FACING_LEFT = False
                   
        ################################################
        elif self.state == "to_baby":
            if (now - self.last_updated) > 180:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.toBaby)
                self.current_image = self.toBaby[self.current_frame]  

                if self.current_image == self.toBaby[-1]:
                    self.state = "baby"
                    self.baby_KEY = False
                    self.isBaby = True
        
        elif self.state == "brutality_shrink":
            if (now - self.last_updated) > 200:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.BrutalityFate)
                self.current_image = self.BrutalityFate[self.current_frame]  

                if self.current_image == self.BrutalityFate[-1]:
                    self.state = "doneshrinking"
                    self.brutal_KEY = False
                    self.complete_shrinkBrutality = True
                    self.rect.y = 5000
                    self.rect.x = 5000
        

        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        elif self.state == "flip_left":
            if (now - self.last_updated) > 30:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.leftFlip)
                self.current_image = self.leftFlip[self.current_frame]  

        elif self.state == "flip_right":
            if (now - self.last_updated) > 30:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.rightFlip)
                self.current_image = self.rightFlip[self.current_frame]   
        
        elif self.state == "come_right":
            if (now - self.last_updated) > 120:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.comeRight)
                self.current_image = self.comeRight[self.current_frame]   
        

        elif self.state == "come_left":
            if (now - self.last_updated) > 120:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.comeLeft)
                self.current_image = self.comeLeft[self.current_frame]

                if self.current_image != self.comeLeft[3] or self.current_image != self.comeLeft[4] or self.current_image != self.comeLeft[5]: 
                    self.rect.x = 300
                
                else:
                    self.rect.x = 550

        else:
            self.state = 'idle'

    def load_frames(self):

        #standing idle left
        self.standingLeft = []
        for i in range(1,7):
            stand_img = pygame.image.load(standing+f"stand_{i}.png")
            stand_img = pygame.transform.flip(stand_img,True,False)
            self.standingLeft.append(pygame.transform.rotozoom(stand_img,0,2))
        
        #standing idle right
        self.standingRight = []
        for i in range(1,7):
            face_right = pygame.image.load(standing+f"stand_{i}.png")
            face_right = pygame.transform.flip(face_right,False,False)
            self.standingRight.append(pygame.transform.rotozoom(face_right,0,2))
        

        #walking left
        self.walking_left = []
        for p in range(1,10):
            img_left = pygame.image.load(walking+f"walk_{p}.png")
            walk_left = pygame.transform.flip(img_left,True,False)
            self.walking_left.append(pygame.transform.rotozoom(walk_left,0,2))
            
        
        #walking right
        self.walking_right = []
        for p in range(1,10):
            img_right = pygame.image.load(walking+f"walk_{p}.png")
            walk_right = pygame.transform.flip(img_right,False,False)
            self.walking_right.append(pygame.transform.rotozoom(walk_right,0,2))
            

        #knife cutting right
        self.cuttingKnifeRight = []
        for p in range(1,10):
            cutRight = pygame.image.load(knife_attack+f"knife{p}.png")
            cutRight = pygame.transform.flip(cutRight,False,False)
            self.cuttingKnifeRight.append(pygame.transform.rotozoom(cutRight,0,2))
        
        #knife cutting left
        self.cuttingKnifeLeft = []
        for p in range(1,10):
            cutLeft = pygame.image.load(knife_attack+f"knife{p}.png")
            cutLeft = pygame.transform.flip(cutLeft,True,False)
            self.cuttingKnifeLeft.append(pygame.transform.rotozoom(cutLeft,0,2))
        
        #punching left
        self.punchLeft = []
        for p in range(1,16):
            pl = pygame.image.load(punches+f"p{p}.png").convert_alpha()
            pl = pygame.transform.flip(pl,False,False)
            self.punchLeft.append(pygame.transform.rotozoom(pl,0,2))
        
        #punching right
        self.punchRight = []
        for p in range(1,16):
            pr = pygame.image.load(punches+f"p{p}.png")
            pr = pygame.transform.flip(pr,True,False)
            self.punchRight.append(pygame.transform.rotozoom(pr,0,2))
        


        #kick right
        self.kickRight = []
        for j in range(1,8):
            kr = pygame.image.load(kicks+f"k{j}.png")
            kr = pygame.transform.flip(kr,False,False)
            self.kickRight.append(pygame.transform.rotozoom(kr,0,2))
        
            
        #kick right
        self.kickLeft = []
        for j in range(1,8):
            kl = pygame.image.load(kicks+f"k{j}.png")
            kl = pygame.transform.flip(kl,True,False)
            self.kickLeft.append(pygame.transform.rotozoom(kl,0,2))
        
        #############################################
        #explsion
        self.Explosion = []
        for x in range(1,18):
            expl = pygame.image.load(explosion+f"e{x}.png")
            expl = pygame.transform.flip(expl,False,False)
            self.Explosion.append(pygame.transform.rotozoom(expl,0,2))
        
        
        ############################################
        self.hitRight = []   
        for x in range(1,10):
            ht = pygame.image.load(hit+f"h{x}.png")
            ht = pygame.transform.flip(ht,False,False)
            self.hitRight.append(pygame.transform.rotozoom(ht,0,2))
        
        self.hitLeft = []   
        for x in range(1,10):
            htl = pygame.image.load(hit+f"h{x}.png")
            htl = pygame.transform.flip(htl,True,False)
            self.hitLeft.append(pygame.transform.rotozoom(htl,0,2))
        

        ############################################
        #special kick left
        self.specialKickLeft = []
        for q in range(1,9):
            skl = pygame.image.load(special_kick+f"k{q}.png")
            skl = pygame.transform.flip(skl,True,False)
            self.specialKickLeft.append(pygame.transform.rotozoom(skl,0,2))
        

        #special kick right
        self.specialKickRight = []
        for q in range(1,9):
            skr = pygame.image.load(special_kick+f"k{q}.png")
            skr = pygame.transform.flip(skr,False,False)
            self.specialKickRight.append(pygame.transform.rotozoom(skr,0,2))
        
        
        ############################################
        #to baby
        self.toBaby = []
        for q in range(1,8):
            baby = pygame.image.load(baby_fatality+f"baby{q}.png")
            baby = pygame.transform.flip(baby,False,False)
            self.toBaby.append(pygame.transform.rotozoom(baby,0,2))
           
        
        #brutality
        self.BrutalityFate = []
        for q in range(1,14):
            brutbaby = pygame.image.load(brutal_fatality+f"f{q}.png")
            brutbaby = pygame.transform.flip(brutbaby,False,False)
            self.BrutalityFate.append(pygame.transform.rotozoom(brutbaby,0,2))
        
        ########################
        ##flipping left
        self.leftFlip = []
        for x in range(1,14):
            flipleft = pygame.image.load(flips+f"f{x}.png")
            flipleft = pygame.transform.flip(flipleft,True,False)
            self.leftFlip.append(pygame.transform.rotozoom(flipleft,0,2))
        
        ##flipping right/backflip
        self.rightFlip = []
        for x in range(1,14):
            flipright = pygame.image.load(flips+f"f{x}.png")
            flipright = pygame.transform.flip(flipright,False,False)
            self.rightFlip.append(pygame.transform.rotozoom(flipright,0,2))
        

        ##come here
        self.comeRight = []
        for x in range(1,10):
            cright = pygame.image.load(come_here+f"c{x}.png")
            cright = pygame.transform.flip(cright,False,False)
            self.comeRight.append(pygame.transform.rotozoom(cright,0,2))
        
        ##come here
        self.comeLeft = []
        for x in range(1,10):
            cleft = pygame.image.load(come_here+f"c{x}.png")
            cleft = pygame.transform.flip(cleft,True,False)
            self.comeLeft.append(pygame.transform.rotozoom(cleft,0,2))