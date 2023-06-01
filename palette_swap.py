import pygame
clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()
pygame.display.set_caption("palette swap test")

WINDOW_SIZE = [420, 106]
screen = pygame.display.set_mode(WINDOW_SIZE)

ryu = pygame.image.load("./ryu/idle.png").convert()
#ryu_copy = ryu

def palette_swap(screen, colOld, colNew):
    img_copy = pygame.Surface(ryu.get_size())
    img_copy.fill(colNew)
    screen.set_colorkey(colOld)
    img_copy.blit(screen,(0,0))
    return img_copy

ryu_orig_cols = [(248,248,248), (200,232,216), (184,200,184), (152,168,152), (112,136,112), (248,0,0), (112,0,0)]
ryu_new_cols =  [(64,64,136), (48,48,96), (32,32,80), (16,16,64), (0,0,48), (168,0,0), (184,0,0)]



for i in range(0, 7):
    ryu = palette_swap(ryu, ryu_orig_cols[i], ryu_new_cols[i])
    

def get_image(sheet, frame, width, height):
    img = pygame.Surface((width, height)).convert()
    img.blit(sheet, (0,0), ((frame * width),0, width, height))
    img.set_colorkey((0,0,0))

    return img

def main():

    anim_list = []
    last_update = pygame.time.get_ticks()
    anim_frame = 0

    for i in range(0,6):
        anim_list.append(get_image(ryu, i, 70, 106))


    #frame_0 = get_image(ryu_copy, 70, 106)

    gameRunning = True

    while gameRunning:
        screen.fill((0,255,0))
        
        current_time = pygame.time.get_ticks()
        
        if current_time - last_update >= 80:
            anim_frame += 1
            last_update = current_time
            if anim_frame >= len(anim_list):
                anim_frame = 0

        screen.blit(anim_list[anim_frame], (0, 0))
        
        #screen.blit(frame_0, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # user closes the window
                gameRunning = False
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()