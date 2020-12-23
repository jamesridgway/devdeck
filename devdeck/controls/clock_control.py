import threading
from datetime import datetime
from time import sleep

from devdeck_core.controls.deck_control import DeckControl


class ClockControl(DeckControl):

    def __init__(self, key_no, **kwargs):
        super().__init__(key_no, **kwargs)
        self.thread = None
        self.running = False

    def initialize(self):
        self.thread = threading.Thread(target=self._update_display)
        self.running = True
        self.thread.start()

    def _update_display(self):
        while self.running is True:
            with self.deck_context() as context:
                now = datetime.now()

                with context.renderer() as r:
                    r.text(now.strftime("%H:%M"))\
                        .center_horizontally() \
                        .center_vertically(-100) \
                        .font_size(150)\
                        .end()
                    r.text(now.strftime("%a, %d %b")) \
                        .center_horizontally() \
                        .center_vertically(100) \
                        .font_size(75) \
                        .end()
            sleep(1)

    def dispose(self):
        self.running = False
        if self.thread:
            self.thread.join()

