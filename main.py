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

# create the buttons and labels
def setup_buttons():
    global store_details, entry_customer_name, entry_receipt_number, entry_item_hired, entry_number_items_hired, total_entries, delete_item, Combobox
    Button(mw, text="Quit", command=quit).grid(column=3, row=2)
    #Button(mw, text="Receipt Print", command=new_window()).grid(column=3, row=3)
    Button(mw, text="Append Details", command=input_check).grid(column=3, row=4)
    Button(mw, text="Print Details", command=print_store_details).grid(column=3, row=5)
    Label(mw, text="Name").grid(column=0, row=2)

    entry_customer_name = Entry(mw)
    entry_customer_name.grid(column=1, row=2)
    Label(mw, text="Receipt Number").grid(column=0, row=3)
    entry_receipt_number = Entry(mw)
    entry_receipt_number.grid(column=1, row=3)

    Label(mw, text="Item Hired").grid(column=0, row=4)
    item = StringVar()
    # Combo box to allow the user to scroll and choose different items
    entry_item_hired = ttk.Combobox(mw, textvariable=item, state="readonly", values=("BBQ LED_lights Balloons Party_animals"), width = 17)
    entry_item_hired.grid(column=1, row=4)

    Label(mw, text="NO. Hired").grid(column=0, row=5)
    entry_number_items_hired = Entry(mw)
    entry_number_items_hired.grid(column=1, row=5)

    Label(mw, text="Row #").grid(column=0, row=6)
    delete_item = Entry(mw)
    delete_item.grid(column=1, row=6)
    Button(mw, text="Delete", command=delete_row).grid(column=2, row=6)

    # Creating a new window for receipt (Testing phase)
#def new_window():
 #   global entry_receipt_number
  #  # get selected items
   # new = Toplevel(mw)
    #new.geometry("500x500")
    #Label(new, text=("Your Reciept Number:" + entry_receipt_number))

# start the program running
def main():
    global mw
    global store_details, total_entries
    store_details = []
    total_entries = 0
    mw = Tk()
    # The Title
    mw.title("Julies Party Hire Store")
    setup_buttons()
    # This stops the user from being able to make the window larger/smaller
    mw.resizable(False, False)
    mw.mainloop()


main()

