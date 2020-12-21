from assertpy import assert_that

from devdeck.controls.name_list_control import NameListControl
from devdeck.core.mock_deck_context import mock_context


class TestNameListControl:
    def test_initialize_sets_icon_and_resets_name_index(self):
        name_list_control = NameListControl(0)
        name_list_control.name_index = 1
        with mock_context(name_list_control) as ctx:
            name_list_control.initialize()
            assert_that(name_list_control.name_index).is_equal_to(0)
            assert_that(ctx.get_icon()).ends_with('users.png')

    def test_pressed_iterates_initials(self):
        settings = {'names': ['Sarah Mcgrath', 'Eduardo Sanders', 'Ellis Banks']}
        name_list_control = NameListControl(0, **settings)
        with mock_context(name_list_control) as ctx:
            # Initial state
            assert_that(name_list_control.name_index).is_equal_to(0)

            name_list_control.pressed()
            ctx.rendered_text('SM', font_size=256)
            assert_that(name_list_control.name_index).is_equal_to(1)

            name_list_control.pressed()
            ctx.rendered_text('ES', font_size=256)
            assert_that(name_list_control.name_index).is_equal_to(2)

            name_list_control.pressed()
            ctx.rendered_text('EB', font_size=256)
            assert_that(name_list_control.name_index).is_equal_to(3)

            name_list_control.pressed()
            assert_that(ctx.get_icon()).ends_with('users.png')

            name_list_control.pressed()
            ctx.rendered_text('SM', font_size=256)
            assert_that(name_list_control.name_index).is_equal_to(1)
