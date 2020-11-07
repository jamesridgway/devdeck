from controls.mic_mute_control import MicMuteControl
from controls.slack_deck import SlackDeck
from deck_controller import DeckController


class MainDeckController(DeckController):
    def deck(self):
        self.register_control(0, MicMuteControl())
        self.register_control(2, SlackDeck(0))
