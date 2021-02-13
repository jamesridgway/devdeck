from datetime import datetime

from assertpy import assert_that

from devdeck.controls.timer_control import TimerControl
from devdeck_core.mock_deck_context import mock_context, assert_rendered

from tests.testing_utils import TestingUtils


class TestTimerControl:
    def test_initialize_sets_icon_and_resets_name_index(self):
        timer_control = TimerControl(0)
        with mock_context(timer_control) as ctx:
            timer_control.initialize()
            assert_rendered(ctx, TestingUtils.get_filename('../devdeck/assets/font-awesome/stopwatch.png'))

    def test_initial_state(self):
        timer_control = TimerControl(0)
        assert_that(timer_control.start_time).is_none()
        assert_that(timer_control.end_time).is_none()

    def test_time_diff_to_str(self):
        start_time = datetime(2020, 12, 22, 10, 48, 0, 0)
        end_time = datetime(2020, 12, 22, 11, 50, 3, 0)
        assert_that(TimerControl.time_diff_to_str(end_time - start_time)).is_equal_to("01:02:03")

    def test_pressed_transitions_state_correctly(self):
        timer_control = TimerControl(0)

        # Timer starts
        timer_control.pressed()
        assert_that(timer_control.start_time).is_not_none()
        assert_that(timer_control.end_time).is_none()

        # Time ends
        timer_control.pressed()
        assert_that(timer_control.start_time).is_not_none()
        assert_that(timer_control.end_time).is_not_none()
        assert_that(timer_control.end_time).is_greater_than_or_equal_to(timer_control.start_time)

        # Timer resets state
        timer_control.pressed()
        assert_that(timer_control.start_time).is_none()
        assert_that(timer_control.end_time).is_none()
