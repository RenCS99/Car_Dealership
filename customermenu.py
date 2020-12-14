import sys
import os
import sqlite3
import Project_Dealership
import random

def customer_registration(_conn):
    s = _conn.cursor()
    inputVals = ["" for x in range(3)]
    print("Please provide the following information: \n")
    i = 0
    while i != -1:
        inputVals[0] = input("Full Name: ")
        inputVals[1] = input("Phone Number (123-456-7890): ")
        inputVals[2] = input("Gender (M - male or F - female): ")

        if inputVals[2] == 'M' or inputVals[2] == "F" or inputVals[2].lower() == "m" or inputVals[2].lower() == "f":
            i = -1
        else:
            print("Please enter either F (for female) or M (for male)")
    
    s.execute("INSERT INTO Customer(c_did, c_name, c_phone, c_gender) VALUES(NULL,?,?,?);", (inputVals[0], inputVals[1], inputVals[2]))
    _conn.commit()
    

def main_menu():
    print("Welcome to the Car Dealership")
    print("\t 1. Buy a car")
    print("\t 2. Search for a car")
    print("\t 3. Sell a car")
    print("\t 4. View inventory")
    print("\t 0. Exit")
    print("")

def choice_of_location():
    print("Please choose your dealership (1-5): ")
    print("\t 1. Choice Vehicles - ALABAMA")
    print("\t 2. Auto Mart - CALIFORNIA")
    print("\t 3. AnyCar - WASHINGTON")
    print("\t 4. Auto Sales - TEXAS")
    print("\t 5. Discount Motors - Florida")
    print("\t 6. Used Cars 4 You - Colorado")
    print("\t 7. AutoWizard - Arizona")
    print("\t 8. Village Auto - Massuchusetts")
    print("\t 9. Vance Ford - Utah")
    print("\t 10. Grand Touring Cars INC - Nevada \n")
    
    while True:
        dId = input("")
        if dId == '0':
            return
        elif dId == '1':
            location = "ALABAMA"
            return location
        elif dId == '2':
            location = "CALIFORNIA"
            return location
        elif dId == '3':
            location = "WASHINGTON"
            return location
        elif dId == '4':
            location = "TEXAS"
            return location
        elif dId == '5':
            location = "Florida"
            return location
        elif dId == '6':
            location = "Colorado"
            return location
        elif dId == '7':
            location = "Arizona"
            return location
        elif dId == '8':
            location = "Massachusetts"
            return location
        elif dId == '9':
            location = "Utah"
            return location
        elif dId == '10':
            location = "NEVADA"
            return location
        else:
            print("Unknown Choice")
            print("Please enter one of the options above")    
    
def buy_car_menu():
    print("How would you like to search for your car?")
    print("\t 1. Search by Price")
    print("\t 2. Search by Location")
    print("\t 3. Search by Make and Model")
    print("\t 4. Search by body type")
    print("\t 5. Search by year")

def sell_car_menu(s):
    inputVals = ["" for x in range(11)]
    print("Please provide the following information of the car you want to sell: \n")
    name = input("Please enter your Full name: ")
    inputVals[0] = input("Condition of the car (Like-New,Excellent,Good,Fair,Salvage): \n")
    inputVals[1] = input("Transmission Type: (1-Automatic, 2-Manual, 3-CVT) \n")
    inputVals[2] = input("Vin #: \n")
    inputVals[3] = input("Model Name: \n")
    inputVals[4] = input("Model Year: \n")
    inputVals[5] = input("Brand Name: \n")
    inputVals[6] = input("Body Style: \n")
    inputVals[7] = input("Color: \n")
    inputVals[9] = input("Manufacturer: \n")
    print("Which state are you located: ")
    inputVals[10] = choice_of_location()
    
    if inputVals[0] == "Excellent" or inputVals[0] == "Like-New":
        print("You are eligble to recieve $20,000 for your car")
        inputVals[8] = 20000
    elif inputVals[0] == "Very Good" or inputVals[0] == "Excellent" or inputVals[0] == "very Good":
        print("You are eligble to recieve $15,000 for your car")
        inputVals[8] = 15000
    elif inputVals[0] == "Good" or inputVals[0] == "Good":
        print("You are eligble to recieve $10,000 for your car")
        inputVals[8] = 10000
    elif inputVals[0] == "Fair" or inputVals[0] == "Fair":
        print("You are eligble to recieve $8,000 for your car")
        inputVals[8] = 8000
    elif inputVals[0] == "Poor" or inputVals[0] == "Salvage":
        print("You are eligble to recieve $3,000 for your car")
        inputVals[8] = 3000
    else:
        print("Sorry we don't accept cars with this condition.")
        return

    inRes = input("Do you accept the amount? (y/n)\n")
    if inRes == "y" or inRes == "yes":
