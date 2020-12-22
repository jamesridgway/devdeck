import sys

from cerberus import Validator

from devdeck.core.control_context import ControlContext
from devdeck.core.settings.control_validation_error import ControlValidationError


class DeckControlContextBlock(Exception):
    pass


class DeckContextManager:
    def __init__(self, deck_context, key_no):
        self.deck_context = deck_context
        self.key_no = key_no

    def __enter__(self):
        if self.deck_context is None:
            sys.settrace(lambda *args, **keys: None)
            frame = sys._getframe(1)
            frame.f_trace = self.trace
        else:
            return ControlContext(self.deck_context, self.key_no)

    def trace(self, frame, event, arg):
        raise DeckControlContextBlock()

    def __exit__(self, type, value, traceback):
        if type is None:
            return  # No exception
        if issubclass(type, DeckControlContextBlock):
            return True  # Suppress special DeckControlContextBlock exception


class DeckControl:
    def __init__(self, key_no, **kwargs):
        self.__deck_context = None
        self.__key_no = key_no
        self.settings = kwargs
        self.validate_settings()

    def set_deck_context(self, deck_context):
        self.__deck_context = deck_context

    def clear_deck_context(self):
        self.__deck_context = None

    def deck_context(self):
        return DeckContextManager(self.__deck_context, self.__key_no)

    def dispose(self):
        pass

    def initialize(self):
        pass

    def pressed(self):
        pass

    def released(self):
        pass

    def settings_schema(self):
        return None

    def validate_settings(self):
        if self.settings_schema() is None:
            return

        validator = Validator(self.settings_schema())
        if not validator.validate(self.settings, self.settings_schema()):
            raise ControlValidationError(self, self.__key_no, validator.errors)
