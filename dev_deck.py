from control_context import ControlContext
from deck_context import DeckContext


class DevDeck:
    def __init__(self, deck):
        self.__deck = deck
        self.__deck.set_brightness(50)
        self.__deck.reset()
        self.__deck.set_key_callback(self.key_callback)
        self.decks = []

    def set_active_deck(self, deck):
        self.decks.append(deck)
        self.get_active_deck().render(DeckContext(self, self.__deck))

    def get_active_deck(self):
        return self.decks[-1]

    def pop_active_deck(self):
        if len(self.decks) == 1:
            return
        self.decks.pop()
        self.get_active_deck().render(DeckContext(self, self.__deck))

    def key_callback(self, deck, key, state):
        if state:
            self.get_active_deck().pressed(ControlContext(DeckContext(self, self.__deck), key))
        else:
            self.get_active_deck().released(ControlContext(DeckContext(self, self.__deck), key))
