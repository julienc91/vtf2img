# -*- coding: utf-8 -*-

from typing import List

from PIL import Image

from ..buffer import Buffer
from ..header import Header

registry = {}


class AbstractFormat:

    # Enum value from https://github.com/ValveSoftware/source-sdk-2013/blob/master/sp/src/public/bitmap/imageformat.h
    id = -1
    has_alpha = False

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if registry.get(cls.id, cls) is not cls:
            raise RuntimeError(f"Invalid configuration, multiple parser for format {cls.id}")
        registry[cls.id] = cls

    @property
    def image_size(self) -> int:
        raise NotImplementedError

    def __init__(self, header: Header, buffer: Buffer):
        self.header = header
        self.buffer = buffer

    def read(self) -> Image:
        position = (self.buffer.getbuffer().nbytes) - self.image_size
        self.buffer.seek(position)
        rgba_pixels = self._convert_to_rgba()
        rgba_pixels = bytes(rgba_pixels)
        return Image.frombytes("RGBA", (self.header.width, self.header.height), rgba_pixels)

    def _convert_to_rgba(self) -> List[int]:
        raise NotImplementedError
