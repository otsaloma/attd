#!/usr/bin/env python3

from setuptools import setup

setup(
    name="attd",
    version="0.1.2",
    author="Osmo Salomaa",
    author_email="otsaloma@iki.fi",
    description="Dictionary with attribute access to keys",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/otsaloma/attd",
    license="MIT",
    py_modules=["attd"],
    python_requires=">=3.1.0",
)
