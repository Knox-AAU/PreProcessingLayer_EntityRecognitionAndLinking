# directory_watcher.py
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class DirectoryWatcher:
    def __init__(self, directory, callback):
        self.directory = directory
        self.callback = callback
        self.is_watching = True
        self.event_handler = FileSystemEventHandler()
        self.event_handler.on_created = self.on_created
        self.observer = Observer()
        self.observer.schedule(self.event_handler, path=self.directory, recursive=False)

    def on_created(self, event):
        if event.is_directory:
            return
        # Call your callback method here
        self.callback(event.src_path)

    def start_watching(self):
        # Define a thread target function
        def run_observer():
            self.observer.start()
            try:
                while self.is_watching:
                    pass
            except KeyboardInterrupt:
                pass
            finally:
                self.stop_watching()

        # Create and start the thread
        watcher_thread = threading.Thread(target=run_observer)
        watcher_thread.start()

        # Return the thread in case you want to manage it externally
        return watcher_thread

    def stop_watching(self):
        self.is_watching = False
        self.observer.stop()
        self.observer.join()
