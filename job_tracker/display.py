

from rich.console import Console
console = Console()
from rich.table import Table

def display_applications(applications):
    table = Table()
    table.add_column("Role")
    table.add_column("Company")
    table.add_column("Application Date")
    table.add_column("Status")
    table.add_column("Notes")

    for application in applications:
        table.add_row(application[1], application[2], application[3] or "-", application[4], application[5] or "N/A")

    console.print("Job Tracker", style="blue")
    console.print(table)