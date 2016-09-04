# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 15:52:31 2015

@author: briantaylor
"""

import random as ra
import statistics as st

alist = list(range(100))

numtrials = 100000

for stop in range(5,50):
    
    benchmarks = []
    choices = []
    lastpicks = []

    for j in range(numtrials):
        #print("\ntrial " + str(j+1) + " --------")
        ra.shuffle(alist)
        #print(alist[:stop])
        benchmark = max(alist[:stop])
        benchmarks.append(benchmark)
        #print("benchmark = " + str(benchmark))
        choice = -1
        for i in range(stop,100):
            if alist[i] > benchmark :
                choice = alist[i]
                break
        if choice == -1 :
            #print("taking last seen object")
            choice = alist[99]
            lastpicks.append(alist[99])
        
        #print("choice = " + str(choice))
        choices.append(choice)
    
    print("Rejecting the first " + str(stop) + " candidates: ")
    
    print("\nmean benchmark = " + str(st.mean(benchmarks)))
    print("median benchmark = " + str(st.median(benchmarks)))
    print("min benchmark = " + str(min(benchmarks)))
    print("max benchmark = " + str(max(benchmarks)))
    
    print("\nmean choice = " + str(st.mean(choices)))
    print("median choice = " + str(st.median(choices)))
    print("min choice = " + str(min(choices)))
    print("max choice = " + str(max(choices)))
    
    print("\nPicked 99 " + str(choices.count(99)) + " times " + str(choices.count(99) / numtrials))
    print("Picked 98 " + str(choices.count(98)) + " times " + str(choices.count(98) / numtrials))
    print("Picked 97 " + str(choices.count(97)) + " times " + str(choices.count(97) / numtrials))
    print("Picked 96 " + str(choices.count(96)) + " times " + str(choices.count(96) / numtrials))
    
    print("\nPicked top 1: " + str(choices.count(99)  / numtrials))
    print("Picked top 2: " + str((choices.count(99) + choices.count(98)) / numtrials))
    print("Picked top 3: " + str((choices.count(99) + choices.count(98) + \
                                    choices.count(97)) / numtrials))
    print("Picked top 4: " + str((choices.count(99) + choices.count(98) + \
                                    choices.count(97) + choices.count(96)) / numtrials))
    
    print("\nTook last pick " + str(benchmarks.count(99)) + " times")
    print("mean last pick = " + str(st.mean(lastpicks)))
    
    print("\nPicked zero " + str(choices.count(0)) + " times")
    print("for a rate of " + str(choices.count(0) / numtrials))
    
    print("\n")








    
# Make sure doctest run when file is run but not imported

if __name__=='__main__':
    import doctest
    EPS = 1.0e-6
    print(doctest.testmod(verbose=False))