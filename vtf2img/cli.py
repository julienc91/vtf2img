# -*- coding: utf-8 -*-

import argparse

from vtf2img.parser import Parser


def main():
    parser = argparse.ArgumentParser(prog="vtf2img", description="Convert a VTF file into an image")
    parser.add_argument("input_path", help="path to the VTF file to convert")
    parser.add_argument("output_path", help="path to the resulting image")

    args = parser.parse_args()

    parser = Parser(args.input_path)
    image = parser.get_image()
    image.save(args.output_path)


if __name__ == "__main__":
    main()
