import importlib


class ControlSettings:
    def __init__(self, settings):
        self.settings = settings

    def control_class(self):
        module_name, class_name = self.settings['name'].rsplit(".", 1)
        return getattr(importlib.import_module(module_name), class_name)

    def control_settings(self):
        if 'settings' in self.settings:
            return self.settings['settings']
        return {}

    def key(self):
        return self.settings['key']
