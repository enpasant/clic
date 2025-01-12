#!/usr/bin/env python3

from rich.console import Console
import subprocess

# Initialize Rich Console
console = Console()

console.print("[bold cyan]clic - v0.01[/]")
console.print("[bold green]clic Started![/]")

def calc():
    while True:
        console.print("[yellow]Put a supported equation with 'clic', or see the guide typing 'help' below.[/]")
        console.print("[cyan]exit, help, clic: [/]", end="")
        chSt = input()

        if chSt == "help":
            console.print("[bold magenta]Guide is currently being worked on.[/]")
            console.print("[bold green] Guide is available at https://github.com/enpasant/clic/ . [/]")
        elif chSt == "exit":
            console.print("[bold red] Quitting... Farewell.  [/]")
            quit()

        elif chSt == "clic":
            console.print("[bold red]This is temporary.[/]")
            console.print("[bold blue]Type down your numbers to calculate.[/]")

            console.print("[green]How many entries?[/]")

            console.print("[cyan]Number of entries: [/]", end="")
            entries = int(input())

            ennum = []
            for i in range(entries):
                console.print(f"[yellow]Insert number {i + 1}: [/]", end="")
                numen = float(input())

                console.print("[yellow]Insert operation (+, -, *, /): [/]", end="")
                equen = input()

                ennum.append((numen, equen))

            result = ennum[0][0]
            for i in range(1, len(ennum)):
                if ennum[i - 1][1] == "+":
                    result += ennum[i][0]
                elif ennum[i - 1][1] == "-":
                    result -= ennum[i][0]
                elif ennum[i - 1][1] == "*":
                    result *= ennum[i][0]
                elif ennum[i - 1][1] == "/":
                    result /= ennum[i][0]

            console.print(f"[bold green]Result: {result}[/]")

# Start the calculator
calc()
