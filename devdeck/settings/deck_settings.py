import importlib


class DeckSettings:
    def __init__(self, config):
        self.config = config

    def serial_number(self):
        return self.config['serial_number']

    def settings(self):
        return self.config['settings']

    def deck_class(self):
        module_name, class_name = self.config['name'].rsplit(".", 1)
        return getattr(importlib.import_module(module_name), class_name)
