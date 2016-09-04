# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 20:43:25 2015

@author: briantaylor
"""


#
# Data Definitions
#
  
# ListOfInt is one of:
# - []
# - [int] + ListOfInt
# interp. a list of integers
  
L1 = []
L2 = [5, 6, -3]
  
#def fn_for_loi(loi):
#    if loi == []:
#        return ...
#    else:
#        return ...loi[0] ...fn_for_loi(loi[1:])
  
  
#
# Functions
#
 
def sum_loi_l(loi):
    """
    (listof int) -> int
      
    Produces the sum of the integers in loi
      
    >>> sum_loi_l([])
    0
      
    >>> sum_loi_l([5, 6, -3])
    8
    """
    acc = 0
     
    for i in loi:
        acc = i + acc
      
    return acc  
     
  
# 
# Make sure tests run when this program runs
#
  
if __name__ == "__main__":
    import doctest
    print( doctest.testmod(verbose=False) )
 