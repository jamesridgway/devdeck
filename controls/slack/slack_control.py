import os

from controls.deck_control import DeckControl


class SlackOnlineControl(DeckControl):
    def initialize(self, context):
        context.set_icon(os.path.join(os.path.dirname(__file__), "../../assets", 'slack.png'))

    def pressed(self, context):
        print('Slack Online!! - {}'.format(context.key_no), flush=True)
