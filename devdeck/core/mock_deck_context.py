from assertpy import assert_that


class MockDeckContext:
    """
    A mock deck context used for designed for use in unit tests for testing controls.
    """

    def __init__(self):
        self.__reset()

    def set_icon(self, key_no, icon_filename):
        self.__reset()
        self.icon_filename = icon_filename

    def set_icon_native(self, key_no, icon):
        self.__reset()
        pass

    def render_text(self, key_no, text, **kwargs):
        self.__reset()
        self.render_text_text = text
        self.render_text_options = kwargs

    def rendered_text(self, text, **kwargs):
        assert_that(text).described_as('rendered text').is_equal_to(self.render_text_text)
        assert_that(kwargs).described_as('rendered text options').is_equal_to(self.render_text_options)

    def get_icon(self):
        return self.icon_filename

    def __reset(self):
        self.icon_filename = None
        self.render_text_text = None
        self.render_text_options = None


def mock_context(control):
    return MockDeckContextManager(control)


class MockDeckContextManager:
    def __init__(self, control):
        self.control = control

    def __enter__(self):
        ctx = MockDeckContext()
        self.control.set_deck_context(ctx)
        return ctx

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.control.clear_deck_context()
