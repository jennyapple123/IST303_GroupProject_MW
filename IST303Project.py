from tkinter import *
#import tkinter as tk
from datetime import *
import csv
import pandas as pd
import numpy as np
import unittest
import tkinter.simpledialog
#import tkinter.messagebox





guest_list = pd.read_csv("IST 303 GuestList.csv", index_col = 0)
#service_list = pd.read_csv("IST 303 services.csv", index_col = 0)


class customer:

    def __init__(self, input_id):
        self.input_id = input_id
        for lab, row in guest_list.iterrows():
            if self.input_id == lab:
                self.check_in = datetime.strptime(row['check_in_date'] + " " + row['check_in_time'], '%m/%d/%y %I:%M %p')
                self.check_out = datetime.strptime(row['check_out_date'] + " " + row['check_out_time'], '%m/%d/%y %I:%M %p')

    def check_for_cust(self):
        """ This function checks if a customer ID is valid
        """
        for lab, row in guest_list.iterrows():
            if self.input_id == lab:
                return True
                messagebox.showinfo("Result", "Valid Customer ID!\n")

        #print str(self.input_id) + " is NOT a valid ID"
        messagebox.showinfo("Result", "Invalid Customer ID!\n")
        return False

    
Reservations = []

class Service(customer):
    def reserve(self, input_id, Input_Date, Input_Time, length):
        self.input_id = input_id
        self.StartTime = datetime.strptime(Input_Date + " " +  Input_Time, '%m/%d/%y %I:%M %p')
        self.length = length
        self.EndTime = self.StartTime + timedelta(minutes = length)
        Reservations.append(self)
        
        messagebox.showinfo("Result", "Reservations Completed!\n")

        #popup_result = Tk()
        #popup_result.title("Reservations Completed!")

class Facial_norm(Service):
    def __init__(self):
        self.price = 2.0
        self.service_id = 0

class Facial_col(Service):
    def __init__(self):
        self.price = 2.0
        self.service_id = 1

class Massage_swe(Service):
    def __init__(self):
        self.price = 3.0
        self.service_id = 2

class Massage_shi(Service):
    def __init__(self):
        self.price = 3.0
        self.service_id = 3

class Massage_deep(Service):
    def __init__(self):
        self.price = 3.0
        self.service_id = 4

class Mineral_bath(Service):
    def __init__(self):
        self.price = 2.5
        self.service_id = 5

class Spec_hot_stone(Service):
    def __init__(self):
        self.price = 3.5
        self.service_id = 6

class Spec_sug_scrub(Service):
    def __init__(self):
        self.price = 3.5
        self.service_id = 7

class Spec_herb_wrap(Service):
    def __init__(self):
        self.price = 3.5
        self.service_id = 8

class Spec_bot_wrap(Service):
    def __init__(self):
        self.price = 3.5
        self.service_id = 9



class AvailableService():
    def __init__(self, Input_Date, Input_Time):
        self.ReserveDateTime = datetime.strptime(Input_Date + " " +  Input_Time, '%m/%d/%y %I:%M %p')
        self.ReserveTime = datetime.strptime(Input_Time, '%I:%M %p')
        self.OpenTime = datetime.strptime("8:00 AM", '%I:%M %p')
        self.CloseTime = datetime.strptime("8:00 PM", '%I:%M %p')
    
    def Check(self):
        ServiceList = ["Facial_norm", "Facial_col", "Massage_swe", "Massage_shi", "Massage_deep",
                       "Mineral_bath", "Spec_hot_stone", "Spec_sug_scrub", "Spec_herb_wrap", "Spec_bot_wrap"]
        NotAvailable = []
        if self.ReserveTime > self.CloseTime or self.ReserveTime < self.OpenTime:
            messagebox.showinfo("Result", "Not in the range of OpenTime and CloseTime\n")
            print("Not in the range of OpenTime and CloseTime")
            return 
    
        for EachResevation in Reservations:
            if EachResevation.StartTime - timedelta(minutes = EachResevation.length) < self.ReserveDateTime or self.ReserveDateTime < EachResevation.EndTime:
                NotAvailable.append(EachResevation.service_id)
       
        printout = [ServiceList[i] for i in range(0, 9, 1) if i not in NotAvailable]
        messagebox.showinfo("Result", '\n'.join(printout))
    


