# pylint: disable=no-value-for-parameter

from importlib import import_module
from pathlib import Path

import click


@click.command()
@click.argument('config_file',
                type=click.Path(exists=True, dir_okay=False, readable=True),
                default='./src/config/color.py')
def run(config_file):
    config_file = Path(config_file)
    config_file = (config_file.parent / config_file.stem).as_posix().replace('/', '.')
    a = import_module(config_file)
    config = a.Config()
    config.run()


if __name__ == '__main__':
    run()
