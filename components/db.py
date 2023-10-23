import sqlite3

async def InitializeIndexDB():
    # Connect to sqlite database
    conn = sqlite3.connect('DB.db')
    # cursor object
    cursor = conn.cursor()
    # # drop query
    # cursor.execute("DROP TABLE IF EXISTS STUDENT")
    # create query
    #IF NOT EXISTS checks whether table exists. Autoincrement increments the id of new rows automatically
    query = """CREATE TABLE IF NOT EXISTS EntityIndex(
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            NAME CHAR(20) NOT NULL
            )"""
    cursor.execute(query)

    # commit and close
    conn.commit()
    conn.close()

def Insert(tableName,entity):
    # Connect to sqlite database
    conn = sqlite3.connect('DB.db')
    # cursor object
    cursor = conn.cursor()
    # stuff that does query
    query = ("INSERT INTO {} (NAME) "
             "VALUES (:NAME)").format(tableName)
    params = {
        'NAME': entity
    }
    print("The query to run: ", query)

    cursor.execute(query, params)

    # commit and close
    conn.commit()
    conn.close()

def Read(tableName):
        # Connect to sqlite database
    conn = sqlite3.connect('DB.db')
    # cursor object
    cursor = conn.cursor()
    # fetches all entries in table
    cursor = conn.execute(("SELECT * from {}").format(tableName))
    rowsInTable = cursor.fetchall() #List of each row contained in tuples e.g. [(id, name), (id2, name2), ..., etc]
    # commit and close
    conn.commit()
    conn.close()
    return rowsInTable

def Update(tableName, indexID, updatedName):
    # Connect to sqlite database
    conn = sqlite3.connect('DB.db')
    # cursor object
    cursor = conn.cursor()
    # updates row in table
    cursor = conn.execute(("UPDATE {} set NAME = '{}' where ID = '{}'").format(tableName, updatedName, indexID))
    # commit and close
    conn.commit()
    conn.close()

def Delete(tableName, indexID):
    # Connect to sqlite database
    conn = sqlite3.connect('DB.db')
    # cursor object
    cursor = conn.cursor()
    # deletes row from table
    conn.execute(("DELETE from {} where ID = '{}';").format(tableName, indexID))
    # commit and close
    conn.commit()
    conn.close()

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
    
