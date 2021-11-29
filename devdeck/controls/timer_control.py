from asyncio.events import get_event_loop
from datetime import datetime
import os
import enum
import asyncio
from time import sleep

from devdeck_core.controls.deck_control import DeckControl


class TimerState(enum.Enum):
    RUNNING = 1
    STOPPED = 2
    RESET = 3


class TimerControl(DeckControl):

    def __init__(self, key_no, **kwargs):
        self.loop = get_event_loop()
        self.start_time: datetime = None
        self.end_time: datetime = None
        self.state = TimerState.RESET
        super().__init__(key_no, ** kwargs)

    def initialize(self):
        self.loop.create_task(self._update_display())
        with self.deck_context() as context:
            with context.renderer() as r:
                r.image(os.path.join(os.path.dirname(__file__),
                        "../assets/font-awesome", 'stopwatch.png')).end()

    def pressed(self):
        match self.state:
            case TimerState.RESET:
                self.start_time = datetime.now()
                self.end_time = None
                self.state = TimerState.RUNNING
            case TimerState.RUNNING:
                if not self.start_time:
                    raise Exception("how did you get here?")
                self.end_time = datetime.now()
                self.state = TimerState.STOPPED
            case TimerState.STOPPED:
                self.start_time = self.end_time = None
                self.state = TimerState.RESET

    async def _update_display(self, repeat=True):
        while True:
            with self.deck_context() as context:
                with context.renderer() as r:
                    match self.state:
                        case TimerState.RUNNING:
                            r.text(TimerControl.time_diff_to_str(datetime.now() - self.start_time))\
                                .font_size(120)\
                                .color('red')\
                                .center_vertically().center_horizontally().end()
                        case TimerState.STOPPED:
                            r.text(TimerControl.time_diff_to_str(self.end_time - self.start_time))\
                                .font_size(120)\
                                .color('yellow')\
                                .center_vertically().center_horizontally().end()
                        case _:
                            r.image(os.path.join(
                                os.path.join(os.path.dirname(__file__), "../assets/font-awesome", 'stopwatch.png'))).end()
            if repeat:
                await asyncio.sleep(0.1)
            else:
                return

    @staticmethod
    def time_diff_to_str(diff):
        total_seconds = diff.total_seconds()
        minutes, seconds = divmod(total_seconds, 60)
        hours, minutes = divmod(minutes, 60)
        if total_seconds < 60:
            return f'{int(seconds):02d}'
        elif total_seconds < 3600:
            return f'{int(minutes):02d}:{int(seconds):02d}'
        return f'{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}'
