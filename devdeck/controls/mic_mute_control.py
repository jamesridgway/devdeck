import os

from pulsectl import pulsectl

from devdeck.core.controls.deck_control import DeckControl


class MicMuteControl(DeckControl):

    def __init__(self, key_no, **kwargs):
        self.pulse = None
        super().__init__(key_no, **kwargs)

    def initialize(self):
        self.pulse = pulsectl.Pulse()
        self.__render_icon()

    def pressed(self):
        mic = self.__get_mic()
        self.pulse.source_mute(mic.index, mute=(not mic.mute))
        self.__render_icon()

    def __get_mic(self):
        sources = self.pulse.source_list()
        return [mic for mic in sources if mic.description == self.settings['microphone']][0]

    def __render_icon(self):
        with self.deck_context() as context:
            mic = self.__get_mic()
            if mic.mute == 0:
                context.set_icon(os.path.join(os.path.dirname(__file__), "../../assets", 'microphone.png'))
            else:
                context.set_icon(os.path.join(os.path.dirname(__file__), "../../assets", 'microphone-mute.png'))
