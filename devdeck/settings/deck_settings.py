from devdeck.settings.control_settings import ControlSettings


class DeckSettings:
    def __init__(self, settings):
        self.settings = settings

    def serial_number(self):
        return self.settings['serial_number']

    def controls(self):
        return [ControlSettings(control_settings) for control_settings in self.settings['controls']]
