import pygame

class Player():
    def __init__(self, x, y):
        self.size = [48, 96]
        self.rect = pygame.Rect(x,y, self.size[0], self.size[1])

        self.xPos = x
        self.yPos = y
        self.xVel = 0
        self.yVel = 0

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        self.speed = 4
        self.gravity = 1
        self.jumpVel = 0

        self.isWalking = False
        #self.isJumping = False
    
    def draw(self, surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)

    def update(self, window_size):
        self.xVel = 0
        self.yVel = 0

        if self.left_pressed or self.right_pressed:
            self.isWalking = True
        else:
            self.isWalking = False

        if self.left_pressed and not self.right_pressed:
            self.xVel = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.xVel = self.speed
            '''
        if self.up_pressed and not self.down_pressed:
            self.yVel = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.yVel = self.speed
            '''
        if self.up_pressed and not self.down_pressed:
            self.jumpVel = -10
        

        self.jumpVel += self.gravity
        self.yVel += self.jumpVel

        #ensure player on screen
        if self.rect.left + self.xVel < 0:
            self.xVel = -self.rect.left        
        if self.rect.right + self.xVel > window_size[0]:
            self.xVel = window_size[0] - self.rect.right
        
        if self.rect.bottom + self.yVel > window_size[1] - 32:
            self.jumpVel = 0
            self.yVel = window_size[1] - 32 - self.rect.bottom

        self.xPos += self.xVel
        self.yPos += self.yVel

        self.rect = pygame.Rect(self.xPos,self.yPos,self.size[0], self.size[1])

        print(self.rect.bottom)