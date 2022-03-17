import typer

from .network.cli import app as network_app
from .pypi.cli import app as pypi_app


__version__ = "0.1.0"


app = typer.Typer(help="Awesome PyPICamp CLI manager.")
app.add_typer(network_app, name="network")
app.add_typer(pypi_app, name="pypi")

@app.command()
def info():
    """
        Prints information about the current PyPICamp installation.
    """
    typer.echo("pypicamp is a simple command line tool for managing your pip packages.")


@app.command()
def version():
    """
        Prints the current version of PyPICamp CLI.
    """
    typer.echo(f"pypicamp v{__version__}")
