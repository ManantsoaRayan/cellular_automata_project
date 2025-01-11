import matplotlib.pyplot as plt

# The ruleset generator
def get_rule(number: int) -> list:
    str_number = [int(e) for e in list(format(number, "b"))]
    return [0] * (8 - len(str_number)) + str_number
    

# Rule application
def apply_rule(left, center, right, rule: list):
    index = 4 * left + 2 * center + right  # Binary to decimal
    return rule[index]

# Generate next generation
def next_generation(cells: list, rule: list):
    new_generation = [0] * len(cells)
    for i in range(len(cells)):
        left = cells[i - 1] if i > 0 else 0  # Left neighbor
        center = cells[i]
        right = cells[i + 1] if i < len(cells) - 1 else 0  # Right neighbor
        new_generation[i] = apply_rule(left, center, right, rule)
    return new_generation

# Interactive visualization
def visualize_rules_interactively():
    generation_number = 1024
    cells = [0] * 1024
    cells[len(cells) // 2] = 1  # Start with a single live cell in the center

    rule_number = 129  # Start with rule 0
    fig, ax = plt.subplots(figsize=(10, 10))
    plt.ion()  # interactive mode

    def update_rule(rule_number):
        """Update the plot for a given rule."""
        nonlocal cells
        ruleset = get_rule(rule_number)
        grid = []

        # Generate grid for the current rule
        temp_cells = cells[:]
        for _ in range(generation_number):
            grid.append(temp_cells)
            temp_cells = next_generation(temp_cells, ruleset)

        # Update the plot
        ax.clear()
        ax.set_title(f"Rule {rule_number}")
        ax.imshow(grid, cmap="binary", interpolation="nearest")
        fig.canvas.draw()

    def on_key(event):
        """Handle key press events."""
        nonlocal rule_number
        if event.key == 'n':
            rule_number = 100 if rule_number == 0 else (rule_number + 1) % 256   # Cycle through rule
            update_rule(rule_number)
        if event.key == 'p':
            rule_number = 100 if rule_number < 100 else (rule_number - 1) % 256  # Cycle through rules
            update_rule(rule_number)

    # Connect the key press event
    fig.canvas.mpl_connect('key_press_event', on_key)

    # Show the first rule
    update_rule(rule_number)
    plt.show(block=True)  # Block until the user closes the window


if __name__ == "__main__":
    visualize_rules_interactively()

