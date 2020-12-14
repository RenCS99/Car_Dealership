import sqlite3
from sqlite3 import Error
import sys
import os
import traceback
import hashlib
import employeemenu
import customer

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

def startOptions(_conn):
    clearscreen()
    
    while True:
        print("Welcome to the Main menu!")
        x = input("Are you an employee or a customer? \n")
        if x.lower() == "employee" or x.lower() == "e":
            clearscreen()
            eID = input("Please Enter your employee ID: ")
            if employeemenu.verification(_conn,eID):
                clearscreen()
                print("Success")
                employeemenu.main(_conn)
                print("Failed")
        elif x.lower() == "customer" or x.lower() == "c":
            clearscreen()
            customer.main(_conn)
            sys.exit(0)
        else:
            print("Invalid Input. Press Enter to try again. \n")

def clearscreen():
    os.system('clear')

def main():
    database = r"data/Dealership.db"

    # create a database connection
    conn = openConnection(database)
   
    with conn:
        startOptions(conn)

    closeConnection(conn, database)
    



if __name__ == '__main__':
    main()
