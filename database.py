# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 12:13:31 2021

@author: Jenny Xin
"""

print("This is the daabase.py module")
print("Its name is {}".format(__name__))

#checks in current folder. if not in local folder, will check through all python modules
import blood_calculator
#import blood_calculator as bc


#only imports specific funciton
#from blood_calculator import hdl_analysis

#imports all functions, no need to type "blood_calculator.     " not good for readability
# DONT USE. you gonna lose points
#from blood_calculator import *


answer = blood_calculator.hdl_analysis(55)
#answer = hdl_analysis(55)
print("The analysis of 55 HDL is {}".format(answer))

#answer2 = blood_calculator.ldl_analysis(200)




