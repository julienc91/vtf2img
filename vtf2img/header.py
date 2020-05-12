# -*- coding: utf-8 -*-

from .buffer import Buffer


class Header:
    """
    A class to parse a VTF file's header data, according to Valve's specifications:
    https://developer.valvesoftware.com/wiki/Valve_Texture_Format#VTF_header

    Attributes:
        * width: the hi-res image width (integer)
        * height: the hi-res image height (integer)
        * image_format: an id refering to the image format used for the hi-res image (integer)
        * version: the VTF version (string)
    """

    def __init__(self, buffer: Buffer):
        signature = buffer.read_char(4)
        version_major = buffer.read_uint32()
        version_minor = buffer.read_uint32()

        buffer.skip(4)

        self.width = buffer.read_ushort()
        self.height = buffer.read_ushort()

        buffer.skip(4 + 2 + 2 + 4 + 4 * 3 + 4 + 4)

        self.image_format = buffer.read_uint32()

        if signature != b"VTF\0":
            raise TypeError("Invalid VTF file")

        if version_major != 7 or version_minor < 2:
            raise TypeError("Incompatible VTF version")

        self.version = f"{version_major}.{version_minor}"
