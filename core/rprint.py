from rich import print as rprint

def error(date, body):
    rprint("[[bold green]" + date + "[/bold green]] [bold red]FuYao[/bold red] [[bold red]error[/bold red]] > [bold yellow]" + body + "[/bold yellow]")

def success(date, body):
    rprint("[[bold green]" + date + "[/bold green]] [bold red]FuYao[/bold red] [[bold green]success[/bold green]] > " + body)

def info(date, body):
    rprint("[[bold green]" + date + "[/bold green]] [bold red]FuYao[/bold red] [[bold blue]info[/bold blue]] > " + body)