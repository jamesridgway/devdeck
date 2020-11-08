import os
from subprocess import Popen, DEVNULL

from controls.deck_control import DeckControl


class CommandControl(DeckControl):
    def initialize(self):
        with self.deck_context() as context:
            context.set_icon(self.settings['icon'])

    def pressed(self):
        Popen(self.settings['command'], stdout=DEVNULL, stderr=DEVNULL)
