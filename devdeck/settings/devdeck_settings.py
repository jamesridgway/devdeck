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
                    'type': 'string'
                },
                'controls': {
                    'type': 'list',
                    'schema': {
                        'type': 'dict',
                        'schema': {
                            'name': {
                                'type': 'string'
                            },
                            'key': {
                                'type': 'integer'
                            },
                            'settings': {
                                'type': 'dict'
                            }
                        }
                    }
                }
            }
        }
    }
}


class DevDeckSettings:
    def __init__(self, settings):
        self.settings = settings

    def decks(self):
        return [DeckSettings(deck_setting) for deck_setting in self.settings['decks']]

    @staticmethod
    def load(filename):
        with open(filename, 'r') as stream:
            settings = yaml.safe_load(stream)

            validator = Validator(schema)
            if validator.validate(settings, schema):
                return DevDeckSettings(settings)
            else:
                raise ValidationError(validator.errors)
