import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Paramètres de la grille
TAILLE = 50
VIDE, ACTIF, REFRACTAIRE = 0, 1, 2
#2 cellule temporairement inactive après activation

def mise_a_jour(grille):
    nouvelle_grille = np.zeros_like(grille)#crée un tableau de la même forme que grille, mais rempli de zéros.sans modifier la grille existante.
    for x in range(TAILLE):
        for y in range(TAILLE):
            voisins = grille[max(x - 1, 0):min(x + 2, TAILLE), max(y - 1, 0):min(y + 2, TAILLE)]#max et min empeche de depasser le grille
            compte_actif = np.sum(voisins == ACTIF) - (grille[x, y] == ACTIF) #Compte les voisins actifs (en soustrayant la cellule centrale si elle est active)

            #regle de transition de brian's brain
            if grille[x, y] == VIDE and compte_actif == 2:
                nouvelle_grille[x, y] = ACTIF
            elif grille[x, y] == ACTIF:
                nouvelle_grille[x, y] = REFRACTAIRE
            elif grille[x, y] == REFRACTAIRE:
                nouvelle_grille[x, y] = VIDE
    return nouvelle_grille


# Init de la grille
grille = np.random.choice([VIDE, ACTIF], size=(TAILLE, TAILLE), p=[0.8, 0.2])

# Crée une figure matplotlib Affiche la grille initiale
fig, ax = plt.subplots()
img = ax.imshow(grille, cmap="Blues_r", interpolation="spline36")#pour la visibilité de la cellule

#mise à jour de chaque frame
def anime(i):
    global grille
    grille = mise_a_jour(grille)
    img.set_data(grille)
    return [img]


ani = animation.FuncAnimation(fig, anime, frames=200, interval=50, blit=True)#200 frame,50ms entre chaque frame et optimise l'affichage
plt.show()
