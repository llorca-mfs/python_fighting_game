import pygame

class Player():
    def __init__(self, x, y):
        self.size = (48, 96)
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

        self.isWalking = False
    
    def draw(self, surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)

    def update(self):
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

        self.xPos += self.xVel

        self.rect = pygame.Rect(self.xPos,self.yPos,self.size[0], self.size[1])