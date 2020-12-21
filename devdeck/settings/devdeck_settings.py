import yaml
from cerberus import Validator

from devdeck.settings.deck_settings import DeckSettings
from devdeck.settings.validation_error import ValidationError

schema = {
    'decks': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'serial_number': {
                    'type': 'string',
                    'required': True
                },
                'name': {
                    'type': 'string',
                    'required': True
                },
                'settings': {
                    'type': 'dict',
                    'required': True
                }
            }
        }
    }
}


class DevDeckSettings:
    def __init__(self, settings):
        self.settings = settings

    def deck(self, serial_number):
        settings_for_deck = [deck_setting for deck_setting in self.decks() if
                             deck_setting.serial_number() == serial_number[0:12]]
        if settings_for_deck:
            return settings_for_deck[0]
        return None

    def decks(self):
        return [DeckSettings(deck_setting) for deck_setting in self.settings['decks']]

    @staticmethod
    def load(filename):
        with open(filename, 'r') as stream:
            settings = yaml.safe_load(stream)

            validator = Validator(schema)
            if validator.validate(settings, schema):
                return DevDeckSettings(settings)
            raise ValidationError(validator.errors)
