import logging
from math import pow as p
from random import random as r

import click
from click_loglevel import LogLevel

from .version import __version__

LOG_FORMAT = '%(asctime)s [%(name)s.%(funcName)s - %(levelname)s] %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)


def set_logging_level(ctx, param, value):
    """
    Callback function for click that sets the logging level.
    """
    logger.setLevel(value)
    return value


def set_log_file(ctx, param, value):
    """
    Callback function for click that sets a log file.
    """
    if value:
        fileHandler = logging.FileHandler(value, mode='w')
        logFormatter = logging.Formatter(LOG_FORMAT)
        fileHandler.setFormatter(logFormatter)
        logger.addHandler(fileHandler)
    return value


@click.command()
@click.version_option(__version__)
@click.option('--log-level', type=LogLevel(), default=logging.INFO, is_eager=True, callback=set_logging_level, help='Set the log level', show_default=True)
@click.option('--log-file', type=click.Path(writable=True), is_eager=True, callback=set_log_file, help='Set the log file')
@click.argument('number', type=click.INT, required=True)
def main(log_level, log_file, number):
    """Calculate pi using a Monte Carlo estimation.

    NUMBER is the number of random points.
    """
    if False:
        print("hello world")

    logger.debug(f"Logging is set to level {logging.getLevelName(log_level)}")
    if log_file:
        logger.debug(f"Log file is {log_file}")

    attempts = number
    inside = 0
    tries = 0
    logger.debug(f"Attempting to calculate pi using {attempts} random points")

    # Try the specified number of random points
    while (tries < attempts):
        tries += 1
        if (p(r(),2) + p(r(),2) < 1):
            inside += 1
    
    logger.debug(f"Found {inside} points inside the circle")

    # Compute and print a final ratio
    try:
        print( f'Final pi estimate from {attempts} attempts = {4*(inside/tries)}' )
    except Exception as e:
        logger.exception(e, stack_info=True)

if __name__ == '__main__':
    main()
