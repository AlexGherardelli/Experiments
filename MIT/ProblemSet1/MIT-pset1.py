#! C:\Users\Gherardelli\Documents\PortableApps\WinPython\python-2.7.10\python.exe
# -*- coding: UTF-8 -*-
"""
Created on Wed Oct 21 17:43:40 2015

@author: AlexGherardelli

Produces a plot of temperature differences
from a set of data in text form
"""
import pylab
import numpy as np

def load():
    inFile = open("julyTemps.txt", "r")

    high = []
    low = []
    for line in inFile:
        fields = line.split()
        if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
            continue
        else:
            high.append(fields[1])
            low.append(fields[2])
    return (low, high)

def producePlot(lowTemps, highTemps):
    temperatures = load()
    lowTemps = map(int, temperatures[0])
    highTemps = map(int, temperatures[1])

    highTemps = np. array(highTemps)
    lowTemps = np. array(lowTemps)
    diffTemps = highTemps - lowTemps
    return diffTemps

pylab.title("Day by Day Ranges in Temperature in Boston in July 2012")
pylab.xlabel("Days")
pylab.ylabel("Temperature Ranges")
pylab.plot(range(1,32), diffTemps)
