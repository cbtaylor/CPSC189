# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 14:06:50 2015

@author: Brian
"""
import numpy

F = numpy.matrix([[1, 1], [1, 0]])
print(F)

for i in range(1,92):
    print("Fibonacci " + str(i) + ": " + str((F ** (i-1))[0, 0]))
    