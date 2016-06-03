from Tkinter import *
#root = Tk()
#root.mainloop()
from datetime import *
import csv
import pandas as pd
import numpy as np
import unittest


guest_list = pd.read_csv("IST 303 GuestList.csv", index_col = 0)
service_list = pd.read_csv("IST 303 services.csv", index_col = 0)



class customer:

    def __init__(self, input_id):
        self.input_id = input_id

    def check_for_cust(self):
        """ This function checks if a customer ID is valid
        """
        for lab, row in guest_list.iterrows():
            if self.input_id == lab:
                print str(self.input_id) + " is a valid ID"
                self.check_in_date = row['check_in_date']
                self.check_out_date = row['check_out_date']
                self.check_in_time = row['check_in_time']
                self.check_out_time = row['check_out_time']
                self.check_in = datetime.strptime(row['check_in_date'] + " " + row['check_in_time'], '%m/%d/%y %I:%M %p')
                self.check_out = datetime.strptime(row['check_out_date'] + " " + row['check_out_time'], '%m/%d/%y %I:%M %p')
                return True
        print str(self.input_id) + " is NOT a valid ID"
        return False

    def validate_service_CheckinCheckout(self, Input_Date, Input_Time):
        """ This function checks if Input_Time is in the range of check in and check out range.
        """
        if self.check_for_cust():
            ServiceTime = datetime.strptime(Input_Date + " " +  Input_Time, '%m/%d/%y %I:%M %p')
            if ServiceTime > self.check_in and ServiceTime < self.check_out:
                print Input_Date + " " +  Input_Time + " is in the range of check in and check out time"
                return True
            print Input_Date + " " +  Input_Time + " is NOT in the range of check in and check out time"
            return False


    def validate_service(self, Input_Date, Input_Time, Input_Service):
        """ This function validate whether there are duplicate reservations.
            It also checks whether the reservation is available.
        """
        if self.check_for_cust() and self.validate_service_CheckinCheckout(Input_Date, Input_Time):
            for lab1, row1 in service_list.iterrows():
                if row1['StartTime'] == Input_Time and row1['Date'] == Input_Date and row1['Services'] == Input_Service:
                    if row1['ID']== 999999:
                        print Input_Service + " on " + Input_Date + " " +  Input_Time + " is available. Would you like to book it?"
                        #customer.start_reserving(self, Input_Time, Input_Service)
                        return True
                    else:
                        if self.input_id == int(row1['ID']):
                        #print row1['StartTime'],row1['Services']
                            print "You ( ID = " + str(self.input_id) + ") already have booked that time slot"
                            return False
                        else:
                            print "Someone else has booked that time slot!"
                            return False
            print "There is NO such service type or time slots. Please check your spelling!!"
            return False
        return False

    def start_reserving(self, Input_Date, Input_Time, Input_Service):
        """ This function helps to reserve a certain time slot for a certain type of service.
        """
        for lab1, row1 in service_list.iterrows():
            if row1['StartTime'] == Input_Time and row1['Date'] == Input_Date and row1['Services'] == Input_Service:
                if row1['ID']== 999999:
                    service_list.set_value(lab1, 'ID' , self.input_id)
                    print "Reservation for " + Input_Service + " on " + Input_Date + " " +  Input_Time + " is completed!"
                    return

    def lookup_service(self):
        """ This function lists all the reservations made for a given customer
        """
        for lab, row in guest_list.iterrows():
            if self.input_id == lab:
                print "Customer ID is valid. Here are the reservation info"
                print row
                for lab1, row1 in service_list.iterrows():
                    if self.input_id == int(row1['ID']):
                        print row1
                        print "\n"
                print "No reservation yet"
                return
        print "Customer ID is not valid"




############ Object reservations (to be used in iteration2)
"""
class reservations(customer):
    def __init__(self, mineral_bath, massage, facial, specialty):
        self.mineral_bath = mineral_bath
        self.massage = massage
        self.facial = facial
        self.specialty = specialty
"""

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
