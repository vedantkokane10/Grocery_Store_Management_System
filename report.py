import mysql.connector
import tkinter as tk
from tkinter import ttk,messagebox
from tkinter import *


def create_window():
    root = Tk()


    root.geometry("1000x900")

    def Show():
        # for displaying the data
        cols = ('Employee id','Employee name','Total No of orders','Amount')
        listbox = ttk.Treeview(root,columns=cols,show='headings')
        for col in cols:
            listbox.heading(col,text=col)
            listbox.column(col, anchor="center")
            listbox.grid(row=1,column=0,columnspan=2)
            listbox.place(x = 100, y = 180)
        db = mysql.connector.connect(host="127.0.0.1", user="root", passwd="Password",database="GroceryStore")
        cursor = db.cursor()
        cursor.execute("SELECT Employee.employeeId, Employee.name, COUNT(OrderDetails.orderId), SUM(OrderDetails.price) FROM Employee INNER JOIN OrderDetails ON Employee.employeeId = OrderDetails.employeeId GROUP BY Employee.employeeId, Employee.name")
        result = cursor.fetchall()
        for i, (id,name,total,amount) in enumerate(result,start=1):
            listbox.insert("","end",value=(id,name,total,amount))
        db.close()
        



    tk.Label(root,text="Report on Sales",fg="grey",font=(None,30)).place(x=420,y=5)
    Button(root, text = "Show" , command = Show, height = 3, width = 13).place(x= 450,y=100) 
if __name__ == "__main__":
    root = tk.Tk()
    create_window()
    root.mainloop()
