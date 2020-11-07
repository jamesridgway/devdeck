import os

from controls.deck_control import DeckControl


class SlackOnlineControl(DeckControl):
    def initialize(self, control_context):
        control_context.set_icon(os.path.join(os.path.dirname(__file__), "../../assets", 'slack.png'))

    def pressed(self, control_context):
        print('Slack Online!! - {}'.format(control_context.key_no), flush=True)
