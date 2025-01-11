# Import des bibliothèques nécessaires pour le calcul et l'affichage
import numpy as np
import matplotlib.pyplot as plt


# Définition de la règle 30 pour les automates cellulaires élémentaires
def rule_30(current_state):
    """Applique la règle 30 à une ligne d'état binaire."""
    # Longueur de la ligne actuelle
    length = len(current_state)

    # Initialisation de la nouvelle ligne d'état (même taille, toutes les cellules à 0)
    new_state = np.zeros(length, dtype=int)

    # Application de la règle de transition pour chaque cellule (sauf les bords)
    for i in range(1, length - 1):
        # Extraction des valeurs gauche, centre, et droite pour le voisinage
        left, center, right = current_state[i - 1], current_state[i], current_state[i + 1]

        # Calcul de la nouvelle valeur en fonction de la règle 30
        new_state[i] = left ^ (center or right)  # XOR logique de la règle 30

    return new_state


# Paramètres de la simulation
size = 101  # Largeur de la grille (nombre de cellules)
iterations = 50  # Nombre de générations (lignes à dessiner)

# Initialisation de la première ligne : une seule cellule active au centre
state = np.zeros(size, dtype=int)
state[size // 2] = 1  # La cellule centrale est active (1)

# Liste pour stocker l'évolution de l'automate cellulaire au fil des générations
history = [state]

# Génération de chaque nouvelle ligne d'état en appliquant la règle 30
for _ in range(iterations):
    # Appliquer la règle et obtenir la nouvelle ligne d'état
    state = rule_30(state)

    # Ajouter la nouvelle ligne à l'historique
    history.append(state)

# Transformation de l'historique en tableau NumPy pour l'affichage
history = np.array(history)

# Configuration de la figure pour un joli rendu visuel
plt.figure(figsize=(10, 8))
plt.imshow(history, cmap='binary', interpolation='nearest')
plt.title("Illustration de l'Automate Cellulaire avec Règle 30", fontsize=16, color="blue")
plt.xlabel("Cellules", fontsize=12)
plt.ylabel("Générations", fontsize=12)
plt.xticks([])
plt.yticks([])
plt.grid(False)

# Affichage du motif généré
plt.show()
