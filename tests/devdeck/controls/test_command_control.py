from assertpy import assert_that

from devdeck.controls.command_control import CommandControl
from devdeck_core.mock_deck_context import mock_context


class TestCommandControl:
    def test_initialize_sets_icon(self):
        control = CommandControl(0, **{'icon': 'my-icon-path'})
        with mock_context(control) as ctx:
            control.initialize()
            assert_that(ctx.get_icon()).is_equal_to('my-icon-path')