#s.execute("INSERT INTO Customer(c_did, c_name, c_phone, c_gender) VALUES(NULL,?,?,?);", (inputVals[0], inputVals[1], inputVals[2]))
        dId = getDID(s, inputVals[10])
        eId = getRanEID(s, dId)
        cId = getCID(s, name)
        s.execute("INSERT INTO Sales(s_eid,s_did,s_cid,s_vin,s_date,s_saleMethod,s_price) VALUES(?,?,?,?,datetime('now','localtime'),'B',?);", (eId,inputVals[10],cId, inputVals[2],inputVals[8]) )
        s.execute("INSERT into Inventory(i_location, i_did, i_condition, i_oid, i_vin) VALUES(?,?,?,?,?);", (inputVals[10], dId, inputVals[0], inputVals[1], inputVals[2],))
        invId = getInvId(s, inputVals[2])
        s.execute("INSERT INTO Vehicles(v_modelName,v_modelYear, v_brandName, v_bodyStyle, v_color, v_price, v_inventoryId, v_manufacturer) VALUES(?,?,?,?,?,?,?,?);", (inputVals[3],inputVals[4],inputVals[5],inputVals[6],inputVals[7],inputsVals[8],invId,inputVals[9],))
        print("Thank you for doing business with us.")
    elif inRes == 'n' or inRes == 'no':
        print("We are sorry to hear that. Your business is always welcome.")
    else:
        print("Invalid input.")
        return
        

    
    
def view_all_listed_cars(_conn):
    print("Would you like to view cars from one location/dealership or from all locations? \n")
    print("Please input all (for all locations) or one (for one location)\n")
    i = 0
    while i != -1: 
        choice= input("")
        if choice.lower() == "all" or choice.upper() == "ALL" or choice.lower() == "a" or choice.upper() == "A":
            s = _conn.cursor()
            s.execute("SELECT i_inventoryId, v_brandName, v_modelName, v_modelYear, i_location, i_condition, i_vin FROM Inventory, Vehicle WHERE i_inventoryId = v_inventoryId;")
            rows = s.fetchall()
            l = '{:>} {:>} {:>} {:>} {:>} {:>} {:>}'.format("Inventory ID", "Brand Name","Model Name", "Model Year", "Location", "Condition", "VIN#")
            print(l + "\n")
            
            for row in rows:
                l = '{:>} {:>} {:>} {:>} {:>} {:>} {:>}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                print(l + "\n")
            i = -1

        elif choice.lower() == "one" or choice.upper() == "ONE" or choice.lower() == "o" or choice.upper() == "O":
            inputLoc = choice_of_location()
            s = _conn.cursor()
            s.execute("SELECT i_inventoryId, v_brandName, v_modelName, v_modelYear, i_location, i_condition, i_vin FROM Inventory,Vehicle WHERE i_inventoryId = v_inventoryId AND i_location = ?;", (inputLoc,))
            rows = s.fetchall()
            l = '{:>} {:>} {:>} {:>} {:>} {:>} {:>}'.format("Inventory ID", "Brand Name","Model Name", "Model Year", "Location", "Condition", "VIN#")
            print(l + "\n")
            
            for row in rows:
                l = '{:>} {:>} {:>} {:>} {:>} {:>} {:>}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                print(l + "\n")
            i = -1

        else:
            print("Please enter either all (for all locations) or one (for one location)")

