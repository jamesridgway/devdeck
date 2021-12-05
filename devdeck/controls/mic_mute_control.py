from asyncio import sleep
from asyncio.events import get_event_loop
from asyncio.tasks import Task
import logging
import os

import pulsectl
import pulsectl_asyncio

from devdeck_core.controls.deck_control import DeckControl


class MicMuteControl(DeckControl):
    event_listener: Task
    def __init__(self, key_no, **kwargs):
        self.loop = get_event_loop()
        self.pulse = None
        self.__logger = logging.getLogger('devdeck')
        super().__init__(key_no, **kwargs)

    async def _init(self):
        if self.pulse is None:
            self.pulse = pulsectl_asyncio.PulseAsync('MicMuteControl')
            await self.pulse.connect()
        self.event_listener = self.loop.create_task(self._listen_mute())
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
        async for event in self.pulse.subscribe_events('source'):
            if event.t == pulsectl.PulseEventTypeEnum.change:
                await self._update_display()

    def initialize(self):
        self.loop.create_task(self._init())

    def pressed(self):
        self.loop.create_task(self._handle_mute())

    async def _handle_mute(self):
        mic = await self._get_source()
        await self.pulse.source_mute(mic.index, mute=(not mic.mute))
        await self._update_display()

    async def _get_source(self):
        sources = await self.pulse.source_list()
        server_info = await self.pulse.server_info()
        default_source_name = server_info.default_source_name
        return next((source for source in sources if source.name == default_source_name), None)

    async def _update_display(self):
        with self.deck_context() as context:
            mic = await self._get_source()
            with context.renderer() as r:
                try:
                    match mic.mute:
                        case 0:
                            r.image(os.path.join(os.path.dirname(__file__),
                                                "../assets/font-awesome", 'microphone.png')).end()
                        case 1:
                            r.image(os.path.join(os.path.dirname(__file__),
                                    "../assets/font-awesome", 'microphone-mute.png')).end()
                except AttributeError:
                    r \
                        .text('MIC \nNOT FOUND') \
                        .color('red') \
                        .center_vertically() \
                        .center_horizontally() \
                        .font_size(85) \
                        .text_align('center') \
                        .end()

    def settings_schema(self):
        return {
            'microphone': {
                'type': 'string'
            }
        }
