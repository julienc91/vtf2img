# -*- coding: utf-8 -*-

from PIL import Image

from .buffer import Buffer
from .header import Header
from .image_formats import get_parser


class Parser:
    """
    Parse a VTF file to extract its header information and its hi-res image.

    Attributes:
        * header: a Header instance for the current VTF file
    """

    def __init__(self, path: str):
        """
        Create a new Parser instance for the given VTF file
        :param path: the path to the VTF file
        """
        self.path = path
        self._header = None

    @property
    def header(self):
        if not self._header:
            self._header = self._parse_header()
        return self._header

    def _get_buffer(self) -> Buffer:
        with open(self.path, "rb") as f:
            data = f.read()
        return Buffer(data)

    def _parse_header(self) -> Header:
        """
        Parse the VTF file's header
        :return: a Header instance
        """
        buffer = self._get_buffer()
        return Header(buffer)

    def get_image(self) -> Image:
        """
        Parse the hi-res image from the VTF file
        :return: a Pillow's Image instance
        """
        buffer = self._get_buffer()
        image_parser = get_parser(self.header.image_format)(self.header, buffer)
        return image_parser.read()