def priceSearch(s):
    minPrice = input("Please Enter your lowest price:")
    maxPrice = input("Please enter your highest price:")
    s.execute("SELECT * FROM Vehicle WHERE v_price <= ? AND v_price >= ?;", (maxPrice, minPrice,))
    results = s.fetchall()
    if [x[0] for x in results] == []:
        print("No results found")
        i = input("Would you like to search with another price range?")
        if i.lower() == "yes" or i.lower() == "y":
            priceSearch(s)
            return
        elif i.lower() == "no" or i.lower() == "n":
            return
        else:
            return
    else:           
        for res in results:
            l = '{:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>}'.format(res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], res[8])
            print(l + "\n")
            return

def locationSearch(s):
    print("\t 1. ALABAMA")
    print("\t 2. CALIFORNIA")
    print("\t 3. WASHINGTON")
    print("\t 4. TEXAS")
    print("\t 5. NEVADA \n")
    while True:
        l_input = input("Please select your location: ")

        if l_input == "1": 
            l_input = "ALABAMA"
            s.execute("Select i_inventoryId, v_brandName, v_modelName, v_modelYear, i_location, i_condition FROM Inventory, Vehicle WHERE i_location = ? AND v_inventoryId = i_inventoryId", (l_input,))
            rows = s.fetchall()
            l = '{:>} {:>} {:>} {:>} {:>} {:>}'.format("Inventory ID", "Brand Name","Model Name", "Model Year", "Location", "Condition")
            print(l + "\n")
            
            for row in rows:
                l = '{:>} {:>} {:>} {:>} {:>} {:>}'.format(row[0], row[1], row[2], row[3], row[4], row[5])
                print(l + "\n")
            return
        elif l_input == "2":
            l_input = "CALIFORNIA"
            s.execute("Select i_inventoryId, v_brandName, v_modelName, v_modelYear, i_location, i_condition FROM Inventory, Vehicle WHERE i_location = ? AND v_inventoryId = i_inventoryId", (l_input,))
            rows = s.fetchall()
            l = '{:>} {:>} {:>} {:>} {:>} {:>}'.format("Inventory ID", "Brand Name","Model Name", "Model Year", "Location", "Condition")
            print(l + "\n")
            
            for row in rows:
                l = '{:>} {:>} {:>} {:>} {:>} {:>}'.format(row[0], row[1], row[2], row[3], row[4], row[5])
                print(l + "\n")
            return
        elif l_input == "3":
            l_input = "WASHINGTON"
            s.execute("Select i_inventoryId, v_brandName, v_modelName, v_modelYear, i_location, i_condition FROM Inventory, Vehicle WHERE i_location = ? AND v_inventoryId = i_inventoryId", (l_input,))
            rows = s.fetchall()
            l = '{:>} {:>} {:>} {:>} {:>} {:>}'.format("Inventory ID", "Brand Name","Model Name", "Model Year", "Location", "Condition")
            print(l + "\n")
            
            for row in rows:
                l = '{:>} {:>} {:>} {:>} {:>} {:>}'.format(row[0], row[1], row[2], row[3], row[4], row[5])
                print(l + "\n")
            return
        elif l_input == "4":
            l_input = "TEXAS"
            s.execute("Select i_inventoryId, v_brandName, v_modelName, v_modelYear, i_location, i_condition FROM Inventory, Vehicle WHERE i_location = ? AND v_inventoryId = i_inventoryId", (l_input,))
            rows = s.fetchall()
            l = '{:>} {:>} {:>} {:>} {:>} {:>}'.format("Inventory ID", "Brand Name","Model Name", "Model Year", "Location", "Condition")
            print(l + "\n")
            
            for row in rows:
                l = '{:>} {:>} {:>} {:>} {:>} {:>}'.format(row[0], row[1], row[2], row[3], row[4], row[5])
                print(l + "\n")
            return
        elif l_input == "5":
            l_input = "NEVADA"
            s.execute("Select i_inventoryId, v_brandName, v_modelName, v_modelYear, i_location, i_condition FROM Inventory, Vehicle WHERE i_location = ? AND v_inventoryId = i_inventoryId", (l_input,))
            rows = s.fetchall()
            l = '{:>} {:>} {:>} {:>} {:>} {:>}'.format("Inventory ID", "Brand Name","Model Name", "Model Year", "Location", "Condition")
            print(l + "\n")
            
            for row in rows:
                l = '{:>} {:>} {:>} {:>} {:>} {:>}'.format(row[0], row[1], row[2], row[3], row[4], row[5])
                print(l + "\n")
            return
        else:
            x = input("Invalid Selection Press enter to try again.")

