import pygame, os, sys

pygame.init()

my_image = pygame.image.load ('assignments/code_jam/media/pumpkin.png')
screen = pygame.display.set_mode((950,540))
# screen.fill((255,255,0))
running = True
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((230,3,79))
    screen.blit(my_image, (300,100))
    pygame.display.flip()