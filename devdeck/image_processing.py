from PIL import Image
from StreamDeck.ImageHelpers import PILHelper


def render_key_image(deck, icon_filename):
    icon = Image.open(icon_filename)
    image = PILHelper.create_scaled_image(deck, icon, margins=[0, 0, 20, 0])
    return PILHelper.to_native_format(deck, image)
