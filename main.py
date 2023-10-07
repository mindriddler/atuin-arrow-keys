from beaupy import select
from rich.console import Console

if __name__ == "__main__":
    console = Console()
    yes_or_no = ["No", "Yes"]
    console.print("Does up and down arrow keys work?", style="bold blue")
    selection = select(yes_or_no, cursor="> ", cursor_style="bold red")
    if selection == "Yes":
        console.print("Arrow keys work!", style="bold green")
    else:
        console.print("Arrow keys don't work!", style="bold red")
