# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 12:17:56 2015

@author: briantaylor
"""



import random as ra
import statistics as st
import math as ma


def first_digit(x):
    """
    Int -> Int
    
    Produces the first digit of a given number
    Assumes x >= 1
    
    >>> first_digit(1234)
    1
    
    >>> first_digit(87)
    8
    
    >>> first_digit(34.5)
    3
    """
    num_digits = int(ma.log10(x))
    modulo = int(ma.pow(10,num_digits))
    other_digits = x % modulo
    first_digit = int((x - other_digits) / modulo)
    return first_digit

def first_digit2(x):
    """
    Int -> Int
    
    Produces the first digit of a given number
    Assumes x >= 1
    
    >>> first_digit2(1234)
    1
    
    >>> first_digit2(87)
    8
    
    >>> first_digit2(34.5)
    3
    """
    
    return int(str(x)[0])

buckets = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
trials = 10000

MAX = 9999999

for j in range(trials):
    RANDMAX = ra.randint(1, MAX)


    for i in range(trials):
        rand_int = ra.randint(1, RANDMAX)
    
        index = first_digit2(rand_int)
        buckets[index] += 1

    
    
print(buckets[1:10])

    
# Make sure doctest run when file is run but not imported

if __name__=='__main__':
    import doctest
    EPS = 1.0e-6
    print(doctest.testmod(verbose=False))