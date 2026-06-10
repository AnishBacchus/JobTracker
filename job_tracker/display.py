

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


    status_colors = {
            "Applied" : "white",
            "Interviewing" : "yellow",
            "Rejected" : "red",
            "Offer" : "green"
        }
    
    for application in applications:
        
        status = application[4]
        color = status_colors.get(status, 'white')
        colored_status = f"[{color}]{status}[/{color}]"


        table.add_row(application[1], application[2], application[3] or "-", colored_status, application[5] or "N/A")

    console.print("")
    console.print("Welcome to your Job Tracker!", style="bold dark_slate_gray2")
    console.print("Here are all the jobs you applied for :")
    console.print(table)