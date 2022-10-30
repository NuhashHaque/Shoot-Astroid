import pygame
BLACK=(0,0,0)

class Paddle(pygame.sprite.Sprite):
    # This class represent a paddle. It drives from the "Sprite class"
    def __init__(self, color,width,height):
        # call the parent class (Sprite) constrctor
        super().__init__()
        self.image = pygame.image.load('space_craft.png').convert_alpha() 
        self.rect = self.image.get_rect()
        self.rect.center = (width,height)
    
    def moveLeft(self,pixels):
        self.rect.x -=pixels
        # check that you are not going too far(off the screen)
        if self.rect.x<0:
            self.rect.x=0
    
    def moveRight(self,pixels):
        self.rect.x +=pixels
        # check that you are not going too far(off the screen)
        if self.rect.x >700:
            self.rect.x=700
    def moveUp(self,pixels):
        self.rect.y -=pixels
        # check that out off the screen
        if self.rect.y <20:
            self.rect.y=20
    def moveDown(self,pixels):
        self.rect.y +=pixels
        #check lower off the screen
        if self.rect.y>580:
            self.rect.y=580
            
            