from assertpy import assert_that

from devdeck.decks.single_page_deck_controller import SinglePageDeckController
from devdeck.settings.deck_settings import DeckSettings
from devdeck.settings.devdeck_settings import DevDeckSettings
from devdeck.settings.validation_error import ValidationError
from tests.testing_utils import TestingUtils


class TestDevDeckSettings:
    def test_empty_config(self):
        devdeck_settings = DevDeckSettings.load(
            TestingUtils.get_filename('devdeck/settings/test_devdeck_settings_empty.yml'))
        assert_that(devdeck_settings.decks()).is_empty()

    def test_invalid_config_raises_exception(self):
        filename = TestingUtils.get_filename('devdeck/settings/test_devdeck_settings_not_valid.yml')
        assert_that(DevDeckSettings.load).raises(ValidationError).when_called_with(filename) \
            .is_equal_to('The following validation errors occurred:\n * decks.0.settings: required field.')

    def test_deck_returns_settings_specific_for_deck(self):
        devdeck_settings = DevDeckSettings.load(
            TestingUtils.get_filename('devdeck/settings/test_devdeck_settings_valid.yml'))
        assert_that(devdeck_settings.deck('unknown s/n')).is_none()

        assert_that(devdeck_settings.deck('ABC123')).is_instance_of(DeckSettings)

    def test_valid_config(self):
        devdeck_settings = DevDeckSettings.load(
            TestingUtils.get_filename('devdeck/settings/test_devdeck_settings_valid.yml'))
        # There is one deck, with the series number ABC123
        assert_that(devdeck_settings.decks()).is_length(1)
        deck = devdeck_settings.decks()[0]
        assert_that(deck.serial_number()).is_equal_to('ABC123')
        assert_that(deck.deck_class()).is_equal_to(SinglePageDeckController)
        assert_that(deck.settings()['controls']).is_length(2)
