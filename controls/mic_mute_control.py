import os

from controls.deck_control import DeckControl


class MicMuteControl(DeckControl):
    def initialize(self, context):
        context.set_icon(os.path.join(os.path.dirname(__file__), "../assets", 'microphone.png'))
        self.muted = False

    def pressed(self, context):
        self.muted = not self.muted
        if self.muted:
            context.set_icon(os.path.join(os.path.dirname(__file__), "../assets", 'microphone-mute.png'))
        else:
            context.set_icon(os.path.join(os.path.dirname(__file__), "../assets", 'microphone.png'))
