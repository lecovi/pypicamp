import requests


def get_top_pypi_packages_downloads_json(url):
    """ Gets the top 5000 PyPI packages downloads for the past 30 days. """
    response = requests.get(url)
    return response.json()


def create_top_pypi_packages_downloads_list(packages_json, max_items=5000):
    """ 
        Creates a list with the top PyPI packages downloads name for the past 30 days 
        from the JSON response. 
    """

    if max_items > 5000:
        raise ValueError("The max_items parameter must be less than 5000.")

    return [package["project"] for package in packages_json["rows"][:max_items]]


def write_top_pypi_packages_downloads_file(packages_list, file_path):
    """ Writes the top PyPI packages downloads list to a file. """

    with open(file_path, "w") as f:
        packages = "\n".join(packages_list)
        f.writelines(packages)