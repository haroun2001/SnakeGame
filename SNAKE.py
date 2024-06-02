import pygame
import time
import random

# Initialiser Pygame
pygame.init()

# Couleurs
blanc = (255, 255, 255)
jaune = (255, 255, 102)
noir = (0, 0, 0)
rouge = (213, 50, 80)
vert = (0, 255, 0)
bleu = (50, 153, 213)

# Dimensions de la fenêtre
largeur = 800
hauteur = 600

# Création de la fenêtre de jeu
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption('Snake Game')

horloge = pygame.time.Clock()

# Taille des blocs du serpent
taille_bloc = 20
vitesse = 15

# Police de caractère
police_style = pygame.font.SysFont("bahnschrift", 25)

# Fonction pour afficher le score
def afficher_score(score, niveau):
    valeur = police_style.render("Score: " + str(score) + " Niveau: " + str(niveau), True, noir)
    fenetre.blit(valeur, [0, 0])

# Boucle principale du jeu
def boucle_jeu():
    game_over = False
    game_close = False

    x1 = largeur / 2
    y1 = hauteur / 2

    x1_change = 0
    y1_change = 0

    serpent_corps = []
    longueur_serpent = 1

    nourriturex = round(random.randrange(0, largeur - taille_bloc) / 20.0) * 20.0
    nourrituredx = round(random.randrange(0, hauteur - taille_bloc) / 20.0) * 20.0

    score = 0
    niveau = 1
    obstacles = []

    while not game_over:

        while game_close:
            fenetre.fill(blanc)
            message = police_style.render("Vous avez perdu ! Appuyez sur Q-Quitter ou C-Continuer", True, rouge)
            fenetre.blit(message, [largeur / 6, hauteur / 3])
            afficher_score(score, niveau)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        boucle_jeu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -taille_bloc
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = taille_bloc
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -taille_bloc
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = taille_bloc
                    x1_change = 0

        if x1 >= largeur or x1 < 0 or y1 >= hauteur or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        fenetre.fill(bleu)

        for obstacle in obstacles:
            pygame.draw.rect(fenetre, rouge, [obstacle[0], obstacle[1], taille_bloc, taille_bloc])

        pygame.draw.rect(fenetre, vert, [nourriturex, nourrituredx, taille_bloc, taille_bloc])
        serpent_tete = []
        serpent_tete.append(x1)
        serpent_tete.append(y1)
        serpent_corps.append(serpent_tete)
        if len(serpent_corps) > longueur_serpent:
            del serpent_corps[0]

        for x in serpent_corps[:-1]:
            if x == serpent_tete:
                game_close = True

        for x in serpent_corps:
            pygame.draw.rect(fenetre, noir, [x[0], x[1], taille_bloc, taille_bloc])

        afficher_score(score, niveau)

        pygame.display.update()

        if x1 == nourriturex and y1 == nourrituredx:
            nourriturex = round(random.randrange(0, largeur - taille_bloc) / 20.0) * 20.0
            nourrituredx = round(random.randrange(0, hauteur - taille_bloc) / 20.0) * 20.0
            longueur_serpent += 1
            score += 1

            if score % 5 == 0:
                niveau += 1
                # Ajouter un nouvel obstacle
                obstacle_x = round(random.randrange(0, largeur - taille_bloc) / 20.0) * 20.0
                obstacle_y = round(random.randrange(0, hauteur - taille_bloc) / 20.0) * 20.0
                obstacles.append([obstacle_x, obstacle_y])

        for obstacle in obstacles:
            if x1 == obstacle[0] and y1 == obstacle[1]:
                game_close = True

        horloge.tick(vitesse)

    pygame.quit()
    quit()

boucle_jeu()
