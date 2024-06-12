from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    page_description = f.read()

setup(
    name='text-progress-bar',
    version='0.0.1',
    description='A simple text progress bar for the command line',
    long_description=page_description,
    long_description_content_type='text/markdown',
    author='Felipe',
    url='https://github.com/linhares06/dio-desafio-projeto-criacao-pacotes',
    packages=find_packages(),
    python_requires='>=3.6',
)
