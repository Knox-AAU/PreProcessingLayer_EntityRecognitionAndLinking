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
    # IF NOT EXISTS checks whether table exists. Autoincrement increments the id of new rows automatically
    query = """CREATE TABLE IF NOT EXISTS EntityIndex(
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            NAME CHAR(20) NOT NULL
            )"""
    cursor.execute(query)

    # commit and close
    conn.commit()
    conn.close()


async def Insert(dbPath, tableName, entity):
    # Connect to sqlite database
    conn = sqlite3.connect(dbPath)
    # cursor object
    cursor = conn.cursor()
    # stuff that does query
    query = ("INSERT INTO {} (NAME) " "VALUES (:NAME)").format(tableName)
    params = {"NAME": entity}

    cursor.execute(query, params)

    last_inserted_id = cursor.lastrowid

    # commit and close
    conn.commit()
    conn.close()
    
    return last_inserted_id


async def Read(dbPath, tableName):
    # Connect to sqlite database
    conn = sqlite3.connect(dbPath)
    # cursor object
    cursor = conn.cursor()
    # fetches all entries in table
    cursor = conn.execute(("SELECT * from {}").format(tableName))
    rowsInTable = (
        cursor.fetchall()
    )  # List of each row contained in tuples e.g. [(id, name), (id2, name2), ..., etc]
    # commit and close
    conn.commit()
    conn.close()
    return rowsInTable


async def Update(dbPath, tableName, indexID, updatedName):
    # Connect to sqlite database
    conn = sqlite3.connect(dbPath)
    # cursor object
    cursor = conn.cursor()
    # updates row in table
    cursor = conn.execute(
        ("UPDATE {} set NAME = '{}' where ID = '{}'").format(
            tableName, updatedName, indexID
        )
    )
    # commit and close
    conn.commit()
    conn.close()


async def Delete(dbPath, tableName, indexID):
    # Connect to sqlite database
    conn = sqlite3.connect(dbPath)
    # cursor object
    cursor = conn.cursor()
    # deletes row from table
    conn.execute(("DELETE from {} where ID = '{}';").format(tableName, indexID))
    # commit and close
    conn.commit()
    conn.close()

async def SortDB(dbPath, tableName):
# Connect to sqlite database
    conn = sqlite3.connect(dbPath)
    # cursor object
    cursor = conn.cursor()
    
    # Query to fetch data sorted by NAME
    query = "SELECT * FROM {} ORDER BY NAME".format(tableName)
    cursor.execute(query)
    
    # Fetch all rows
    rows = cursor.fetchall()
    
    # Query to drop the old table if it exists
    query = ("DROP TABLE IF EXISTS {}").format(tableName)
    cursor.execute(query)
    #Creates the table anew to keep incrementing from 1, 2, 3 etc in ID
    await InitializeIndexDB(dbPath)
    # commit and close
    conn.commit()
    conn.close()

    # Insert the sorted rows back into the table
    for row in rows:
        await Insert(dbPath, tableName, row[1])  # assuming NAME is the second column

# the following 15 lines of code can be replaced by "IF NOT EXISTS" in the sql query
# def TableExists(tableName):
#     conn = sqlite3.connect('DB.db')
#     curr = conn.cursor()
#     # check if table exists
#     qString = ("""SELECT tableName FROM sqlite_master WHERE type='table'
#     AND tableName='{}'; """).format(tableName)
#     contains = False
#     try:
#         listOfTables = curr.execute(
#         qString).fetchall()
#         conn.commit()
#         conn.close()
#         if listOfTables == []:
#             contains = False
#         else:
#             contains = True
#     except:
#         print("empty")
#     return contains
