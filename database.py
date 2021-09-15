# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 12:13:31 2021

@author: Jenny Xin
"""

#checks in current folder. if not in local folder, will check through all python modules
import blood_calculator
#import blood_calculator as bc


#only imports specific funciton
#from blood_calculator import hdl_analysis

#imports all functions, no need to type "blood_calculator.     " not good for readability
# DONT USE. you gonna lose points
#from blood_calculator import *

def create_database_entry(patient_name, id_no, age):
    new_patient = [patient_name, id_no, age, []]
    return new_patient

def print_database(db):
    #indexes and also allows you to run through db
    locations = ["Room 1", "Room 4", "ER", "Post-OP"]
    
    # for i, patient in enumerate(db):
    #     print("{} - {} - {}".format(i, patient, locations[i]))
    #     # print(patient)
    
    # for i, (patient,location) in enumerate(zip(db, locations)):
    #     print("{} - {}".format(patient, location))
    
    for patient, location in zip(db, locations):
        print("{} - {}".format(patient, location))
    
    #a[-1] get last entry. [-2] gives second to last entry. Also applicable to strings
    #a[1:3] gives you range of 1-2 (will not include 3)
    #a[-3:] gives you the rest of the list starting from 3rd to last
    #db[1][0] will print names
    
def above_age(db, age):
    for patient in db:
        if patient[2] > age:
            print(patient[0])
            
def get_patient(db, id_no):
    for patient in db:
        if patient[1] == id_no:
            return patient
    
def main():
    db = []
    x = create_database_entry("Ann Ables", 120, 30)
    db.append(x)
    x = create_database_entry("Bob Boyles", 24, 31)
    db.append(x) 
    x = create_database_entry("Chris Chou", 33, 33)
    db.append(x)
    x = create_database_entry("David Dinkins", 14, 34)
    db.append(x)
    
    
    patient_id_tested = 24
    test_done = ("HDL",65)
    
    patient = get_patient(db, patient_id_tested)
    patient[3].append(test_done)
    
    print_database(db)
    
    #above_age(db, 32)
    

    
if __name__ == "__main__":
    main()










#answer = blood_calculator.hdl_analysis(55)
#answer = hdl_analysis(55)
#print("The analysis of 55 HDL is {}".format(answer))

#answer2 = blood_calculator.ldl_analysis(200)




