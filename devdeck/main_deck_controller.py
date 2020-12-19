import importlib
import os
from pathlib import Path

import yaml

from devdeck.deck_controller import DeckController


class MainDeckController(DeckController):

    def __init__(self, **kwargs):
        super().__init__(None, **kwargs)

    def deck_controls(self):

        with open(os.path.join(str(Path.home()), '.devdeck', 'settings.yml'), 'r') as stream:
            settings = yaml.safe_load(stream)
            settings = settings['decks'][0]

            for control in settings['controls']:
                module_name, class_name = control['name'].rsplit(".", 1)
                ControlClass = getattr(importlib.import_module(module_name), class_name)
                control_settings = control['settings'] if 'settings' in control else {}
                self.register_control(control['key'], ControlClass, **control_settings)

