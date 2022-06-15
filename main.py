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

        # This allows the user to Append the details

def append_name():
    global store_details, entry_customer_name, entry_receipt_number, entry_item_hired, entry_number_items_hired, total_entries, entries

    # Lists all possible boxes able to be filled and adds it to the rows
    entries = str([entry_customer_name, entry_receipt_number, entry_item_hired, entry_number_items_hired])
    store_details.append([entry_customer_name.get(), entry_receipt_number.get(), entry_item_hired.get(), entry_number_items_hired.get()])
    # This clears out the old information after the details have been appended
    entry_customer_name.delete(0, 'end')
    entry_receipt_number.delete(0, 'end')
    entry_item_hired.delete(0, 'end')
    entry_number_items_hired.delete(0, 'end')
    total_entries += 1


    global error_check
    error_check = 0
    if len(entry_customer_name.get()) == 0:
        # error message box will be displayed
        messagebox.showerror("Customer name", "Item name is required")
        # error check will equal 1
        error_check = 1
# if nothing is inputted into number entry
    if len(entry_number_items_hired.get()) == 0:
        # error message box will be displayed
        messagebox.showerror("Quantity Hired", "Item quantity is required")
        error_check = 1
    if len(entry_number_items_hired.get()) == 0:
        # error message box will be displayed
        messagebox.showerror("Quantity Hired", "Item quantity is required")
        error_check = 1
    if len(entry_number_items_hired.get()) == 0:
        # error message box will be displayed
        messagebox.showerror("Quantity Hired", "Item quantity is required")
        error_check = 1

    # if error check is 0
    if error_check == 0:
        # append details function will be excecuted
        
        
        # delete a row from the list
def delete_row():
    global store_details, delete_item, total_entries, item_count
    del store_details[int(delete_item.get())]
    total_entries = total_entries - 1
    delete_item.delete(0, 'end')

    # This deletes each items label
    Label(mw, text="       ").grid(column=0, row=item_count + 7)
    Label(mw, text="       ").grid(column=1, row=item_count + 7)
    Label(mw, text="       ").grid(column=2, row=item_count + 7)
    Label(mw, text="       ").grid(column=3, row=item_count + 7)
    Label(mw, text="       ").grid(column=4, row=item_count + 7)
    print_store_details()
