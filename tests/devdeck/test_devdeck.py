from unittest import mock

from assertpy import assert_that

from devdeck.devdeck import DevDeck


class TestDevDeck:
    @mock.patch('StreamDeck.Devices.StreamDeck.StreamDeck')
    @mock.patch('StreamDeck.Devices.StreamDeck.StreamDeck')
    def test_set_active_deck(self, first_mock_deck, second_mock_deck):
        dev_deck = DevDeck(first_mock_deck)

        assert_that(dev_deck.get_active_deck()).is_none()

        # Sets active deck
        dev_deck.set_active_deck(first_mock_deck)
        assert_that(dev_deck.get_active_deck()).is_equal_to(first_mock_deck)

        # Set active deck to another instance
        dev_deck.set_active_deck(second_mock_deck)
        first_mock_deck.clear_deck_context.assert_called_once()
        assert_that(dev_deck.get_active_deck()).is_equal_to(second_mock_deck)

    @mock.patch('StreamDeck.Devices.StreamDeck.StreamDeck')
    @mock.patch('StreamDeck.Devices.StreamDeck.StreamDeck')
    def test_pop_active_deck(self, first_mock_deck, second_mock_deck):
        dev_deck = DevDeck(first_mock_deck)

        # Two active decks and the second is active
        dev_deck.set_active_deck(first_mock_deck)
        dev_deck.set_active_deck(second_mock_deck)
        assert_that(dev_deck.get_active_deck()).is_equal_to(second_mock_deck)

        dev_deck.pop_active_deck()
        second_mock_deck.clear_deck_context.assert_called_once()
        assert_that(dev_deck.get_active_deck()).is_equal_to(first_mock_deck)

    @mock.patch('StreamDeck.Devices.StreamDeck.StreamDeck')
    def test_pop_active_deck_does_not_remove_root_deck(self, first_mock_deck):
        dev_deck = DevDeck(first_mock_deck)
        dev_deck.set_active_deck(first_mock_deck)
        assert_that(dev_deck.get_active_deck()).is_equal_to(first_mock_deck)

        # Root deck is still active even if a pop is attempted
        dev_deck.pop_active_deck()
        assert_that(dev_deck.get_active_deck()).is_equal_to(first_mock_deck)

    @mock.patch('StreamDeck.Devices.StreamDeck.StreamDeck')
    def test_key_callback_propogates_to_active_deck(self, first_mock_deck):
        dev_deck = DevDeck(first_mock_deck)
        dev_deck.set_active_deck(first_mock_deck)

        # Pressed
        dev_deck.key_callback(first_mock_deck, 12, True)
        first_mock_deck.pressed.called_pnce_with(12)

        # Released
        dev_deck.key_callback(first_mock_deck, 23, False)
        first_mock_deck.released.called_pnce_with(23)