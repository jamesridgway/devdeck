import datetime

from controls.deck_control import DeckControl


class TimerControl(DeckControl):

    def __init__(self, **kwargs):
        self.start_time = None
        self.end_time = None
        super().__init__(**kwargs)

    def initialize(self, control_context):
        control_context.render_text('00:00:00', 120)

    def pressed(self, control_context):
        if self.start_time is None:
            self.start_time = datetime.datetime.now()
        elif self.end_time is None:
            self.end_time = datetime.datetime.now()
            seconds = (self.end_time - self.start_time).total_seconds()
            m, s = divmod(seconds, 60)
            h, m = divmod(m, 60)
            control_context.render_text(f'{int(h):d}:{int(m):02d}:{int(s):02d}', 120)
        else:
            self.start_time = None
            self.end_time = None
