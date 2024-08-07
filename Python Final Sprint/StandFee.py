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
   # global header, driverNum, name, address, phoneNum, licenseNum, licenseExpDate, insProvider, policyNum, carOwner, balDue
    try:
        with open("employees.dat", "r") as file:
            header = "Driver #, Name, Address, Phone #, License #, License Exp. Date, Insurance Provider, Ins. Policy #, Car Owner, Bal. Due"
            lines = file.readlines.split(", ")
            driverNum = lines[0]
            name = lines[1]
            address = lines[2]
            phoneNum = lines[3]
            licenseNum = lines[4]
            licenseExpDate = lines[5]
            insProvider = lines[6]
            policyNum = lines[7]
            carOwner = lines[8]
            balDue = lines[9]
            return header, driverNum, name, address, phoneNum, licenseNum, licenseExpDate, insProvider, policyNum, carOwner, balDue
    except FileNotFoundError:
        with open("employees.dat", "a") as file:
            header = "Driver #, Name, Address, Phone #, License #, License Exp. Date, Insurance Provider, Ins. Policy #, Car Owner, Bal. Due"
            return header, driverNum, name, address, phoneNum, licenseNum, licenseExpDate, insProvider, policyNum, carOwner, balDue

# Main program starts here.

while True:
    
    if carOwner == name: