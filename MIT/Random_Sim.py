# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 17:36:10 2015

@author: GHERARDELLI
"""

import Random_walks1

def walk(f, d, numSteps):
    '''
    Takes field, drunk and number of steps.
    '''
    start= f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return (start.distFrom(f.getLoc(d)))