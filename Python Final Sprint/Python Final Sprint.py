# Title:       Python Final Sprint
# Description: A program for HAB Taxi 
#              Services to record expenses.
# Author:      Noah Whiffen - SD12 - Robot Group 9
# Date:        August 3rd, 2024 - 


# Import required libraries.

import datetime

# Constants and variables
invNum = 20
invDate = datetime.datetime.now()
invDateFormat = invDate.strftime('%Y-%M-%d')
HST_RATE = 0.15
subtotal = 0 # initialize subtotal

# Declare program functions.

def getLastInvNum(invNum):
    try:
        with open("expenses.dat", "r") as f:
            lines = f.readlines()
            if lines:
                lastLine = lines[-1].strip()
                lastID = int(lastLine.split(',')[0].strip()) + 1
                return lastID + 1
            else:
                return invNum
    except FileNotFoundError:
        return invNum



def updateFile():
    header = "Invoice #, Invoice Date, Driver #, Item #, Item Desc., Item Cost, Item Quantity, Item Total, subtotal, HST, total\n"
    try:
        with open("expenses.dat", "a") as f:
            f.write(f"{invNum}")
            f.write(f"{invDateFormat}")
            f.write(f"{driverNum}")
            f.write(f"{itemNum}")
            f.write(f"{descript}")
            f.write(f"{cost}")
            f.write(f"{quantity}")
            f.write(f"{itemTotal}")
            f.write(f"{hst}")
            f.write(f"{subtotal}")
            f.write(f"{total}")
    except FileNotFoundError:
        with open("expenses.dat", "w") as f:
            f.write(header)

# Main program starts here.

while True:

    # Parse values from file and apply to constants.

    # Collect User inputs.
    print()
    print("---------------------------------------")
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
        cost = input("Enter cost of item: ")
        if cost.isdigit():
            cost = float(cost)
            break
        else:
            print("Please enter a number.")
    while True:
        quantity = input("Enter the quantity of the item: ")
        if quantity.isdigit():
            quantity = float(quantity)
            break
        else:
            print("Please enter a number.")
    
    # Perform required calculations.

    itemTotal = cost * quantity
    subtotal += itemTotal
    hst = subtotal * HST_RATE
    total = subtotal + hst
    # Append info to file.
    
    getLastInvNum(invNum)
    invNum += 1
    updateFile()
    
    # Output values.
    print("----------------------------------------------------------")
    print()
    print()
    print("       HAB Taxi Services Expense Report")
    print("------------------------------------------------")
    print(f"Invoice #:  {invNum}             Invoice Date:  {invDateFormat}")
    print(f"Driver #:   {driverNum}")
    print(f"Item #:     {itemNum}           Item Desc.:    {descript}")
    print("----------------------------------------------------------")
    print(f"Item Cost:  {cost}           Item Quantity: {quantity}")
    print(f"Item Total: {itemTotal}          HST:           {hst}")
    print(f"subtotal:   {subtotal}          Total:         {total}")

    # Prompt to create another invoice.
    cont = input("Would you like to create another invoice?(Y/N): ").upper()
    if cont