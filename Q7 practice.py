# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 20:12:26 2015

@author: briantaylor
"""

from io import StringIO
"""
>>> data = '1234,23.8,159.99\n 3142,-42.3,175.14\n 1234,23.84,159.98\n 1551,32.6,63.23\n'
>>> f = StringIO(data)
>>> find_locns(f, 2315)
[]

>>> f = StringIO(data)
>>> find_locns(f, 1234)
[(23.8, 159.99), (23.84, 159.98)]
"""

def find_locns(f, tag_id):
    
    sightings = []
    
    for line in f:
        ID, lat, long = line.strip().split(',')
        if int(ID) == tag_id:
            sightings.append((float(lat), float(long)))
    return sightings

# Make sure tests run when this module is run

if __name__ == "__main__":
    import doctest
    EPS = 1.0e-9
    print(doctest.testmod(verbose=False))