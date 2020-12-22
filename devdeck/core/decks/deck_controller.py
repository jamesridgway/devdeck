import logging

from devdeck.core.controls.deck_control import DeckControl


class DeckController(DeckControl):

    def __init__(self, key_no, **kwargs):
        self.__logger = logging.getLogger('devdeck')
        self.controls = {}
        super().__init__(key_no, **kwargs)
        self.deck_controls()

    def clear_deck_context(self):
        for key_no, control in self.controls.items():
            control.clear_deck_context()
        super().clear_deck_context()

    def dispose(self):
        for key_no, control in self.controls.items():
            control.dispose()

    def register_control(self, key_no, control_class, **settings):
        self.controls[key_no] = control_class(key_no, **settings)

    def deck_controls(self):
        pass

    def render(self, deck_context):
        self.__logger.info("Rendering deck: %s", type(self).__name__)
        self.__deck_context = deck_context
        deck_context.reset_deck()
        for key_no, control in self.controls.items():
            control.set_deck_context(deck_context)
            control.initialize()

    def pressed(self, key_no):
        if key_no not in self.controls:
            return
        if issubclass(type(self.controls[key_no]), DeckController):
            return
        self.__logger.info("Key %s pressed on %s", key_no, type(self).__name__)
        self.controls[key_no].pressed()

    def released(self, key_no):
        if key_no not in self.controls:
            return
        if issubclass(type(self.controls[key_no]), DeckController):
            self.__deck_context.set_active_deck(self.controls[key_no])
            return
        self.__logger.info("Key %s released on %s", key_no, type(self).__name__)
        self.controls[key_no].released()
        self.__deck_context.pop_active_deck()
