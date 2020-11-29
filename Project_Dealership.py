import sqlite3
from sqlite3 import Error

def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def startOptions(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Are you interested in buying or selling a car: ")

    

    print("++++++++++++++++++++++++++++++++++")

def main():
    database = r"data/Dealership.db"

    # create a database connection
    conn = openConnection(database)
    with conn:
        startOptions(conn, database)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
