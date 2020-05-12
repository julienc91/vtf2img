# vtf2img

A Python library to convert [Valve Texture Format (VTF)](https://developer.valvesoftware.com/wiki/Valve_Texture_Format) files to images.


## Installation

### With pip

```
$ pip install vtf2img
```

### From source

```
$ git clone https://github.com/julienc91/vtf2img
$ cd vtf2img
$ python setup.py install
```


## QuickStart

### As a library

```python
from vtf2img import Parser


vtf_file = "materials/models/weapons/customization/paints/custom/workshop/ak47_asiimov.vtf"

parser = Parser(vtf_file)
header = parser.header

print(f"VTF version: {header.version}, Image size: {header.width}x{header.height}")
# VTF version: 7.5, Image size: 2048x2048

image = parser.get_image()

image.show()
image.save("ak47_asiimov.png")
```

The result of `get_image` is an instance of [Pillow's `Image` class](https://pillow.readthedocs.io/en/stable/reference/Image.html#the-image-class),
which allows [exporting](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save) in many different formats (PNG, JPG, BMP, ...).


### As a CLI command

If you installed the package as instructed in the previous section, a `vtf2img` command should
be available.

```
$ vtf2img dragon_awp.wtf awp_dragon_lore.png
```

Otherwise, you can execute the package's `__main__.py` file with:

```
$ python -m vtf2img dragon_awp.wtf awp_dragon_lore.png
```


## Limitations

* many image formats supported by the VTF format are not (yet?) supported by this program (see the section below)
* this program only considers the hi-res image contained in the VTF file
* all the flags that might have been set by the VTF's creator are purely ignored

## VTF compatibility

Works with VTF version 7.2+.

Compatibility of image formats:

| Format            | Supported |
|-------------------|:---------:|
| A8                | ✗         |
| ABGR8888          | ✓         |
| ARGB8888          | ✓         |
| BGR565            | ✗         |
| BGR888            | ✓         |
| BGR888_BLUESCREEN | ✗         |
| BGRA4444          | ✗         |
| BGRA5551          | ✗         |
| BGRA8888          | ✓         |
| BGRX5551          | ✗         |
| BGRX8888          | ✗         |
| DXT1              | ✓         |
| DXT1_ONEBITALPHA  | ✗         |
| DXT3              | ✗         |
| DXT5              | ✓         |
| I8                | ✗         |
| IA88              | ✗         |
| P8                | ✗         |
| RGB565            | ✗         |
| RGB888            | ✓         |
| RGB888_BLUESCREEN | ✗         |
| RGBA16161616      | ✗         |
| RGBA16161616F     | ✗         |
| RGBA8888          | ✓         |
| UV88              | ✗         |
| UVLX8888          | ✗         |
| UVWQ8888          | ✗         |

Most VTF Files are using either DXT1 or DXT5.

_Note:_ DXT1 and DXT5 decoding algorithms were adapted from [Harry Jeffery](https://github.com/eXeC64/)'s implementation
on [vtf2png](https://github.com/eXeC64/vtf2png).
