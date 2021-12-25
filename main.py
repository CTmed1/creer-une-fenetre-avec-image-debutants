# importer pygame
import pygame



# créer la fenêtre
pygame.display.set_caption('Bonne année!')
screen = pygame.display.set_mode((225, 225))


# importer et charger l'image
background = pygame.image.load('th.jpg')



# créer la boucle
running = True

while running:

    # appliquer l'image
    screen.blit(background, ((0, 0)))
    pygame.display.flip()


    # appliquer la boucle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
