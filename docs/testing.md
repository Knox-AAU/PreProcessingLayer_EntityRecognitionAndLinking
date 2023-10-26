# Testing

For testing purposes, we are using `PyTest` and `PyTest-Asyncio`.
Parameters for PyTest are automatically appended and can be found in the `pyproject.toml` file.

## PyTest

All the necessary requirements for testing is already in the requirements.txt file.
Testing the software should already be available by running `pytest` or `python3 -m pytest` in the terminal.

### Async functions

Asynchronous functions can be tested by utilizing the plugin `PyTest-Asyncio`. Simply mark your test function with
`@pytest.mark.asyncio` to tell pytest that the function is asynchronous.

## Folder Structure

All tests are located in the **_/tests_** folder. From this folder we branch out to the different types of testing; integration, unit etc.
Simply create a test_XXX.py file, and import PyTest at the top level to begin testing.

## Examples

Here are some example tests:

```PYTHON
def test_GetText_fileExists():
    with open("test_article_file.txt", "w") as testFile:
        testFile.write("This is a testfile")

    testText = GetSpacyData.GetText("test_article_file.txt")
    assert testText == "This is a testfile"
```

### Async

```PYTHON
@pytest.mark.asyncio
async def test_InitializeIndexDB():
    # Arrange
    dbFolder = "tests/unit/temp"
    os.mkdir(dbFolder)
    dbPath = dbFolder + "/testdb.db"
    # Act
    await Db.InitializeIndexDB(dbPath)
    # Assert
    assert os.path.isfile(dbPath) == True
    # delete the file again
    rmDB()
```

## Known issues

### Module not found

Sometimes pytest can't find modules etc. This is most likely due to relative paths.
the fix is adding the following to the top of your test.py file:

```PYTHON
import sys
sys.path.append(".")
```

After these two lines, `from XXX import XXX` should work.
