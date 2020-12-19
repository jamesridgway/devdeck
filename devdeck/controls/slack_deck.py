import os

from devdeck.controls.slack.slack_control import SlackOnlineControl
from devdeck.deck_controller import DeckController


class SlackDeck(DeckController):
    def __init__(self, key_no, **kwargs):
        self.offset = kwargs['offset']
        super().__init__(key_no, **kwargs)

    def initialize(self):
        with self.deck_context() as context:
            context.set_icon(os.path.join(os.path.dirname(__file__), "../../assets", 'slack.png'))

    def deck_controls(self):
        self.register_control(self.offset + 0, SlackOnlineControl)
        self.register_control(self.offset + 2, SlackOnlineControl)
        self.register_control(self.offset + 4, SlackOnlineControl)
        self.register_control(self.offset + 6, SlackOnlineControl)
        self.register_control(self.offset + 8, SlackOnlineControl)
        self.register_control(self.offset + 10, SlackOnlineControl)
        if self.offset == 0:
            self.register_control(self.offset + 12, SlackDeck, offset=1)
        else:
            self.register_control(self.offset + 12, SlackOnlineControl)
