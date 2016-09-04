# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 11:07:02 2015

@author: Brian
"""

def my_f(p1, p2, *args, **kwargs):
    print(p1, " ", p2)
    for a in args:
        print(a)
    for k in kwargs:
        print(k, kwargs[k])
        