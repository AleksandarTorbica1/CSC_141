import pygame, sys

pygame.init()

pumpkin_image = pygame.image.load ('assignments/code_jam/media/pumpkin.png')
pumpkin_image = pygame.transform.scale(pumpkin_image, (430,430))

face_1 = pygame.image.load ('assignments/code_jam/media/face_1.png')
face_1 = pygame.transform.scale(face_1, (200,200))

face_2 = pygame.image.load ('assignments/code_jam/media/face_3.png')
face_2 = pygame.transform.scale(face_2, (200,200))

faces = [face_1, face_2]

screen = pygame.display.set_mode((950,540))
current = 0
melt = 0
melting = False

screen = pygame.display.set_mode((950,540))
clock = pygame.time.Clock()

running = True
rotate_amount = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:      
                melting = True
            if event.key == pygame.K_RETURN:     
                current = 1 - current
                melt = 0
                melting = False
            if event.key in (pygame.K_DELETE, pygame.K_BACKSPACE):
                melt = 0
                melting = False

    screen.fill((30,30,30))
    screen.blit(pumpkin_image, (300,100))

    if melting:
        melt += 2

    if melt < 150:
        face = pygame.transform.scale(faces[current], (200, 200 + melt))
        face.set_alpha(int(255 - melt * 1.7))
        screen.blit(face, (385,250))              

    pygame.display.flip()
    clock.tick(60)