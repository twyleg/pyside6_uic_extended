# Copyright (C) 2023 twyleg
import os
from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="pyside6_uic_extended",
    version=read('VERSION.txt'),
    author="Torsten Wylegala",
    author_email="mail@twyleg.de",
    description=("Extended functionality for pyside6-uic"),
    license="GPL 3.0",
    keywords="pyside6 uic",
    url="https://github.com/twyleg/pyside6-uic-extended",
    packages=find_packages(),
    include_package_data=True,
    long_description=read('README.md'),
    install_requires=[
        'PySide6'
    ],
    entry_points={
        'console_scripts': [
            'pyside6-uic-extended = pyside6_uic_extended.uic:start',
        ]
    }
)