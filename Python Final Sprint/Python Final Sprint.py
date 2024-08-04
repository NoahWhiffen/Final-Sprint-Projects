# Title:       Python Final Sprint
# Description: A program for HAB Taxi 
#              Services to record expenses.
# Author:      Noah Whiffen - SD12 - Robot Group 9
# Date:        August 3rd, 2024 - 


# Import required libraries.

import datetime

# Constants and variables
invNum = None
invDate = datetime.datetime.now()
invDateFormat = invDate.strftime('%Y-%M-%d')
HST_RATE = 0.15
subtotal = 0 # initialize subtotal

# Declare program functions.

# Main program starts here.

while True:

    # Parse values from file and apply to constants.

    # Collect User inputs.
    while True:
        driverNum = input("Enter driver's employee number: ")
        if driverNum.isdigit():
            break
        else:
            print("Please enter a number.")
    while True:
        itemNum = input("Enter item number: ")
        if itemNum.isdigit():
            break
        else:
            print("Please enter a number.")
    descript = input("Enter a brief description of item: ")
    while True:
        cost = input("Enter cost of item")
        if cost.isdigit():
            cost = float(cost)
            break
        else:
            print("Please enter a number.")
    while True:
        quantity = input("Enter the quantity of the item: ")
        if quantity.isdigit():
            break
        else:
            print("Please enter a number.")
    
    # Perform required calculations.

    itemTotal = cost * quantity
    subtotal += itemTotal
    hst = subtotal * HST_RATE
    total = subtotal + hst

    # Possibly add Employee pay????

    # Append info to file.

    # Output values.

    print()
    print("       HAB Taxi Services Expense Report")
    print("------------------------------------------------")