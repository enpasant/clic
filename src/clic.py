#!/usr/bin/env python3

import argparse
from rich.console import Console
from asciimatics.screen import Screen
import numpy as np

# Initialize Rich Console
console = Console()

console.print("[bold cyan]clic - v1.23[/]")

def calc(equation):
    try:
        # Evaluate the equation with safe math functions
        result = eval(equation, {"__builtins__": None}, {"sin": np.sin, "cos": np.cos, "tan": np.tan, 
                                                          "sqrt": np.sqrt, "log": np.log, "pi": np.pi, 
                                                          "e": np.e, "abs": abs})
        console.print(f"[bold green]Result: {result}[/]")
        return result
    except Exception as e:
        console.print(f"[bold red]Error in the equation: {e}[/]")
        return None

def draw_graph(equation, screen):
    try:
        # Generate x and y values for the graph
        x_values = np.linspace(-10, 10, screen.width)
        y_values = eval(equation, {"__builtins__": None}, {"x": x_values, "sin": np.sin, "cos": np.cos, 
                                                            "tan": np.tan, "sqrt": np.sqrt, "log": np.log, 
                                                            "pi": np.pi, "e": np.e, "abs": abs})

        # Normalize y values to fit the screen
        y_min, y_max = np.min(y_values), np.max(y_values)
        y_range = y_max - y_min if y_max != y_min else 1
        y_normalized = ((y_values - y_min) / y_range) * (screen.height - 1)

        # Draw graph on screen
        for i in range(len(x_values)):
            y_pos = int(screen.height - 1 - y_normalized[i])
            screen.print_at("●", i, y_pos, colour=2)

        screen.refresh()
        screen.get_key()  # Wait for any key press
    except Exception as e:
        console.print(f"[bold red]Error in the graph: {e}[/]")

# Setup command-line arguments
parser = argparse.ArgumentParser(description="cli calculator with graphing support")
parser.add_argument('-e', '--equation', type=str, required=True, help="Usage: clic -e 'equation'")
parser.add_argument('-g', '--graph', action='store_true', help="Generate a graph for the equation (use 'x' as the variable)")

# Parse arguments
args = parser.parse_args()

if args.graph:
    console.print("[bold cyan]Generating ASCII graph...[/]")
    Screen.wrapper(draw_graph, arguments=[args.equation])
else:
    calc(args.equation)
