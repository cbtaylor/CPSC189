# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 14:20:36 2016

@author: Brian
"""

from random import random

A_match = 0
B_match = 0

for i in range(100000):
    
    A_tot = 0
    B_tot = 0
    edge = 0.55
    
    while True:
        A = 0
        B = 0
        
        while True:
            if random() > edge:
                A += 1
            else:
                B += 1
            #print A,B
            if (A >= 11 or B >= 11) and abs(A - B) >= 2:
                #print
                break
        if A > B:
            A_tot += 1
        else:
            B_tot += 1
        #print "---"
        #print A_tot, B_tot
        #print "---"
        if A_tot == 3 or B_tot == 3:
            break
    if A_tot == 3:
        A_match += 1
    else:
        B_match += 1

print A_match, B_match
