import pytest
from unittest.mock import MagicMock, patch
from lib.DirectoryWatcher import DirectoryWatcher
import asyncio

@pytest.mark.asyncio
async def test_on_created():
    # Mock the async_callback function
    async_callback_mock = MagicMock()
    watcher = DirectoryWatcher(directory='/path/to/watch', async_callback=async_callback_mock)
    
    # Mock asyncio.run to avoid the RuntimeError
    with patch('asyncio.run'):
        # Simulate an on_created event
        event_mock = MagicMock(is_directory=False, src_path='/path/to/file.txt')
        watcher.on_created(event_mock)

    # Ensure that async_callback is called with the correct parameters
    async_callback_mock.assert_called_once_with('/path/to/file.txt')

@pytest.mark.asyncio
async def test_start_and_stop_watching():
    # Mock the observer and async_callback
    observer_mock = MagicMock()
    async_callback_mock = MagicMock()

    # Create a watcher with mocked components
    watcher = DirectoryWatcher(directory='/path/to/watch', async_callback=async_callback_mock)
    watcher.observer = observer_mock

    # Start watching
    watcher_thread = watcher.start_watching()

    # Ensure that observer is scheduled and started
    observer_mock.schedule.assert_called_once()
    observer_mock.start.assert_called_once()

    # Stop watching
    watcher.stop_watching()

    # Ensure that observer is stopped and joined
    observer_mock.stop.assert_called_once()
    observer_mock.join.assert_called_once()

    # Ensure that the watcher thread has completed
    watcher_thread.join()

@pytest.mark.asyncio
async def test_run_once():
    # Create a watcher with mocked components
    watcher = DirectoryWatcher(directory='/path/to/watch', async_callback=lambda x: x)

    # Ensure that run_once does not raise any exceptions
    await watcher.run_once()

# You can add more tests as needed, especially for edge cases and specific behaviors.
