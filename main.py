#JULIE'S PARTY HIRE
#Julie runs a party hire store and has a range of items for hire. 
#This program is designed so we can help Julie keep track of items that are currently unavailable

# import tkinter so we can make a GUI
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


# quit subroutine
def quit():
    root.destroy()
#print details of the store
def print_store_details():
    global item_count, total_entries, main_color
    item_count = 0
    # Main labels
    Label(root, font='bold', text="Row").grid(column=0, row=7)
    Label(root, font='bold', text="Name").grid(column=1, row=7)
    Label(root, font='bold', text="Receipt Number").grid(column=2, row=7)
    Label(root, font='bold', text="Item Hired").grid(column=3, row=7)
    Label(root, font='bold', text="Num. Items Hired").grid(column=4, row=7)

    while item_count < total_entries:
        Label(root, text=item_count).grid(column=0, row=item_count + 8)
        Label(root, text=(store_details[item_count][0])).grid(column=1, row=item_count + 8)
        Label(root, text=(store_details[item_count][1])).grid(column=2, row=item_count + 8)
        Label(root, text=(store_details[item_count][2])).grid(column=3, row=item_count + 8)
        Label(root, text=(store_details[item_count][3])).grid(column=4, row=item_count + 8)
        item_count += 1

        # This allows the user to Append the details


def check_inputs():
    # these are the global variables that are used
    global store_details, entry_customer_name, entry_receipt_number, entry_item_hired, main_color, entry_number_items_hired, total_entries
    input_check = 0
    Label(root, text="                                   ") .grid(column=2, row=2)
    Label(root, text="                                   ") .grid(column=2, row=3)
    Label(root, text="                                   ") .grid(column=2, row=4)
    Label(root, text="                                   ") .grid(column=2, row=5)
    # Check that Customers_Full_Name is not blank, set error text if blank
    if len(entry_customer_name.get()) == 0:
        Label(root, fg="red", text="Required/letters only", bg=main_color) .grid(column=2, row=2)
        input_check = 1 
    # Check that Item_Hired is not blank, set error text if blank


    # Check the Number_of_Items_Hired is not blank and between 1 and 500, set error text if blank
    if ( entry_number_items_hired.get().isdigit()):
        if int( entry_number_items_hired.get()) < 1 or int( entry_number_items_hired.get()) > 500:
            Label(root, fg="red", text="1-500 only", bg=main_color) .grid(column=2, row=5)
            input_check = 1
            
    else:
        Label(root, fg="red", text="Required/1-500", bg=main_color) .grid(column=2, row=5)
        input_check = 1
    # Check that Receipt Number is not blank, set error text if blank
    if len(entry_receipt_number.get()) == 0:
        Label(root, fg="red", text="Required/number only", bg=main_color) .grid(column=2, row=3)
        input_check = 1
    if input_check == 0:
       append_name()


 
def append_name():
    global store_details, entry_customer_name, entry_receipt_number, entry_item_hired, main_color, entry_number_items_hired, total_entries, entries

    # Lists all possible boxes able to be filled and adds it to the rows
    entries = str([entry_customer_name, entry_receipt_number, entry_item_hired, entry_number_items_hired])
    store_details.append([entry_customer_name.get(), entry_receipt_number.get(), entry_item_hired.get(), entry_number_items_hired.get()])
    # This clears out the old information after the details have been appended
    entry_customer_name.delete(0, 'end')
    entry_receipt_number.delete(0, 'end')
    entry_item_hired.delete(0, 'end')
    entry_number_items_hired.delete(0, 'end')
    total_entries += 1


def delete_row():
    global store_details, delete_item, total_entries, item_count
    del store_details[int(delete_item.get())]
    total_entries = total_entries - 1
    delete_item.delete(0, 'end')

    # This deletes each items label
    Label(root, text="       ").grid(column=0, row=item_count + 7)
    Label(root, text="       ").grid(column=1, row=item_count + 7)
    Label(root, text="       ").grid(column=2, row=item_count + 7)
    Label(root, text="       ").grid(column=3, row=item_count + 7)
    Label(root, text="       ").grid(column=4, row=item_count + 7)
    print_store_details()

# create the buttons and labels to help Julie know what she needs to type 
def setup_buttons():
    global main_color
    global store_details, entry_customer_name, entry_receipt_number, entry_item_hired, entry_number_items_hired, total_entries, delete_item, Combobox
    Button(root, text="Quit", command=quit).grid(column=3, row=2)
    #Button(root, text="Receipt Print", command=new_window()).grid(column=3, row=3)
    Button(root, text="Append Details", command=check_inputs).grid(column=3, row=4)
    Button(root, text="Print Details", command=print_store_details).grid(column=3, row=5)
    Label(root, text="Name", bg=main_color).grid(column=0, row=2)

    entry_customer_name = Entry(root)
    entry_customer_name.grid(column=1, row=2)
    Label(root, text="Receipt Number", bg=main_color).grid(column=0, row=3)
    entry_receipt_number = Entry(root)
    entry_receipt_number.grid(column=1, row=3)

    Label(root, text="Item Hired", bg=main_color).grid(column=0, row=4)
    item = StringVar()
    # Combo box to allow the user to scroll and choose different items
    entry_item_hired = ttk.Combobox(root, textvariable=item, state="readonly", values=("Decorations LED_lights Balloons Party_animals Ribbons Confetti Party_Hats Banners Other"), width = 17)
    entry_item_hired.grid(column=1, row=4)


    Label(root, text="NO. Hired", bg=main_color).grid(column=0, row=5)
    entry_number_items_hired = Entry(root)
    entry_number_items_hired.grid(column=1, row=5)

    Label(root, text="Row #", bg=main_color).grid(column=0, row=6)
    delete_item = Entry(root)
    delete_item.grid(column=1, row=6)
    Button(root, text="Delete", command=delete_row).grid(column=2, row=6)



# start the program running
def main():
    global root
    global store_details, total_entries
    global main_color
    main_color = "SpringGreen2"
    store_details = []
    total_entries = 0
    root = Tk()
    # The Title
    root.title("Julies Party Hire Store")
    setup_buttons()
    # This stops the user from being able to make the window larger/smaller
    root.config(bg=main_color)
    root.mainloop()


main()

