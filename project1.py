import pygame
pygame.init()

screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Ball Bounce Game")

x = 300
y = 200
dx = 3
dy = 3

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += dx
    y += dy

    if x > 580 or x < 20:
        dx = -dx
    if y > 380 or y < 20:
        dy = -dy

    screen.fill((255,255,255))
    pygame.draw.circle(screen,(0,0,255),(x,y),20)
    pygame.display.update()

pygame.quit()
