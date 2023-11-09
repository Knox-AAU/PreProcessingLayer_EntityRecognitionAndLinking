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
    # Act
    await Db.Insert(
        dbPath, "EntityIndex", queryInformation={"entity": "Morten"}
    )
    sentence = "this is a string"
    await Db.Insert(
        dbPath,
        "sentence",
        queryInformation={
            "filename": "artikel.txt",
            "string": sentence,
            "startindex": 0,
            "endindex": 20,
        },
    )
    await Db.Insert(
        dbPath,
        "entitymention",
        queryInformation={
            "string": sentence,
            "mention": "this",
            "filename": "artikel.txt",
            "startindex": 0,
            "endindex": 5,
        },
    )

    cursorSentence = conn.execute("SELECT * FROM sentence")
    cursorEntityIndex = conn.execute("SELECT * from EntityIndex")
    cursorMentions = conn.execute("SELECT * FROM entitymention")
    rowForComparisonSentence = cursorSentence.fetchall()
    rowForComparisonEntityIndex = cursorEntityIndex.fetchall()
    rowForComparisonMentions = cursorMentions.fetchall()
    print(rowForComparisonMentions[0])
    conn.commit()
    conn.close()
    # Assert
    assert rowForComparisonEntityIndex[0][1] == "Morten"
    assert rowForComparisonSentence[0] == (
        1,
        "this is a string",
        "artikel.txt",
        0,
        20,
    )
    assert rowForComparisonMentions[0] == (1, 1, "this", 0, 5, "artikel.txt")

    # delete the file again
    rmDB()


@pytest.mark.asyncio
async def test_Read():
    # Arrange
    await DBFolderInit()
    await Db.Insert(
        dbPath, "EntityIndex", queryInformation={"entity": "Morten"}
    )
    await Db.Insert(
        dbPath, "EntityIndex", queryInformation={"entity": "Allan"}
    )
    await Db.Insert(
        dbPath, "EntityIndex", queryInformation={"entity": "Vagn-Erik"}
    )
    await Db.Insert(
        dbPath, "EntityIndex", queryInformation={"entity": "Anders"}
    )
    sentence = "this is a string"
    await Db.Insert(
        dbPath,
        "sentence",
        queryInformation={
            "filename": "artikel.txt",
            "string": sentence,
            "startindex": 0,
            "endindex": 20,
        },
    )
    await Db.Insert(
        dbPath,
        "entitymention",
        queryInformation={
            "string": sentence,
            "mention": "this",
            "filename": "artikel.txt",
            "startindex": 0,
            "endindex": 5,
        },
    )
    # Act
    testReadEntityIndexAll = await Db.Read(dbPath, "EntityIndex")
    testReadEntityIndexPred = await Db.Read(dbPath, "EntityIndex", "a")
    testReadEntityIndexPredCapital = await Db.Read(dbPath, "EntityIndex", "A")
    testReadSentenceAll = await Db.Read(dbPath, "sentence")
    testReadSentencePred = await Db.Read(dbPath, "sentence", "a")
    testReadSentencePredCapital = await Db.Read(dbPath, "sentence", "A")
    # Assert
    assert testReadEntityIndexAll[0][0] == 1
    assert testReadEntityIndexAll[0][1] == "Morten"
    assert testReadEntityIndexAll[1][0] == 2
    assert testReadEntityIndexAll[1][1] == "Allan"
    assert testReadEntityIndexAll[2][0] == 3
    assert testReadEntityIndexAll[2][1] == "Vagn-Erik"
    assert testReadEntityIndexAll[3][0] == 4
    assert testReadEntityIndexAll[3][1] == "Anders"
    assert testReadEntityIndexPred[0][0] == 2
    assert testReadEntityIndexPred[0][1] == "Allan"
    assert testReadEntityIndexPred[1][0] == 4
    assert testReadEntityIndexPred[1][1] == "Anders"
    assert testReadEntityIndexPredCapital[0][0] == 2
    assert testReadEntityIndexPredCapital[0][1] == "Allan"
    assert testReadEntityIndexPredCapital[1][0] == 4
    assert testReadEntityIndexPredCapital[1][1] == "Anders"
    assert testReadSentenceAll[0] == (
        1,
        "this is a string",
        "artikel.txt",
        0,
        20,
    )
    assert testReadSentencePred[0] == (
        1,
        "this is a string",
        "artikel.txt",
        0,
        20,
    )
    assert testReadSentencePredCapital[0] == (
        1,
        "this is a string",
        "artikel.txt",
        0,
        20,
    )

    # delete the file again
    rmDB()


@pytest.mark.asyncio
async def test_Update():
    # Arrange
    await DBFolderInit()
    await Db.Insert(
        dbPath, "EntityIndex", queryInformation={"entity": "Morten"}
    )
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
    await Db.Insert(
        dbPath, "EntityIndex", queryInformation={"entity": "Morten"}
    )
    await Db.Insert(
        dbPath, "EntityIndex", queryInformation={"entity": "Alija"}
    )
    await Db.Insert(
        dbPath, "EntityIndex", queryInformation={"entity": "Peter"}
    )
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
