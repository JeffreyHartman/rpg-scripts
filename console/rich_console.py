import os
import shutil
from .io_handler import IOHandler
from rich.console import Console as Console
from rich.console import Group
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout
from rich.text import Text
from rich import box
from rich.align import Align
from rich.prompt import Prompt
from rich.padding import Padding
from typing import List, Dict, Any


class RichConsoleImpl(IOHandler):
    """Implements a console using the Rich library.

    Args:
        Console (_type_): _description_
    """
    def __init__(self):
        self.console = Console()
        self.clear_screen()
        self.width = min(80, shutil.get_terminal_size().columns)

    def clear_screen(self):
        self.console.clear()
        # call os clear command because the rich one above doesn't seem to work on windows
        os.system('cls' if os.name == 'nt' else 'clear') 

    def display_frame(self, content: Any, title: str):
        self.clear_screen()

        # Header panel
        header_panel = Panel(
            Align.center(title, vertical="middle"),
            style="bold magenta",
            padding=(1, 2),
            width=self.width,
            box=box.DOUBLE,
        )

        # Content panel
        content_panel = Panel(
            content if isinstance(content, (Table, Panel)) else Group(*content),
            width=self.width,
            box=box.ROUNDED,
        )

        # Combine and print
        self.console.print(header_panel)
        self.console.print(content_panel)

    def display_menu(self, options: Dict[str, str], title: str = None):
        table = Table(box=box.SIMPLE_HEAVY)
        table.add_column("Choice", style="bold cyan", justify="center")
        table.add_column("Description", style="bold")

        for key, desc in options.items():
            table.add_row(key, desc)

        if title:
            table.title = title

        return table
    
    def display_result(self, result: str):
        if isinstance(result, dict):
            # Display each key-value pair in its own panel
            panels = []
            for key, value in result.items():
                panels.append(
                    Panel(
                        Text(str(value), justify="left"),
                        title=key,
                        title_align="left",
                        border_style="green",
                        width=self.width - 4,
                        box=box.ROUNDED
                    )
                )
            content = Align.center(Group(*panels))
        else:
            # display result in a panel
            content = Panel(
                Text(str(result), justify="left"),
                border_style="green",
                width=self.width - 4,
                box=box.ROUNDED
            )

        self.console.print(content)
        self.console.input("\nPress Enter to continue...")

    def display_input_prompt(self, promt: str) -> str:
        return self.console.input(promt)
    
    def display_error(self, message: str):
        self.console.print(f"[bold red]{message}[/bold red]")

    def display_message(self, message: str):
        self.console.print(message)