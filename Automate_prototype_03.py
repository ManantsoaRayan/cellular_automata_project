import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Paramètres de la simulation
grid_size = 50  # Taille de la grille (50x50 cellules)
initial_density = 0.2  # Probabilité qu'une cellule soit vivante au départ
iterations = 100  # Nombre d'itérations de la simulation

# Initialisation de la grille avec des cellules vivantes de façon aléatoire
grid = np.random.choice([0, 1], size=(grid_size, grid_size), p=[1 - initial_density, initial_density])


def update(grid):
    """Met à jour la grille selon les règles du Jeu de la Vie."""
    # Création d'une nouvelle grille pour stocker l'état futur
    new_grid = grid.copy()

    # Parcours de chaque cellule dans la grille
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            # Calcul du nombre de voisins vivants autour de la cellule (i, j)
            total = (grid[i - 1, j - 1] + grid[i - 1, j] + grid[i - 1, (j + 1) % grid_size] +
                     grid[i, j - 1] + grid[i, (j + 1) % grid_size] +
                     grid[(i + 1) % grid_size, j - 1] + grid[(i + 1) % grid_size, j] + grid[
                         (i + 1) % grid_size, (j + 1) % grid_size])

            # Appliquer les règles de Conway
            if grid[i, j] == 1:
                # Règle de survie ou mort
                if total < 2 or total > 3:
                    new_grid[i, j] = 0  # La cellule meurt
            else:
                # Règle de naissance
                if total == 3:
                    new_grid[i, j] = 1  # Une nouvelle cellule naît

    return new_grid


def animate(frame, img, grid):
    """Fonction d'animation pour mettre à jour l'image de la grille."""
    # Mettre à jour la grille pour le prochain état
    new_grid = update(grid)
    img.set_array(new_grid)

    # Copier la nouvelle grille pour l'utiliser dans la prochaine itération
    grid[:] = new_grid[:]
    return img,


# Configuration de la figure et de l'animation
fig, ax = plt.subplots()
img = ax.imshow(grid, cmap='binary')
ani = animation.FuncAnimation(fig, animate, fargs=(img, grid), frames=iterations, interval=200, repeat=False)

# Affichage de l'animation
plt.title("Jeu de la Vie de Conway")
plt.show()
