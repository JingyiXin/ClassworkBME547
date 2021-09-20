class Patient:
    
    def __init__(self, input_name, id_no, age):
        self.name = input_name
        self.id_no = id_no
        self.age = age
        self.tests = []
        #underscore in front of variable means dont touch
        self._x = 3
        
    def __repr__(self):
        return"{}: {}".format(self.id_no, self.name)
        
    def is_adult(self):
        if self.age >= 21:
            return True
        else:
            return False
        
        
def class_work():
    new_patient = Patient("Ann Ables", 120, 36)
    #similar to new_patient = [] or new_patient = list()
    print(new_patient.id_no)
    print(new_patient.name)
    
    x = Patient("Bob Boyles", 24, 33)
    x.name = "Bobby Boyles"
    print(x.name)
    print(x._x)
    

#checks in current folder. if not in local folder, will check through all python modules
import blood_calculator
#import blood_calculator as bc

#only imports specific funciton
#from blood_calculator import hdl_analysis

#imports all functions, no need to type "blood_calculator.     " not good for readability
# DONT USE. you gonna lose points
#from blood_calculator import *

def create_database_entry(patient_name, id_no, age):
    #ignore the parameter self when you call it
    new_patient = Patient(patient_name, id_no, age)
    #new_patient = {"patient_name":patient_name, "id_no":id_no, "age":age, "location":[], "tests":[]}
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
        if patient["age"] > age:
            print(patient["patient_name"])
            
def get_patient(db, id_no):
    patient = db[id_no]
    return patient
    
def main():
    #class_work()
    
    db = {}
    x = create_database_entry("Ann Ables", 120, 30)
    #db[x["id_no"]] = x
    db[x.id_no] = x
    #This makes an entry in the dictionary with the key being id number and the entry being x
    x = create_database_entry("Bob Boyles", 24, 31)
    db[x.id_no] = x 
    x = create_database_entry("Chris Chou", 33, 33)
    db[x.id_no] = x
    x = create_database_entry("David Dinkins", 14, 34)
    db[x.id_no] = x
    print(db)
    
    
    patient_id_tested = 24
    test_done = ("HDL",65)
    
    patient = get_patient(db, patient_id_tested)
    patient.tests.append(test_done)
    print(db[24].tests)
    # patient["tests"].append(test_done)
    # patient[3].append(test_done)
    
    print_database(db)
    
    #above_age(db, 32)
    

    
if __name__ == "__main__":
    main()


#answer = blood_calculator.hdl_analysis(55)
#answer = hdl_analysis(55)
#print("The analysis of 55 HDL is {}".format(answer))

#answer2 = blood_calculator.ldl_analysis(200)




