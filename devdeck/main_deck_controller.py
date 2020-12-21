import logging

from devdeck.deck_controller import DeckController


class MainDeckController(DeckController):

    def __init__(self, **kwargs):
        self.__logger = logging.getLogger('devdeck')
        self.settings = kwargs["settings"]
        super().__init__(None, **kwargs)

    def deck_controls(self):
        for control in self.settings.controls():
            control_class = control.control_class()
            control_settings = control.control_settings()
            self.register_control(control.key(), control_class, **control_settings)
