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
        cols = ('productId','name','quantity','category','price')
        listbox = ttk.Treeview(root,columns=cols,show='headings')
        # first delete the existing records
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        row_id = listBox.selection()[0]
        select = listBox.set(row_id)
        e1.insert(0,select['productId'])
        e2.insert(0,select['name'])
        e3.insert(0,select['quantity'])
        e4.insert(0,select['category'])
        e5.insert(0,select['price'])


    # adding/creating new Data
    def Add():
        id = e1.get()
        name = e2.get()
        quantity = e3.get()
        category = e4.get()
        price = e5.get()
        db = mysql.connector.connect(host="127.0.0.1", user="root", passwd="Password",database="GroceryStore")
        cursor = db.cursor()
        try:
            cursor.execute(f"insert into Product values({id},'{name}',{quantity},'{category}',{price})")
            db.commit()
            print("Data added successfully")
            messagebox.showinfo("information","Data updated Successfully !")
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


    # deleting  Data
    def Delete():
        id = e1.get()
        name = e2.get()
        quantity = e3.get()
        category = e4.get()
        price = e5.get()
        db = mysql.connector.connect(host="127.0.0.1", user="root", passwd="Password",database="GroceryStore")
        cursor = db.cursor()
        try:
            cursor.execute(f"delete from Product where productId = {id}")
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
        id = e1.get()
        name = e2.get()
        quantity = e3.get()
        category = e4.get()
        price = e5.get()
        db = mysql.connector.connect(host="127.0.0.1", user="root", passwd="Password",database="GroceryStore")
        cursor = db.cursor()
        try:
            cursor.execute(f"update  Product set name = '{name}' , quantity = {quantity} , category = '{category}' , price = {price} where productId = {id}")
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
        cols = ('Product id','Product name','Quantity','Category','Price')
        listbox = ttk.Treeview(root,columns=cols,show='headings')
        for col in cols:
            listbox.heading(col,text=col)
            listbox.column(col, anchor="center")
            listbox.grid(row=1,column=0,columnspan=2)
            listbox.place(x = 10, y = 300)
        db = mysql.connector.connect(host="127.0.0.1", user="root", passwd="Password",database="GroceryStore")
        cursor = db.cursor()
        cursor.execute("select * from Product")
        result = cursor.fetchall()
        for i, (id,name,Quantity,Category,Price) in enumerate(result,start=1):
            listbox.insert("","end",value=(id,name,Quantity,Category,Price))
        db.close()
        listbox.bind('<Double-Button-1>',getValue)



    # Design part 
    root = Tk()


    root.geometry("1000x900")

    global e1
    global e2
    global e3
    global e4
    global e5

    tk.Label(root,text="Add new Product",fg="grey",font=(None,30)).place(x=400,y=5)


    tk.Label(root,text="Product id").place(x=10,y=10) # this is label i.e text
    Label(root,text="Product Name").place(x=10,y=40)
    Label(root,text="Quanity").place(x=10,y=70)
    Label(root,text="Category").place(x=10,y=100)
    Label(root,text="Price").place(x=10,y=130)

    # adding text boxes
    e1 = Entry(root)
    e1.place(x=140, y=10)

    e2 = Entry(root)
    e2.place(x=140, y=40)

    e3 = Entry(root)
    e3.place(x=140, y=70)

    e4 = Entry(root)
    e4.place(x=140, y=100)

    e5 = Entry(root)
    e5.place(x=140, y=130)


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
