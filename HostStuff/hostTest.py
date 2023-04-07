from cgitb import text
import tkinter
from tkinter import *
from tkinter import ttk
import csv
import os


def hostTables():
    tableStatus = Toplevel(root)
    #tableStatus = tkinter.Tk(className="Table Status",)
    #tableStatus.grid()
    tableStatus.title("Host Table View")
    ttk.Label(tableStatus, text="All Tables: ").grid(column=0, row=0)
    #currently all table buttons only shut down the program
    ttk.Button(tableStatus, text="Table 1", command=(lambda: tbStatWindow(1))).grid(column=0, row=1)
    ttk.Button(tableStatus, text="Table 2", command=(lambda: tbStatWindow(2))).grid(column=0, row=2)
    ttk.Button(tableStatus, text="Table 3", command=(lambda: tbStatWindow(3))).grid(column=0, row=3)
    ttk.Button(tableStatus, text="Table 4", command=(lambda: tbStatWindow(4))).grid(column=1, row=1)
    ttk.Button(tableStatus, text="Table 5", command=(lambda: tbStatWindow(5))).grid(column=1, row=2)
    ttk.Button(tableStatus, text="Table 6", command=(lambda: tbStatWindow(6))).grid(column=1, row=3)
    ttk.Button(tableStatus, text="Table 7", command=(lambda: tbStatWindow(7))).grid(column=2, row=1)
    ttk.Button(tableStatus, text="Table 8", command=(lambda: tbStatWindow(8))).grid(column=2, row=2)
    ttk.Button(tableStatus, text="Table 9", command=(lambda: tbStatWindow(9))).grid(column=2, row=3)
    ttk.Label(tableStatus, text="").grid(column=2, row=4)
    ttk.Button(tableStatus, text="Exit", command=tableStatus.destroy).grid(column=2, row=5)
    
    #For table CSV file:
    # A,B,C
    # A = Table Number
    # B = Availability 
        # 0 = Available
        # 1 = Occupied
        # 2 = Dirty
    # C = Waiter Name
        # 0 = Empty

wsName = ""
def tbStatWindow(tbid):
    
    tableStat = Toplevel(root)
    tableStat.title('Table ' + str(tbid))
    ttk.Label(tableStat,text="Status: "+ str(printTBstat(tbid-1))).grid(column=0,row=0)
    if str(printTBstat(tbid-1)) == "Available":
        #ttk.Label(tableStat,text="Enter Party Size: ").grid(column=0,row=2)
        #psEntry = ttk.Entry(tableStat).grid(column=1,row=2)
        empList = ["John", "George", "Paul", "Ringo"]
        ttk.Label(tableStat,text="Select Waitstaff: ").grid(column=0,row=3)
        wsMenu = StringVar(tableStat)
        wsMenu.set("John")

        wsmenu1 = ttk.OptionMenu(tableStat, wsMenu, *empList).grid(column=1,row=3)
        
        ttk.Button(tableStat,text="Submit",command=(lambda: assignWaitstaff(wsMenu.get()))).grid(column=1,row=4)
    elif str(printTBstat(tbid-1)) == "Occupied":
        ttk.Button(tableStat,text="Reset Table",command =(lambda: resetTable())).grid(column=1,row=4)

    def resetTable():
        newFile = open("C:/Users/malch/AppData/Local/Programs/Python/Python39/Scripts/RestaurantAutomation/HostStuff/tempCSV.csv",'w',newline="")
        file = open("C:/Users/malch/AppData/Local/Programs/Python/Python39/Scripts/RestaurantAutomation/HostStuff/hostTableCSV.csv")
        csvreader = csv.reader(file)
        csvWriter = csv.writer(newFile)
        rows = []
        for row in csvreader:
            rows.append(row)
        rows[tbid-1][2] = "Empty"
        rows[tbid-1][1] = "Dirty"
        for row in rows:
            csvWriter.writerow(row)
       
        file.close()
        newFile.close()
        os.remove("C:/Users/malch/AppData/Local/Programs/Python/Python39/Scripts/RestaurantAutomation/HostStuff/hostTableCSV.csv")
        old_name = r"C:\Users\malch\AppData\Local\Programs\Python\Python39\Scripts\RestaurantAutomation\HostStuff\tempCSV.csv"
        new_name = r"C:\Users\malch\AppData\Local\Programs\Python\Python39\Scripts\RestaurantAutomation\HostStuff\hostTableCSV.csv"
        os.rename(old_name,new_name)
        tableStat.destroy()
    def assignWaitstaff(waitstaffName):
        newFile = open("C:/Users/malch/AppData/Local/Programs/Python/Python39/Scripts/RestaurantAutomation/HostStuff/tempCSV.csv",'w',newline="")
        file = open("C:/Users/malch/AppData/Local/Programs/Python/Python39/Scripts/RestaurantAutomation/HostStuff/hostTableCSV.csv")
        csvreader = csv.reader(file)
        csvWriter = csv.writer(newFile)
        rows = []
        for row in csvreader:
            rows.append(row)
        rows[tbid-1][2] = waitstaffName
        rows[tbid-1][1] = "Occupied"
        for row in rows:
            csvWriter.writerow(row)
       
        file.close()
        newFile.close()
        os.remove("C:/Users/malch/AppData/Local/Programs/Python/Python39/Scripts/RestaurantAutomation/HostStuff/hostTableCSV.csv")
        old_name = r"C:\Users\malch\AppData\Local\Programs\Python\Python39\Scripts\RestaurantAutomation\HostStuff\tempCSV.csv"
        new_name = r"C:\Users\malch\AppData\Local\Programs\Python\Python39\Scripts\RestaurantAutomation\HostStuff\hostTableCSV.csv"
        os.rename(old_name,new_name)
        tableStat.destroy()
        
        

             




def printTBstat(tbid):
    file = open("C:/Users/malch/AppData/Local/Programs/Python/Python39/Scripts/RestaurantAutomation/HostStuff/hostTableCSV.csv")
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        rows.append(row)
    
    statusId = (rows[tbid][1])
    return statusId
    file.close()


    
#main
root = tkinter.Tk(className="Login",)
root.grid()

#lets find out what role everyone is
ttk.Label(root, text="I am a: ").grid(column=0, row=0)
#ttk.Button(root, text="Waiter", command=waiterOrder).grid(column=1, row=0)
#ttk.Button(root, text="Cook", command=cookOrders).grid(column=2, row=0)
#ttk.Button(root, text="Busser", command=busserTables).grid(column=3, row=0)
ttk.Button(root, text="Host", command=hostTables).grid(column=4, row=0)

ttk.Label(root, text="").grid(column=0, row=2)
exitForm = ttk.Button(root, text="Exit", command=root.destroy).grid(column=4, row=3)


root.mainloop()