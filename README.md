# Calculate PI

A python poetry project demo for calculating PI.

## Prerequisites

- Git
- Docker
- Python >= 3.11 (prefer using [asdf](https://asdf-vm.com/) or [pyenv](https://github.com/pyenv/pyenv) to system python)
- [Poetry](https://python-poetry.org/) (prefer [asdf-poetry](https://github.com/asdf-community/asdf-poetry) plugin or installing with [pipx](https://github.com/pypa/pipx))
  
  ```console
  > curl -sSL https://install.python-poetry.org | python3 -
  ```

- poetry-bumpversion plugin
  
  ```console
  > poetry self add poetry-bumpversion
  ```

## Installation

```console
> git clone git@github.com:eriksf/calculate-pi.git
> cd calculate-pi
> poetry install
```

## Usage

```console
> calculate-pi --help
Usage: calculate-pi [OPTIONS] NUMBER

  Calculate pi using a Monte Carlo estimation.

  NUMBER is the number of random points.

Options:
  --version                       Show the version and exit.
  --log-level [NOTSET|DEBUG|INFO|WARNING|ERROR|CRITICAL]
                                  Set the log level  [default: 20]
  --log-file PATH                 Set the log file
  --help                          Show this message and exit.
```

## Development

To update the version, use the `poetry version <major|minor|patch>` command (aided by the poetry-bumpversion plugin):

```console
> poetry version patch
Bumping version from 0.3.0 to 0.3.1
poetry_bumpversion: processed file calculate_pi/version.py
```

This will update the version in both the `pyproject.toml` and the `calculate_pi/version.py` files. If you want to test the version bump before updating files, you can use the `--dry-run` option:

```console
> poetry version patch --dry-run
Bumping version from 0.3.0 to 0.3.1
poetry_bumpversion: processed file calculate_pi/version.py
```

After updating the version and committing the changes back to the repo, you should `tag` the repo to match this version:

```console
> git tag -a 0.3.1 -m "Version 0.3.1"
> git push origin 0.3.1
```
