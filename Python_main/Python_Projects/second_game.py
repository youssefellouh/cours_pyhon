import pygame
import time
import random

pygame.init()

# Paramètres du jeu
largeur = 800
hauteur = 600
taille_case = 20

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (255, 0, 0)

# Initialisation de l'écran
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu de Snake")

# Fonction principale du jeu
def jeu_snake():
    serpent = [(largeur / 2, hauteur / 2)]
    direction = (0, 0)
    pomme = creer_pomme()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction = (0, -taille_case)
                elif event.key == pygame.K_DOWN:
                    direction = (0, taille_case)
                elif event.key == pygame.K_LEFT:
                    direction = (-taille_case, 0)
                elif event.key == pygame.K_RIGHT:
                    direction = (taille_case, 0)

        serpent[0] = (serpent[0][0] + direction[0], serpent[0][1] + direction[1])

        # Vérifier les collisions
        if serpent[0] == pomme:
            serpent.append((0, 0))  # Ajouter une nouvelle partie au serpent
            pomme = creer_pomme()

        # Dessiner l'écran
        ecran.fill(blanc)
        for partie in serpent:
            pygame.draw.rect(ecran, noir, (partie[0], partie[1], taille_case, taille_case))

        pygame.draw.rect(ecran, rouge, (pomme[0], pomme[1], taille_case, taille_case))
        pygame.display.update()

        # Limiter la vitesse du serpent
        time.sleep(0.1)

# Fonction pour créer une nouvelle pomme
def creer_pomme():
    x = random.randrange(0, largeur - taille_case, taille_case)
    y = random.randrange(0, hauteur - taille_case, taille_case)
    return x, y

# Lancer le jeu
jeu_snake()
