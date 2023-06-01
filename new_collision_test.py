import pygame
clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()
pygame.display.set_caption("new collision system test")

WINDOW_SIZE = [512, 480]
screen = pygame.display.set_mode(WINDOW_SIZE)

#TODO: check if surface x and y is optimal for changing values, consider using sprites

def main():
    gameRunning = True

    player_dimensions = [48,84]
    attack_coords = [24, 108] #relative to centerx of sprite rect

    player_sprite_surf = pygame.Surface((192,192))

    while gameRunning:

        screen.fill((0,0,0))
        player_sprite_surf.fill((0,0,255))

        player_hitbox_rect = pygame.Rect(player_sprite_surf.get_rect().centerx - (player_dimensions[0]/2), 192 - player_dimensions[1], player_dimensions[0], player_dimensions[1])

        # attack right
        attack_rect = pygame.Rect(player_sprite_surf.get_rect().centerx + attack_coords[0],player_sprite_surf.get_rect().top + attack_coords[1],48,18)

        pygame.draw.rect(player_sprite_surf,(255,0,0), player_hitbox_rect)
        pygame.draw.rect(player_sprite_surf,(0,255,0), attack_rect)

        player_sprite_surf = pygame.transform.flip(player_sprite_surf, True, False)
        screen.blit(player_sprite_surf, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # user closes the window
                gameRunning = False
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()