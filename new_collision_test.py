import pygame
clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()
pygame.display.set_caption("new collision system test")

WINDOW_SIZE = [512, 480]
screen = pygame.display.set_mode(WINDOW_SIZE)

ryu_attack = pygame.image.load("./ryu_hitbox_test.png").convert_alpha()

#TODO: check if surface x and y is optimal for changing values, consider using sprites

class PlayerSurf:
    def __init__(self, x, y):
        self.spritesurf = pygame.Surface((192,192))
        self.size = [48,84]

        #relative to centerx of sprite rect
        #attack_coords = [24, 108]
        self.attack_coords = [120, 108]

        self.xPos = x
        self.yPos = y
        self.xVel = 0
        self.yVel = 0

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        self.speed = 4

        self.hitbox_rect = pygame.Rect(self.spritesurf.get_rect().centerx - (self.size[0]/2), 192 - self.size[1], self.size[0], self.size[1])
        self.attack_rect = pygame.Rect(self.attack_coords[0],self.attack_coords[1],48,18)

        #with midpoint (centerx)
        #attack_rect = pygame.Rect(player_sprite_surf.get_rect().centerx + attack_coords[0],player_sprite_surf.get_rect().top + attack_coords[1],48,18)

        self.isFlipped = False

    def draw(self):
        self.spritesurf.fill((0,0,255))

        pygame.draw.rect(self.spritesurf,(255,0,0), self.hitbox_rect)
        pygame.draw.rect(self.spritesurf,(0,255,0), self.attack_rect)
        self.spritesurf.blit(ryu_attack, (0,0))

    def update(self, window):
        self.xVel = 0
        self.yVel = 0

        if self.left_pressed and not self.right_pressed:
            self.xVel = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.xVel = self.speed
        if self.up_pressed and not self.down_pressed:
            self.yVel = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.yVel = self.speed

        self.xPos += self.xVel
        self.yPos += self.yVel

        window.blit(pygame.transform.flip(self.spritesurf, self.isFlipped, False), (self.xPos, self.yPos))

        #pygame.transform.flip(image, False, True), (x,y)

def main():
    gameRunning = True

    player = PlayerSurf(0,0)

    while gameRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #player exits window
                gameRunning = False
            if event.type == KEYDOWN:
                if event.key == pygame.K_a:
                    player.left_pressed = True
                if event.key == pygame.K_d:
                    player.right_pressed = True
                if event.key == pygame.K_w:
                    player.up_pressed = True
                if event.key == pygame.K_s:
                    player.down_pressed = True
                if event.key == pygame.K_SPACE:
                    player.isFlipped = True if not player.isFlipped else False
            if event.type == KEYUP:
                if event.key == pygame.K_a:
                    player.left_pressed = False
                if event.key == pygame.K_d:
                    player.right_pressed = False
                if event.key == pygame.K_w:
                    player.up_pressed = False
                if event.key == pygame.K_s:
                    player.down_pressed = False

        screen.fill((0,0,0))

        player.draw()
        player.update(screen)

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()