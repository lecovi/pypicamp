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
