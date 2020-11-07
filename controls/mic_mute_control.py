import os

from controls.deck_control import DeckControl


class MicMuteControl(DeckControl):
    def initialize(self, control_context):
        control_context.set_icon(os.path.join(os.path.dirname(__file__), "../assets", 'microphone.png'))
        self.muted = False

    def pressed(self, control_context):
        self.muted = not self.muted
        if self.muted:
            control_context.set_icon(os.path.join(os.path.dirname(__file__), "../assets", 'microphone-mute.png'))
        else:
            control_context.set_icon(os.path.join(os.path.dirname(__file__), "../assets", 'microphone.png'))
