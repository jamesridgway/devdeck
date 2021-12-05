from asyncio import sleep
from asyncio.events import get_event_loop
from asyncio.tasks import Task
import logging
import os

import pulsectl
import pulsectl_asyncio

from devdeck_core.controls.deck_control import DeckControl


class VolumeMuteControl(DeckControl):
    event_listener: Task

    def __init__(self, key_no, **kwargs):
        self.loop = get_event_loop()
        self.pulse = None
        self.__logger = logging.getLogger('devdeck')
        super().__init__(key_no, **kwargs)

    async def _init(self):
        if self.pulse is None:
            self.pulse = pulsectl_asyncio.PulseAsync('VolumeMuteControl')
            await self.pulse.connect()
        self.loop.create_task(self._listen_mute())
        self.loop.create_task(self._connection_watcher())
        self.loop.create_task(self._update_display())
    
    async def _connection_watcher(self):
        while True:
            while not self.pulse.connected:
                self.event_listener.cancel()
                try:
                    self.pulse.connect()
                    self._update_display()
                except:
                    await sleep(5)

            await sleep(10)

    async def _listen_mute(self):
        async for event in self.pulse.subscribe_events('sink'):
            if event.t == pulsectl.PulseEventTypeEnum.change:
                await self._update_display()

    def initialize(self):
        self.loop.create_task(self._init())

    def pressed(self):
        self.loop.create_task(self._handle_mute())

    async def _handle_mute(self):
        output = await self._get_sink()
        await self.pulse.sink_mute(output.index, mute=(not output.mute))
        await self._update_display()

    async def _get_sink(self):
        outputs = await self.pulse.sink_list()
        server_info = await self.pulse.server_info()
        default_sink_name = server_info.default_sink_name
        return next((output for output in outputs if output.name == default_sink_name), None)

    async def _update_display(self):
        with self.deck_context() as context:
            sink = await self._get_sink()
            with context.renderer() as r:
                try:
                    match sink.mute:
                        case 0:
                            r.image(os.path.join(os.path.dirname(__file__),
                                                    "../assets/font-awesome", 'volume-up-solid.png')).end()
                        case 1:
                            r.image(os.path.join(os.path.dirname(__file__),
                                    "../assets/font-awesome", 'volume-off-solid.png')).end()
                except AttributeError:
                    r \
                        .text('OUTPUT \nNOT FOUND') \
                        .color('red') \
                        .center_vertically() \
                        .center_horizontally() \
                        .font_size(85) \
                        .text_align('center') \
                        .end()
