# -*- coding: utf-8 -*-

import glob
import importlib
import logging
from os.path import basename, dirname, join
from typing import Type

from .abstract_format import AbstractFormat, registry


def load_available_formats():
    modules = glob.glob(join(dirname(__file__), "*.py"))

    for module in modules:
        if module.endswith(("__init__.py", "abstract_format.py")):
            continue

        importlib.import_module("." + basename(module)[:-3], "vtf2img.image_formats")

    logging.debug(f"Loaded {len(registry)} image format(s)")


def get_parser(image_format: int) -> Type[AbstractFormat]:
    for image_format_id, parser in registry.items():
        if image_format == image_format_id:
            return parser

    raise TypeError(f"Unknown image format {image_format}")


if not registry:
    load_available_formats()


__all__ = ["AbstractFormat", "get_parser"]
