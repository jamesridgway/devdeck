from assertpy import assert_that

from devdeck.controls.mic_mute_control import MicMuteControl
from devdeck.controls.timer_control import TimerControl
from devdeck.settings.deck_settings import DeckSettings
from devdeck.settings.devdeck_settings import DevDeckSettings
from devdeck.settings.validation_error import ValidationError
from tests.testing_utils import TestingUtils


class TestDevDeckSettings:
    def test_empty_config(self):
        devdeck_settings = DevDeckSettings.load(TestingUtils.get_filename('devdeck/settings/test_devdeck_settings_empty.yml'))
        assert_that(devdeck_settings.decks()).is_empty()

    def test_invalid_config_raises_exception(self):
        filename = TestingUtils.get_filename('devdeck/settings/test_devdeck_settings_not_valid.yml')
        assert_that(DevDeckSettings.load).raises(ValidationError).when_called_with(filename)\
            .is_equal_to('The following validation errors occurred:\n * decks.0.controls.2.keyx: unknown field.')

    def test_deck_returns_settings_specific_for_deck(self):
        devdeck_settings = DevDeckSettings.load(
            TestingUtils.get_filename('devdeck/settings/test_devdeck_settings_valid.yml'))
        assert_that(devdeck_settings.deck('unknown s/n')).is_none()

        assert_that(devdeck_settings.deck('ABC123')).is_instance_of(DeckSettings)

    def test_empty_config(self):
        devdeck_settings = DevDeckSettings.load(TestingUtils.get_filename('devdeck/settings/test_devdeck_settings_valid.yml'))
        # There is one deck, with the series number ABC123
        assert_that(devdeck_settings.decks()).is_length(1)
        deck = devdeck_settings.decks()[0]
        assert_that(deck.serial_number()).is_equal_to('ABC123')
        # And it has a MicMuteControl on key 0 and TimerControl on key 3
        micmute = deck.controls()[0]
        assert_that(micmute.control_class()).is_equal_to(MicMuteControl)
        assert_that(micmute.key()).is_equal_to(0)
        # And it has a MicMuteControl on key 0 and TimerControl on key 3
        timer = deck.controls()[1]
        assert_that(timer.control_class()).is_equal_to(TimerControl)
        assert_that(timer.key()).is_equal_to(3)
