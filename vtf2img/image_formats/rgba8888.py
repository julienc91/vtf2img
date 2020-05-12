# -*- coding: utf-8 -*-

from .abstract_format import AbstractFormat


class RGBA8888(AbstractFormat):
    id = 0
    has_alpha = True

    @property
    def _pixel_size(self):
        return 4 if self.has_alpha else 3

    @property
    def image_size(self):
        return self.header.width * self.header.height * self._pixel_size

    @staticmethod
    def _sort_pixel_rgba(pixel):
        return pixel

    def _convert_to_rgba(self):
        decoded = []
        for y in range(self.header.height):
            for x in range(self.header.width):
                pixel = [self.buffer.read_uint8() for _ in range(self._pixel_size)]
                pixel = self._sort_pixel_rgba(pixel)
                if not self.has_alpha:
                    pixel.append(0xFF)
                decoded.extend(pixel)
        return decoded
