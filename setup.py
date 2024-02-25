from setuptools import setup, find_packages

with open('requirements.txt', encoding='utf-16le') as file:
    requirements = file.read().splitlines()

if requirements and requirements[0].startswith('\ufeff'):
    requirements[0] = requirements[0][1:]

setup(
    name='apollo_sdk',
    version='1.0',
    packages=find_packages(),
    install_requires=requirements
)
