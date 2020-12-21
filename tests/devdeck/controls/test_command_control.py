from assertpy import assert_that

from devdeck.controls.command_control import CommandControl
from devdeck.core.mock_control_context import mock_control_context


class TestCommandControl:
    def test_initialize_sets_icon(self):
        control = CommandControl(0, **{'icon': 'my-icon-path'})
        with mock_control_context(control) as ctx:
            control.initialize()
            assert_that(ctx.get_icont()).is_equal_to('my-icon-path')

    def test_pressed_runs_command(self):
        pass
