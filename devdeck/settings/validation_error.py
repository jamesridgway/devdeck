import collections


class ValidationError(Exception):
    def __init__(self, errors):
        self.errors = ValidationError.format_errors(errors)
        message = 'The following validation errors occurred:\n{}' \
            .format('\n'.join([" * {}: {}.".format(field, msg) for field, msg in self.errors.items()]))
        super().__init__(message)

    @staticmethod
    def format_errors(d):
        obj = collections.OrderedDict()

        def recurse(t, parent_key=""):
            if isinstance(t, list):
                for i in range(len(t)):
                    recurse(t[i], str(parent_key) if parent_key else str(i))
            elif isinstance(t, dict):
                for k, v in t.items():
                    recurse(v, str(parent_key) + '.' + str(k) if parent_key else k)
            else:
                obj[parent_key] = t

        recurse(d)
        return obj