def make_model_search(s):
    makeName = input("Please enter the make of the vehicle: ")
    modelName = input("Please enter the model of the vehicle: ")
    s.execute("SELECT * FROM Vehicle WHERE v_modelName = ? AND v_brandName = ?;", (modelName, makeName,))
    results = s.fetchall()
    if [x[0] for x in results] == []:
        print("No results found")
        return
    else:           
        for res in results:
            l = '{:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>}'.format(res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], res[8])
            print(l + '\n')
    return

def bodytype_search(s):
    print("\t 1. Sports")
    print("\t 2. Truck")
    print("\t 3. Luxury")
    print("\t 4. SubCompact")
    print("\t 5. Compact")
    print("\t 6. SUV")
    
    while True:
        bodyType = input("Please enter the body type of the vehicle(1-6): ")

        if bodyType == "1":
            bodyType = "SPORTS"
            s.execute("SELECT * FROM Vehicle WHERE v_bodyStyle = ?;", (bodyType,))
            results = s.fetchall()
            
            if [x[0] for x in results] == []:
                print("No results found")
                return
            else:
                print("\n")
                l = '{:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>}'.format("Vehicle_ID", "Model Name", "Model Year", "Brand Name", "Body Style", "Color", "Price", "Inventory_ID", "Manufacturer")
                print(l + "\n")           
                for res in results:
                    l = '{:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>}'.format(res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], res[8])
                    print(l + "\n")
            return

        elif bodyType == "2":
            bodyType = "TRUCK"
            s.execute("SELECT * FROM Vehicle WHERE v_bodyStyle = ?;", (bodyType,))
            results = s.fetchall()
        
            if [x[0] for x in results] == []:
                print("No results found")
                return
            else:       
                print("\n")
                l = '{:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>}'.format("Vehicle_ID", "Model Name", "Model Year", "Brand Name", "Body Style", "Color", "Price", "Inventory_ID", "Manufacturer")
                print(l + "\n")    
                for res in results:
                    l = '{:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>}'.format(res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], res[8])
                    print(l + "\n")
            return

        elif bodyType == "3":
            bodyType = "LUXURY"
            s.execute("SELECT * FROM Vehicle WHERE v_bodyStyle = ?;", (bodyType,))
            results = s.fetchall()
            
            if [x[0] for x in results] == []:
                print("No results found")
                return
            else:           
                print("\n")
                l = '{:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>}'.format("Vehicle_ID", "Model Name", "Model Year", "Brand Name", "Body Style", "Color", "Price", "Inventory_ID", "Manufacturer")
                print(l + "\n") 
                for res in results:
                    l = '{:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>}'.format(res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], res[8])
                    print(l + "\n")
            return

        elif bodyType == "4":
            bodyType = "SUBCOMPACT"
            s.execute("SELECT * FROM Vehicle WHERE v_bodyStyle = ?;", (bodyType,))
            results = s.fetchall()
            
            if [x[0] for x in results] == []:
                print("No results found")
                return
            else:           
                print("\n")
                l = '{:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>}'.format("Vehicle_ID", "Model Name", "Model Year", "Brand Name", "Body Style", "Color", "Price", "Inventory_ID", "Manufacturer")
                print(l + "\n") 
                for res in results:
                    l = '{:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>}'.format(res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], res[8])
                    print(l + "\n")
            return

        elif bodyType == "5":
            bodyType = "COMPACT"
            s.execute("SELECT * FROM Vehicle WHERE v_bodyStyle = ?;", (bodyType,))
            results = s.fetchall()
            
            if [x[0] for x in results] == []:
                print("No results found")
                return
            else:     
                print("\n")
                l = '{:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>}'.format("Vehicle_ID", "Model Name", "Model Year", "Brand Name", "Body Style", "Color", "Price", "Inventory_ID", "Manufacturer")
                print(l + "\n")       
                for res in results:
                    l = '{:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>}'.format(res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], res[8])
                    print(l + "\n")
            return 

        elif bodyType == "6":
            bodyType = "SUV"
            s.execute("SELECT * FROM Vehicle WHERE v_bodyStyle = ?;", (bodyType,))
            results = s.fetchall()
            
            if [x[0] for x in results] == []:
                print("No results found")
                return
            else:      
                print("\n")
                l = '{:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>}'.format("Vehicle_ID", "Model Name", "Model Year", "Brand Name", "Body Style", "Color", "Price", "Inventory_ID", "Manufacturer")
                print(l + "\n")      
                for res in results:
                    l = '{:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>}'.format(res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], res[8])
                    print(l + "\n")
            return
        else:
            nb = input("Invalid car body style")
    return

