class ControlContext:
    def __init__(self, deck_context, key_no):
        self.deck_context = deck_context
        self.key_no = key_no

    def set_icon(self, icon_filename):
        icon = self.deck_context.render_image(icon_filename)
        self.deck_context.set_key_image(self.key_no, icon)

    def set_icon_native(self, icon):
        self.deck_context.set_key_image_native(self.key_no, icon)