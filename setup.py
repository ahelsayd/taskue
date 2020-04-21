#!/usr/bin/env python3
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="taskue",
    version="1.0",
    author="Ahmed El-Sayed",
    author_email="ahmed.m.elsayed93@gmail.com",
    description="Multi stages task queue",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ahelsayd/taskue",
    install_requires=[],
    packages=find_packages(),
    entry_points={"console_scripts": ["taskue=taskue.cli:cli"]},
)
