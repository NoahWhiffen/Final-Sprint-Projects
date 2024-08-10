# Title: Python Final Sprint - Menu Option 8
# Description: A program to generate a summary of 
#              all the data populating the data files.
# Author:      Noah Whiffen - SD12 - Robot Group 9
# Date:        August 10th, 2024 -

# Define required libraries.

import datetime

# Define program constants.

currDate = datetime.datetime.now()
currDateFormat = currDate.strftime("%Y-%M-%d")
with open("defaults.dat", "r") as file:
    f = file.readlines()
    nextTransNum = f[0].strip()
    nextDriverNum = f[1].strip()
    standFee = float(f[2].strip())
    dailyRentFee = float(f[3].strip())
    weekRentFee = float(f[4].strip())
    HSTRate = float(f[5].strip())

# Program functions.

def employeeFile():
    try:
        with open("employees.dat", "r") as file:
            lines = file.readlines()
            empHeader = lines[0].strip()
            for line in lines[1:]:
                employeeData = line.strip().split(", ")
                driverNum = employeeData[0]
                name = employeeData[1]
                address = employeeData[2]
                phoneNum = employeeData[3]
                licenseNum = employeeData[4]
                licenseExpDate = employeeData[5]
                insProvider = employeeData[6]
                policyNum = employeeData[7]
                carOwner = employeeData[8]
                balDue = employeeData[9]
                return empHeader, driverNum, name, address, phoneNum, licenseNum, licenseExpDate, insProvider, policyNum, carOwner, balDue
    except FileNotFoundError:
        with open("employees.dat", "a") as file:
            file.write("Driver #, Name, Address, Phone #, License #, License Exp. Date, Insurance Provider, Ins. Policy #, Car Owner, Bal. Due\n")

def revenueFile():
    try:
        with open("revenue.dat", "r") as file:
            lines = file.readlines()
            revHeader = lines[0].strip()
            for line in lines[1:]:
                revenueData = line.strip().split(", ")
                transID = revenueData[0]
                revDriverNum = revenueData[1]
                transDate = revenueData[2]
                transDesc = revenueData[3]
                transAmt = revenueData[4]
                hst = revenueData[5]
                total = revenueData[6]
                return revHeader, transID, revDriverNum, transDate, transDesc, transAmt, hst, total
    except FileNotFoundError:
        with open("revenue.dat", "a") as file:
                file.write("Trans. ID, Driver #, Trans. Date, Trans. Desc., Trans. Amt., HST, total\n")

def expensesFile():
    try:
        with open("expenses.dat", "r") as file:
            lines = file.readlines()
            expHeader = lines[0].strip()
            for line in lines[1:]:
                expData = line.strip().split(", ")
                invNum = expData[0]
                invDate = expData[1]
                driverNum = expData[2]
                itemNum = expData[3]
                itemDesc = expData[4]
                itemCost = expData[5]
                itemQuantity = expData[6]
                itemTotal = expData[7]
                subtotal = expData[8]
                hst = expData[9]
                total = expData[10]
                return expHeader, invNum, invDate, driverNum, itemNum, itemDesc, itemCost, itemQuantity, itemTotal, subtotal, hst, total
    except FileNotFoundError:
        with open("expenses.dat", "a") as file:
            file.write("Invoice #, Invoice Date, Driver #, Item #, Item Desc., Item Cost, Item Quantity, Item Total, subtotal, HST, total\n")


# Main program starts here:


employeeFile()
revenueFile()
expensesFile()

# Generate report headings.
print()
print(f"HAB Taxi Services Summary Report as of {currDateFormat:<9s} ")
print()

# Initialize counters and accumulators.

driverCtr = 0
invCtr = 0
transCtr = 0
itemCtr = 0

invAcc = 0
balDueAcc = 0
transAcc = 0
revTotAcc = 0
expTotAcc = 0


