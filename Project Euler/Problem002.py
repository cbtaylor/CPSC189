# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 19:40:48 2015

@author: Brian
"""
import numpy as np

def sum_even_fibs(upper_bound):
    """
    int -> int
    
    Produce the sum of the even Fibonacci numbers below upper_bound
    """
    total = 0
    for f in fibs(upper_bound):
        if f%2 == 0:
            total += f
    return total
    
def fibs(upper_bound):
    """
    int -> (listof int)
    
    Produce a list of Fibonacci numbers less than upper_bound
    """
    fibs = [1, 1]
    while (fibs[-1] + fibs[-2] < upper_bound):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
    
def fibs_array(upper_bound):
    fibs_arr = np.array(fibs(upper_bound))
    return np.sum(fibs_arr[fibs_arr %2 == 0])
    
    