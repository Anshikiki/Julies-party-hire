#JULIE'S PARTY HIRE
#Julie runs a party hire store and has a range of items for hire. 
#This program is designed so we can help Julie keep track of items that are currently unavailable

# import tkinter so we can make a GUI
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


# quit subroutine
def quit():
    mw.destroy()
#print details of the store
def print_store_details():
    global item_count, total_entries
    item_count = 0
    # Main labels
    Label(mw, font='bold', text="Row").grid(column=0, row=7)
    Label(mw, font='bold', text="Name").grid(column=1, row=7)
    Label(mw, font='bold', text="Receipt Number").grid(column=2, row=7)
    Label(mw, font='bold', text="Item Hired").grid(column=3, row=7)
    Label(mw, font='bold', text="Num. Items Hired").grid(column=4, row=7)

    while item_count < total_entries:
        Label(mw, text=item_count).grid(column=0, row=item_count + 8)
        Label(mw, text=(store_details[item_count][0])).grid(column=1, row=item_count + 8)
        Label(mw, text=(store_details[item_count][1])).grid(column=2, row=item_count + 8)
        Label(mw, text=(store_details[item_count][2])).grid(column=3, row=item_count + 8)
        Label(mw, text=(store_details[item_count][3])).grid(column=4, row=item_count + 8)
        item_count += 1