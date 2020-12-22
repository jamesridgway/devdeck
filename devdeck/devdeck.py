import logging

from devdeck.deck_context import DeckContext


class DevDeck:
    def __init__(self, deck):
        self.__logger = logging.getLogger('devdeck')
        self.__deck = deck
        self.__deck.set_brightness(50)
        self.__deck.reset()
        self.__deck.set_key_callback(self.key_callback)
        self.decks = []

    def set_active_deck(self, deck):
        self.__logger.info("Setting active deck: %s", type(deck).__name__)
        for deck_itr in self.decks:
            deck_itr.clear_deck_context()
        self.decks.append(deck)
        self.get_active_deck().render(DeckContext(self, self.__deck))

    def get_active_deck(self):
        if not self.decks:
            return None
        return self.decks[-1]

    def pop_active_deck(self):
        if len(self.decks) == 1:
            return
        popped_deck = self.decks.pop()
        self.__logger.info("Exiting deck: %s", type(popped_deck).__name__)
        popped_deck.clear_deck_context()
        self.get_active_deck().render(DeckContext(self, self.__deck))

    def key_callback(self, deck, key, state):
        if state:
            self.get_active_deck().pressed(key)
        else:
            self.get_active_deck().released(key)

    def close(self):
        keys = self.__deck.key_count()
        for deck in self.decks:
            deck.dispose()
        for key_no in range(keys):
            self.__deck.set_key_image(key_no, None)