import threading
import os


class FileWatcher:
    def __init__(self, filename, interval, callback):
        self._cached_stamp = os.stat(filename).st_mtime
        self.filename = filename
        self.interval = interval
        self.callback = callback

        self.is_running = True

    def start(self):
        if self.is_running:
            threading.Timer(self.interval, self.start).start()
            stamp = os.stat(self.filename).st_mtime
            if stamp != self._cached_stamp:
                self._cached_stamp = stamp
                self.callback()

    def stop(self):
        self.is_running = False
