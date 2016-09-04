# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 17:24:18 2015

@author: Brian
"""

#Quiz 2A

# Robot is dict(x=int, y=int)
# interp. a robot located at coordinate (x, y)

R1 = dict(x=0, y=-1)
R2 = dict(x=5, y=-3)
R3 = dict(x=7, y=5)
R4 = dict(x=5, y=5)

def coord_at_lor(lor, c):
    """
    (listof Robot) int -> (listof Robot)
    
    Produce a list of Robots with an x or y coordinate equal to c, given
    a list of Robots
    
    >>> coord_at_lor([], 0)
    []
    
    >>> act = coord_at_lor([R1, R2, R3, R4], 5)
    >>> exp = [{'x': 5, 'y': -3}, {'x': 7, 'y': 5}, {'x': 5, 'y': 5}]
    >>> act == exp
    True
    """
    return [r for r in lor if test_robot(r, c)]
    
    
def test_robot(r, c):
    """
    Robot, int -> Boolean
    
    Produce true if x or y coordinate of Robot is c
    
    >>> test_robot(R1, 5)
    False
    
    >>> test_robot(R2, 5)
    True
    """
    return r['x'] == c or r['y'] == c
   
    
    
    
    
    
    
    
    
    # Make sure tests run when this module is run

if __name__ == '__main__':
    import doctest
    EPS = 1.0e-9  # for testing floats
    print(doctest.testmod(verbose=False))
