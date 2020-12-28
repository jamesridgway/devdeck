import logging
import os

from pulsectl import pulsectl

from devdeck_core.controls.deck_control import DeckControl


class MicMuteControl(DeckControl):

    def __init__(self, key_no, **kwargs):
        self.pulse = None
        self.__logger = logging.getLogger('devdeck')
        super().__init__(key_no, **kwargs)

    def initialize(self):
        if self.pulse is None:
            self.pulse = pulsectl.Pulse('MicMuteControl')
        self.__render_icon()

    def pressed(self):
        mic = self.__get_mic()
        if mic is None:
            return
        self.pulse.source_mute(mic.index, mute=(not mic.mute))
        self.__render_icon()

    def __get_mic(self):
        sources = self.pulse.source_list()

        selected_mic = [mic for mic in sources if mic.description == self.settings['microphone']]
        if len(selected_mic) == 0:
            possible_mics = [output.description for output in sources]
            self.__logger.warning("Microphone '%s' not found in list of possible inputs:\n%s",
                                  self.settings['microphone'],
                                  '\n'.join(possible_mics))
            return None
        return selected_mic[0]

    def __render_icon(self):
        with self.deck_context() as context:
            mic = self.__get_mic()
            if mic is None:
                with context.renderer() as r:
                    r \
                        .text('MIC \nNOT FOUND') \
                        .color('red') \
                        .center_vertically() \
                        .center_horizontally() \
                        .font_size(85) \
                        .text_align('center') \
                        .end()
                return
            if mic.mute == 0:
                with context.renderer() as r:
                    r.image(os.path.join(os.path.dirname(__file__), "../../assets/font-awesome", 'microphone.png')).end()
            else:
                with context.renderer() as r:
                    r.image(os.path.join(os.path.dirname(__file__), "../../assets/font-awesome", 'microphone-mute.png')).end()

    def settings_schema(self):
        return {
            'microphone': {
                'type': 'string'
            }
        }