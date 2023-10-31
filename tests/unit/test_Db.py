import sys, sqlite3, pytest, os
sys.path.append(".")
from components import Db


dbFolder = "tests/unit/TestDatabases"

dbPath = dbFolder + "/testdb.db"


async def DBFolderInit():
    os.mkdir(dbFolder)
    await Db.InitializeIndexDB(dbPath)


def rmDB():
    os.remove(dbPath)
    os.rmdir(dbFolder)


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
    # Arrrange
    await DBFolderInit()
    await Db.Insert(dbPath, "EntityIndex", "Morten")
    # Act
    testRead = await Db.Read(dbPath, "EntityIndex")
    # Assert
    assert testRead[0][0] == 1
    assert testRead[0][1] == "Morten"
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
    assert tableAfterDelete[0][1] == "Morten" and tableAfterDelete[1][1] == "Peter"
    conn.commit()
    conn.close()
    #delete the file again
    rmDB()


@pytest.mark.asyncio
async def test_SortDB():
    #Arrange
    dbPath = 'tests/unit/TestDatabases/testdb.db'
    await Db.InitializeIndexDB(dbPath)
    await Db.Insert('tests/unit/TestDatabases/testdb.db', 'EntityIndex', 'Morten Kjær')
    await Db.Insert('tests/unit/TestDatabases/testdb.db', 'EntityIndex', 'Alija')
    await Db.Insert('tests/unit/TestDatabases/testdb.db', 'EntityIndex', 'Beter')
    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()
    #Act
    await Db.SortDB(dbPath, 'EntityIndex')
    cursor = conn.execute("SELECT * from EntityIndex")
    sortedTable = cursor.fetchall()
    #Assert
    assert sortedTable[0][1] == 'Alija'
    assert sortedTable[1][1] == 'Beter'
    assert sortedTable[2][1] == 'Morten Kjær'
    conn.commit()
    conn.close()
    #delete the file again
    rmDB()


