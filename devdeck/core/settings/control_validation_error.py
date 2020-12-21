from devdeck.core.settings.cerberus_utils import CerberusUtils


class ControlValidationError(Exception):
    def __init__(self, control, key_no, errors):
        self.errors = CerberusUtils.format_errors(errors)
        message = 'The following validation errors occurred for {} on key {}:\n{}' \
            .format(
                control.__class__.__name__,
                key_no,
                '\n'.join([" * {}: {}.".format(field, msg) for field, msg in self.errors.items()])
        )
        super().__init__(message)
