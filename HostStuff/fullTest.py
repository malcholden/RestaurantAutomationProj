
#when in doubt import it all
import tkinter
from tkinter import *
from tkinter import ttk
import csv
import os
from cgitb import text



#Allows the waiter to enter the customer's order:
def waiterOrder():
    submitOrder = Toplevel()
    submitOrder.geometry("700x400")
    submitOrder.title("Submit New Order")
    Label(submitOrder, text="New Pizza Order").grid(sticky="W", column=0, row=0)

    #crust time bb
    crust1 = StringVar()    #Any Crust

    ttk.Label(submitOrder, text="",).grid(sticky="W", column=0, row=1)
    ttk.Label(submitOrder, text="Please Select A Crust: ",).grid(sticky="W", column=0, row=2)
    ttk.Radiobutton(submitOrder, text="Regular", value="Regular", variable=crust1).grid(sticky="W", column=1, row=2)
    ttk.Radiobutton(submitOrder, text="Stuffed", value="Stuffed", variable=crust1).grid(sticky="W", column=2, row=2)
    ttk.Radiobutton(submitOrder, text="Gluten Free", value="Gulten Free", variable=crust1).grid(sticky="W", column=3, row=2)

    #lets get lost in the sauce
    cb1 = StringVar()   #Tomato
    cb2 = StringVar()   #Garlic
    cb3 = StringVar()   #Ranch
    cb4 = StringVar()   #BBQ

    ttk.Label(submitOrder, text="").grid(sticky="W", column=0, row=3)   #Empty Space
    ttk.Label(submitOrder, text="Please Select Sauces: ").grid(sticky="W", column=0, row=4)
    ttk.Checkbutton(submitOrder, text="Tomato",     variable=cb1, onvalue="Tomato, ",   offvalue="").grid(sticky="W", column=1, row=4)
    ttk.Checkbutton(submitOrder, text="Garlic",     variable=cb2, onvalue="Garlic, ",   offvalue="").grid(sticky="W", column=2, row=4)
    ttk.Checkbutton(submitOrder, text="Ranch",      variable=cb3, onvalue="Ranch, ",     offvalue="").grid(sticky="W", column=3, row=4)
    ttk.Checkbutton(submitOrder, text="BBQ",        variable=cb4, onvalue="BBQ, ",         offvalue="").grid(sticky="W", column=4, row=4)

    #toppings for winners
    top1 = StringVar()   #Bacon
    top2 = StringVar()   #Pepperoni
    top3 = StringVar()   #Ham
    top4 = StringVar()   #Sausage
   
    ttk.Label(submitOrder, text="").grid(sticky="W", column=0, row=5)   #Empty Space
    ttk.Label(submitOrder, text="Please Select Toppings: ").grid(sticky="W", column=0, row=6)
    ttk.Checkbutton(submitOrder, text="Bacon",     variable=top1, onvalue="Bacon, ",     offvalue="").grid(sticky="W", column=1, row=6)
    ttk.Checkbutton(submitOrder, text="Pepperoni", variable=top2, onvalue="Pepperoni, ", offvalue="").grid(sticky="W", column=2, row=6)
    ttk.Checkbutton(submitOrder, text="Ham",       variable=top3, onvalue="Ham, ",       offvalue="").grid(sticky="W", column=3, row=6)
    ttk.Checkbutton(submitOrder, text="Sausage",   variable=top4, onvalue="Sausage, ",   offvalue="").grid(sticky="W", column=4, row=6)

    #Additional Notes
    ttk.Label(submitOrder, text="").grid(sticky="W", column=0, row=7)   #Empty Space
    ttk.Label(submitOrder, text="Additional Notes:").grid(sticky="W", column=0, row=8)

    notesVar = StringVar()
    ttk.Entry(submitOrder, textvariable=notesVar, width=50).grid(column=1, row=8, columnspan=4)

    #Submit order
    ttk.Label(submitOrder, text="",).grid(sticky="W", column=0, row=10) #Empty Space
    def Submitted():
        #Tells Wait Staff Order has been sent
       ttk.Label(submitOrder, text="Your Pizza has: \nCrust Type: " + crust1.get() + "\n"        #CRUST
        "Sauces: "+ cb1.get() +cb2.get() +cb3.get() +cb4.get()+ "\n" +                           #SAUCEY
        "Toppings: " + top1.get() +top2.get() +top3.get() +top4.get()+ "\n"                      #TOPS
        + "Additional Notes: " + notesVar.get()).grid(sticky="W", column=4, row=12)              #ADDITIONAL NOTES
       
       ttk.Label(submitOrder, text="").grid( column=4, row=13)          #Empty Space
       ttk.Label(submitOrder, text="Order Submitted!").grid(sticky="W", column=4, row=14)

    #Submit Button, calls on def submitted
    ttk.Button(submitOrder, text="Submit Order >", command=Submitted).grid(sticky="W", column=4, row=11)





