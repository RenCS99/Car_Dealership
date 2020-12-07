import os
import sys
import sqlite3

def mainmenu():
    print("++++++++++++++++++++++++")
    print("Employee Main Menu")
    print("++++++++++++++++++++++++")
    print("\t 1. ")
    
def clearscreen():
    os.system('clear')

def main(_conn):
    global s
    s = _conn.cursor()
    
    while True:
        #sql = """SELECT COUNT(*) FROM Employee WHERE e_eid = ?;"""
        
        eid = input("Please enter your employee ID : \n")
        s.execute("select * FROM Employee where e_eid = ?",(eid,))
        tup = s.fetchall()
        if eid != 0:
            if [x[0] for x in tup] != []:
                clearscreen()
                print("Please choose your dealership (1-5): ")
                print("\t 1. Choice Vehicles - ALABAMA")
                print("\t 2. Auto Mart - CALIFORNIA")
                print("\t 3. AnyCar - WASHINGTON")
                print("\t 4. Auto Sales - TEXAS")
                print("\t 5. Discount Motors - NEVADA \n")
                did = input("")
                s.execute("SELECT COUNT(*) FROM Employee WHERE e_eid = ? AND e_did = ?", (eid,did,))
                res = s.fetchall()
                print(res[0][0])
                # if res[0][0] == 1:
        
        elif eid == "m":
            Project_Dealership.startOptions()
        else:
            print("Invalid Input. Try again")

    
