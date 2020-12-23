import os

from PIL import Image, ImageFont, ImageDraw
from devdeck.rendering.badge_count_renderer import BadgeCountRenderer
from devdeck.rendering.emoji_renderer import EmojiRenderer
from devdeck.rendering.text_renderer import TextRenderer


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

    def emoji(self, text):
        return EmojiRenderer(self, text)

    def text(self, text):
        return TextRenderer(self, text)

    def render(self):
        return self.image

