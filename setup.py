#!/usr/bin/python2
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "labbook",
    version = "0.0.1",
    packages = find_packages(),
    entry_points={
        'console_scripts': [
            'lb = labbook.cli:main',
            ],
        }
    )
