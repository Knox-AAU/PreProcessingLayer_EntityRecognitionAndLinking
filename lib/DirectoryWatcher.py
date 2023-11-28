import threading
import asyncio
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class DirectoryWatcher:
    def __init__(self, directory, async_callback):
        self.directory = directory
        self.async_callback = async_callback
        self.is_watching = True
        self.event_handler = FileSystemEventHandler()
        self.event_handler.on_created = self.on_created
        self.observer = Observer()

    def on_created(self, event):
        if event.is_directory:
            return
        # Call the asynchronous callback using asyncio.run
        asyncio.run(self.async_callback(event.src_path))

    def start_watching(self):
        # Define a thread target function
        def run_observer():
            self.observer.schedule(
                self.event_handler, path=self.directory, recursive=False
            )
            self.observer.start()
            try:
                while self.is_watching:
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    loop.run_until_complete(self.run_once())
            except KeyboardInterrupt:
                pass
            finally:
                self.stop_watching()

        # Create and start the thread
        watcher_thread = threading.Thread(target=run_observer)
        watcher_thread.start()

        # Return the thread in case you want to manage it externally
        return watcher_thread

    async def run_once(self):
        await asyncio.sleep(1)  # Adjust as needed

    def stop_watching(self):
        self.is_watching = False
        self.observer.stop()
        self.observer.join()
