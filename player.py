import pygame

class Player():
    def __init__(self, x, y, isPlayer2):
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
        self.attack_pressed = False

        self.speed = 4
        self.gravity = 1
        self.jumpVel = 0
        self.height_duck = 72
        self.isPlayer2 = isPlayer2

        self.attack_rect = pygame.Rect(x,y,96,32)

        self.isWalking = False
        self.isJumping = False
        self.isDucking = False
        self.isAttacking = False

    def draw(self, surface):
        pygame.draw.rect(surface, (0,0,255) if self.isPlayer2 else (255,0,0), self.rect)
        #if self.isAttacking:
        pygame.draw.rect(surface,(0,255,0), self.attack_rect)

    def update(self, window_size):
        self.xVel = 0
        self.yVel = 0

        if self.left_pressed or self.right_pressed:
            self.isWalking = True
        else:
            self.isWalking = False

        if self.isDucking == False:
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

        #JUMPING
        if self.up_pressed and not self.down_pressed and not self.isJumping:
            self.jumpVel = -(self.speed * 4)
            self.isJumping = True
        
        #DUCKING
        if self.down_pressed and not self.isJumping:
            #self.yPos = self.rect.top #y coordinate of hitbox when ducking
            self.isDucking = True
        elif self.down_pressed == False:
            #self.size[1] = 96
            self.isDucking = False

        #ATTACKING
        if self.attack_pressed:
            self.isAttacking = True
        else:
            self.isAttacking = False

        #self.yPos = self.rect.top + self.size[1]

        self.jumpVel += self.gravity
        self.yVel += self.jumpVel

        #ensure player on screen
        if self.rect.left + self.xVel < 0:
            self.xVel = -self.rect.left        
        if self.rect.right + self.xVel > window_size[0]:
            self.xVel = window_size[0] - self.rect.right
        
        #TODO: make actual collison for floor
        if self.rect.bottom + self.yVel > window_size[1] - 32:
            self.jumpVel = 0
            self.isJumping = False
            self.yVel = window_size[1] - 32 - self.rect.bottom

        self.xPos += self.xVel
        self.yPos += self.yVel

        #print(self.yPos + (self.size[1] - self.height_duck))

        self.attack_rect = pygame.Rect(self.rect.right - (2 * self.rect.width) if self.isPlayer2 else self.rect.left,self.yPos,96,32)
        #self.rect = pygame.Rect(self.xPos, self.yPos,self.size[0], self.height_duck if self.isDucking else self.size[1])
        self.rect = pygame.Rect(self.xPos, self.yPos,self.size[0], self.size[1])
            

        