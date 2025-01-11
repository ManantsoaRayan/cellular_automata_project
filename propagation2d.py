"""
    Propagation d'un incendie de foret basecur le voisinage de moore
    REGLE:
        chaque cellule peut etre dans l'un de ces etats:
            0 : Cellule vide(pas d'arbre)
            1 : cellule contenant un arbre sain(pas en feu)
            2 : Cellule en feu
    REGLE DE TRANSITION 
        * Un arbre sain devient en feu si au moins un voisin est en feu
        * Une cellule en feu devient vide apres une etape
        * une cellule vide reste vide
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors as mcolors

rows, cols = 100, 100
steps = 100

grid = np.random.choice([0, 1], size = (rows, cols), p =[0.3, 0.7])
#allumer un arbre au centre
grid[rows // 2, cols // 2]= 2

def count_fire_neighbors(grid, x, y):
    fire_count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0  and dy == 0:
                continue 
            nx, ny = (x + dx)% rows, (y + dy) % cols
            if grid[nx, ny] == 2:
                fire_count += 1
    return fire_count

def update(grid):
    new_grid = grid.copy()
    for x in range (rows):
        for y in range (cols):
            if grid[x, y] == 1:
                if count_fire_neighbors(grid, x, y) > 0:
                    new_grid[x, y] = 2
            elif grid[x, y] == 2:
                new_grid[x, y] =0
    return new_grid

def animate(frame):
    global grid
    grid[:] = update(grid)
    mat.set_data(grid)
    return [mat]
    
if __name__ == "__main__":
    
    fig, ax = plt.subplots()
    cmap = mcolors.ListedColormap(["black", "green", "red"])
    bounds= [0, 0.5, 1.5, 2.5]
    norm = mcolors.BoundaryNorm(bounds, cmap.N )

    mat = ax.matshow(grid, cmap = cmap, norm = norm)
    plt.colorbar(mat)

    ani = animation.FuncAnimation(fig, animate, frames = steps, interval = 100, blit = True)
    plt.title("automate cellulaire 2D - Propagation de feu")
    plt.show()





