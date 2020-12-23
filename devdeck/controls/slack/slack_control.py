import os

from devdeck_core.controls.deck_control import DeckControl


class SlackOnlineControl(DeckControl):
    def initialize(self):
        with self.deck_context() as context:
            context.set_icon(os.path.join(os.path.dirname(__file__), "../../../assets", 'slack.png'))

    def pressed(self):
        print('Slack Online!!')
