import typer
from . import (
    get_top_pypi_packages_downloads_json,
    create_top_pypi_packages_downloads_list,
    write_top_pypi_packages_downloads_file,
)
from pypicamp.contants import (
    TOP_PYPI_PACKAGES_DOWNLOADS_FILE_PATH,
    TOP_PYPI_PACKAGES_DOWNLOADS_URL,
)


app = typer.Typer(help="Awesome PyPICamp PyPI CLI manager.")


@app.command()
def mirror():
    """
        Prints the command to update bandersnatch mirror with PyPICamp.
    """
    message_start = "Make sure you are running containers with: "
    compose_up = typer.style("docker compose up -d", fg=typer.colors.BLUE)
    message = message_start + compose_up
    typer.echo(message)

    typer.echo("\nThen run:\n")
    typer.secho("\n\tdocker compose exec bandersnatch bandersnatch mirror\n\n",
        fg=typer.colors.BRIGHT_WHITE, bold=True)

@app.command()
def write_packages_file(
    url: str = typer.Option(
        TOP_PYPI_PACKAGES_DOWNLOADS_URL, 
        help="The URL to get the top PyPI packages downloads."
    ),
    file_path: str = typer.Option(
        TOP_PYPI_PACKAGES_DOWNLOADS_FILE_PATH, 
        help="Path to the file to write the packages list."
    ),
    max_items: int = typer.Option(
        5000,
        help="Maximum number of items to write to the file."
    ),
):
    """
        Writes the top PyPI packages downloads list to a file.
    """
    packages_json = get_top_pypi_packages_downloads_json(url=url)
    packages_list = create_top_pypi_packages_downloads_list(
        packages_json=packages_json, max_items=max_items)
    write_top_pypi_packages_downloads_file(
        packages_list=packages_list, file_path=file_path)