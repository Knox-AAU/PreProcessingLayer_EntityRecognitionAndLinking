import os
import time
import pytest
from lib.FileWatcher import FileWatcher


class TestFileWatcher:
    TEST_INTERVAL = 1

    @pytest.fixture
    def test_file(self, tmpdir):
        test_file = tmpdir.join("test_file.txt")
        with open(test_file, 'w') as f:
            f.write("Test content")
        return str(test_file)

    def test_file_watcher_calls_callback_on_change(self, test_file):
        callback_called = False

        def test_callback():
            nonlocal callback_called
            callback_called = True

        watcher = FileWatcher(test_file, self.TEST_INTERVAL, test_callback)
        watcher.start()

        time.sleep(self.TEST_INTERVAL / 2)  # Wait for watcher to start

        # Modify the test file
        with open(test_file, 'a') as f:
            f.write("Additional content")

        time.sleep(self.TEST_INTERVAL * 2)  # Wait for watcher to detect changes

        assert callback_called

    def test_file_watcher_does_not_call_callback_if_no_change(self, test_file):
        callback_called = False

        def test_callback():
            nonlocal callback_called
            callback_called = True

        watcher = FileWatcher(test_file, self.TEST_INTERVAL, test_callback)
        watcher.start()

        time.sleep(self.TEST_INTERVAL * 2)  # Wait for watcher to complete at least one cycle
        print(callback_called)
        assert not callback_called