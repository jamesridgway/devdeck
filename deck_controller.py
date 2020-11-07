from control_context import ControlContext
from controls.deck_control import DeckControl


class DeckController(DeckControl):

    def __init__(self):
        self.controls = {}
        self.deck()

    def register_control(self, key_no, control):
        self.controls[key_no] = control

    def deck(self):
        pass

    def render(self, deck_context):
        deck_context.reset_deck()
        for key_no, control in self.controls.items():
            control.initialize(ControlContext(deck_context, key_no))

    def pressed(self, control_context):
        if control_context.key_no not in self.controls:
            return
        if issubclass(type(self.controls[control_context.key_no]), DeckController):
            return
        self.controls[control_context.key_no].pressed(control_context)

    def released(self, control_context):
        if control_context.key_no not in self.controls:
            return
        if issubclass(type(self.controls[control_context.key_no]), DeckController):
            control_context.deck_context.set_active_deck(self.controls[control_context.key_no])
            return
        self.controls[control_context.key_no].released(control_context)
        control_context.deck_context.pop_active_deck()
