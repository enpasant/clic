#!/usr/bin/env python3

import argparse
from rich.console import Console

# Initialize Rich Console
console = Console()

console.print("[bold cyan]clic - v1.22[/]")
def calc(equation):
    try:
        # Evaluate the equation passed as a string
        result = eval(equation)
        console.print(f"[bold green]Result: {result}[/]")
    except Exception as e:
        console.print(f"[bold red]Error in the equation: {e}[/]")

# Setup command line arguments
parser = argparse.ArgumentParser(description="cli calculator")
parser.add_argument('-e', '--equation', type=str, required=True, help="Usage: clic -e 'equation' ")

# Parse arguments
args = parser.parse_args()

# Call the calc function with the equation
calc(args.equation)
