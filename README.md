# PyPICamp

PyPI Cache helper for Python Argentina's PyCamp

## Abstract

This is a simple script that helps you to cache your packages on PyPI.

1. It will check if your computer has internet connection.
2. It will send you an email with the connection status.
3. It will update your PyPI cache.

# Installation

Install all dependencies with:

```bash
poetry install
```

## Configuration

1. Copy the `env.dist` to `.env`
2. Change environment variables according to your configuration.

# Usage

```bash
poetry run python -m pypicamp
```

# PyPI Mirror & Cache

This section contains the information about the PyPI mirror and the cache.
We are using [bandersnatch](https://bandersnatch.readthedocs.io/en/latest/index.html)
and [devpi]().

`bandersnatch` help us to get a mirror of the PyPI packages. We can use a list of the
top downloaded packages into the configuration file. You can check the list on 
[PyPI Stats](https://pypistats.org/top) or in [Top PyPI Packages](https://hugovk.github.io/top-pypi-packages/).
Check out https://pypi.org/stats/ for more information about the PyPI statistics and the
size of the projects.

`devpi` will help us to cache the packages that we need to download and they aren't in
`bandersnatch`.

## Prerequisites

Build your images:

```bash
docker compose build
```

## Clients configuration

### pip

Config your `pip` editing your `$HOME/.pip/pip.conf`. Create file if doesn't exists.

```
[global]
index-url=http://SERVER_IP_ADDRESS:3141/root/pypi/+simple/
timeout=300
[install]
trusted-host=SERVER_IP_ADDRESS
```

### docker

Config your `docker` editing your `/etc/docker/daemon.conf`. Create file if doesn't exists.


```json
{
  "registry-mirrors": [
    "http://192.168.242:5000"
  ]
}
```

Restart your `docker` daemon (something like: `sudo systemctl restart docker`).

## Usage

Run your containers with:

```bash
docker compose up
```

Download top packages from PyPI using `pypicamp`:

```bash
poetry run python pypicamp pypi write-package-file --max-items N
```

This will write a `top-pypi-packages.txt` file with the top N packages. 
You should copy the content of this file to your clipboard and paste it on the 
`[allowlist]` section of the `bandersnatch/bandersnatch.conf` file.

Then, update `bandersnatch` mirror with:

```bash
docker compose exec bandersnatch bandersnatch mirror
```

## Bandersnatch and Devpi

- `bandersnatch` will be available at your server IP address on port 8080.
- `devpi` will be available at your server IP address on port 3141.
