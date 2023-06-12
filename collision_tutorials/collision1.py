import pygame, sys

pygame.init()
clock = pygame.time.Clock()
width, height = 800, 800

screen = pygame.display.set_mode((width, height))

moving_rect = pygame.Rect(350,350, 100,100)
x_speed, y_speed = 5, 4

other_rect = pygame.Rect(300, 600, 200, 100)
other_speed = 2

def bouncing_rect():
    global x_speed, y_speed

    #move rect via x and y coords
    moving_rect.x += x_speed
    moving_rect.y += y_speed

    #collision with screen borders

    #if collision is detected in left or right area of screen
    if moving_rect.right >= width or moving_rect.left <= 0:
        x_speed = -x_speed

    #if collision is detected in top or bottom area of screen
    if moving_rect.bottom >= height or moving_rect.top <= 0:
        y_speed = -y_speed

    #collision with rect
    collision_tolerance = 10

    if moving_rect.colliderect(other_rect):
        #top of red rect and bottom of white rect collide
        if abs(other_rect.top - moving_rect.bottom) < collision_tolerance:
            y_speed *= -1
        if abs(other_rect.bottom - moving_rect.top) < collision_tolerance:
            y_speed *= -1
        if abs(other_rect.right - moving_rect.left) < collision_tolerance:
            x_speed *= -1
        if abs(other_rect.left - moving_rect.right) < collision_tolerance:
            x_speed *= -1

    pygame.draw.rect(screen, (255,255,255), moving_rect)
    pygame.draw.rect(screen, (255,0,0), other_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill ((30,30,30))

    bouncing_rect()
    print("x: {0}, y: {1}".format(moving_rect.x, moving_rect.y))

    pygame.display.update()
    clock.tick(60)
