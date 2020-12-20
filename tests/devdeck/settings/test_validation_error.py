from assertpy import assert_that

from devdeck.settings.validation_error import ValidationError


class TestValidationError:
    def test_errors_parsed(self):
        errors = {'decks': [{0: [{'controls': [{3: [{'keyx': ['unknown field']}]}]}]}]}
        exception = ValidationError(errors)
        assert_that(str(exception)) \
            .is_equal_to('The following validation errors occurred:\n * decks.0.controls.3.keyx: unknown field.')