def yearSearch(s):
    bYear = input("Please enter the first year: ")
    aYear = input("Please enter the second year: ")
    s.execute("SELECT * FROM Vehicle WHERE v_modelYear >= ? AND v_modelYear <= ?;", (bYear, aYear,))
    results = s.fetchall()
    if [x[0] for x in results] == []:
        print("No results found")
        return
    else:
        print("Showing results from filtered search based on the year range: " + bYear + "-" + aYear)           
        for res in results:
            l = '{:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>}'.format(res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], res[8])
            print(l + '\n')
    return
    
def buymenu(s):
    print("Please select the car you would like to purchase by the Inventory ID.")
    selection = input()
    if checkInventory(s, selection):
        confirm = input("Please confirm this is the vehicle you want to purchase (y/n): ")
        s.execute("SELECT * FROM Vehicle WHERE v_inventoryId = ?", (selection,))
        l = '{:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>}'.format("Vehicle_ID", "Model Name", "Model Year", "Brand Name", "Body Style", "Color", "Price", "Inventory_ID", "Manufacturer")
        print(l + '\n')
        rows = s.fetchall()
        for row in rows:
            l = '{:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            print(l + "\n")
        if confirm == 'y' or confirm == 'yes':
            s.execute("SELECT i_location FROM Inventory WHERE i_inventoryId = ?;", (selection,))
            res = s.fetchall()
            cName = input("Please enter Full Name: \n")
            cId = getCID(s, cName)
            dId = getDID(s, res[0][0])
            eId = getRanEID(s, dId)
            vinNum = getVinNum(s, selection)
            price = getPrice(s, selection)
            sellMethod = 'S'
            s.execute("INSERT INTO Sales(s_eid, s_did, s_cid, s_vin, s_date, s_saleMethod, s_price) VALUES(?,?,?,?,datetime('now', 'localtime'),?,?);", (eId, dId, cId, vinNum, sellMethod, price,))
            print("Car Successfully Bought")
        else:
            return
    else:
        print("Vehicle not found with given Inventory ID.")
    
def checkInventory(s, invId):
    s.execute("select i_inventoryId from Inventory where i_inventoryId = ?",(invId,))
    results = s.fetchall()
    if [x[0] for x in results] == []:
        return False
    else:
        return True

def removeCar(s, invId):
    s.execute("DELETE FROM Vehicle WHERE v_inventoryId = ?;", (invId,))
    s.execute("DELETE FROM Inventory WHERE i_inventoryId = ?;", (invId,))
    

def getDID(s, location):
    s.execute("SELECT d_did FROM Dealer WHERE d_location = ?;", (location,))
    res = s.fetchall()
    return res[0][0]

def getRanEID(s, dId):
    s.execute("SELECT e_eid FROM Employee WHERE e_did = ?;", (dId,))
    res = s.fetchall()
    i = random.randint(0, len(res)-1)
    return res[i][0]

def getPrice(s, invId):
    s.execute("SELECT v_price FROM Vehicle WHERE v_inventoryId = ?;", (invId,))
    res = s.fetchall()
    return res[0][0]

def getVinNum(s, invId):
    s.execute("SELECT i_vin FROM Inventory WHERE i_inventoryId = ?;", (invId,))
    res = s.fetchall()
    return res[0][0]

def getCID(s, cName):
    s.execute("SELECT c_cid FROM Customer WHERE c_name = ?;", (cName,))
    res = s.fetchall()
    return res[0][0]

def getInvId(s, vinNum)
    s.execute("SELECT i_inventoryId FROM Inventory WHERE i_vin = ?;", (vinNum,))
    res = s.fetchall()
    return res[0][0]