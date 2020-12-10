import sys
import os
import sqlite3
import Project_Dealership

def main(_conn):
    s = _conn.cursor()
    while True:
        Project_Dealership.clearscreen()
        customermenu.main_menu()
        userinput = input()
        if userinput = '1':
            

  