# [Directory Watcher](https://github.com/Knox-AAU/PreProcessingLayer_EntityRecognitionAndLinking/blob/main/lib/DirectoryWatcher.py)
The pipeline starts when a new file is placed in a watched folder by pipeline part A. The Directory Watcher's responsibility is to call a callback function when a new file is created in the watched folder.

## Features
- [watchdog](https://pypi.org/project/watchdog/) for file events
- Async callback support
- [Threading](https://docs.python.org/3/library/threading.html)

## Overview

The `DirectoryWatcher` provides a simple way to monitor a specified directory for file creation events and execute asynchronous callbacks in response. It utilizes the [watchdog](https://pypi.org/project/watchdog/) library for filesystem monitoring and integrates with [asyncio](https://docs.python.org/3/library/asyncio.html) for handling asynchronous tasks. Furthermore the `DirectoryWatcher` uses [threading](https://docs.python.org/3/library/threading.html).

> **_NOTE:_**  [Threading](https://docs.python.org/3/library/threading.html) is used to avoid blocking the main thread's code from executing.


## Example usage
```python
# Importing
from lib.DirectoryWatcher import DirectoryWatcher

dirPath = "some/path/to/a/directory"

# Setup
async def newFileCreated(file_path: str):
    print("New file created in " + file_path)


dirWatcher = DirectoryWatcher(
    directory=dirPath, async_callback=newFileCreated
)

# A fast API event function running on startup
@app.on_event("startup")
async def startEvent():
    dirWatcher.start_watching()

# A fast API event function running on shutdown
@app.on_event("shutdown")
def shutdown_event():
    dirWatcher.stop_watching()
```

> **_NOTE:_**  The fast API event functions are not needed to use the `Directory Watcher`


## Methods
```python
def __init__(self, directory, async_callback):
```
### Parameters:
- **directory** (str): A path to the directory you want to watch ie. `some/path/to/a/directory`
- **async_callback** (function): An async callback function to be called when a new file is created in the **directory**. This function should accept a single parameter, which is the path of the created file.

```python
def start_watching(self) -> threading.Thread:
```

```python
def stop_watching(self):
```