######################################################################################################################################



#Shows the host all tables and their state:
def hostTables():
    tableStatus = Toplevel(root)
    tableStatus.title("Host Table View")
    ttk.Label(tableStatus, text="All Tables: ").grid(column=0, row=0)
    #table buttons open up new windows that show table status
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

# opens table status window with parameter of table id
def tbStatWindow(tbid):
    
    tableStat = Toplevel(root)
    tableStat.title('Table ' + str(tbid))
    ttk.Label(tableStat,text="Status: "+ str(printTBstat(tbid-1))).grid(column=0,row=0)

    #if the table is available, allow host to assign waitstaff to table
    if str(printTBstat(tbid-1)) == "Available":
        empList = ["John", "George", "Paul", "Ringo"]
        ttk.Label(tableStat,text="Select Waitstaff: ").grid(column=0,row=3)
        wsMenu = StringVar(tableStat)
        wsMenu.set("John")

        wsmenu1 = ttk.OptionMenu(tableStat, wsMenu, *empList).grid(column=1,row=3)
        
        ttk.Button(tableStat,text="Submit",command=(lambda: assignWaitstaff(wsMenu.get()))).grid(column=1,row=4)
    # if table is occupied, only option can be to reset the table. This is when a customer finishes eating and goes to pay their bill.
    elif str(printTBstat(tbid-1)) == "Occupied":
        ttk.Button(tableStat,text="Reset Table",command =(lambda: resetTable())).grid(column=1,row=4)

    # resets the table back to being Dirty and Empty
    def resetTable():
        newFile = open("tempCSV.csv",'w',newline="")
        file = open("hostTableCSV.csv")
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
        os.remove("hostTableCSV.csv")
        old_name = r"tempCSV.csv"
        new_name = r"hostTableCSV.csv"
        os.rename(old_name,new_name)
        tableStat.destroy()
    def assignWaitstaff(waitstaffName):
        newFile = open("tempCSV.csv",'w',newline="")
        file = open("hostTableCSV.csv")
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



########################################################################################



#Shows the cooks what needs to be made next:
def cookOrders():
    print("the cook's order list")

########################################################################################
def busserTables():
    tableStatus = Toplevel(root)
    tableStatus.title("Busser Table View")
    ttk.Label(tableStatus, text="All Tables: ").grid(column=0, row=0)
    #currently all table buttons only shut down the program
    ttk.Button(tableStatus, text="Table 1", command=(lambda: busWindow(1))).grid(column=0, row=1)
    ttk.Button(tableStatus, text="Table 2", command=(lambda: busWindow(2))).grid(column=0, row=2)
    ttk.Button(tableStatus, text="Table 3", command=(lambda: busWindow(3))).grid(column=0, row=3)
    ttk.Button(tableStatus, text="Table 4", command=(lambda: busWindow(4))).grid(column=1, row=1)
    ttk.Button(tableStatus, text="Table 5", command=(lambda: busWindow(5))).grid(column=1, row=2)
    ttk.Button(tableStatus, text="Table 6", command=(lambda: busWindow(6))).grid(column=1, row=3)
    ttk.Button(tableStatus, text="Table 7", command=(lambda: busWindow(7))).grid(column=2, row=1)
    ttk.Button(tableStatus, text="Table 8", command=(lambda: busWindow(8))).grid(column=2, row=2)
    ttk.Button(tableStatus, text="Table 9", command=(lambda: busWindow(9))).grid(column=2, row=3)
    ttk.Label(tableStatus, text="").grid(column=2, row=4)
    ttk.Button(tableStatus, text="Exit", command=tableStatus.destroy).grid(column=2, row=5)

def busWindow(tbid):

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
        
  

########################################################################################
#main
root = tkinter.Tk(className="Login",)
root.title("Login")
root.geometry("500x500")
root.grid()

#lets find out what role everyone is
ttk.Label(root, text="I am a: ").grid(column=0, row=0)
ttk.Button(root, text="Waiter", command=waiterOrder).grid(column=1, row=0)
ttk.Button(root, text="Cook", command=cookOrders).grid(column=2, row=0)
ttk.Button(root, text="Busser", command=busserTables).grid(column=3, row=0)
ttk.Button(root, text="Host", command=hostTables).grid(column=4, row=0)

ttk.Label(root, text="").grid(column=0, row=2)
exitForm = ttk.Button(root, text="Exit", command=root.destroy).grid(column=4, row=3)


root.mainloop()
