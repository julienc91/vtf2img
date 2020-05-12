# -*- coding: utf-8 -*-

from .rgba8888 import RGBA8888


class BGRA8888(RGBA8888):
    id = 12

    @staticmethod
    def _sort_pixel_rgba(pixel):
        return [pixel[2], pixel[1], pixel[0], pixel[3]]
