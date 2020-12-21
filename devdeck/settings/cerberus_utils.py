import collections


class CerberusUtils:
    @staticmethod
    def format_errors(errors):
        obj = collections.OrderedDict()

        def recurse(error_items, parent_key=""):
            if isinstance(error_items, list):
                for list_index in range(len(error_items)):
                    recurse(error_items[list_index], str(parent_key) if parent_key else str(list_index))
            elif isinstance(error_items, dict):
                for field, nested_error in error_items.items():
                    recurse(nested_error, str(parent_key) + '.' + str(field) if parent_key else field)
            else:
                obj[parent_key] = error_items

        recurse(errors)
        return obj
