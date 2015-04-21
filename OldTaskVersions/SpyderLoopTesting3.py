# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 12:08:19 2015

@author: patrickbissett
"""
from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
from copy import deepcopy
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

#NumLearningRepetitions = 50



StopTaskTrials = 272
StopTrialsPerStopStim = 26
GoTrialsPerStopStim = 8
GoTrialsPerGoStim = 34
NumStim = 8
StopTrialList = []

#for i in range (1, StopTaskTrials + 1):
#    if ConditionOne['condition'] == 'go':
#        for j in range (1, GoTrialsPerGoStim + 1): 
#            ConditionOne['StopOrGo'] = 'NoStop'
#            StopTrialList.append(ConditionOne)
#    elif ConditionOne['condition'] == 'stop':
#        for j in range (1, GoTrialsPerStopStim + 1):
#            ConditionOne['StopOrGo'] = 'NoStop'
#            StopTrialList.append(ConditionOne)
if ConditionOne['condition'] == 'go':
    ConditionOne['StopOrGo'] = 'go'
    for i in range(1, GoTrialsPerGoStim + 1):
        StopTrialList.append(ConditionOne)
else:
    for j in range(1, GoTrialsPerStopStim + 1):
        ConditionOne['StopOrGo'] = 'go'
        StopTrialList.append(deepcopy(ConditionOne))
    for i in range(1, StopTrialsPerStopStim + 1):
        ConditionOne['StopOrGo'] = 'stop'
        StopTrialList.append(deepcopy(ConditionOne))
        
if ConditionTwo['condition'] == 'go':
    ConditionTwo['StopOrGo'] = 'go'
    for i in range(1, GoTrialsPerGoStim + 1):
        StopTrialList.append(ConditionTwo)
else:
    for j in range(1, GoTrialsPerStopStim + 1):
        ConditionTwo['StopOrGo'] = 'go'
        StopTrialList.append(deepcopy(ConditionTwo))
    for i in range(1,  StopTrialsPerStopStim + 1):
        ConditionTwo['StopOrGo'] = 'stop'
        StopTrialList.append(deepcopy(ConditionTwo))
        
if ConditionThree['condition'] == 'go':
    ConditionThree['StopOrGo'] = 'go'
    for i in range(1, GoTrialsPerGoStim + 1):
        StopTrialList.append(ConditionThree)
else:
    for j in range(1, GoTrialsPerStopStim + 1):
        ConditionThree['StopOrGo'] = 'go'
        StopTrialList.append(deepcopy(ConditionThree))
    for i in range(1, StopTrialsPerStopStim + 1):
        ConditionThree['StopOrGo'] = 'stop'
        StopTrialList.append(deepcopy(ConditionThree))

if ConditionFour['condition'] == 'go':
    ConditionFour['StopOrGo'] = 'go'
    for i in range(1, GoTrialsPerGoStim + 1):
        StopTrialList.append(ConditionFour)
else:
    for j in range(1, GoTrialsPerStopStim + 1):
        ConditionFour['StopOrGo'] = 'go'
        StopTrialList.append(deepcopy(ConditionFour))
    for i in range(1, StopTrialsPerStopStim + 1):
        ConditionFour['StopOrGo'] = 'stop'
        StopTrialList.append(deepcopy(ConditionFour))

if ConditionFive['condition'] == 'go':
    ConditionFive['StopOrGo'] = 'go'
    for i in range(1, GoTrialsPerGoStim + 1):
        StopTrialList.append(ConditionFive)
else:
    for j in range(1, GoTrialsPerStopStim + 1):
        ConditionFive['StopOrGo'] = 'go'
        StopTrialList.append(deepcopy(ConditionFive))
    for i in range(1, StopTrialsPerStopStim + 1):
        ConditionFive['StopOrGo'] = 'stop'
        StopTrialList.append(deepcopy(ConditionFive))

if ConditionSix['condition'] == 'go':
    ConditionSix['StopOrGo'] = 'go'
    for i in range(1, GoTrialsPerGoStim + 1):
        StopTrialList.append(ConditionSix)
else:
    for j in range(1, StopTrialsPerStopStim + 1):
        ConditionSix['StopOrGo'] = 'go'
        StopTrialList.append(deepcopy(ConditionSix))
    for i in range(1, GoTrialsPerStopStim + 1):
        ConditionSix['StopOrGo'] = 'stop'
        StopTrialList.append(deepcopy(ConditionSix))
        
if ConditionSeven['condition'] == 'go':
    ConditionSeven['StopOrGo'] = 'go'
    for i in range(1, GoTrialsPerGoStim + 1):
        StopTrialList.append(ConditionSeven)
else:
    for j in range(1, GoTrialsPerStopStim + 1):
        ConditionSeven['StopOrGo'] = 'go'
        StopTrialList.append(deepcopy(ConditionSeven))
    for i in range(1, StopTrialsPerStopStim + 1):
        ConditionSeven['StopOrGo'] = 'stop'
        StopTrialList.append(deepcopy(ConditionSeven))
    
if ConditionEight['condition'] == 'go':
    ConditionEight['StopOrGo'] = 'go'
    for i in range(1, GoTrialsPerGoStim + 1):
        StopTrialList.append(ConditionEight)
else:
    for j in range(1, GoTrialsPerStopStim + 1):
        ConditionEight['StopOrGo'] = 'go'
        StopTrialList.append(deepcopy(ConditionEight))
    for i in range(1, StopTrialsPerStopStim + 1):
        ConditionEight['StopOrGo'] = 'stop'
        StopTrialList.append(deepcopy(ConditionEight))
        

shuffle(StopTrialList)