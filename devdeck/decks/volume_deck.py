import logging
import os

from pulsectl import pulsectl
from devdeck_core.decks.deck_controller import DeckController
from devdeck.controls.volume_level_control import VolumeLevelControl

class VolumeDeck(DeckController):
    def __init__(self, key_no, **kwargs):
        self.pulse = None
        self.__logger = logging.getLogger('devdeck')
        super().__init__(key_no, **kwargs)

    def initialize(self):
        self.pulse = pulsectl.Pulse()
        self.__render_icon()

    def deck_controls(self):
        for i in range(0, 11):
            control_settings = dict(self.settings)
            control_settings['volume'] = i * 10
            self.register_control(i, VolumeLevelControl, **control_settings)

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

            with context.renderer() as r:
                r.text("{:.0f}%".format(round(sink.volume.value_flat, 2) * 100)) \
                    .center_horizontally() \
                    .end()
                r.image(os.path.join(os.path.dirname(__file__), "../../assets/font-awesome", 'volume-up-solid.png'))\
                    .width(380)\
                    .height(380) \
                    .center_horizontally() \
                    .y(132) \
                    .end()

    def settings_schema(self):
        return {
            'output': {
                'required': True,
                'type': 'string',
            },
        }
