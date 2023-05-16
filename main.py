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

    isWalking_p1 = "False"
    isWalking_p2 = "False"

    while gameRunning:
        screen.blit(bg, (0,0))
        print("isWalking_p1 = {0}, isWalking_p2 = {1}".format(isWalking_p1, isWalking_p2))

        #PLAYER CONTROLS:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #player exits window
                gameRunning = False

            elif event.type == KEYDOWN:
                #PLAYER 1
                if event.key == K_a and isWalking_p1 == "False":
                    isWalking_p1 = "Left"
                if event.key == K_d and isWalking_p1 == "False":
                    isWalking_p1 = "Right"
                
                #PLAYER 2
                if event.key == K_j and isWalking_p2 == "False":
                    isWalking_p2 = "Left"
                if event.key == K_l and isWalking_p2 == "False":
                    isWalking_p2 = "Right"
            elif event.type == KEYUP:
                #PLAYER 1
                if event.key == K_a and not isWalking_p1 == "False":
                    isWalking_p1 = "False"
                if event.key == K_d and not isWalking_p1 == "False":
                    isWalking_p1 = "False"

                #PLAYER 2
                if event.key == K_j and not isWalking_p2 == "False":
                    isWalking_p2 = "False"
                if event.key == K_l and not isWalking_p2 == "False":
                    isWalking_p2 = "False"
            
            
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()