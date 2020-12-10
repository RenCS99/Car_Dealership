import sqlite3
import os

def getDID(_conn, location):
    _conn.execute("SELECT d_did FROM Dealer WHERE d_location = ?;", (location,))
    res = _conn.fetchall()
    return res[0][0]

def getInvId(_conn, vin):
    _conn.execute("SELECT i_inventoryId FROM Inventory WHERE i_vin = ?;", (vin,))
    invId = _conn.fetchall()
    return invId[0][0]

def displayInv(_conn, location):
    _conn.execute("SELECT i_inventoryId, v_modelName, v_modelYear, i_condition, i_vin FROM Inventory, Vechile WHERE i_inventoryId = v_inventoryId AND i_location = ?;", (location,))
    l = '{:>} {:>} {:>} {:>} {:>} {:>}'.format("Inventory ID", "Model Name", "Model Year", "Location", "Condition", "VIN#")
    rows = _conn.fetchall()
    for row in rows:
        l = '{:>} {:>} {:>} {:>} {:>} {:>}'.format(row[0], row[1], row[2], row[3], row[4], row[5])
        print(l)

def insertInv(_conn, location):
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

    _conn.execute("INSERT INTO Inventory(i_location, i_did, i_condition, i_oid, i_vin) VALUES(?,?,?,?,?);", (location, dId, inputVals[0], inputVals[1], inputVals[2],))
    _conn.commit()

    invId = getInvId(_conn, inputVals[2])

    _conn.execute("INSERT INTO Vehicle(v_modelName, v_modelYear, v_brandName, v_bodyStyle, v_color, v_price, v_inventoryId, v_manufacturer) VALUES(?,?,?,?,?,?,?,?);", (inputVals[3], inputVals[4], inputVals[5], inputVals[6], inputVals[7], inputVals[8], invId, inputVals[9],))
    _conn.commit()

    _conn.execute("SELECT COUNT(*) FROM Vechile WHERE v_inventoryId = ?;", (invId,))
    rows = _conn.fetchall()

    if rows[0][0] == 1:
        print("Insertion Successful")
    else :
        print("Insertion Error")
        x = input("Do you want to try to insert another one? (Yes/No) \n")
        if x.lower() == "yes" or x.lower() == "y":
            insertInv(_conn, location)
        else:
            return


def sellCar(_conn, location):
    vinNum = input("Please type the VIN# for the vechicle: \n")

    dId = getDID(_conn, location)

    invId = getInvId(_conn, vinNum)

    removeCar(_conn, dId, location)
    # for row in rows:
    #     l = '{:<10} {:<20} {:>20} {:>20}'.format(row[0], row[1], row[2], row[3],row[4])
    #     print(l)

def changePricing(_conn, location):
    vinNum = input("Please type the VIN# for the vehicle you want to change the price of: \n")

    invId = getInvId(_conn, vinNum)

    newPrice = input("Please enter the new price for the vehicle: \n")

    _conn.execute("UPDATE Vehicle SET v_price = ? WHERE v_inventoryId = ?;", (newPrice, invId,))

    _conn.execute("SELECT COUNT(*) FROM Vehicle WHERE v_inventoryId = ? AND v_price = ?;", (invId, newPrice,))
    count = _conn.fetchall()

    if count[0][0] == 1:
        print("Price successfully updated")
    else:
        print("Failed to update price")
    

def removeCar(_conn, dId, location):
    return

def lookForInv(_conn, location):
    return