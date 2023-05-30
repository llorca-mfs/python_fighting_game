import pygame
clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()
pygame.display.set_caption("palette swap test")

WINDOW_SIZE = [416, 106]
screen = pygame.display.set_mode(WINDOW_SIZE)

ryu = pygame.image.load("./ryu/idle.png").convert()

def palette_swap(screen, colOld, colNew):
    img_copy = pygame.Surface(ryu.get_size())
    img_copy.fill(colNew)
    screen.set_colorkey(colOld)
    img_copy.blit(screen,(0,0))
    return img_copy


ryu = palette_swap(ryu, (248,248,248),(64,64,136))
ryu = palette_swap(ryu, (200,232,216),(48,48,96))
ryu = palette_swap(ryu, (184,200,184),(32,32,80))
ryu = palette_swap(ryu, (152,168,152),(16,16,64))
ryu = palette_swap(ryu, (112,136,112),(0,0,48))

ryu = palette_swap(ryu, (248,0,0),(168,0,0))
ryu = palette_swap(ryu, (112,0,0),(184,0,0))


#ryu.set_colorkey((0,0,0))

def main():
    gameRunning = True

    while gameRunning:
        screen.fill((0,0,0))
        screen.blit(ryu, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # user closes the window
                gameRunning = False
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()