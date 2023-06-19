import pygame
from player import Player

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()
pygame.display.set_caption("The King of Streets \'23")

WINDOW_SIZE = [340, 256]

screen = pygame.display.set_mode(WINDOW_SIZE)

player_1 = Player(62,128, False)
player_2 = Player(230,128, True)

bg = pygame.image.load("bg_256.png").convert_alpha()

class LifebarSurf:
    def __init__(self, x, y):
        self.spritesurf = pygame.Surface((340,45)).convert_alpha()

        self.xPos = x
        self.yPos = y

        #self.hitbox_rect = pygame.Rect(self.spritesurf.get_rect().centerx - (self.size[0]/2), 192 - self.size[1], self.size[0], self.size[1])

        self.timer_rect = pygame.Rect(147, 0, 45, 45)

        self.life_rect_bg = pygame.Rect(19, 10, 300, 27)

        self.playerL_life_rect_fg = pygame.Rect(19, 10, 128, 27)
        self.playerR_life_rect_fg = pygame.Rect(192, 10, 128, 27)

    def draw(self, window):
        self.spritesurf.fill([0,0,0,0])

        pygame.draw.rect(self.spritesurf,(255,255,255), self.life_rect_bg)
        pygame.draw.rect(self.spritesurf,(195,195,195), self.timer_rect)

        pygame.draw.rect(self.spritesurf,(255,0,0), self.playerL_life_rect_fg)
        pygame.draw.rect(self.spritesurf,(0,0,255), self.playerR_life_rect_fg)
        
        window.blit(self.spritesurf, (self.xPos, self.yPos))
        #self.spritesurf.blit(ryu_attack, (0,0))

    def update(self, playerL_health, playerR_health):
        ratioL = playerL_health / 100
        ratioR = playerR_health / 100

        self.playerL_life_rect_fg = pygame.Rect(128 - (128 * ratioL) + 19, 10, 128 * ratioL, 27)
        self.playerR_life_rect_fg = pygame.Rect(192, 10, 128 * ratioR, 27)

def flip_players(playerL, playerR):
    playerL.isFlipped = False if playerR.rect.centerx > playerL.rect.centerx else True

#might need to update this
def push_player(playerL, playerR):
    collision_tolerance = 10
    if playerL.isWalking:
        if playerL.rect.colliderect(playerR.rect):
            if abs(playerL.rect.right - playerR.rect.left) < collision_tolerance:
                #print("hello")
                playerR.xPos += 4
            if abs(playerL.rect.left - playerR.rect.right) < collision_tolerance:
                playerR.xPos -= 4

def check_collisions(attacker, victim):
    if attacker.attack_rect.colliderect(victim.rect) and attacker.isAttacking:
        print(("player_2" if attacker.isPlayer2 else "player_1") + " attack succeeded")
        victim.health -= 10
    else:
        print(("player_2" if attacker.isPlayer2 else "player_1") + " attack failed")
    attacker.isAttacking = False # might need to change this

def main():

    lifebar = LifebarSurf(0,10)

    gameRunning = True

    while gameRunning:
        screen.blit(bg, (0,0))

        #PLAYER CONTROLS:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #player exits window
                gameRunning = False
            if event.type == KEYDOWN:                
                if event.key == K_d:
                    player_1.right_pressed = True
                if event.key == K_a:
                    player_1.left_pressed = True
                if event.key == K_w:
                    player_1.up_pressed = True
                if event.key == K_SPACE:
                    #player_1.attack_pressed = True
                    player_1.isAttacking = True
                if event.key == K_s:
                    player_1.down_pressed = True

                if event.key == K_KP_6:
                    player_2.right_pressed = True
                if event.key == K_KP_4:
                    player_2.left_pressed = True
                if event.key == K_KP_8:
                    player_2.up_pressed = True
                if event.key == K_KP_0:
                    player_2.isAttacking = True
                if event.key == K_KP_5:
                    player_2.down_pressed = True

            if event.type == KEYUP:
                if event.key == K_d:
                    player_1.right_pressed = False
                if event.key == K_a:
                    player_1.left_pressed = False
                if event.key == K_w:
                    player_1.up_pressed = False
                if event.key == K_SPACE:
                    #player_1.attack_pressed = False
                    player_1.isAttacking = False
                if event.key == K_s:
                    player_1.down_pressed = False
                
                if event.key == K_KP_6:
                    player_2.right_pressed = False
                if event.key == K_KP_4:
                    player_2.left_pressed = False
                if event.key == K_KP_8:
                    player_2.up_pressed = False
                if event.key == K_KP_0:
                    player_2.isAttacking = False
                if event.key == K_KP_5:
                    player_2.down_pressed = False
        
        player_1.update(WINDOW_SIZE)
        player_2.update(WINDOW_SIZE)

        lifebar.update(player_1.health, player_2.health)
        lifebar.draw(screen)
        

        #print(player_1.attack_pressed)
        #print(player_1.rect.top, player_1.isDucking)

        #PLAYER 1 ACTIONS
        player_1.draw(screen)
        flip_players(player_1, player_2)
        if player_1.isAttacking:
            check_collisions(player_1, player_2)
            print("player_1.health: {0}, player_2.health: {1}".format(player_1.health, player_2.health))

        push_player(player_1, player_2)

        #PLAYER 2 ACTIONS
        player_2.draw(screen)
        flip_players(player_2, player_1)
        if player_2.isAttacking:
            check_collisions(player_2, player_1)
            print("player_1.health: {0}, player_2.health: {1}".format(player_1.health, player_2.health))
        
        push_player(player_2, player_1)

        #if player_2.attack_rect.colliderect(player_1.rect) and player_2.isAttacking:
        #    print("player2 attack player1")

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()