import os

from pulsectl import pulsectl

from controls.deck_control import DeckControl


class MicMuteControl(DeckControl):

    def __init__(self, **kwargs):
        self.pulse = pulsectl.Pulse()
        super().__init__(**kwargs)

    def initialize(self, control_context):
        self.__render_icon(control_context)

    def pressed(self, control_context):
        mic = self.__get_mic()
        self.pulse.source_mute(mic.index, mute=(not mic.mute))
        self.__render_icon(control_context)

    def __get_mic(self):
        sources = self.pulse.source_list()
        return [mic for mic in sources if mic.description == self.settings['microphone']][0]

    def __render_icon(self, control_context):
        mic = self.__get_mic()
        if mic.mute == 0:
            control_context.set_icon(os.path.join(os.path.dirname(__file__), "../assets", 'microphone.png'))
        else:
            control_context.set_icon(os.path.join(os.path.dirname(__file__), "../assets", 'microphone-mute.png'))