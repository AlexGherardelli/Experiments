# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 13:48:48 2015

@author: GHERARDELLI
"""

import random

def getEven():
    return random.randrange(0, 100, 2)
    
def deterministicNumber():
    #hard coding answer!
    return 10 or 12 or 14 or 16 or 18 or 20
    
    
def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly 
    distributed even number between 9 and 21
    '''
    return random.randrange(10, 22, 2)
    

    
    
#test function
    '''
even = 0
odd = 0

for i in range(1000):
    if x % 2 == 0:
        even += 1
    else:
        odd += 1
print "Even: " + str(even)
print "Odd: " + str(odd)
    '''