# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 12:39:36 2021

@author: Jenny Xin
"""

def interface():
    print("Blood Calculator")
    keep_running = True
    while keep_running:
        print("Make a Choice")
        print("9 --> Quit")
        choice = int(input("Make a Choice"))
        # print(type(choice))
        if choice == 9:
            keep_running = False
            return choice
        HDL_Driver()
        LDL_Driver()

def HDL_Driver():
    HDL_value = hdl_input()
    HDL_character = hdl_analysis(HDL_value)
    hdl_output(HDL_value, HDL_character)
    
def hdl_input():
    hdl_value = int(input("Enter HDL Value: "))
    return hdl_value

def hdl_analysis(HDL_value):
    if HDL_value >= 60:
        return "Normal"
    elif 40 <= HDL_value < 60:
        return "Borderline Low"
    else:
        return "Low"
    
def hdl_output(HDL_value, HDL_answer):
    print("THe HDL value of {} is considered {}".format(HDL_value, HDL_answer))
    return

def LDL_Driver():
    LDL_value = ldl_input()
    LDL_character = ldl_analysis(LDL_value)
    ldl_output(LDL_value, LDL_character)
    
def ldl_input():
    ldl_value = int(input("Enter LDL Value: "))
    return ldl_value

def ldl_analysis(LDL_value):
    if LDL_value < 130:
        return "Normal"
    elif 130 <= LDL_value <= 159:
        return "Borderline High"
    elif 160 <= LDL_value <= 189:
        return "High"
    else:
        return "Very High"
    
def ldl_output(LDL_value, LDL_answer):
    print("THe LDL value of {} is considered {}".format(LDL_value, LDL_answer))
    return

interface()

    