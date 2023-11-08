import sys, sqlite3, pytest, os

sys.path.append(".")
from components import Db


dbFolder = "tests/unit/TestDatabases"

dbPath = dbFolder + "/testdb.db"


async def DBFolderInit():
    if not os.path.isdir(dbFolder):
        os.mkdir(dbFolder)
    await Db.InitializeIndexDB(dbPath)


def rmDB():
    os.remove(dbPath)
    os.rmdir(dbFolder)


@pytest.mark.asyncio
async def test_InitializeIndexDB():
    # Arrange
    await DBFolderInit()
    # Act
    await Db.InitializeIndexDB(dbPath)
    # Assert
    assert os.path.isfile(dbPath) is True
    # delete the file again
    rmDB()


@pytest.mark.asyncio
async def test_Insert():
    # Arrange
    await DBFolderInit()
    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()
    # Act
    await Db.Insert(dbPath, "EntityIndex", "Morten")
    cursor = conn.execute("SELECT * from EntityIndex")
    rowForComparison = cursor.fetchall()
    conn.commit()
    conn.close()
    # Assert
    assert rowForComparison[0][1] == "Morten"
    # delete the file again
    rmDB()


@pytest.mark.asyncio
async def test_Read():
    # Arrange
    await DBFolderInit()
    await Db.Insert(dbPath, "EntityIndex", "Morten")
    await Db.Insert(dbPath, "EntityIndex", "Allan")
    await Db.Insert(dbPath, "EntityIndex", "Vagn-Erik")
    await Db.Insert(dbPath, "EntityIndex", "Anders")
    # Act
    testReadAll = await Db.Read(dbPath, "EntityIndex")
    testReadPred = await Db.Read(dbPath, "EntityIndex", "a")
    testReadPredCapital = await Db.Read(dbPath, "EntityIndex", "A")
    # Assert
    assert testReadAll[0][0] == 1
    assert testReadAll[0][1] == "Morten"
    assert testReadAll[1][0] == 2
    assert testReadAll[1][1] == "Allan"
    assert testReadAll[2][0] == 3
    assert testReadAll[2][1] == "Vagn-Erik"
    assert testReadAll[3][0] == 4
    assert testReadAll[3][1] == "Anders"
    assert testReadPred[0][0] == 2
    assert testReadPred[0][1] == "Allan"
    assert testReadPred[1][0] == 4
    assert testReadPred[1][1] == "Anders"
    assert testReadPredCapital[0][0] == 2
    assert testReadPredCapital[0][1] == "Allan"
    assert testReadPredCapital[1][0] == 4
    assert testReadPredCapital[1][1] == "Anders"

    # delete the file again
    rmDB()


@pytest.mark.asyncio
async def test_Update():
    # Arrange
    await DBFolderInit()
    await Db.Insert(dbPath, "EntityIndex", "Morten")
    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()
    cursor = conn.execute("SELECT * from EntityIndex")
    tableBeforeUpdate = cursor.fetchall()
    # Act
    await Db.Update(dbPath, "EntityIndex", 1, "Soren")
    cursor = conn.execute("SELECT * from EntityIndex")
    tableAfterUpdate = cursor.fetchall()
    # Assert
    assert tableBeforeUpdate[0][0] == 1
    assert tableBeforeUpdate[0][1] == "Morten"
    assert tableAfterUpdate[0][0] == 1
    assert tableAfterUpdate[0][1] == "Soren"
    conn.commit()
    conn.close()
    # delete the file again
    rmDB()


@pytest.mark.asyncio
async def test_Delete():
    # Arrange
    await DBFolderInit()
    await Db.Insert(dbPath, "EntityIndex", "Morten")
    await Db.Insert(dbPath, "EntityIndex", "Alija")
    await Db.Insert(dbPath, "EntityIndex", "Peter")
    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()
    cursor = conn.execute("SELECT * from EntityIndex")
    tableBeforeDelete = cursor.fetchall()  # Gets table before deletion
    # Act
    await Db.Delete(dbPath, "EntityIndex", 2)
    cursor = conn.execute("SELECT * from EntityIndex")
    tableAfterDelete = cursor.fetchall()  # Gets table after deletion
    # Assert
    assert len(tableBeforeDelete) == 3
    assert len(tableAfterDelete) == 2
    assert (
        tableBeforeDelete[0][1] == "Morten"
        and tableBeforeDelete[1][1] == "Alija"
        and tableBeforeDelete[2][1] == "Peter"
    )
    assert (
        tableAfterDelete[0][1] == "Morten"
        and tableAfterDelete[1][1] == "Peter"
    )
    conn.commit()
    conn.close()
    # delete the file again
    rmDB()


@pytest.mark.asyncio
async def test_SortDB():
    # Arrange
    await DBFolderInit()
    await Db.Insert(dbPath, "EntityIndex", "Morten Kjær")
    await Db.Insert(dbPath, "EntityIndex", "Alija")
    await Db.Insert(dbPath, "EntityIndex", "Beter")
    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()
    # Act
    await Db.SortDB(dbPath, "EntityIndex")
    cursor = conn.execute("SELECT * from EntityIndex")
    sortedTable = cursor.fetchall()
    # Assert
    assert sortedTable[0][1] == "Alija"
    assert sortedTable[1][1] == "Beter"
    assert sortedTable[2][1] == "Morten Kjær"
    conn.commit()
    conn.close()
    # delete the file again
    rmDB()
