# -*- coding: utf-8 -*-

import itertools
import math

from .abstract_format import AbstractFormat


class DXT1(AbstractFormat):
    id = 13
    has_alpha = True

    # adapted from the C program vtf2png by Harry Jeffery
    # https://github.com/eXeC64/vtf2png

    @property
    def image_size(self):
        return math.ceil(self.header.width / 4) * math.ceil(self.header.height / 4) * 8

    @staticmethod
    def rgb565_to_rgb888(pixel):
        r = (pixel >> 11) & 31
        r = (r << 3) | (r >> 2)

        g = (pixel >> 5) & 63
        g = (g << 2) | (g >> 4)

        b = (pixel >> 0) & 31
        b = (b << 3) | (b >> 2)
        return r, g, b

    def decode_dxt_colors(self, x, y, c0, c1, ci, decoded):
        r = [0, 0, 0, 0]
        g = [0, 0, 0, 0]
        b = [0, 0, 0, 0]

        r[0], g[0], b[0] = self.rgb565_to_rgb888(c0)
        r[1], g[1], b[1] = self.rgb565_to_rgb888(c1)

        r[2] = (4 * r[0] + 2 * r[1] + 3) // 6
        g[2] = (4 * g[0] + 2 * g[1] + 3) // 6
        b[2] = (4 * b[0] + 2 * b[1] + 3) // 6

        r[3] = (2 * r[0] + 4 * r[1] + 3) // 6
        g[3] = (2 * g[0] + 4 * g[1] + 3) // 6
        b[3] = (2 * b[0] + 4 * b[1] + 3) // 6

        for y0 in range(4):
            for x0 in range(4):
                decoded[y + y0][4 * x + 4 * x0 + 0] = r[ci & 3]
                decoded[y + y0][4 * x + 4 * x0 + 1] = g[ci & 3]
                decoded[y + y0][4 * x + 4 * x0 + 2] = b[ci & 3]
                ci >>= 2
        return decoded

    def _convert_to_rgba(self):
        decoded = [[0xFF] * 4 * self.header.width for _ in range(self.header.height)]
        for y in range(0, self.header.height, 4):
            for x in range(0, self.header.width, 4):
                c0 = self.buffer.read_uint8()
                c0 |= self.buffer.read_uint8() << 8
                c1 = self.buffer.read_uint8()
                c1 |= self.buffer.read_uint8() << 8
                ci = 0
                for i in range(0, 25, 8):
                    ci |= self.buffer.read_uint8() << i

                self.decode_dxt_colors(x, y, c0, c1, ci, decoded)

                for y0 in range(4):
                    for x0 in range(4):
                        decoded[y + y0][4 * x + 4 * x0 + 3] = 0xFF

        return list(itertools.chain(*decoded))
