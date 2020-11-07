import datetime
import os

from PIL import ImageFont, Image, ImageDraw

from controls.deck_control import DeckControl


class TimerControl(DeckControl):

    def __init__(self, **kwargs):
        self.start_time = None
        self.end_time = None
        super().__init__(**kwargs)

    def initialize(self, control_context):
        self.render_text(control_context, '00:00:00')

    def pressed(self, control_context):
        if self.start_time is None:
            self.start_time = datetime.datetime.now()
        elif self.end_time is None:
            self.end_time = datetime.datetime.now()
            seconds = (self.end_time - self.start_time).total_seconds()
            m, s = divmod(seconds, 60)
            h, m = divmod(m, 60)
            self.render_text(control_context, f'{int(h):d}:{int(m):02d}:{int(s):02d}')
        else:
            self.start_time = None
            self.end_time = None

    def render_text(self, control_context, text):
        font = ImageFont.truetype(os.path.join(os.path.dirname(__file__), "../assets", 'Roboto-Regular.ttf'), 110)

        image = Image.new("RGB", (512, 512))
        draw = ImageDraw.Draw(image)
        label_w, label_h = draw.textsize('%s' % text, font=font)
        label_pos = ((512 - label_w) // 2, (512 - label_h) // 2)
        draw.text(label_pos, text=text, font=font, fill="white")
        control_context.set_icon_native(image)
