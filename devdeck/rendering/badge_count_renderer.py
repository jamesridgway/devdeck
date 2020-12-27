import os

from PIL import ImageFont, ImageDraw


class BadgeCountRenderer:
    def __init__(self, renderer, count):
        self.renderer = renderer
        self.text = str(count)
        self.font_filename = os.path.join(os.path.dirname(__file__), "../../assets", 'Roboto-Regular.ttf')
        self._font_size = 100
        self.fill = 'white'
        self.circle_size = 192
        self.corner_offset = 30

    def font_size(self, size):
        self._font_size = size
        return self

    def end(self):
        font = ImageFont.truetype(self.font_filename, self._font_size)

        draw = ImageDraw.Draw(self.renderer.img)
        label_w, label_h = draw.textsize('%s' % self.text, font=font, stroke_width=4)

        # Circle

        draw.ellipse((self.renderer.img.width - self.circle_size - self.corner_offset,
                      self.renderer.img.height - self.circle_size - self.corner_offset,
                      self.renderer.img.width - self.corner_offset,
                      self.renderer.img.height - self.corner_offset), fill='red')

        # Label
        label_pos = (self.renderer.img.width - (self.circle_size / 2) - self.corner_offset - (label_w / 2),
                     self.renderer.img.height - (self.circle_size / 2) - self.corner_offset - (label_h / 2))
        draw.text(label_pos, text=self.text, font=font, fill=self.fill, stroke_width=4)

        return self.renderer
