import pygame

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()
pygame.display.set_caption("The King of Streets \'23")

WINDOW_SIZE = [340, 256] #snes native resolution

screen = pygame.display.set_mode(WINDOW_SIZE)

bg = pygame.image.load("bg_256.png").convert_alpha()

def main():
    gameRunning = True

    while gameRunning:
        screen.blit(bg, (0,0))

        #PLAYER CONTROLS:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #player exits window
                gameRunning = False
            
            
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()