import os
import sys
import sqlite3
import Project_Dealership
import employeemenuselections

global location 


def employee_selections():
    print("Employee Main Menu")
    print("\t 1. Display Current Inventory")
    print("\t 2. Add To Inventory")
    print("\t 3. Update Cars Sold")
    print("\t 4. Change pricing of a current listing")
    print("\t 5. Look up listing")
        
        
def verification(_conn, eID):
    s = _conn.cursor()
    s.execute("select * FROM Employee where e_eid = ?", (eID,))
    tup = s.fetchall()
    if eID != 0:
        if [x[0] for x in tup] != []:
            clearscreen()
            print("Please choose your dealership (1-5): ")
            print("\t 1. Choice Vehicles - ALABAMA")
            print("\t 2. Auto Mart - CALIFORNIA")
            print("\t 3. AnyCar - WASHINGTON")
            print("\t 4. Auto Sales - TEXAS")
            print("\t 5. Discount Motors - NEVADA \n")
            dId = input("")
            
            s.execute("SELECT COUNT(*) FROM Employee WHERE e_eid = ? AND e_did = ?;", (eID, dId,))
            res = s.fetchall()
            if res[0][0] == 1:
                if dId == '0':
                    return
                elif dId == '1':
                    location = "ALABAMA"
                elif dId == '2':
                    location = "CALIFORNIA"
                elif dId == '3':
                    location = "WASHINGTON"
                elif dId == '4':
                    location = "TEXAS"
                elif dId == '5':
                    location = "NEVADA"
                else:
                    print("Unknown Choice")
                return True
            else:
                return False

def clearscreen():
    os.system('clear')

def main(_conn):
    while True:              
        clearscreen()
        employee_selections()
        userInput = input()
        location = ""
        if userInput == '0':
            return
        elif userInput == '1':
            employeemenuselections.displayInv(_conn, location)
        elif userInput == '2':
            employeemenuselections.insertInv(_conn, location)
        elif userInput == '3':
            employeemenuselections.sellCar(_conn, location)
        elif userInput == '4':
            employeemenuselections.changePricing(_conn, location)
        elif userInput == '5':
            employeemenuselections.removeCar(_conn, location)
        elif userInput == '6':
            employeemenuselections.lookForInv(_conn, location)
        else:
            print("Unknown Choice")

        #uinput = input("To return to menu press enter otherwise type 0 to exit:  ")
