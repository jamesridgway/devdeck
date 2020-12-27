from subprocess import Popen, DEVNULL

from devdeck_core.controls.deck_control import DeckControl


class CommandControl(DeckControl):
    def initialize(self):
        with self.deck_context() as context:
            with context.renderer() as r:
                r.image(self.settings['icon']).end()

    def pressed(self):
        Popen(self.settings['command'], stdout=DEVNULL, stderr=DEVNULL)
