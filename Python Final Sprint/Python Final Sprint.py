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
    running = True

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
            quantity = int(quantity)
            break
        else:
            print("Please enter a number.")
    
    # Perform required calculations.

    itemTotal = cost * quantity
    itemTotal = float(itemTotal)
    subtotal += itemTotal
    hst = subtotal * HST_RATE
    total = subtotal + hst
    # Append info to file.
    
    invNum = getLastInvNum(invNum)
    invNum += 1
    updateFile()
    
    # Output values.
    print("----------------------------------------------------------")
    print()
    print()
    print("              HAB Taxi Services Expense Report")
    print("----------------------------------------------------------")
    print(f"Invoice #:  {invNum:>8d}           Invoice Date:  {invDateFormat}")
    print(f"Driver #:   {driverNum:>8s}")
    print(f"Item #:     {itemNum:>8s}           Item Desc.:    {descript:>12s}")
    print("----------------------------------------------------------")
    print(f"Item Cost:   ${cost:>5.2f}           Item Quantity: {quantity:>5d}")
    print(f"Item Total:  ${itemTotal:>5.2f}           HST:           ${hst:>5.2f}")
    print(f"subtotal:    ${subtotal:>5.2f}           Total:         ${total:5.2f}")

    # Prompt to create another invoice.
    while True:
        cont = input("Would you like to create another invoice?(Y/N): ").upper()
        if cont == "N":
            running = False
            break
        elif cont == "Y":
            running = True
            break
        else:
            print("Please enter a Y or an N.")