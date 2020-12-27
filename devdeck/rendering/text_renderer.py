import os

from PIL import ImageFont, ImageDraw


class TextRenderer:
    def __init__(self, renderer, text):
        self.renderer = renderer
        self.text = text
        self.font_filename = os.path.join(os.path.dirname(__file__), "../../assets", 'Roboto-Regular.ttf')
        self._font_size = 120
        self.fill = 'white'
        self.center_vertical = None
        self.center_horizontal = None
        self.align = 'left'
        self._x = 0
        self._y = 0

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

    def font_size(self, size):
        self._font_size = size
        return self

    def color(self, color):
        self.fill = color
        return self

    def text_align(self, align):
        self.align = align
        return self

    def end(self):
        font = ImageFont.truetype(self.font_filename, self._font_size)

        draw = ImageDraw.Draw(self.renderer.img)
        label_w, label_h = draw.textsize('%s' % self.text, font=font)

        # Positioning
        label_pos = (self._x, self._y)
        if self.center_vertical is not None:
            label_pos = (label_pos[0], ((self.renderer.img.height - label_h) // 2) + self.center_vertical)
        if self.center_horizontal is not None:
            label_pos = (((self.renderer.img.width - label_w) // 2) + self.center_horizontal, label_pos[1])

        draw.text(label_pos, text=self.text, font=font, fill=self.fill, align=self.align)

        return self.renderer
