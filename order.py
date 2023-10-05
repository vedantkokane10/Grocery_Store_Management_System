import mysql.connector
import tkinter as tk
from tkinter import ttk,messagebox
from tkinter import *

def create_window():

    # Logic Part
    global displayed

    displayed= 0
    # insertion of values
    def getValue(event):
        cols = ('orderId','customerName','productId','quantity','employeeId')
        listbox = ttk.Treeview(root,columns=cols,show='headings')
        # first delete the existing records
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        # e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        row_id = listBox.selection()[0]
        select = listBox.set(row_id)
        e1.insert(0,select['orderId'])
        e2.insert(0,select['customerName'])
        e3.insert(0,select['productId'])
        # e4.insert(0,select['price'])
        e5.insert(0,select['quantity'])
        e6.insert(0,select['employeeId'])


    # adding/creating new Data
    # adding/creating new Data
    def Add():
        orderId = e1.get()
        name = e2.get()
        productId = e3.get()
        quantity = e5.get()
        employeeId = e6.get()
        db = mysql.connector.connect(host="127.0.0.1", user="root", passwd="vedant123", database="GroceryStore")
        cursor = db.cursor()
        
        try:
            cursor.execute(f"SELECT quantity, price FROM Product WHERE productId = {productId}")
            row = cursor.fetchone()
            
            if row is not None:
                amount = row[0]
                price_per_unit = row[1]
                cursor.execute(f"SELECT employeeId FROM Employee WHERE employeeId = {employeeId}")
                row = cursor.fetchone()

                if row is not None:
                    if amount >= int(quantity):
                        price = price_per_unit * int(quantity)
                        cursor.execute(f"INSERT INTO OrderDetails VALUES ({orderId}, '{name}', {productId}, {price}, {quantity}, {employeeId})")
                        db.commit()
                        print("Data added successfully")
                        total = amount - int(quantity)
                        cursor.execute(f"UPDATE Product SET quantity = {total} WHERE productId = {productId}")
                        db.commit()
                        messagebox.showinfo("Information", "Data updated Successfully !")
                        e1.delete(0, END)
                        e2.delete(0, END)
                        e3.delete(0, END)
                        e5.delete(0, END)
                        e6.delete(0, END)
                        e1.focus_set()
                    else:
                        messagebox.showinfo("Information", "Order cannot be placed as not enough quantity of the product available.")
                else:
                    messagebox.showinfo("Information", "Employee not found.")
            else:
                messagebox.showinfo("Information", "Product not found.")
        except Exception as e:
            print("error")
            print(e)
            db.rollback()
        finally:
            db.close()




    # deleting  Data
    def Delete():
        orderId = e1.get()
        db = mysql.connector.connect(host="127.0.0.1", user="root", passwd="vedant123",database="GroceryStore")
        cursor = db.cursor()
        try:
            cursor.execute(f"delete from OrderDetails where orderId = {orderId}")
            db.commit()
            print("Data deleted successfully")
            messagebox.showinfo("information","Data deleted Successfully !")
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
            e5.delete(0,END)
            e1.focus_set()
        except Exception as e:
            print("error")
            print(e)
            db.rollback()
            db.close()

    # updating  Data
    def Update():
        orderId = e1.get()
        name = e2.get()
        productId = e3.get()
        # price = e4.get()
        quantity = e5.get()
        employeeId = e6.get()
        db = mysql.connector.connect(host="127.0.0.1", user="root", passwd="vedant123",database="GroceryStore")
        cursor = db.cursor()
        try:
            cursor.execute(f"update OrderDetails set customerName = '{name}' , productId = {productId} , price = {price} , quantity = {quantity} , employeeId = {employeeId} where orderId = {orderId}")
            db.commit()
            print("Data updated successfully")
            messagebox.showinfo("information","Data Updated Successfully !")
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
            e5.delete(0,END)
            e1.focus_set()
        except Exception as e:
            print("error")
            print(e)
            db.rollback()
            db.close()

    def Show():
        # for displaying the data
        cols = ('Order id','Customer name','Product id','Price','Quantity','Employee id')
        listbox = ttk.Treeview(root,columns=cols,show='headings')
        for col in cols:
            listbox.heading(col,text=col)
            listbox.column(col, anchor="center")
            listbox.grid(row=1,column=0,columnspan=2)
            listbox.place(x = 10, y = 300)
        db = mysql.connector.connect(host="127.0.0.1", user="root", passwd="vedant123",database="GroceryStore")
        cursor = db.cursor()
        cursor.execute("select * from OrderDetails")
        result = cursor.fetchall()
        for i, (orderId,name,productId,price,quantity,employeeId) in enumerate(result,start=1):
            listbox.insert("","end",value=(orderId,name,productId,price,quantity,employeeId))
        db.close()
        listbox.bind('<Double-Button-1>',getValue)



    # Design part 
    root = Tk()


    root.geometry("1000x900")

    global e1
    global e2
    global e3
    # global e4
    global e5
    global e6
    tk.Label(root,text="Place a new Order",fg="grey",font=(None,30)).place(x=400,y=5)


    tk.Label(root,text="Order id").place(x=10,y=10) # this is label i.e text
    Label(root,text="Customer Name").place(x=10,y=40)
    Label(root,text="Product id").place(x=10,y=70)
    # Label(root,text="Price").place(x=10,y=100)
    Label(root,text="Quantity").place(x=10,y=130)
    Label(root,text="Employee id").place(x=10,y=160)

    # adding text boxes
    e1 = Entry(root)
    e1.place(x=140, y=10)

    e2 = Entry(root)
    e2.place(x=140, y=40)

    e3 = Entry(root)
    e3.place(x=140, y=70)

    # e4 = Entry(root)
    # e4.place(x=140, y=100)

    e5 = Entry(root)
    e5.place(x=140, y=130)

    e6 = Entry(root)
    e6.place(x=140, y=160)

    # adding  buttons
    Button(root, text = "Add" , command = Add, height = 3, width = 13).place(x=30,y=200) 
    Button(root, text = "Delete" , command = Delete, height = 3, width = 13).place(x=190,y=200) 
    Button(root, text = "Update" , command = Update, height = 3, width = 13).place(x= 350,y=200) 
    Button(root, text = "Show" , command = Show, height = 3, width = 13).place(x= 530,y=200) 
   # Button(root, text = "Deleted" , command = Deleted, height = 3, width = 13).place(x= 730,y=140) 
    root.mainloop() 


if __name__ == "__main__":
    root = tk.Tk()
    create_window()
    root.mainloop()

