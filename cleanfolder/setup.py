from setuptools import setup, find_namespace_packages
import sys

setup(
    name='cleanfolder',
    version='1.0.0',
    description='Sort files',
    url='https://github.com/Andrij-Latkiv/DZ-6/blob/main/sort_4.py',
    author='Andrij Latkivkiy',
    author_email='latkivskijandrij@gmail.com',
    license='Apache License 2.0',
    packages=find_namespace_packages(),
    install_requires=['markdown'],
    entry_points={'console_scripts': ['clean-folder = cleanfolder.clean:clean']}
)

