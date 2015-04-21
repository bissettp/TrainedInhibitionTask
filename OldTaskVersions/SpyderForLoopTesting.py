# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 12:08:19 2015

@author: patrickbissett
"""
from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import random
#Redo = 1
colors = ['yellow', 'white', 'orange', 'magenta', 'green', 'gray', 'cyan', 'blue']
shapes = ['triangle', 'square', 'line', 'invertedtriangle', 'hexagon', 'diamond', 'cross', 'circle']
rewards = [0.5, 1, 2, 4] * 2
conditions = ['go', 'go', 'go', 'go', 'stop', 'stop', 'stop', 'stop']
trialDetailsList = []

shuffle(colors)
shuffle(shapes)

for i, color in enumerate(colors): # cycle through each color and keep track of an index number
    trialDetails = {} # a dictionary of key-value pairs
    trialDetails['fileName'] = shapes[i] + color + '.gif'
    trialDetails['reward'] = rewards[i]
    trialDetails['condition'] = conditions[i]
    trialDetailsList.append(trialDetails)

shuffle(trialDetailsList) # do this now to ensure that order of presentation of rewards and conditions is also shuffled

ConditionOne = trialDetailsList[0]
ConditionTwo = trialDetailsList[1]
ConditionThree = trialDetailsList[2]
ConditionFour = trialDetailsList[3]
ConditionFive = trialDetailsList[4]
ConditionSix = trialDetailsList[5]
ConditionSeven = trialDetailsList[6]
ConditionEight = trialDetailsList[7]

StopTaskTrials = 272
StopTrialsPerStopStim = 26
GoTrialsPerStopStim = 8
GoTrialsPerGoStim = 34
NumStim = 8
StopTrialList = []

if ConditionOne['condition'] == 'go':
    ConditionOne['StopOrGo'] = 'go'
    for i in range(1, GoTrialsPerGoStim + 1):
        StopTrialList.append(ConditionOne)
else:
    ConditionOne['StopOrGo'] = 'go'
    for j in range(1, GoTrialsPerStopStim + 1):
        StopTrialList.append(ConditionOne)
    ConditionOne['StopOrGo'] = 'stop'
    for i in range(1, GoTrialsPerStopStim + 1):
        StopTrialList.append(ConditionOne)
        
if ConditionTwo['condition'] == 'go':
    ConditionTwo['StopOrGo'] = 'go'
    for i in range(1, GoTrialsPerGoStim + 1):
        StopTrialList.append(ConditionTwo)
else:
    ConditionTwo['StopOrGo'] = 'go'
    for j in range(1, GoTrialsPerStopStim + 1):
        StopTrialList.append(ConditionTwo)
    ConditionTwo['StopOrGo'] = 'stop'
    for i in range(1,  GoTrialsPerStopStim + 1):
        StopTrialList.append(ConditionTwo)
        
if ConditionThree['condition'] == 'go':
    ConditionThree['StopOrGo'] = 'go'
    for i in range(1, GoTrialsPerGoStim + 1):
        StopTrialList.append(ConditionThree)
else:
    ConditionThree['StopOrGo'] = 'go'
    for j in range(1, GoTrialsPerStopStim + 1):
        StopTrialList.append(ConditionThree)
    ConditionThree['StopOrGo'] = 'stop'
    for i in range(1, GoTrialsPerStopStim + 1):
        StopTrialList.append(ConditionThree)

if ConditionFour['condition'] == 'go':
    ConditionFour['StopOrGo'] = 'go'
    for i in range(1, GoTrialsPerGoStim + 1):
        StopTrialList.append(ConditionFour)
else:
    ConditionFour['StopOrGo'] = 'go'
    for j in range(1, GoTrialsPerStopStim + 1):
        StopTrialList.append(ConditionFour)
    ConditionFour['StopOrGo'] = 'stop'
    for i in range(1, GoTrialsPerStopStim + 1):
        StopTrialList.append(ConditionFour)

if ConditionFive['condition'] == 'go':
    ConditionFive['StopOrGo'] = 'go'
    for i in range(1, GoTrialsPerGoStim + 1):
        StopTrialList.append(ConditionFive)
else:
    ConditionFive['StopOrGo'] = 'go'
    for j in range(1, GoTrialsPerStopStim + 1):
        StopTrialList.append(ConditionFive)
    ConditionFive['StopOrGo'] = 'stop'
    for i in range(1, GoTrialsPerStopStim + 1):
        StopTrialList.append(ConditionFive)

if ConditionSix['condition'] == 'go':
    ConditionSix['StopOrGo'] = 'go'
    for i in range(1, GoTrialsPerGoStim + 1):
        StopTrialList.append(ConditionSix)
else:
    ConditionSix['StopOrGo'] = 'go'
    for j in range(1, GoTrialsPerStopStim + 1):
        StopTrialList.append(ConditionSix)
    ConditionSix['StopOrGo'] = 'stop'
    for i in range(1, GoTrialsPerStopStim + 1):
        StopTrialList.append(ConditionSix)
        
if ConditionSeven['condition'] == 'go':
    ConditionSeven['StopOrGo'] = 'go'
    for i in range(1, GoTrialsPerGoStim + 1):
        StopTrialList.append(ConditionSeven)
else:
    ConditionSeven['StopOrGo'] = 'go'
    for j in range(1, GoTrialsPerStopStim + 1):
        StopTrialList.append(ConditionSeven)
    ConditionSeven['StopOrGo'] = 'stop'
    for i in range(1, GoTrialsPerStopStim + 1):
        StopTrialList.append(ConditionSeven)
    
if ConditionEight['condition'] == 'go':
    ConditionEight['StopOrGo'] = 'go'
    for i in range(1, GoTrialsPerGoStim + 1):
        StopTrialList.append(ConditionEight)
else:
    ConditionEight['StopOrGo'] = 'go'
    for j in range(1, GoTrialsPerStopStim + 1):
        StopTrialList.append(ConditionEight)
    ConditionEight['StopOrGo'] = 'stop'
    for i in range(1, GoTrialsPerStopStim + 1):
        StopTrialList.append(ConditionEight)
        
        
#for i in range (1, NumStim + 1): 
#    for j in range (1, GoTrialsPerGoStim + 1):
#        if ConditionOne['condition'] = 'go' :
            
#for i in range(1, GoTrialsPerGoStim + 1):
#        for j in range (1, GoTrialsPerGoStim + 1):
#    StopTrialList.append(ConditionOne)
#    StopTrialList.append(ConditionTwo)
#    StopTrialList.append(ConditionThree)
#    StopTrialList.append(ConditionFour)
#    StopTrialList.append(ConditionFive)
#    StopTrialList.append(ConditionSix)
#    StopTrialList.append(ConditionSeven)
#    StopTrialList.append(ConditionEight)

#for k in range(1, StopTaskTrials + 1):
#    for l in range(1, )
#shuffle(StopTrialList)