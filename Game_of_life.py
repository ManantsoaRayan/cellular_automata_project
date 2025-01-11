import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Dimensions de la grille
grid_size = 50

# Création de la grille initiale avec des cellules vivantes aléatoirement
np.random.seed(0)
grid = np.random.choice([0, 1], size=(grid_size, grid_size), p=[0.8, 0.2])


def update_grid(grid):
    """Met à jour la grille selon les règles du Jeu de la Vie de Conway."""
    # Création d'une copie de la grille pour éviter les modifications en place
    new_grid = grid.copy()

    for row in range(grid_size):
        for col in range(grid_size):
            # Comptage des cellules vivantes dans le voisinage (8 voisins)
            total = int((grid[row, (col - 1) % grid_size] + grid[row, (col + 1) % grid_size] +
                         grid[(row - 1) % grid_size, col] + grid[(row + 1) % grid_size, col] +
                         grid[(row - 1) % grid_size, (col - 1) % grid_size] + grid[
                             (row - 1) % grid_size, (col + 1) % grid_size] +
                         grid[(row + 1) % grid_size, (col - 1) % grid_size] + grid[
                             (row + 1) % grid_size, (col + 1) % grid_size]))

            # Règles du Jeu de la Vie
            if grid[row, col] == 1:
                if (total < 2) or (total > 3):  # Moins de 2 ou plus de 3 voisins : meurt
                    new_grid[row, col] = 0
            else:
                if total == 3:  # Exactement 3 voisins : naissance d'une nouvelle cellule
                    new_grid[row, col] = 1

    return new_grid


# Création de l'animation
fig, ax = plt.subplots()
img = ax.imshow(grid, cmap="binary")


def animate(i):
    """Fonction d'animation pour mettre à jour la grille à chaque étape."""
    global grid
    grid = update_grid(grid)
    img.set_data(grid)
    return img,


# Lancer l'animation
ani = animation.FuncAnimation(fig, animate, frames=50, interval=200, blit=True)
plt.title("Jeu de la Vie de Conway", fontsize=16, color="pink")
plt.show()
