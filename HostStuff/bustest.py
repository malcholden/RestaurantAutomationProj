#when in doubt import it all
import tkinter
from tkinter import *
from tkinter import ttk
import csv
import os

def busserTables():
    tableStatus = Toplevel(root)
    tableStatus.title("Busser Table View")
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
    ttk.Button(tableStatus, text="Exit", command=root.destroy).grid(column=2, row=5)

wsName = ""
def tbStatWindow(tbid):

    tableStat = Toplevel(root)
    tableStat.title('Table ' + str(tbid))
    ttk.Label(tableStat, text="Status: " + str(printTBstat(tbid-1))).grid(column=0, row=0)
    if str(printTBstat(tbid-1)) == "Dirty":
        ttk.Button(tableStat,text="Clean Table",command =(lambda: cleanTable(tbid))).grid(column=1,row=4)
        

    def cleanTable(tbid):
        newFile = open("tempCSV.csv",'w',newline="")
        file = open("hostTableCSV.csv")
        csvreader = csv.reader(file)
        csvWriter = csv.writer(newFile)
        rows = []
        for row in csvreader:
            rows.append(row)
        rows[tbid-1][1] = "Available"
        for row in rows:
            csvWriter.writerow(row)
       
        file.close()
        newFile.close()
        os.remove("hostTableCSV.csv")
        old_name = r"tempCSV.csv"
        new_name = r"hostTableCSV.csv"
        os.rename(old_name,new_name)
        tableStat.destroy()
        
def printTBstat(tbid):
    file = open("hostTableCSV.csv")
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
#ttk.Button(frm, text="Waiter", command=waiterOrder()).grid(column=1, row=0)
#ttk.Button(frm, text="Cook", command=cookOrders()).grid(column=2, row=0)
ttk.Button(root, text="Busser", command=busserTables).grid(column=3, row=0)
#ttk.Button(frm, text="Host", command=hostTables()).grid(column=4, row=0)

ttk.Label(root, text="").grid(column=0, row=2)
exitForm = ttk.Button(root, text="Exit", command=root.destroy).grid(column=4, row=3)

root.mainloop()