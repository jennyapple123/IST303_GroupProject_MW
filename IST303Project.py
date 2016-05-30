#from Tkinter import *
#root = Tk()
#root.mainloop()
from datetime import *
import csv
import pandas as pd
import numpy as np

guest_list = pd.read_csv("C:\Users\MSI CES 2014\Documents\IST 303 GuestList.csv", index_col = 0)
service_list = pd.read_csv("C:\Users\MSI CES 2014\Documents\IST 303 services.csv", index_col = 0)



class customer:

    def __init__(self, input_id):
        self.input_id = input_id

    def check_for_cust(self):
        for lab, row in guest_list.iterrows():
            if CustomerInstance.input_id== lab:
                print "yes"
                return True
        print "no"
        return False

    def validate_service(self, Input_Time, Input_Service):
        #if not customer.check_for_cust():
        #    return
        for lab, row in guest_list.iterrows():
            if CustomerInstance.input_id == lab:
                print "Customer ID is valid. Here are the reservation info"
                #print row
                for lab1, row1 in service_list.iterrows():
                    if row1['StartTime'] == Input_Time and row1['Services'] == Input_Service:
                        if row1['ID']== 999999:
                            print "This service at this time slot is available, would you like to book it?"
                            customer.start_reserving(self, Input_Time, Input_Service)
                            return
                        else:
                            if CustomerInstance.input_id == int(row1['ID']):
                            #print row1['StartTime'],row1['Services']
                                print "You already have booked that time slot"
                                return
                            else:
                                print "Someone else has booked that time slot"
                                return
                        return
                print "There is no such service type or time slots. please check your spelling!!"
                return
        print "Customer ID is not valid"

    def start_reserving(self, Input_Time, Input_Service):
        for lab1, row1 in service_list.iterrows():
            if row1['StartTime'] == Input_Time and row1['Services'] == Input_Service and row1['ID'] == 999999:
                service_list.set_value(lab1, 'ID' , CustomerInstance.input_id)
                print "reservation complete"
                return

    def lookup_service(self):
        # if not customer.check_for_cust():
        #    return
        for lab, row in guest_list.iterrows():
            if CustomerInstance.input_id == lab:
                print "Customer ID is valid. Here are the reservation info"
                print row
                for lab1, row1 in service_list.iterrows():
                    if CustomerInstance.input_id == int(row1['ID']):
                        print row1
                print "No reservation yet"
                return
        print "Customer ID is not valid"





class reservations(customer):
    def __init__(self, mineral_bath, massage, facial, specialty):
        self.mineral_bath = mineral_bath
        self.massage = massage
        self.facial = facial
        self.specialty = specialty

    #def Check_Duplicate_Reservation(self, Input_ID, Input_Service, Input_TimeSlot):





#answer = customer(input("Enter customer ID"))
#answer.check_for_cust()

#Input_ID = input("Enter customer ID")
#CustomerInstance = customer(Input_ID)
#CustomerInstance = customer(102)


#Input_time = input("Enter time slot  ")
#Input_service = input("Enter service type  ")

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
"""

CustomerInstance = customer(102)
print "\n Before reserving, Cusotmer102 8:30 AM Facial_norm"
CustomerInstance.validate_service("8:30 AM", "Facial_norm")

CustomerInstance.start_reserving("8:30 AM", "Facial_norm")
#print service_list

print "\n After reserving, Cusotmer102 8:30 AM Facial_norm"
CustomerInstance.validate_service("8:30 AM", "Facial_norm")


