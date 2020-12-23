from devdeck_core.settings.cerberus_utils import CerberusUtils


class ValidationError(Exception):
    def __init__(self, errors):
        self.errors = CerberusUtils.format_errors(errors)
        message = 'The following validation errors occurred:\n{}' \
            .format('\n'.join([" * {}: {}.".format(field, msg) for field, msg in self.errors.items()]))
        super().__init__(message)
