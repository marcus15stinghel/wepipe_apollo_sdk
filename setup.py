from os import path
from typing import List
from setuptools import setup, find_packages


def get_requirements(requirements_file_path: str) -> List[str]:
    with open(requirements_file_path, 'r', encoding='utf-8-sig') as requirements_file:
        return [req.strip() for req in requirements_file.readlines()]


name = "wepipe_apollo_sdk"
version = '1.0.0'
all_requirements = get_requirements(requirements_file_path="requirements.txt")
here = path.abspath(path.dirname(__file__))
source = "src"
packages = find_packages(where=path.join(here, source))

setup(name=name, version=version, install_requires=all_requirements, packages=packages)
