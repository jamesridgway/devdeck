import os
from subprocess import Popen, DEVNULL

from controls.deck_control import DeckControl


class CommandControl(DeckControl):
    def initialize(self, control_context):
        control_context.set_icon(self.settings['icon'])

    def pressed(self, control_context):
        Popen(self.settings['command'], stdout=DEVNULL, stderr=DEVNULL)
