import os

from devdeck_core.controls.deck_control import DeckControl


class NameListControl(DeckControl):

    def __init__(self, key_no, **kwargs):
        self.name_index = 0
        super().__init__(key_no, **kwargs)

    def initialize(self):
        self.name_index = 0
        with self.deck_context() as context:
            context.set_icon(os.path.join(os.path.dirname(__file__), "../../assets/font-awesome", 'users.png'))

    def pressed(self):
        with self.deck_context() as context:
            if self.name_index > len(self.settings['names']) - 1:
                self.name_index = 0
                context.set_icon(os.path.join(os.path.dirname(__file__), "../../assets", 'users.png'))
            else:
                initials = ''.join(list(map(lambda x: x[0], self.settings['names'][self.name_index].split(' '))))
                context.render_text(initials, font_size=256)
                self.name_index += 1

    def settings_schema(self):
        return {
            'names': {
                'type': 'list',
                'schema': {
                    'type': 'string'
                }
            }
        }
