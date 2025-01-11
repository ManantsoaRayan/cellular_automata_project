import numpy as np
import matplotlib.pyplot as plt

# Paramètres de la simulation
grid_size = 20
iterations = 7
densite = 0.4

# Initialisation de la grille 3D avec des cellules vivantes aléatoires pomur controler le flux d'apparition des cellules vivant p 0.1 est bien equlibré
grid = np.random.choice([0, 1], size=(grid_size, grid_size, grid_size), p=[1 - densite, densite])


def count_neighbors(x, y, z, grid):
    """Compte les voisins vivants autour d'une cellule """
    count = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                # exclure le centre, on ne compte pas sont propre cellule comme voisin
                if (i == x and j == y and k == z):
                    continue
                # Compte si la cellule voisine est vivante et dans les limites de la grille
                if 0 <= i < grid_size and 0 <= j < grid_size and 0 <= k < grid_size:
                    count += grid[i, j, k]
    return count


def update(grid):
    """Met à jour la grille suivant le  "Jeu de la Vie" en 3D."""
    new_grid = grid.copy()

    for x in range(grid_size):
        for y in range(grid_size):
            for z in range(grid_size):
                # Compter les voisins vivants
                neighbors = count_neighbors(x, y, z, grid)

                # Règles en 3D
                if grid[x, y, z] == 1:
                    # Si 4 trop peu de cellule vivant si sup à 6 trop de population alors cellule morte
                    if neighbors < 4 or neighbors > 6:
                        new_grid[x, y, z] = 0
                else:
                    # Une cellule morte devient vivante si elle a exactement 5 voisins vivants
                    if neighbors == 5:
                        new_grid[x, y, z] = 1

    return new_grid


# micreer nouvelle fenêtre de figure vide
fig = plt.figure()
#1ère ligne /1ère colonne /1er graphique
ax = fig.add_subplot(111, projection='3d')#indique hoe mila graphique 3D
#ax dessine la figure 3D

# Couleurs et positions pour les cellules vivantes
def plot_grid(grid):
    ax.clear()# clear the last dessin
    ax.set_title("Automate Cellulaire 3D")
    x, y, z = grid.nonzero()  # trouver rapidement les indices des éléments qui sont 1 ou vivant et le dessine dans la figure 3D

    # Scatter pour dessiner les cellules vivantes avec des couleurs
    ax.scatter(x, y, z, color='indigo', marker='*', s=20, alpha=0.8)
    #dessiner anle axe de grille entre 0 et 20x20x20
    ax.set_xlim([0, grid_size])
    ax.set_ylim([0, grid_size])
    ax.set_zlim([0, grid_size])


# Simuler et afficher avec les nombre d'iteration qu'on veut
for i in range(iterations):
    plot_grid(grid)
    plt.pause(1)  # Pause d'une seconde pour voir l'evolution de l'automate
    grid = update(grid)  # Mise à jour de la grille

plt.show()
