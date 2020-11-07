import threading

from StreamDeck.DeviceManager import DeviceManager

from dev_deck import DevDeck
from main_deck_controller import MainDeckController

if __name__ == "__main__":
    streamdecks = DeviceManager().enumerate()

    for index, deck in enumerate(streamdecks):
        deck.open()
        dev_deck = DevDeck(deck)
        dev_deck.set_active_deck(MainDeckController())

        for t in threading.enumerate():
            if t is threading.currentThread():
                continue

            if t.is_alive():
                t.join()
