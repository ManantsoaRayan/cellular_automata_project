import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Paramètres de la grille
TAILLE = 50
VIDE, ACTIF, REFRACTAIRE = 0, 1, 2
PROBA_REVIVRE = 0.01  # Probabilité qu'une cellule morte devienne active spontanément


def mise_a_jour(grille):
    nouvelle_grille = np.zeros_like(grille)
    for x in range(TAILLE):
        for y in range(TAILLE):
            voisins = grille[max(x - 1, 0):min(x + 2, TAILLE), max(y - 1, 0):min(y + 2, TAILLE)]
            compte_actif = np.sum(voisins == ACTIF) - (grille[x, y] == ACTIF)

            if grille[x, y] == VIDE:
                # Revivification aléatoire
                if np.random.random() < PROBA_REVIVRE:
                    nouvelle_grille[x, y] = ACTIF
                elif compte_actif == 2:
                    nouvelle_grille[x, y] = ACTIF
            elif grille[x, y] == ACTIF:
                nouvelle_grille[x, y] = REFRACTAIRE
            elif grille[x, y] == REFRACTAIRE:
                nouvelle_grille[x, y] = VIDE
    return nouvelle_grille


# Initialisation de la grille
grille = np.random.choice([VIDE, ACTIF], size=(TAILLE, TAILLE), p=[0.8, 0.2])

# Animation
fig, ax = plt.subplots()
img = ax.imshow(grille, cmap="magma", interpolation="spline36")

#mise à jour de chaque frame
def anime(i):
    global grille
    grille = mise_a_jour(grille)
    img.set_data(grille)
    return [img]


ani = animation.FuncAnimation(fig, anime, frames=200, interval=50, blit=True)
plt.show()
