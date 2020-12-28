import logging

from devdeck_core.decks.deck_controller import DeckController
from devdeck.settings.control_settings import ControlSettings


class SinglePageDeckController(DeckController):

    def __init__(self, key_no, **kwargs):
        self.__logger = logging.getLogger('devdeck')
        self.settings = kwargs
        super().__init__(key_no, **kwargs)

    def initialize(self):
        with self.deck_context() as context:
            with context.renderer() as r:
                r.image(self.settings['icon']).end()

    def deck_controls(self):
        controls = [ControlSettings(control_settings) for control_settings in self.settings['controls']]
        for control in controls:
            control_class = control.control_class()
            control_settings = control.control_settings()
            self.register_control(control.key(), control_class, **control_settings)

    def settings_schema(self):
        return {
            'controls': {
                'type': 'list',
                'required': True,
                'schema': {
                    'type': 'dict',
                    'schema': {
                        'name': {
                            'type': 'string',
                            'required': True
                        },
                        'key': {
                            'type': 'integer',
                            'required': True
                        },
                        'settings': {
                            'type': 'dict'
                        }
                    }
                }
            },
            'icon': {
                'type': 'string',
            },
        }
