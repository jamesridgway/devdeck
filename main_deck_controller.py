import importlib

import yaml

from deck_controller import DeckController


class MainDeckController(DeckController):
    def deck(self):

        with open("settings.yml", 'r') as stream:
            settings = yaml.safe_load(stream)
            settings = settings['decks'][0]

            for control in settings['controls']:
                module_name, class_name = control['name'].rsplit(".", 1)
                ControlClass = getattr(importlib.import_module(module_name), class_name)
                ctrl_instance = ControlClass(**control['settings']) if 'settings' in control else ControlClass()
                self.register_control(control['key'], ctrl_instance)
