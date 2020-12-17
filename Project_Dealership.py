import sqlite3
from sqlite3 import Error
import sys
import os
import traceback
import hashlib
import employeemenu
import customer
import csv

def openConnection(_dbFile):
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        
    except Error as e:
        print(e)

   

    return conn

def closeConnection(_conn, _dbFile):
    try:
        _conn.close()
        
    except Error as e:
        print(e)

   
def startOptions(_conn):
    print("Welcome to the Main menu!")
    while True:
        x = input("Are you an employee or a customer? \n")
        if x.lower() == "employee" or x.lower() == "e":
            clearscreen()
            eID = input("Please Enter your employee ID: ")
            if employeemenu.verification(_conn,eID):
                clearscreen()
                print("Success")
                employeemenu.main(_conn)
                sys.exit(0)
            else:    
                print("Failed Try Again.")
                employeemenu.verification(_conn,eID)
                
        elif x.lower() == "customer" or x.lower() == "c":
            print("Welcome!")
            customer.main(_conn)
            sys.exit(0)
        else:
            print("Invalid Input. Press Enter to try again. \n")
            print("Hit Enter to retry: ")
            zxc = input()

def clearscreen():
    os.system('clear')

def main():
    database = r"data/Dealership.db"

    # create a database connection
    conn = openConnection(database)
    populateDB(conn)
   
    with conn:
        startOptions(conn)

    closeConnection(conn, database)
    
def populateDB(conn):
    cur = conn.cursor()
    a_file = open("Inventory.csv")
    rows = csv.reader(a_file)
    cur.executemany("INSERT INTO Inventory(i_location, i_did, i_condition, i_oid, i_vin) VALUES(?,?,?,?,?)", rows)
    conn.commit()
    

    b_file = open("vehicles.csv")
    rows = csv.reader(b_file)
    cur.executemany("INSERT INTO Vehicle(v_modelName, v_modelYear, v_brandName, v_bodyStyle, v_color, v_price, v_inventoryId, v_manufacturer) VALUES(?,?,?,?,?,?,?,?)", rows)
    conn.commit()
    
    

if __name__ == '__main__':
    main()
