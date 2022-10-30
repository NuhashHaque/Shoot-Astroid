import pygame
import random
BLACK = (0,0,0)

class Brick(pygame.sprite.Sprite):
    #This class represents a brick. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.ast1 = pygame.image.load('images/ast1.jpg')
        self.ast2 = pygame.image.load('images/ast2.jpg')
        self.ast3 = pygame.image.load('images/ast3.jpg')
        self.ast4 = pygame.image.load('images/ast4.jpg')
        ast_list = [self.ast1, self.ast2, self.ast3, self.ast4]

        self.image = random.choice(ast_list)
        self.rect = self.image.get_rect()
        self.rect.center = (width,height)