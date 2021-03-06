#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The setup script."""

from setuptools import setup, find_packages

requirements = ["requests", "pandas", "openpyxl", "tablib"]

setup(
    name="kolada",
    version="0.4.1",
    description="A simple wrapper around the Kolada api",
    long_description="",
    author="Henric Sundberg",
    author_email="henric.sundberg@gmail.com",
    url="https://github.com/htp84/kolada",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords="kolada",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
