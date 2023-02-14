"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
``[options.entry_points]`` section in ``setup.cfg``::

    console_scripts =
         fibonacci = json_one_line.skeleton:run

Then run ``pip install .`` (or ``pip install -e .`` for editable mode)
which will install the command ``fibonacci`` inside your current environment.

Besides console scripts, the header (i.e. until ``_logger``...) of this file can
also be used as template for Python modules.

Note:
    This file can be renamed depending on your needs or safely removed if not needed.

References:
    - https://setuptools.pypa.io/en/latest/userguide/entry_point.html
    - https://pip.pypa.io/en/stable/reference/pip_install
"""
from typing import Dict
import argparse
import logging
import sys
import json

from os import PathLike
from json_one_line import __version__

__author__ = "jonnyyu"
__copyright__ = "jonnyyu"
__license__ = "MIT"

_logger = logging.getLogger(__name__)

try:
    import fsspec
    _open = fsspec.open
except:
    _open = open

# ---- Python API ----
# The functions defined in this section can be imported by users in their
# Python scripts/interactive interpreter, e.g. via
# `from json_one_line.skeleton import fib`,
# when using this Python module as a library.


def json_load(json_file: PathLike, *args, **kwargs) -> Dict:
    '''load json file from path'''
    with _open(json_file, 'r', encoding='utf-8') as fi:
        return json.load(fi, *args, **kwargs)

def json_save(obj: Dict, json_file: PathLike, *args, **kwargs) -> None:
    '''save object to json'''
    with _open(json_file, 'w', encoding='utf-8') as fo:
        json.dump(obj, fo, *args, **kwargs)
