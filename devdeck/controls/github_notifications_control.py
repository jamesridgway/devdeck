import os
import threading
from subprocess import Popen, DEVNULL
from time import sleep
from typing import Any, Dict

import requests as requests
from devdeck_core.controls.deck_control import DeckControl


class GithubNotificationsControl(DeckControl):
    def __init__(self, key_no: int, **kwargs) -> None:
        super().__init__(key_no, **kwargs)
        self.thread = None
        self.running = False
        self.last_url = None

    def initialize(self) -> None:
        self.thread = threading.Thread(target=self._update_loop)
        self.running = True
        self.thread.start()

    def pressed(self) -> None:
        if self.last_url is None:
            self._update_display()
            return

        browser = self.settings.get('browser') or 'firefox'
        Popen([browser, self.last_url], stdout=DEVNULL, stderr=DEVNULL)

        # Wait 5 seconds for the browser to load the page before refreshing the display.
        sleep(5)
        self._update_display()

    def get_notifications(self) -> Dict[str, Any]:
        assert self.settings['token'], 'Please specify your Github API token in `settings.yml`'
        headers = {
            'Authorization': f"token {self.settings['token']}",
            'User-Agent': 'devdeck',
        }
        return requests.get('https://api.github.com/notifications', headers=headers).json()

    def _update_display(self) -> None:
        notifications = self.get_notifications()
        count = len(notifications)
        alert_color = self.settings.get('color') or '#ff2b2b'
        color = alert_color if count > 0 else '#ffffff'

        self.last_url = notifications[0]['subject']['url'] \
            .replace('api.', '').replace('repos/', '').replace('pulls/', 'pull/') \
            if count > 0 else None

        with self.deck_context() as context:
            with context.renderer() as r:
                r.image(os.path.join(os.path.dirname(__file__), "../assets/font-awesome", 'github.png')) \
                    .width(240) \
                    .height(240) \
                    .center_horizontally() \
                    .y(225) \
                    .end()

                r.text(str(count)) \
                    .center_horizontally() \
                    .center_vertically(-175) \
                    .font_size(150) \
                    .color(color) \
                    .end()

    def _update_loop(self) -> None:
        while self.running is True:
            self._update_display()
            sleep(self.settings.get('refresh_seconds') or 60)

    def dispose(self) -> None:
        self.running = False
        if self.thread:
            self.thread.join()
