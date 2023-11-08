import threading
import os


class FileWatcher:
    def __init__(self, filename, interval, callback):
        self._cached_stamp = 0
        self.filename = filename
        self.interval = interval
        self.callback = callback

    def start(self):
        threading.Timer(self.interval, self.start).start()
        stamp = os.stat(self.filename).st_mtime
        if stamp != self._cached_stamp:
            self._cached_stamp = stamp
            self.callback()
