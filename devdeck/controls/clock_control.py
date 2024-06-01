import asyncio
from datetime import datetime

from devdeck_core.controls.deck_control import DeckControl


class ClockControl(DeckControl):

    def __init__(self, key_no, **kwargs):
        super().__init__(key_no, **kwargs)
        self.running = False

    async def initialize(self):
        asyncio.create_task(self.periodic_task(1, self._update_display))
        self.running = True

    async def periodic_task(self, interval, task):
        while self.running is True:
            await task()
            await asyncio.sleep(interval)

    async def _update_display(self):
        with self.deck_context() as context:
            now = datetime.now()

            with context.renderer() as r:
                r.text(now.strftime("%H:%M")) \
                    .center_horizontally() \
                    .center_vertically(-100) \
                    .font_size(150) \
                    .end()
                r.text(now.strftime("%a, %d %b")) \
                    .center_horizontally() \
                    .center_vertically(100) \
                    .font_size(75) \
                    .end()

    async def dispose(self):
        self.running = False
        if self.thread:
            self.thread.join()
