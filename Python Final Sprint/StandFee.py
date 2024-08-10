# Title:       Python Final Sprint - Stand Fee
# Description: A program to calculate the 
#              stand fee for HAB Taxi Services
# Author:      Noah Whiffen - SD12 - Robot Group 9
# Date:        August 6th, 2024 - 


# Program libraries

import datetime

# Program functions

def paymentDate():
    today = datetime.datetime.today()
    if today.month == 12:
        firstPayment = today.replace(year=today.year + 1, month=1, day=1)
    else:
        firstPayment = today.replace(month=today.month + 1, day=1)
    return firstPayment


def employeeFile():
    global empHeader, driverNum, name, address, phoneNum, licenseNum, licenseExpDate, insProvider, policyNum, carOwner, balDue
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
    global revHeader, transID, revDriverNum, transDate, transDesc, transAmt, hst, total
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

# Constants.
with open("defaults.dat", "r") as file:
    f = file.readlines()
    nextTransNum = f[0].strip()
    nextDriverNum = f[1].strip()
    standFee = float(f[2].strip())
    dailyRentFee = float(f[3].strip())
    weekRentFee = float(f[4].strip())
    HSTRate = float(f[5].strip())

today = datetime.datetime.today()

# Calculations

standFeeHST = standFee * HSTRate
standFeeTotal = standFeeHST + standFee


# Main program starts here.

while True:
    if today.day == 1:
        employeeFile()
        revenueFile()
        if name == carOwner:
            newTransNum = nextTransNum
            nextTransNum += 1
            newDriverNum = nextDriverNum
            nextDriverNum += 1
            with open("revenue.dat", "a") as f:
                f.write(f"{nextTransNum}, {paymentDate}, Monthly Stand Fees, {nextDriverNum}, {standFee}, {standFeeHST}, {standFeeTotal} ")
                

    # The balance due will be updated next.
