#JULIE'S PARTY HIRE
#Julie runs a party hire store and has a range of items for hire. 
#This program is designed so we can help Julie keep track of items that are currently unavailable


# import tkinter so we can make a GUI
from tkinter import *

# quit subroutine


def quit():
    main_window.destroy()

#print details of the store
def print_store_details ():
    # these are the global variables that are used total_entries, item_count
    global total_entries, item_count
    item_count = 0
    # Create the column headings
    Label(main_window, font='arial 14 bold',
    text="Julie's Party Hire").grid(column=0,row=7)
    Label(main_window, font='arial 14 bold',
    text="Customers Full Name").grid(column=1,row=7)
    Label(main_window, font='arial 14 bold',
    text="Receipt Number").grid(column=2,row=7)
    Label(main_window, font='arial 14 bold',
    text="Item Hired").grid(column=3,row=7)
    Label(main_window, font='arial 14 bold',
    text="Number of Items Hired").grid(column=4,row=7)


    #add each item in the list into its own row
    while item_count < total_entries:
        Label(main_window, text=item_count).grid(column=0, row=item_count+8)
        Label(main_window, text=(camp_details[item_count][0])).grid(
            column=1, row=item_count+8)
        Label(main_window, text=(camp_details[item_count][1])).grid(
            column=2, row=item_count+8)
        Label(main_window, text=(camp_details[item_count][2])).grid(
            column=3, row=item_count+8)
        Label(main_window, text=(camp_details[item_count][3])).grid(
            column=4, row=item_count+8)
        item_count += 1

# Check the inputs are all valid


def check_inputs():
    # these are the global variables that are used
    global camp_details, entry_leader, entry_location, entry_campers, entry_weather, total_entries
    input_check = 0
    Label(main_window, text="               ") .grid(column=2, row=0)
    Label(main_window, text="               ") .grid(column=2, row=1)
    Label(main_window, text="               ") .grid(column=2, row=2)
    Label(main_window, text="               ") .grid(column=2, row=3)
    # Check that leader is not blank, set error text if blank
    if len(entry_leader.get()) == 0:
        Label(main_window, fg="red", text="Required") .grid(column=2, row=0)
        input_check = 1
    # Check that location is not blank, set error text if blank
    if len(entry_location.get()) == 0:
        Label(main_window, fg="red", text="Required") .grid(column=2, row=1)
        input_check = 1
    # Check the number of campers is not blank and between 5 and 10, set error text if blank
    if (entry_campers.get().isdigit()):
        if int(entry_campers.get()) < 5 or int(entry_campers.get()) > 10:
            Label(main_window, fg="red", text="5-10 only") .grid(column=2, row=2)
            input_check = 1
    else:
        Label(main_window, fg="red", text="5-10 only") .grid(column=2, row=2)
        input_check = 1
    # Check that weather is not blank, set error text if blank
    if len(entry_weather.get()) == 0:
        Label(main_window, fg="red", text="Required") .grid(column=2, row=3)
        input_check = 1
    if input_check == 0:
        append_name()

# add the next camper to the list


def append_name():
    # these are the global variables that are used
    global camp_details, entry_leader, entry_location, entry_campers, entry_weather, total_entries
    # append each item to its own area of the list
    camp_details.append([entry_leader.get(), entry_location.get(),
                         entry_campers.get(), entry_weather.get()])
    # clear the boxes
    entry_leader.delete(0, 'end')
    entry_location.delete(0, 'end')
    entry_campers.delete(0, 'end')
    entry_weather.delete(0, 'end')
    total_entries += 1

# delete a row from the list


def delete_row():
    # these are the global variables that are used
    global camp_details, delete_item, total_entries, name_count
    # find which row is to be deleted and delete it
    del camp_details[int(delete_item.get())]
    total_entries = total_entries - 1
    delete_item.delete(0, 'end')
    # clear the last item displayed on the GUI
    Label(main_window, text="       ").grid(column=0, row=name_count+7)
    Label(main_window, text="       ").grid(column=1, row=name_count+7)
    Label(main_window, text="       ").grid(column=2, row=name_count+7)
    Label(main_window, text="       ").grid(column=3, row=name_count+7)
    Label(main_window, text="       ").grid(column=4, row=name_count+7)
    # print all the items in the list
    print_camp_details()

# create the buttons and labels


def setup_buttons():
    # these are the global variables that are used
    global camp_details, entry_leader, entry_location, entry_campers, entry_weather, total_entries, delete_item
    # create all the empty and default labels, buttons and entry boxes. Put them in the correct grid location
    Label(main_window, text="Leader") .grid(column=0, row=0, sticky=E)
    entry_leader = Entry(main_window)
    entry_leader.grid(column=1, row=0)
    Label(main_window, text="Location") .grid(column=0, row=1, sticky=E)
    entry_location = Entry(main_window)
    entry_location.grid(column=1, row=1)
    Button(main_window, text="Quit", command=quit,
           width=10) .grid(column=4, row=0, sticky=E)
    Button(main_window, text="Append Details",
           command=check_inputs) .grid(column=3, row=1)
    Button(main_window, text="Print Details", command=print_camp_details,
           width=10) .grid(column=4, row=1, sticky=E)
    Label(main_window, text="No of Campers") .grid(column=0, row=2, sticky=E)
    entry_campers = Entry(main_window)
    entry_campers.grid(column=1, row=2)
    Label(main_window, text="Weather") .grid(column=0, row=3, sticky=E)
    entry_weather = Entry(main_window)
    entry_weather.grid(column=1, row=3)
    Label(main_window, text="Row #") .grid(column=3, row=2, sticky=E)
    delete_item = Entry(main_window)
    delete_item .grid(column=4, row=2)
    Button(main_window, text="Delete Row", command=delete_row,
           width=10) .grid(column=4, row=3, sticky=E)
    Label(main_window, text="               ") .grid(column=2, row=0)

# start the program running


def main():
    # these are the global variables that are used
    global main_window
    global camp_details, entry_name, entry_age, entry_gender, total_entries
    # create empty list for camp details and empty variable for entries in the list
    camp_details = []
    total_entries = 0
    # create the GUI and start it up
    main_window = Tk()
    setup_buttons()
    main_window.mainloop()


main()