import logging
import os
import sys
import threading
from logging.handlers import RotatingFileHandler
from pathlib import Path

from StreamDeck.DeviceManager import DeviceManager

from devdeck.deck_manager import DeckManager
from devdeck.filters import InfoFilter
from devdeck.settings.devdeck_settings import DevDeckSettings
from devdeck.settings.validation_error import ValidationError


def main():
    os.makedirs(os.path.join(str(Path.home()), '.devdeck'), exist_ok=True)

    root = logging.getLogger('devdeck')
    root.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    info_handler = logging.StreamHandler(sys.stdout)
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(formatter)
    info_handler.addFilter(InfoFilter())
    root.addHandler(info_handler)

    error_handler = logging.StreamHandler(sys.stderr)
    error_handler.setLevel(logging.WARNING)
    error_handler.setFormatter(formatter)
    root.addHandler(error_handler)

    fileHandler = RotatingFileHandler(os.path.join(str(Path.home()), '.devdeck', 'devdeck.log'), maxBytes=100000,
                                      backupCount=5)
    fileHandler.setFormatter(formatter)
    root.addHandler(fileHandler)

    streamdecks = DeviceManager().enumerate()

    settings_filename = os.path.join(str(Path.home()), '.devdeck', 'settings.yml')
    if not os.path.exists(settings_filename):
        root.warning("No settings file detected!")

        serial_numbers = []
        for index, deck in enumerate(streamdecks):
            deck.open()
            serial_numbers.append(deck.get_serial_number())
            deck.close()
        if len(serial_numbers) > 0:
            root.info("Generating a setting file as none exist: %s", settings_filename)
            DevDeckSettings.generate_default(settings_filename, serial_numbers)
        else:
            root.info("""No stream deck connected. Please connect a stream deck to generate an initial config file. \n
                         If you are having difficulty detecting your stream deck please follow the installation
                         instructions: https://github.com/jamesridgway/devdeck/wiki/Installation""")
            exit(0)

    try:
        settings = DevDeckSettings.load(settings_filename)
    except ValidationError as validation_error:
        print(validation_error)

    for index, deck in enumerate(streamdecks):
        deck.open()
        root.info('Connecting to deck: %s (S/N: %s)', deck.id(), deck.get_serial_number())

        deck_settings = settings.deck(deck.get_serial_number())
        if deck_settings is None:
            root.info("Skipping deck %s (S/N: %s) - no settings present", deck.id(), deck.get_serial_number())
            deck.close()
            continue

        deck_manager = DeckManager(deck)

        # Instantiate deck
        main_deck = deck_settings.deck_class()(None, **deck_settings.settings())
        deck_manager.set_active_deck(main_deck)

        for t in threading.enumerate():
            if t is threading.currentThread():
                continue

            if t.is_alive():
                try:
                    t.join()
                except KeyboardInterrupt as ex:
                    deck_manager.close()
                    deck.close()

    if len(streamdecks) == 0:
        root.info("No streamdecks detected, exiting.")


if __name__ == '__main__':
    main()
