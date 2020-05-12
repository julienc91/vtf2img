# -*- coding: utf-8 -*-

import struct
from io import BytesIO


class Buffer(BytesIO):

    """
    A buffer-like object with shortcut methods to read C objects
    """

    def __read(self, size: int, unpack=None):
        res = self.read(size)
        if unpack:
            res = struct.unpack(unpack, res)[0]
        return res

    def read_char(self, size=1) -> bytes:
        """
        Read `size` char(s) from the buffer and move the cursor
        :param size: the number of char(s) to read
        :return: a bytes instance
        """
        return self.__read(size)

    def read_uint8(self) -> int:
        """
        Read an unsigned int8 from the buffer and move the cursor
        :return: a positive integer
        """
        return self.__read(1, "<B")

    def read_uint32(self) -> int:
        """
        Read an unsigned int32 from the buffer and move the cursor
        :return: a positive integer
        """
        return self.__read(4, "<I")

    def read_ushort(self) -> int:
        """
        Read an unsigned short from the buffer and move the cursor
        :return: a positive integer
        """
        return self.__read(2, "<H")

    def read_float(self) -> float:
        """
        Read a float from the buffer and move the cursor
        :return: a float number
        """
        return self.__read(4, "<f")

    def skip(self, size: int) -> None:
        """
        Skip the next `size` bytes by moving the cursor
        :param size: number of bytes to skip
        """
        self.__read(size)
