# -*- coding: utf-8 -*-

import pathlib

from setuptools import setup, find_packages


setup(
    name="vtf2img",
    version="0.1.0",
    author="Julien Chaumont",
    author_email="vtf2img@julienc.io",
    description="A library to convert Valve Texture Format (VTF) files into images",
    long_description=(pathlib.Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/julienc91/vtf2img/",
    packages=find_packages(),
    entry_points={"console_scripts": ["vtf2img = vtf2img.cli:main",],},
    install_requires=["Pillow"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
)
