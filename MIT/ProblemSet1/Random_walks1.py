# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 12:17:27 2015

@author: GHERARDELLI
"""
import random

class Location(object):
    '''
    Models the location part
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)
    
    def getX(self):
        return self.x
        
    def getY(self):
        return self.y
        
    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5
    
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'
        
class Field(object):
    '''
    Models the field
    '''
    def __init__(self):
        self.drunks ={}
        
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError("Duplicate drunk")
        else:
            self.drunks[drunk] = loc
            
    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError("Drunk not in field")
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        self.drunks[drunk] = currentLocation.move(xDist, yDist)
    
    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError("Drunknot in field")
        return self.drunks[drunk]

class Drunk(object):
    '''
    Models drunks
    '''
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "This drunk is named " + self.name
        
class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = \
        [(0.0, 1.0), (0.0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)