import os

from controls.deck_control import DeckControl


class NameListControl(DeckControl):

    def __init__(self, **kwargs):
        self.name_index = 0
        super().__init__(**kwargs)

    def initialize(self, control_context):
        control_context.set_icon(os.path.join(os.path.dirname(__file__), "../assets", 'users.png'))

    def pressed(self, control_context):
        if self.name_index > len(self.settings['names']) -1:
            self.name_index = 0
            control_context.set_icon(os.path.join(os.path.dirname(__file__), "../assets", 'users.png'))
        else:
            initials = ''.join(list(map(lambda x: x[0], self.settings['names'][self.name_index].split(' '))))
            control_context.render_text(initials, 256)
            self.name_index += 1
