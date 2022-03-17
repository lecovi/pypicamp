from dotenv import load_dotenv
import typer

from pypicamp.network.core import (
    check_internet_connection,
    network_status,
    get_network_interfaces,
    chek_internet_connection_speed,
    send_connection_status_email,
)

app = typer.Typer(help="Awesome PyPICamp Network CLI manager.")

@app.command()
def ifaces():
    """
        Prints information about the current network interfaces.
    """
    ifaces = get_network_interfaces()
    typer.echo(f"Network interfaces: {ifaces}")


@app.command()
def status():
    """
        Checks the network status.
    """
    network = network_status()
    #FIXME: beautify
    typer.echo(f"Network status: {network}")


@app.command()
def internet_speed():
    """
        Checks the internet connection speed.
    """
    if check_internet_connection():
        typer.echo(f"Checking Internet connection speed...")
        results = chek_internet_connection_speed()
        #FIXME: beautify
        typer.echo(f"Internet connection speed: {results}")
    else:
        typer.echo(f"The computer is not connected to the internet.")


def test():
    load_dotenv()

    get_network_interfaces()

    network = network_status()

    if check_internet_connection():
        results = chek_internet_connection_speed()
        
        connection_status ={
            "network": network,
            "results": results,
        }
        send_connection_status_email(connection_status=connection_status)