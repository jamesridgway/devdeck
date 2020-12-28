from devdeck_core.mock_deck_context import mock_context, assert_rendered

from devdeck.controls.command_control import CommandControl
from tests.testing_utils import TestingUtils


class TestCommandControl:
    def test_initialize_sets_icon(self):
        control = CommandControl(0, **{'icon': TestingUtils.get_filename('test-icon.png')})
        with mock_context(control) as ctx:
            control.initialize()
            assert_rendered(ctx, TestingUtils.get_filename('test-icon.png'))
