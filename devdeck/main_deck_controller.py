import logging
import os
from pathlib import Path

from devdeck.deck_controller import DeckController
from devdeck.settings.devdeck_settings import DevDeckSettings
from devdeck.settings.validation_error import ValidationError


class MainDeckController(DeckController):

    def __init__(self, **kwargs):
        self.__logger = logging.getLogger('devdeck')
        super().__init__(None, **kwargs)

    def deck_controls(self):

        settings_filename = os.path.join(str(Path.home()), '.devdeck', 'settings.yml')
        if not os.path.exists(settings_filename):
            self.__logger.warning("No settings file detected!")
            return

        try:
            settings = DevDeckSettings.load(settings_filename)

            # TODO: Better handling of multiple decks
            for deck in settings.decks():
                for control in deck.controls():
                    control_class = control.control_class()
                    control_settings = control.control_settings()
                    self.register_control(control.key(), control_class, **control_settings)

        except ValidationError as validation_error:
            print(validation_error)
