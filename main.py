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
        print(("player2" if attacker.isPlayer2 else "player1") + " hits other player")
    else:
        print("no collision")
    attacker.isAttacking = False # might need to change this

def main():
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

        #print(player_1.attack_pressed)
        #print(player_1.rect.top, player_1.isDucking)

        #PLAYER 1 ACTIONS
        player_1.draw(screen)
        flip_players(player_1, player_2)
        if player_1.isAttacking:
            check_collisions(player_1, player_2)

        push_player(player_1, player_2)

        #PLAYER 2 ACTIONS
        player_2.draw(screen)
        flip_players(player_2, player_1)
        if player_2.isAttacking:
            check_collisions(player_2, player_1)
        
        push_player(player_2, player_1)

        #if player_2.attack_rect.colliderect(player_1.rect) and player_2.isAttacking:
        #    print("player2 attack player1")

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()