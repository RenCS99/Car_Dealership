import sqlite3
from sqlite3 import Error
import sys
import os
import traceback
import hashlib
import employeemenu
import usermenu

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
    try:
        _conn.close()
        print("Ended")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def startOptions(_conn, _dbFile):
    clearscreen()
    x = 'n'
    eid = 0
    while (x == 'n'):
        print("Welcome to the Main menu!")
        x = input("Are you an employee or a customer? \n")
        if x == "employee" or x == "e":
            print("To return to the main menu type m")
            employeemenu.main(_conn)

    

    print("++++++++++++++++++++++++++++++++++")


def clearscreen():
    os.system('clear')

def main():
    database = r"data/Dealership.db"

    # create a database connection
    conn = openConnection(database)
   
    with conn:
        startOptions(conn, database)

    closeConnection(conn, database)
    



if __name__ == '__main__':
    main()
