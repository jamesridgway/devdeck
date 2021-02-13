from assertpy import assert_that
from devdeck_core.renderer import Renderer

from devdeck.controls.name_list_control import NameListControl
from devdeck_core.mock_deck_context import mock_context, assert_rendered

from tests.testing_utils import TestingUtils


class TestNameListControl:
    def test_initialize_sets_icon_and_resets_name_index(self):
        name_list_control = NameListControl(0)
        name_list_control.name_index = 1
        with mock_context(name_list_control) as ctx:
            name_list_control.initialize()
            assert_that(name_list_control.name_index).is_equal_to(0)
            assert_rendered(ctx, TestingUtils.get_filename('../devdeck/assets/font-awesome/users.png'))

    def test_pressed_iterates_initials(self):
        settings = {'names': ['Sarah Mcgrath', 'Eduardo Sanders', 'Ellis Banks']}
        name_list_control = NameListControl(0, **settings)
        with mock_context(name_list_control) as ctx:
            # Initial state
            assert_that(name_list_control.name_index).is_equal_to(0)

            name_list_control.pressed()
            assert_rendered(ctx, Renderer().text('SM').font_size(256).center_vertically().center_horizontally().end())
            assert_that(name_list_control.name_index).is_equal_to(1)

            name_list_control.pressed()
            assert_rendered(ctx, Renderer().text('ES').font_size(256).center_vertically().center_horizontally().end())
            assert_that(name_list_control.name_index).is_equal_to(2)

            name_list_control.pressed()
            assert_rendered(ctx, Renderer().text('EB').font_size(256).center_vertically().center_horizontally().end())
            assert_that(name_list_control.name_index).is_equal_to(3)

            name_list_control.pressed()
            assert_rendered(ctx, TestingUtils.get_filename('../devdeck/assets/font-awesome/users.png'))

            name_list_control.pressed()
            assert_rendered(ctx, Renderer().text('SM').font_size(256).center_vertically().center_horizontally().end())
            assert_that(name_list_control.name_index).is_equal_to(1)
