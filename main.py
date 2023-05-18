import pygame
from player import Player

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()
pygame.display.set_caption("The King of Streets \'23")

WINDOW_SIZE = [340, 256]

screen = pygame.display.set_mode(WINDOW_SIZE)

player_1 = Player(62,128)
#player_2 = Player(230,128)

bg = pygame.image.load("bg_256.png").convert_alpha()

def main():
    gameRunning = True

    while gameRunning:
        screen.blit(bg, (0,0))

        print(player_1.isDucking)

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
                if event.key == K_s:
                    player_1.down_pressed = True
            if event.type == KEYUP:
                if event.key == K_d:
                    player_1.right_pressed = False
                if event.key == K_a:
                    player_1.left_pressed = False
                if event.key == K_w:
                    player_1.up_pressed = False
                if event.key == K_s:
                    player_1.down_pressed = False
            
        player_1.draw(screen)
        player_1.update(WINDOW_SIZE)

        #player_2.draw(screen)

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()