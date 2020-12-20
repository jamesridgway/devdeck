from assertpy import assert_that

from devdeck.controls.timer_control import TimerControl
from devdeck.settings.control_settings import ControlSettings


class TestControlSetting:
    def test_control_settings_tolerates_no_settings(self):
        control_settings = ControlSettings({'name': 'devdeck.controls.timer_control.TimerControl', 'key': 123})
        assert_that(control_settings.control_settings()).is_empty()

    def test_control_settings_parses_settings(self):
        control_settings = ControlSettings({
            'name': 'devdeck.controls.timer_control.TimerControl',
            'key': 123,
            'settings': {'hello': 'world'}
        })
        assert_that(control_settings.control_settings()).is_equal_to({'hello': 'world'})

    def test_control_class_provides_class(self):
        control_settings = ControlSettings({'name': 'devdeck.controls.timer_control.TimerControl', 'key': 123})
        assert_that(control_settings.control_class()).is_equal_to(TimerControl)

    def test_key(self):
        control_settings = ControlSettings({'name': 'devdeck.controls.timer_control.TimerControl', 'key': 123})
        assert_that(control_settings.key()).is_equal_to(123)
