# -*- coding: utf-8 -*-
"""
Created on Fri May 20 10:32:06 2016

@author: briantaylor
"""

import random

ctotal = 0
utotal = 0
rtotal = 0
ttotal = 0
trials = 100000

for i in range(trials):

    common = 0
    uncommon = 0
    rare = 0
    numtrials = 0
    
    while common == 0 or uncommon == 0 or rare == 0:
        choice = random.randint(1,6)
        numtrials += 1
        
        if choice < 4:
            common += 3
        
        if choice > 3 and choice < 6:
            uncommon += 2
        
        if choice == 6:
            rare += 1
            
    ctotal += common
    utotal += uncommon
    rtotal += rare
    ttotal += numtrials
    
    print("common:    " + str(common))
    print("uncommon:  " + str(uncommon))
    print("rare:      " + str(rare))
    print("numtrials: " + str(numtrials))
    print("")

print("Averages:")
print("common:   " + str(ctotal/trials) + " " + str(ctotal/rtotal))
print("uncommon: " + str(utotal/trials) + " " + str(utotal/rtotal))
print("rare:     " + str(rtotal/trials))
print("trials:   " + str(ttotal/trials))