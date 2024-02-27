from setuptools import setup

with open('requirements.txt', encoding='utf-16le') as file:
    requirements = file.read().splitlines()

if requirements and requirements[0].startswith('\ufeff'):
    requirements[0] = requirements[0][1:]

setup(
    name='wepipe_apollo_sdk',
    version='1.0',
    author='Marcus Stinghel',
    author_email='caio@pythonando.com.br',
    description='Python SDK for Apollo',
    packages=['src'],
    package_dir={"": "src"},
    install_requires=requirements
)
