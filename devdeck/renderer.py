import os

from PIL import Image, ImageFont, ImageDraw


class RendererManager:
    def __init__(self, key_no, deck_context):
        self.key_no = key_no
        self.deck_context = deck_context
        self.renderer = Renderer()

    def __enter__(self):
        return self.renderer

    def __exit__(self, type, value, traceback):
        image = self.renderer.render()
        self.deck_context.set_key_image_native(self.key_no, image)


class Renderer:
    def __init__(self):
        self.image = Image.new("RGB", (512, 512))

    def background_color(self, color):
        draw = ImageDraw.Draw(self.image)
        draw.rectangle((0, 0, self.image.width, self.image.height), fill=color)

    def badge_count(self, count):
        return BadgeCountRenderer(self, count)

    def text(self, text):
        return TextRenderer(self, text)

    def render(self):
        return self.image


class BadgeCountRenderer:
    def __init__(self, renderer, count):
        self.renderer = renderer
        self.text = str(count)
        self.font_filename = os.path.join(os.path.dirname(__file__), "../assets", 'Roboto-Regular.ttf')
        self._font_size = 100
        self.fill = 'white'
        self.circle_size = 192
        self.corner_offset = 30

    def font_size(self, size):
        self._font_size = size
        return self

    def end(self):
        font = ImageFont.truetype(self.font_filename, self._font_size)

        draw = ImageDraw.Draw(self.renderer.image)
        label_w, label_h = draw.textsize('%s' % self.text, font=font)

        # Circle

        draw.ellipse((self.renderer.image.width - self.circle_size - self.corner_offset,
                      self.renderer.image.height - self.circle_size - self.corner_offset,
                      self.renderer.image.width - self.corner_offset,
                      self.renderer.image.height - self.corner_offset), fill='red')

        # Label
        label_pos = (self.renderer.image.width - (self.circle_size / 2) - self.corner_offset - (label_w / 2),
                     self.renderer.image.height - (self.circle_size / 2) - self.corner_offset - (label_h / 2))
        draw.text(label_pos, text=self.text, font=font, fill=self.fill, stroke_width=2)

        return self.renderer


class TextRenderer:
    def __init__(self, renderer, text):
        self.renderer = renderer
        self.text = text
        self.font_filename = os.path.join(os.path.dirname(__file__), "../assets", 'Roboto-Regular.ttf')
        self._font_size = 120
        self.fill = 'white'
        self.center_vertical = None
        self.center_horizontal = None
        self._x = 0
        self._y = 0

    def x(self, x):
        self._x = x

    def x(self, y):
        self._y = y


    def center_vertically(self, offset=0):
        self.center_vertical = offset
        return self

    def center_horizontally(self, offset=0):
        self.center_horizontal = offset
        return self

    def font_size(self, size):
        self._font_size = size
        return self

    def end(self):
        font = ImageFont.truetype(self.font_filename, self._font_size)

        draw = ImageDraw.Draw(self.renderer.image)
        label_w, label_h = draw.textsize('%s' % self.text, font=font)

        # Positioning
        label_pos = (self._x, self._y)
        if self.center_vertical:
            label_pos = (label_pos[0], ((self.renderer.image.height - label_h) // 2) + self.center_vertical)
        if self.center_horizontal:
            label_pos = (((self.renderer.image.width - label_w) // 2) + self.center_horizontal, label_pos[1])

        draw.text(label_pos, text=self.text, font=font, fill=self.fill)

        return self.renderer
