class ControlContext:
    def __init__(self, deck_context, key_no):
        self.deck_context = deck_context
        self.key_no = key_no

    def set_icon(self, icon_filename):
        self.deck_context.set_icon(self.key_no, icon_filename)

    def set_icon_native(self, icon):
        self.deck_context.set_key_image_native(self.key_no, icon)

    def render_text(self, text, **kwargs):
        self.deck_context.render_text(self.key_no, text, **kwargs)

    def renderer(self):
        return self.deck_context.renderer(self.key_no)