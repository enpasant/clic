#!/usr/bin/env python3

import argparse
from rich.console import Console
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
import asciichartpy

# Initialize Rich Console
console = Console()

console.print("[bold cyan]clic - v1.22[/]")

# Function to evaluate and print result
def calc(equation):
    try:
        # Support for symbolic math and variables
        symbols = sp.symbols('x y z')  # You can define any symbols like x, y, z
        parsed_expr = sp.sympify(equation)
        
        # If the equation has variables, solve them symbolically
        result = parsed_expr.simplify()
        console.print(f"[bold green]Result: {result}[/]")
        
    except Exception as e:
        console.print(f"[bold red]Error in the equation: {e}[/]")

# Function to plot an ASCII graph
def plot_graph(equation):
    try:
        x_vals = np.linspace(-10, 10, 1000)  # Generate x values
        y_vals = np.array([eval(equation.replace('x', str(x))) for x in x_vals])  # Evaluate equation

        # Create ASCII graph using asciichart
        graph = asciichartpy.plot(y_vals.tolist(), {'height': 10, 'min': -10, 'max': 10})
        console.print(f"[bold yellow]Graph (ASCII):\n{graph}[/]")

    except Exception as e:
        console.print(f"[bold red]Error plotting graph: {e}[/]")

# Setup command line arguments
parser = argparse.ArgumentParser(description="CLI calculator with advanced math and ASCII graphing")
parser.add_argument('-e', '--equation', type=str, required=True, help="Usage: clic -e 'equation'")
parser.add_argument('--plot', action='store_true', help="Plot the equation as an ASCII graph")

# Parse arguments
args = parser.parse_args()

# Call the calc function with the equation
calc(args.equation)

# If --plot is specified, plot the equation as an ASCII graph
if args.plot:
    plot_graph(args.equation)
