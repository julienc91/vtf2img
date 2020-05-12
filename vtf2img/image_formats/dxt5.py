# -*- coding: utf-8 -*-

import itertools
import math

from .dxt1 import DXT1


class DXT5(DXT1):
    id = 15
    has_alpha = True

    # adapted from the C program vtf2png by Harry Jeffery
    # https://github.com/eXeC64/vtf2png

    @property
    def image_size(self):
        return math.ceil(self.header.width / 4) * math.ceil(self.header.height / 4) * 16

    def _convert_to_rgba(self):
        decoded = [[0xFF] * 4 * self.header.width for _ in range(self.header.height)]
        for y in range(0, self.header.height, 4):
            for x in range(0, self.header.width, 4):
                alpha = [0x00] * 8
                alpha[0] = self.buffer.read_uint8()
                alpha[1] = self.buffer.read_uint8()

                if alpha[0] > alpha[1]:
                    for i in range(6):
                        alpha[2 + i] = (((6 - i) * alpha[0]) + ((1 + i) * alpha[1])) // 7
                else:
                    for i in range(4):
                        alpha[2 + i] = (((4 - i) * alpha[0]) + ((1 + i) * alpha[1])) // 5
                    alpha[6] = 0x00
                    alpha[7] = 0xFF

                ai = 0
                for i in range(0, 41, 8):
                    ai |= self.buffer.read_uint8() << i

                for y0 in range(4):
                    for x0 in range(4):
                        decoded[y + y0][4 * x + 4 * x0 + 3] = alpha[ai & 7]
                        ai >>= 3

                c0 = self.buffer.read_uint8()
                c0 |= self.buffer.read_uint8() << 8
                c1 = self.buffer.read_uint8()
                c1 |= self.buffer.read_uint8() << 8
                ci = 0
                for i in range(0, 25, 8):
                    ci |= self.buffer.read_uint8() << i

                self.decode_dxt_colors(x, y, c0, c1, ci, decoded)

        return list(itertools.chain(*decoded))
