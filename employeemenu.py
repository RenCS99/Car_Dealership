import os
import sys
import sqlite3
import Project_Dealership
import employeemenuselections

def employee_selections():
    print("Employee Main Menu")
    print("\t 1. Display Current Inventory")
    print("\t 2. Add To Inventory")
    print("\t 3. Update Cars Sold")
    print("\t 4. Change pricing of a current listing")
    print("\t 5. Look up listing")     
        
def verification(_conn, eID):
    global location
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
            print("\t 5. Discount Motors - Florida")
            print("\t 6. Used Cars 4 You - Colorado")
            print("\t 7. AutoWizard - Arizona")
            print("\t 8. Village Auto - Massachusetts")
            print("\t 9. Vance Ford - Utah")
            print("\t 10. Grand Touring Cars INC - Nevada \n")
            print("\t Input 0 to go back.")
            i = 0
            while i != -1:
                dId = input("")
                if dId == '0':
                    return
                elif dId == '1':
                    location = "ALABAMA"
                    i = -1
                elif dId == '2':
                    location = "CALIFORNIA"
                    i = -1
                elif dId == '3':
                    location = "WASHINGTON"
                    i = -1
                elif dId == '4':
                    location = "TEXAS"
                    i = -1
                elif dId == '5':
                    location = "Florida"
                    i = -1
                elif dId == '6':
                    location = "Colorado"
                    i = -1
                elif dId == '7':
                    location = "Arizona"
                    i = -1
                elif dId == '8':
                    location = "Massachusetts"
                    i = -1
                elif dId == '9':
                    location = "Utah"
                    i = -1
                elif dId == '10':
                    location = "NEVADA"
                    i = -1
                else:
                    print("Unknown Choice")
                    print("Please enter one of the options above")

            s.execute("SELECT COUNT(*) FROM Employee WHERE e_eid = ? AND e_did = ?;", (eID, dId,))
            res = s.fetchall()
    
            if res[0][0] == 1:
                return True
            else:
                return False

def clearscreen():
    os.system('clear')

def main(_conn):

    while True:              
        employee_selections()
        userInput = input("")
        if userInput == '0':
            return
        elif userInput == '1':
            employeemenuselections.displayInv(_conn, location)
        elif userInput == '2':
            employeemenuselections.insertInv(_conn, location)
        elif userInput == '3':
            employeemenuselections.sellOrBuyCar(_conn, location)
        elif userInput == '4':
            employeemenuselections.changePricing(_conn, location)
        elif userInput == '5':
            employeemenuselections.lookForInv(_conn, location)
        else:
            print("Unknown Choice")

        #uinput = input("To return to menu press enter otherwise type 0 to exit:  ")