class AvailableTimeForService():
    def __init__(self, Start_Date, Start_Time, End_Date, End_Time, InputService, length, OpenTime, CloseTime):
        self.OpenTime = datetime.strptime("8:00 AM", '%I:%M %p').time()
        self.CloseTime = datetime.strptime("8:00 PM", '%I:%M %p').time()
        self.StartDateTime = datetime.strptime(Start_Date + " " +  Start_Time, '%m/%d/%y %I:%M %p')
        self.EndDateTime = datetime.strptime(End_Date + " " +  End_Time, '%m/%d/%y %I:%M %p')
        self.length = length
        #self.length = eval(InputService).length
        #self.step = timedelta(minutes = self.length)
        self.step = timedelta(minutes = 30)

        StartTimeList = []
        NotAvailableTime = []

        while  self.StartDateTime < self.EndDateTime:
            if self.StartDateTime.time() < self.CloseTime and \
               self.StartDateTime.time() >= self.OpenTime:
                StartTimeList.append(self.StartDateTime)
            self.StartDateTime += self.step

        #print(Reservations[0].StartTime.strftime('%m/%d/%y %I:%M %p') + " " + str(Reservations[0].service_id))
        #print(Reservations[1].StartTime.strftime('%m/%d/%y %I:%M %p') + " " + str(Reservations[1].service_id))


        # Record all the not available time slots
        for EachResevation in Reservations:
            if EachResevation.service_id == eval(InputService).service_id and EachResevation.StartTime not in NotAvailableTime:
                NotAvailableTime.append(EachResevation.StartTime)
                if length == 60 or 90:
                    NotAvailableTime.append(EachResevation.StartTime - timedelta(minutes = 30))
                    NotAvailableTime.append(EachResevation.StartTime + timedelta(minutes = 30))
                if length == 90:
                    NotAvailableTime.append(EachResevation.StartTime - timedelta(minutes = 60))          
                    NotAvailableTime.append(EachResevation.StartTime + timedelta(minutes = 60))

        #print(NotAvailableTime)

        # Remove all the unavailable time slots
        for i in StartTimeList:
            if i not in NotAvailableTime:
                #print("\n")
                EndTime = i + timedelta(minutes = length)
                print(i.strftime('%m/%d/%y %I:%M %p') + " -- " + EndTime.strftime('%I:%M %p'))  


class AvailableTimeForCustomer():

    def __init__(self, Input_ID):
        CustomerCase = customer(Input_ID)
        self.OpenTime = datetime.strptime("8:00 AM", '%I:%M %p').time()
        self.CloseTime = datetime.strptime("8:00 PM", '%I:%M %p').time()
        self.ID = Input_ID
        now = datetime.now()
        self.StartDateTime = datetime(now.year, now.month, now.day, now.hour, now.minute)
        self.EndDateTime = CustomerCase.check_out
        self.step = timedelta(minutes = 30)

        StartTimeList = []
        NotAvailableTime = []

        # Round up the current time
        if self.StartDateTime.minute <= 30:
            NewMin = 30
        else:
            NewMin = 60
        self.StartDateTime = self.StartDateTime.replace(minute = 0)
        self.StartDateTime += timedelta(minutes = NewMin)

        while  self.StartDateTime < self.EndDateTime:
            if self.StartDateTime.time() < self.CloseTime and \
            self.StartDateTime.time() >= self.OpenTime:
                StartTimeList.append(self.StartDateTime)
            self.StartDateTime += self.step

        # Record all the not available time slots only for him
        for EachResevation in Reservations:
            if EachResevation.input_id == self.ID:
                NotAvailableTime.append(EachResevation.StartTime)


        # Remove all the unavailable time slots
        for i in StartTimeList:
            if i not in NotAvailableTime:
                EndTime = i + timedelta(minutes = 30)
                print(i.strftime('%m/%d/%y %I:%M %p') + " -- " + EndTime.strftime('%I:%M %p'))  



class charge(Service):
    def __init__(self, Input_ID):
        SumBill = 0
        CustomerCase = customer(Input_ID)
        
        for EachResevation in Reservations:
            if EachResevation.input_id == Input_ID:
                SumBill += EachResevation.length * EachResevation.price
        print ("Customer " + str(Input_ID) + " billing is " + str(SumBill) + " dollars")





"""
print("############# AvailableTimeForService")
#ATFS = AvailableTimeForService("5/22/16", "8:00 AM", "5/23/16", "8:00 PM", "Massage_swe()", 60, "8:00 AM", "8:00 PM")
print("############# AvailableTimeForService for Facial_norm")
FN2 = Facial_norm()
FN2.reserve(102, "6/5/16", "9:00 AM", 30)
#ATFS = AvailableTimeForService("5/22/16", "8:00 AM", "5/23/16", "8:00 PM", "Facial_norm()", 60, "8:00 AM", "8:00 PM")
print("\n ############# AvailableTimeForCustomer")
#ATFC = AvailableTimeForCustomer(102)

bill = charge(102)
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





class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Reserve", command = self.reserveKT)
        self.hi_there.pack(side=LEFT)

        self.hi_there = Button(frame, text="DislayAvailableService", command = self.DislayAvailableService)
        self.hi_there.pack(side=LEFT)


    def reserveKT(self):
        # Input the information
        input_id_value = simpledialog.askinteger("test", "Please enter customer ID: ")
        Input_Date_value = simpledialog.askstring("test","Please enter date for reservation: ") 
        Input_Time_value = simpledialog.askstring("test","Please enter time for reservation: ")
        InputService_value = simpledialog.askstring("test","Which services do you want?")
        length_value = simpledialog.askinteger("test", "For how long?")

        #CustomerInstance = customer(input_id)
        ServiceObject = eval(InputService_value)
        ServiceObject.reserve(input_id_value, Input_Date_value, Input_Time_value, length_value)


    def DislayAvailableService(self):
       # Input the information
        Input_Date_value = simpledialog.askstring("test","Please enter date: ") 
        Input_StartTime_value = simpledialog.askstring("test","Please enter start time: ")
        
        AS = AvailableService(Input_Date_value, Input_StartTime_value)
        AS.Check()

root = Tk()
app = App(root)
root.geometry('500x500')
root.mainloop()
root.destroy() # optional; see description below
