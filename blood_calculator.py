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
        print(type(choice))
        if choice == 9:
            keep_running = False
            
    print(choice)
    return choice

interface()