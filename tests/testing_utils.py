import os


class TestingUtils:
    @staticmethod
    def get_filename(relative_path):
        return os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path))