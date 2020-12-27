import os
import requests
from pathlib import Path

from PIL import ImageDraw, Image


class ImageRenderer:
    def __init__(self, renderer, filename):
        self.renderer = renderer
        self.filename = filename
        self._x = 0
        self._y = 0
        self._width = None
        self._height = None
        self.center_vertical = None
        self.center_horizontal = None

    def x(self, x):
        self._x = x
        return self

    def y(self, y):
        self._y = y
        return self

    def center_vertically(self, offset=0):
        self.center_vertical = offset
        return self

    def center_horizontally(self, offset=0):
        self.center_horizontal = offset
        return self

    def height(self, h):
        self._height = h
        return self

    def width(self, w):
        self._width = w
        return self

    def end(self):
        img = Image.open(self.filename)
        if self._width is not None and self._height is not None:
            img.thumbnail((self._width, self._height), Image.ANTIALIAS)

        img_pos = (self._x, self._y)
        if self.center_vertical is not None:
            img_pos = (img_pos[0], ((self.renderer.img.height - img.height) // 2) + self.center_vertical)
        if self.center_horizontal is not None:
            img_pos = (((self.renderer.img.width - img.width) // 2) + self.center_horizontal, img_pos[1])

        self.renderer.img.paste(img, img_pos)
        return self.renderer
