import os

from devdeck_core.controls.deck_control import DeckControl


class NameListControl(DeckControl):

    def __init__(self, key_no, **kwargs):
        self.name_index = 0
        super().__init__(key_no, **kwargs)

    def initialize(self):
        self.name_index = 0
        with self.deck_context() as context:
            with context.renderer() as r:
                r.image(os.path.join(os.path.join(os.path.dirname(__file__), "../../assets/font-awesome", 'users.png'))).end()

    def pressed(self):
        if 'name' not in self.settings or len(self.settings['names']) == 0:
            return
        with self.deck_context() as context:
            if self.name_index > len(self.settings['names']) - 1:
                self.name_index = 0
                with context.renderer() as r:
                    r.image(os.path.join(
                        os.path.join(os.path.dirname(__file__), "../../assets/font-awesome", 'users.png'))).end()
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
