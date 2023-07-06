#!/usr/bin/env python3
import click
from random import random as r
from math import pow as p
from sys import argv

VERSION = '0.1.0'


@click.command()
@click.version_option(VERSION)
@click.argument('number', type=click.INT, required=True)
def main(number):
    """Calculate pi using Monte Carlo estimation.

    NUMBER is the number of random points.
    """
    attempts = number
    inside = 0
    tries = 0

    # Try the specified number of random points
    while (tries < attempts):
        tries += 1
        if (p(r(),2) + p(r(),2) < 1):
            inside += 1

    # Compute and print a final ratio
    print( f'Final pi estimate from {attempts} attempts = {4*(inside/tries)}' )

if __name__ == '__main__':
    main()
