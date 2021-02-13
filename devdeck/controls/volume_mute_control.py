import logging
import os

from pulsectl import pulsectl

from devdeck_core.controls.deck_control import DeckControl


class VolumeMuteControl(DeckControl):

    def __init__(self, key_no, **kwargs):
        self.pulse = None
        self.__logger = logging.getLogger('devdeck')
        super().__init__(key_no, **kwargs)

    def initialize(self):
        self.pulse = pulsectl.Pulse()
        self.__render_icon()

    def pressed(self):
        output = self.__get_output()
        if output is None:
            return
        self.pulse.sink_mute(output.index, mute=(not output.mute))
        self.__render_icon()

    def __get_output(self):
        sinks = self.pulse.sink_list()
        selected_output = [output for output in sinks if output.description == self.settings['output']]
        if len(selected_output) == 0:
            possible_ouputs = [output.description for output in sinks]
            self.__logger.warning("Output '%s' not found in list of possible outputs:\n%s", self.settings['output'], '\n'.join(possible_ouputs))
            return None
        return selected_output[0]

    def __render_icon(self):
        with self.deck_context() as context:
            sink = self.__get_output()
            if sink is None:
                with context.renderer() as r:
                    r\
                        .text('OUTPUT \nNOT FOUND')\
                        .color('red')\
                        .center_vertically()\
                        .center_horizontally()\
                        .font_size(85)\
                        .text_align('center')\
                        .end()
                return
            if sink.mute == 0:
                with context.renderer() as r:
                    r.image(os.path.join(os.path.dirname(__file__), "../assets/font-awesome", 'volume-up-solid.png')).end()
            else:
                with context.renderer() as r:
                    r.image(os.path.join(os.path.dirname(__file__), "../assets/font-awesome", 'volume-off-solid.png')).end()
