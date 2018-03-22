#!/usr/bin/env python3
# coding: utf-8

from setuptools import find_packages
from setuptools import setup


setup(
    name='parsing',
    version='0.1.0',
    description='A dependency parser for natural language implemented in Python.',
    url='https://github.com/mitsuse/parsing-python',
    author='Tomoya Kose',
    author_email='tomoya@mitsuse.jp',
    install_requires=[
        'typing-extensions>=3.6.2<=4.0.0',
    ],
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords=[
        'natural language',
        'dependency parser',
    ],
    packages=find_packages(
        exclude=[
        ]
    ),
    entry_points={
        'console_scripts': [
        ],
    },
)
