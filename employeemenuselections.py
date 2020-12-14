import sqlite3
import os
import employeemenu

def getDID(_conn, location):
    s = _conn.cursor()
    s.execute("SELECT d_did FROM Dealer WHERE d_location = ?;", (location,))
    res = s.fetchall()
    return res[0][0]

def getInvId(_conn, vin):
    s = _conn.cursor()
    s.execute("SELECT i_inventoryId FROM Inventory WHERE i_vin = ?;", (vin,))
    res = s.fetchall()
    return res[0][0]

def getCID(_conn, cName):
    s = _conn.cursor()
    s.execute("SELECT c_cid FROM Customer WHERE c_name = ?;", (cName,))
    cID = s.fetchall()
    return cID[0][0]

def displayInv(_conn, location):
    s = _conn.cursor()
    s.execute("SELECT i_inventoryId, v_brandName, v_modelName, v_modelYear, i_condition, i_vin FROM Inventory,Vehicle WHERE i_inventoryId = v_inventoryId AND i_location = ?;", (location,))
    l = '{:>} {:>} {:>} {:>} {:>} {:>}'.format("Inventory ID", "Brand Name","Model Name", "Model Year", "Condition", "VIN#")
    print(l + "\n")
    rows = s.fetchall()
    for row in rows:
        l = '{:>} {:>} {:>} {:>} {:>} {:>}'.format(row[0], row[1], row[2], row[3], row[4], row[5])
        print(l + "\n")


def insertInv(_conn, location):
    s = _conn.cursor()
    inputVals = ["" for x in range(10)]
    print("Please provide the following information: \n")
    inputVals[0] = input("Condition of the car: \n")
    inputVals[1] = input("Transmission Type: (1-Automatic, 2-Manual, 3-CVT) \n")
    inputVals[2] = input("Vin #: \n")
    inputVals[3] = input("Model Name: \n")
    inputVals[4] = input("Model Year: \n")
    inputVals[5] = input("Brand Name: \n")
    inputVals[6] = input("Body Style: \n")
    inputVals[7] = input("Color: \n")
    inputVals[8] = input("Price: \n")
    inputVals[9] = input("Manufacturer: \n")
    
    dId = getDID(_conn, location)

    s.execute("INSERT INTO Inventory(i_location, i_did, i_condition, i_oid, i_vin) VALUES(?,?,?,?,?);", (location, dId, inputVals[0], inputVals[1], inputVals[2],))

    invId = getInvId(_conn, inputVals[2])

    s.execute("INSERT INTO Vehicle(v_modelName, v_modelYear, v_brandName, v_bodyStyle, v_color, v_price, v_inventoryId, v_manufacturer) VALUES(?,?,?,?,?,?,?,?);", (inputVals[3], inputVals[4], inputVals[5], inputVals[6], inputVals[7], inputVals[8], invId, inputVals[9],))

    s.execute("SELECT COUNT(*) FROM Vehicle WHERE v_inventoryId = ?;", (invId,))
    rows = s.fetchall()

    if rows[0][0] != 0:
        print("Insertion Successful")
    else :
        print("Insertion Error")
        x = input("Do you want to try to insert another one? (Yes/No) \n")
        if x.lower() == "yes" or x.lower() == "y":
            insertInv(_conn, location)
        else:
            return
    return


def sellOrBuyCar(_conn, location):
    s = _conn.cursor()
    vinNum = input("Please type the VIN# for the vechicle: \n")
    eId = input("Please enter your employee ID: \n")
    cName = input("Please enter the customer name: \n")
    sellMethod = input("Did you sell or buy the vehicle: (B - bought, S - sold) \n")

    if sellMethod == 'b' or sellMethod.lower() == 'bought' or sellMethod == 'B':
        sellMethod = 'B'
        insertInv(_conn, location)

        cId = getCID(_conn, cName)
        dId = getDID(_conn, location)
        invId = getInvId(_conn, vinNum)

        s.execute("SELECT v_price FROM Vehicle WHERE v_inventoryId = ?", (invId,))
        res = s.fetchall()

        price = res[0][0]

        s.execute("INSERT INTO Sales(s_eid, s_did, s_cid, s_vin, s_date, s_saleMethod, s_price) VALUES(?,?,?,?,datetime('now', 'localtime'),?,?);", (eId, dId, cId, vinNum, sellMethod, price,))

        s.execute("SELECT COUNT(s_sid) FROM Sales WHERE s_vin = ?;", (vinNum,))
        x = s.fetchall()

        if x[0][0] == 1:
            print("Vehicle successfully registered as Bought.")

    elif sellMethod == 's' or sellMethod.lower() == 'bought' or sellMethod == 'S':
        cId = getCID(_conn, cName)
        dId = getDID(_conn, location)
        invId = getInvId(_conn, vinNum)
        sellMethod = 'S'
        
        s.execute("SELECT v_price FROM Vehicle WHERE v_inventoryId = ?", (invId,))
        res = s.fetchall()
        price = res[0][0]
        
        s.execute("INSERT INTO Sales(s_eid, s_did, s_cid, s_vin, s_date, s_saleMethod, s_price) VALUES(?,?,?,?,datetime('now', 'localtime'),?,?);", (eId, dId, cId, vinNum, sellMethod, price,))
        removeCar(_conn, invId)
        s.execute("SELECT COUNT(*) FROM Sales WHERE s_vin = ?;", (vinNum,))
        x = s.fetchall()

        if x[0][0] != 0:
            print("Vehicle successfully registered as Sold.")
        

def changePricing(_conn, location):
    s = _conn.cursor()
    vinNum = input("Please type the VIN# for the vehicle you want to change the price of: \n")

    invId = getInvId(_conn, vinNum)

    newPrice = input("Please enter the new price for the vehicle: \n")

    s.execute("UPDATE Vehicle SET v_price = ? WHERE v_inventoryId = ?;", (newPrice, invId,))

    s.execute("SELECT COUNT(*) FROM Vehicle WHERE v_inventoryId = ? AND v_price = ?;", (invId, newPrice,))
    count = s.fetchall()

    if count[0][0] == 1:
        print("Price successfully updated")
        return
    else:
        print("Failed to update price")
        return
    

def removeCar(_conn, invId):
    s = _conn.cursor()
    s.execute("DELETE FROM Vehicle WHERE v_inventoryId = ?;", (invId,))
    

    s.execute("DELETE FROM Inventory WHERE i_inventoryId = ?;", (invId,))


def lookForInv(_conn, location):
    s = _conn.cursor()
    vinNum = input("What is the VIN# for the vehicle you are looking for?\n")

    s.execute("SELECT * FROM Vehicle, Inventory WHERE v_inventoryID = i_inventoryId AND i_vin = ?;", (vinNum,))
    results = s.fetchall()

    if [x[0] for x in results] == []:
        print("No Vehicle with the given VIN# found \n")
        i = input("Do you want to look for another vehicle? (Yes/No)\n")
        if i.lower() == "yes" or i.lower() == 'y':
            lookForInv(_conn, location)
        else:
            return
    else:
        l = '{:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>}'.format("Vehicle_ID", "Model Name", "Model Year", "Brand Name", "Color", "Price", "Inventory ID", "Manufacturer")
        print(l + "\n")
        for res in results:
            l = '{:>} {:>} {:>} {:>} {:>} {:>} {:>} {:>}'.format(res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7])
            print(l + "\n")
        return

