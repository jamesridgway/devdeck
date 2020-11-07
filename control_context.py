import os

from PIL import ImageFont, Image, ImageDraw


class ControlContext:
    def __init__(self, deck_context, key_no):
        self.deck_context = deck_context
        self.key_no = key_no

    def set_icon(self, icon_filename):
        icon = self.deck_context.render_image(icon_filename)
        self.deck_context.set_key_image(self.key_no, icon)

    def set_icon_native(self, icon):
        self.deck_context.set_key_image_native(self.key_no, icon)

    def render_text(self, text, font_size):
        font = ImageFont.truetype(os.path.join(os.path.dirname(__file__), "assets", 'Roboto-Regular.ttf'), font_size)

        image = Image.new("RGB", (512, 512))
        draw = ImageDraw.Draw(image)
        label_w, label_h = draw.textsize('%s' % text, font=font)
        label_pos = ((512 - label_w) // 2, (512 - label_h) // 2)
        draw.text(label_pos, text=text, font=font, fill="white")
        self.set_icon_native(image)
