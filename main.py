import tkinter as tk
from tkinter import ttk,messagebox
from tkinter import *
import product
import order
import employee
import report

def open_window1():
    product.create_window()

def open_window2():
    order.create_window()

def open_window3():
    report.create_window()

def open_window4():
    employee.create_window()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Grocery Store Management")
    root.geometry("800x500")
    Button(root, text = "Add new Prodcut" , command = open_window1, height = 3, width = 13).place(x=325,y=100)
    Button(root, text = "Place a new Order" , command = open_window2, height = 3, width = 13).place(x=325,y=200)
    Button(root, text = "Report on sales" , command = open_window3, height = 3, width = 13).place(x=325,y=300)
    Button(root, text = "Manage Employee" , command = open_window4, height = 3, width = 13).place(x=325,y=400)
    root.mainloop()
