import sys
import os
import sqlite3
import Project_Dealership
import customermenu

def main(_conn):
    s = _conn.cursor()
    Project_Dealership.clearscreen()
    customermenu.customer_registration(_conn)
    while True:
        customermenu.main_menu()
        userinput = input()
        if userinput == '1':
            customermenu.buy_car_menu()
            uI = input("Please select how you would like to search for your vehicle: ")
            if uI == '1':
                customermenu.priceSearch(s)
                customermenu.buymenu(s)
            elif uI == '2':
                customermenu.locationSearch(s)
                customermenu.buymenu(s)
            elif uI == '3':
                customermenu.make_model_search(s)
                customermenu.buymenu(s)
            elif uI == '4':
                customermenu.bodytype_search(s)
                customermenu.buymenu(s)
            elif uI == '5':
                customermenu.yearSearch(s)
                customermenu.buymenu(s)
            else:
                pl = input("Invalid input. Press enter to try again")
        elif userinput == '2':
            customermenu.buy_car_menu()
            uI = input("Please select how you would like to search for your vehicle: ")
            if uI == '1':
                customermenu.priceSearch(s)
            elif uI == '2':
                customermenu.locationSearch(s)
            elif uI == '3':
                customermenu.make_model_search(s)
            elif uI == '4':
                customermenu.bodytype_search(s)
            elif uI == '5':
                customermenu.yearSearch(s)
            else:
                pl = input("Invalid input. Press enter to try again")
        elif userinput == '3':
            customermenu.sell_car_menu(s)
        elif userinput == '4':
            customermenu.view_all_listed_cars(_conn)
            



  
            



  
            


  
            


  
            


  
            


  
            


  
            


  
            


  
            


  
            


  
            


  
            


  
            


  
            


  
            


  