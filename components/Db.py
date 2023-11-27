import sqlite3
import sys
import os

sys.path.append(".")


async def InitializeIndexDB(dbPath):
    # Connect to sqlite database
    folder = os.path.dirname(dbPath)
    if not os.path.exists(folder):
        os.mkdir(folder)
    conn = sqlite3.connect(dbPath)
    # cursor object
    cursor = conn.cursor()
    # # drop query
    # cursor.execute("DROP TABLE IF EXISTS STUDENT")
    # create query
    # IF NOT EXISTS checks whether table exists.
    # Autoincrement increments the id of new rows automatically
    createEntityIndexTable = """CREATE TABLE IF NOT EXISTS EntityIndex(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name CHAR(20) NOT NULL
            )"""
    createSentenceTable = """CREATE TABLE IF NOT EXISTS sentence(
            "sid" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            "fileName" varchar NOT NULL,
            "text" varchar,
            "startIndex" int NOT NULL,
            "endIndex" int NOT NULL
            )"""
    createEntityMentionsTable = """CREATE TABLE IF NOT EXISTS entitymention(
            "eid" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            "sid" int references sentence(sid),
            "fileName" varchar NOT NULL,
            "name" varchar,
            "startIndex" int NOT NULL,
            "endIndex" int NOT NULL,
            "label" varchar NOT NULL,
            "type" varchar NOT NULL,
            "iri" varchar
            )"""
    cursor.execute(createEntityIndexTable)
    cursor.execute(createEntityMentionsTable)
    cursor.execute(createSentenceTable)

    # commit and close
    conn.commit()
    conn.close()


async def Insert(dbPath, tableName, queryInformation):
    # Connect to sqlite database
    conn = sqlite3.connect(dbPath)
    # cursor object
    cursor = conn.cursor()
    # stuff that does query

    if tableName == "sentence":
        query = f"INSERT INTO {tableName} (fileName, text, startIndex, endIndex) VALUES (?, ?, ?, ?)"
        queryInfo = (
            queryInformation["fileName"],
            queryInformation["text"],
            queryInformation["startIndex"],
            queryInformation["endIndex"],
        )
        cursor.execute(query, queryInfo)
    elif tableName == "entitymention":
        query = f"INSERT INTO {tableName} (sid, name, fileName, startIndex, endIndex, label, type, iri) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        queryInfo = (
            queryInformation.sid,
            queryInformation.name,
            queryInformation.fileName,
            queryInformation.startIndex,
            queryInformation.endIndex,
            queryInformation.label,
            queryInformation.type,
            queryInformation.iri,
        )
        cursor.execute(query, queryInfo)
    else:
        query = f"INSERT INTO {tableName} (NAME) VALUES (?)"
        cursor.execute(query, (queryInformation["entity"],))

    last_inserted_id = cursor.lastrowid

    # commit and close
    conn.commit()
    conn.close()

    return last_inserted_id


async def Read(dbPath, tableName, searchPred=""):
    # Connect to sqlite database
    conn = sqlite3.connect(dbPath)
    # cursor object
    cursor = conn.cursor()
    # fetches all entries in table
    if searchPred is None:
        cursor = conn.execute((f"SELECT * from {tableName}"))
        rowsInTable = cursor.fetchall()
        # List of each row contained in tuples
        # e.g. [(id, name), (id2, name2), ..., etc]
        # commit and close
        conn.commit()
        conn.close()
        return rowsInTable
    if tableName == "EntityIndex" and searchPred is not None:
        cursor = conn.execute(
            f"SELECT * from {tableName} WHERE name LIKE ?", (f"{searchPred}%",)
        )
        rowsInTable = cursor.fetchall()
        conn.commit()
        conn.close()
        return rowsInTable
    elif tableName == "sentence" and searchPred is not None:
        cursor = conn.execute(
            (f"SELECT * FROM {tableName} WHERE fileName = '%{searchPred}%'")
        )
    elif tableName == "entitymention" and searchPred is not None:
        cursor = conn.execute(
            (f"SELECT * FROM {tableName} WHERE fileName = '%{searchPred}%'")
        )
    rowsInTable = cursor.fetchall()
    conn.commit()
    conn.close()
    return rowsInTable

async def JoinOnFileName(dbPath, selects, table1, table2, commonKey, fileName):
    conn = sqlite3.connect(dbPath)
    # cursor object
    cursor = conn.cursor()

    joinedSelects = ",".join(selects)

    query = f"SELECT {joinedSelects} FROM {table1,table2} WHERE {table1}.{commonKey} = {table2}.{commonKey} AND {table1}.fileName = '{fileName}'"
    
    cursor = conn.execute(query)
    
    rowsInTable = cursor.fetchall()
    conn.commit()
    conn.close()
    return rowsInTable

async def Update(dbPath, tableName, indexID, updatedName):
    # Connect to sqlite database
    conn = sqlite3.connect(dbPath)
    # cursor object
    cursor = conn.cursor()

    # update row in table
    if tableName == "sentence":
        query = f"UPDATE {tableName} SET string = '{updatedName}' WHERE sid = '{indexID}'"
    elif tableName == "entitymention":
        query = f"UPDATE {tableName} SET mention = '{updatedName}' WHERE eid = '{indexID}'"
    else:
        query = f"UPDATE {tableName} SET name = '{updatedName}' WHERE id = '{indexID}'"

    cursor.execute(query)

    # commit and close
    conn.commit()
    conn.close()


async def Delete(dbPath, tableName, indexID):
    # Connect to sqlite database
    conn = sqlite3.connect(dbPath)
    # cursor object
    cursor = conn.cursor()

    # delete row from table
    if tableName == "sentence":
        query = f"DELETE FROM {tableName} WHERE sid = '{indexID}'"
    elif tableName == "entitymention":
        query = f"DELETE FROM {tableName} WHERE eid = '{indexID}'"
    else:
        query = f"DELETE FROM {tableName} WHERE id = '{indexID}'"

    cursor.execute(query)

    # commit and close
    conn.commit()
    conn.close()

