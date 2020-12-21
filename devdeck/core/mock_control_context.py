class MockDeckContext:
    """
    A mock deck context used for designed for use in unit tests for testing controls.
    """

    def set_icon(self, key_no, icon_filename):
        self.icon_filename = icon_filename

    def get_icon(self):
        return icon

    def set_icon_native(self, key_no, icon):
        pass

    def render_text(self, text, **kwargs):
        pass


def mock_context(control):
    return MockCDeckContextManager(control)


class MockCDeckContextManager:
    def __init__(self, control):
        self.control = control

    def __enter__(self):
        ctx = MockDeckContext()
        self.control.set_deck_context(ctx)
        return ctx

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.control.clear_deck_context()
