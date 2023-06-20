import pygame




class HandleBackground:
    def __init__(self):
        self.pos = 0
        self.let_background_moveRight = False
        self.let_background_moveLeft = False
        self.bg_x = 0.3

    def draw_bg(self,screen,bg1,width):
        screen.blit(bg1, (self.pos, 0))
        screen.blit(bg1, (width + self.pos, 0))

        if self.pos <= -width:
            screen.blit(bg1, (width + self.pos, 0))
            self.pos = 0
            self.bg_x = 0.3

        if self.let_background_moveRight:
            self.pos += self.bg_x
        
        elif self.let_background_moveLeft:
            self.pos -= self.bg_x


