import asyncio
from asyncio.events import get_event_loop
import threading
from datetime import datetime
from asyncio import sleep

from devdeck_core.controls.deck_control import DeckControl


class ClockControl(DeckControl):

    def __init__(self, key_no: int, **kwargs):
        self.loop = get_event_loop()
        super().__init__(key_no, **kwargs)

    def initialize(self):
        self.loop.create_task(self._update_display())

    async def _update_display(self):
        while True:
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
            await sleep(1)
