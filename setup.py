from codecs import open
from os import path
from typing import List, Dict

from setuptools import setup, find_packages

from src.wepipe_apollo_sdk.__version__ import __version__

PACKAGE = "wepipe_apollo_sdk"
NAME = "wepipe_apollo_sdk"
SOURCE = "src"
REQUIREMENTS_FILE = "requirements.txt"

here = path.abspath(path.dirname(__file__))


def get_requirements(requirements_file_path: str) -> List[str]:
    """
    Obtém todas as dependências listadas em um arquivo de dependências.

    :param requirements_file_path: caminho para o arquivo de dependências.
    :return: lista de strings contendo as dependências.
    """
    with open(requirements_file_path) as requirements_file:
        return [req.strip() for req in requirements_file.readlines()]


all_requirements = get_requirements(requirements_file_path=REQUIREMENTS_FILE)

setup(
    name=NAME,
    version=__version__,
    install_requires=all_requirements,
    package_dir={PACKAGE: path.join(SOURCE, PACKAGE)},
    packages=find_packages(where=path.join(here, SOURCE))
)
