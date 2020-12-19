import os

from PIL import ImageFont, Image, ImageDraw
from StreamDeck.ImageHelpers import PILHelper
from devdeck.image_processing import render_key_image


class DeckContext:
    def __init__(self, devdeck, deck):
        self.__devdeck = devdeck
        self.__deck = deck

    def set_icon(self, key_no, icon_filename):
        icon = self.render_image(icon_filename)
        self.set_key_image(key_no, icon)

    def reset_deck(self):
        keys = self.__deck.key_count()
        for key_no in range(keys):
            self.__deck.set_key_image(key_no, None)

    def render_image(self, icon_filename):
        return render_key_image(self.__deck, icon_filename)

    def set_key_image(self, key_no, icon):
        self.__deck.set_key_image(key_no, icon)

    def set_key_image_native(self, key_no, icon):
        image = PILHelper.to_native_format(self.__deck, icon)
        self.__deck.set_key_image(key_no, image)

    def set_active_deck(self, deck):
        self.__devdeck.set_active_deck(deck)

    def pop_active_deck(self):
        self.__devdeck.pop_active_deck()

    def render_text(self, key_no, text, font_size=120, fill="white"):
        font = ImageFont.truetype(os.path.join(os.path.dirname(__file__), "../assets", 'Roboto-Regular.ttf'), font_size)

        image = Image.new("RGB", (512, 512))
        draw = ImageDraw.Draw(image)
        label_w, label_h = draw.textsize('%s' % text, font=font)
        label_pos = ((512 - label_w) // 2, (512 - label_h) // 2)
        draw.text(label_pos, text=text, font=font, fill=fill)
        self.set_key_image_native(key_no, image)
