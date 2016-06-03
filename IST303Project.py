#from Tkinter import *
#root = Tk()
#root.mainloop()
from datetime import *
import csv
import pandas as pd
import numpy as np
import unittest


guest_list = pd.read_csv("IST 303 GuestList.csv", index_col = 0)
#service_list = pd.read_csv("IST 303 services.csv", index_col = 0)


class customer:

    def __init__(self, input_id):
        self.input_id = input_id

    def check_for_cust(self):
        """ This function checks if a customer ID is valid
        """
        for lab, row in guest_list.iterrows():
            if self.input_id == lab:
                #print str(self.input_id) + " is a valid ID"
                self.check_in_date = row['check_in_date']
                self.check_out_date = row['check_out_date']
                self.check_in_time = row['check_in_time']
                self.check_out_time = row['check_out_time']
                self.check_in = datetime.strptime(row['check_in_date'] + " " + row['check_in_time'], '%m/%d/%y %I:%M %p')
                self.check_out = datetime.strptime(row['check_out_date'] + " " + row['check_out_time'], '%m/%d/%y %I:%M %p')
                return True
        #print str(self.input_id) + " is NOT a valid ID"
        return False

    
Reservations = []

class Service(customer):
    def __init__(self, input_id):
        self.input_id = input_id

    def reserve(self, Input_Date, Input_Time, length):
        self.StartTime = datetime.strptime(Input_Date + " " +  Input_Time, '%m/%d/%y %I:%M %p')
        self.length = length
        self.EndTime = self.StartTime + timedelta(minutes = length)
        Reservations.append(self)

class Facial_norm(Service):
    def __init__(self, input_id):
        self.input_id = input_id
        self.service_id = 0

class Facial_col(Service):
    def __init__(self, input_id):
        self.input_id = input_id
        self.service_id = 1


class AvailableService():
    def __init__(self, Input_Date, Input_Time, OpenTime, CloseTime):
        self.ReserveDateTime = datetime.strptime(Input_Date + " " +  Input_Time, '%m/%d/%y %I:%M %p')
        self.ReserveTime = datetime.strptime(Input_Time, '%I:%M %p')
        self.OpenTime = datetime.strptime("8:00 AM", '%I:%M %p')
        self.CloseTime = datetime.strptime("8:00 PM", '%I:%M %p')
    
    def Check(self):
        ServiceList = ["Facial Norm", "Facial Collagen"]
        NotAvailable = []
        if self.ReserveTime > self.CloseTime or self.ReserveTime < self.OpenTime:
            print("Not in the range of OpenTime and CloseTime")
            return 
    
        for EachResevation in Reservations:
            if EachResevation.StartTime - timedelta(minutes = EachResevation.length) < self.ReserveDateTime or self.ReserveDateTime < EachResevation.EndTime:
                NotAvailable.append(EachResevation.service_id)
        print(NotAvailable)
        for i in range(0, 2, 1):
            if i not in NotAvailable:
                print(ServiceList[i])





CustomerInstance = customer(102)
FN1 = Facial_norm(102)
FN1.reserve("5/22/16", "8:00 AM", 60)
print(Reservations[0].EndTime)

AS = AvailableService("5/22/16", "8:00 AM", "8:00 AM", "8:00 PM")
AS.Check()

#print "\n Cusotmer102 8:00 AM Massage"
#CustomerInstance.validate_service("8:00 AM", "Massage")


############ Interactive inputs
"""
answer = customer(input("Enter customer ID"))
answer.check_for_cust()

Input_ID = input("Enter customer ID")
CustomerInstance = customer(Input_ID)
CustomerInstance = customer(102)


Input_time = input("Enter time slot  ")
Input_service = input("Enter service type  ")
"""

############ Testing
"""
CustomerInstance = customer(102)
print "\n Cusotmer102's reservations and time: "
CustomerInstance.lookup_service()

CustomerInstance = customer(102)
print "\n Cusotmer102 8:00 AM Massage"
CustomerInstance.validate_service("8:00 AM", "Massage")
print "\n Cusotmer102 8:00 AM Massage_swe"
CustomerInstance.validate_service("8:00 AM", "Massage_swe")
print "\n Cusotmer102 8:00 AM Facial_col"
CustomerInstance.validate_service("8:00 AM", "Facial_col")
print "\n Cusotmer102 8:00 AM Facial_norm"
CustomerInstance.validate_service("8:00 AM", "Facial_norm")


CustomerInstance = customer(102)
print "\n Before reserving, Cusotmer102 8:30 AM Facial_norm"
CustomerInstance.validate_service("8:30 AM", "Facial_norm")

CustomerInstance.start_reserving("8:30 AM", "Facial_norm")
#print service_list

print "\n After reserving, Cusotmer102 8:30 AM Facial_norm"
CustomerInstance.validate_service("8:30 AM", "Facial_norm")
"""
