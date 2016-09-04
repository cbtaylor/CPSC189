# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 18:14:08 2015

@author: Brian
"""

def problem1(upper_bound):
    """
    int -> int
    
    Produce the sum of all multiples of either 3 or 5 below
    upper_bound
    """
    return sum(filter(lambda t: t%3 == 0 or t%5 == 0, range(upper_bound)))
                      