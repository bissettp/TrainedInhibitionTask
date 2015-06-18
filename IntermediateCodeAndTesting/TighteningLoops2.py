#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Tue Apr 21 15:54:56 2015
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Initialize components for Routine "StimSetup"
StimSetupClock = core.Clock()
from copy import deepcopy
colors = ['yellow', 'white', 'orange', 'magenta', 'green', 'gray', 'cyan', 'blue']
shapes = ['triangle', 'square', 'line', 'invertedtriangle', 'hexagon', 'diamond', 'cross', 'circle']
rewards = [0.50, 1.00, 2.00, 4.00] * 2
conditions = ['go', 'go', 'go', 'go', 'stop', 'stop', 'stop', 'stop']
trialDetailsList = []
learningTrialList = []
learningPracTrialList = []
auctionTrialList = []
rewardList = []
Redo = 1 
rewardCount = 1
numStim = 8
numLearningTrials = 400
numLearningRepetitions = 50
numLearningPracTrial = 10
stopTaskTrials = 288
stopTrialsPerStopStim = 27
goTrialsPerStopStim = 9
goTrialsPerGoStim = 36
stopTrialList = []
stopPracTrialList = []

shuffle(colors)
shuffle(shapes)

for i, color in enumerate(colors): # cycle through each color and keep track of an index number
    trialDetails = {} # a dictionary of key-value pairs
    trialDetails['fileName'] = shapes[i] + color + '.gif'
    trialDetails['reward'] = rewards[i]
    trialDetails['condition'] = conditions[i]
    trialDetailsList.append(trialDetails)

shuffle(trialDetailsList) # do this now to ensure that order of presentation of rewards and conditions is also shuffled

for k in range(0, numLearningRepetitions):
    for n in range (0, numStim): 
        learningTrialList.append(trialDetailsList[n])

shuffle(learningTrialList)

for o in range(0, numLearningPracTrial):
    p = random.randrange(0, numStim)
    learningPracTrialList.append(trialDetailsList[p])

shuffle(learningPracTrialList)

for q in range (0, numStim):
    if trialDetailsList[q] == 'go':
        trialDetailsList[q]['stopOrGo'] =  'go'
        for i in range(0, goTrialsPerGoStim):
            stopTrialList.append(deepcopy(trialDetailsList[q])
    elif trialDetailsList[q] == 'stop':
        for j in range(0, goTrialsPerStopStim):
            trialDetailsList[q]['stopOrGo'] = 'go'
            stopTrialList.append(deepcopy(trialDetailsList[q])
        for i in range(0, stopTrialsPerStopStim + 1):
            trialDetailsList[q]['stopOrGo'] = 'stop'
            stopTrialList.append(deepcopy(trialDetailsList[q])
            
            
if conditionTwo['condition'] == 'go':
    conditionTwo['stopOrGo'] = 'go'
    stopPracTrialList.append(deepcopy(conditionTwo))
    stopPracTrialList.append(deepcopy(conditionTwo))
    for i in range(1, goTrialsPerGoStim + 1):
        stopTrialList.append(deepcopy(conditionTwo))
else:
    for j in range(1, goTrialsPerStopStim + 1):
        conditionTwo['stopOrGo'] = 'go'
        stopTrialList.append(deepcopy(conditionTwo))
    stopPracTrialList.append(deepcopy(conditionTwo))
    for i in range(1,  stopTrialsPerStopStim + 1):
        conditionTwo['stopOrGo'] = 'stop'
        stopTrialList.append(deepcopy(conditionTwo))
    stopPracTrialList.append(deepcopy(conditionTwo))
if conditionThree['condition'] == 'go':
    conditionThree['stopOrGo'] = 'go'
    stopPracTrialList.append(deepcopy(conditionThree))
    for i in range(1, goTrialsPerGoStim + 1):
        stopTrialList.append(deepcopy(conditionThree))
else:
    for j in range(1, goTrialsPerStopStim + 1):
        conditionThree['stopOrGo'] = 'go'
        stopTrialList.append(deepcopy(conditionThree))
    for i in range(1, stopTrialsPerStopStim + 1):
        conditionThree['stopOrGo'] = 'stop'
        stopTrialList.append(deepcopy(conditionThree))
    stopPracTrialList.append(deepcopy(conditionThree))
if conditionFour['condition'] == 'go':
    conditionFour['stopOrGo'] = 'go'
    stopPracTrialList.append(deepcopy(conditionFour))
    for i in range(1, goTrialsPerGoStim + 1):
        stopTrialList.append(deepcopy(conditionFour))
else:
    for j in range(1, goTrialsPerStopStim + 1):
        conditionFour['stopOrGo'] = 'go'
        stopTrialList.append(deepcopy(conditionFour))
    for i in range(1, stopTrialsPerStopStim + 1):
        conditionFour['stopOrGo'] = 'stop'
        stopTrialList.append(deepcopy(conditionFour))
    stopPracTrialList.append(deepcopy(conditionFour))
if conditionFive['condition'] == 'go':
    conditionFive['stopOrGo'] = 'go'
    stopPracTrialList.append(deepcopy(conditionFive))
    for i in range(1, goTrialsPerGoStim + 1):
        stopTrialList.append(deepcopy(conditionFive))
else:
    for j in range(1, goTrialsPerStopStim + 1):
        conditionFive['stopOrGo'] = 'go'
        stopTrialList.append(deepcopy(conditionFive))
    for i in range(1, stopTrialsPerStopStim + 1):
        conditionFive['stopOrGo'] = 'stop'
        stopTrialList.append(deepcopy(conditionFive))
    stopPracTrialList.append(deepcopy(conditionFive))
if conditionSix['condition'] == 'go':
    conditionSix['stopOrGo'] = 'go'
    stopPracTrialList.append(deepcopy(conditionSix))
    for i in range(1, goTrialsPerGoStim + 1):
        stopTrialList.append(deepcopy(conditionSix))
else:
    for j in range(1, stopTrialsPerStopStim + 1):
        conditionSix['stopOrGo'] = 'go'
        stopTrialList.append(deepcopy(conditionSix))
    for i in range(1, goTrialsPerStopStim + 1):
        conditionSix['stopOrGo'] = 'stop'
        stopTrialList.append(deepcopy(conditionSix))
    stopPracTrialList.append(deepcopy(conditionSix))
if conditionSeven['condition'] == 'go':
    conditionSeven['stopOrGo'] = 'go'
    stopPracTrialList.append(deepcopy(conditionSeven))
    for i in range(1, goTrialsPerGoStim + 1):
        stopTrialList.append(deepcopy(conditionSeven))
else:
    for j in range(1, goTrialsPerStopStim + 1):
        conditionSeven['stopOrGo'] = 'go'
        stopTrialList.append(deepcopy(conditionSeven))
    for i in range(1, stopTrialsPerStopStim + 1):
        conditionSeven['stopOrGo'] = 'stop'
        stopTrialList.append(deepcopy(conditionSeven))
    stopPracTrialList.append(deepcopy(conditionSeven))
if conditionEight['condition'] == 'go':
    conditionEight['stopOrGo'] = 'go'
    stopPracTrialList.append(deepcopy(conditionEight))
    for i in range(1, goTrialsPerGoStim + 1):
        stopTrialList.append(deepcopy(conditionEight))
else:
    for j in range(1, goTrialsPerStopStim + 1):
        conditionEight['stopOrGo'] = 'go'
        stopTrialList.append(deepcopy(conditionEight))
    for i in range(1, stopTrialsPerStopStim + 1):
        conditionEight['stopOrGo'] = 'stop'
        stopTrialList.append(deepcopy(conditionEight))
    stopPracTrialList.append(deepcopy(conditionEight))

shuffle(stopTrialList)
shuffle(stopPracTrialList)

auctionTrials = 80
auctionTrialsPerStim = 10
auctionAmounts = 5
eachAuctionAmountCount = 2
auctionAmountsOne = [34, 68, 102, 136, 170, 204]
auctionAmountsTwo = [39, 78, 117, 156, 195, 234]
auctionAmountsThree = [44, 88, 132, 176, 220, 264]
auctionAmountsFour = [49, 98, 147, 196, 245, 294]
auctionAmountsFive = [54, 108, 162, 216, 270, 324]

for l in range(1, auctionAmounts + 1):
    if l == 1:
        for m in range (1, eachAuctionAmountCount + 1):
            shuffle(auctionAmountsOne)
            conditionOne['auctionAmount'] = auctionAmountsOne
            auctionTrialList.append(deepcopy(conditionOne))
            shuffle(auctionAmountsOne)
            conditionTwo['auctionAmount'] = auctionAmountsOne
            auctionTrialList.append(deepcopy(conditionTwo))
            shuffle(auctionAmountsOne)
            conditionThree['auctionAmount'] = auctionAmountsOne
            auctionTrialList.append(deepcopy(conditionThree))
            shuffle(auctionAmountsOne)
            conditionFour['auctionAmount'] = auctionAmountsOne
            auctionTrialList.append(deepcopy(conditionFour))
            shuffle(auctionAmountsOne)
            conditionFive['auctionAmount'] = auctionAmountsOne
            auctionTrialList.append(deepcopy(conditionFive))
            shuffle(auctionAmountsOne)
            conditionSix['auctionAmount'] = auctionAmountsOne
            auctionTrialList.append(deepcopy(conditionSix))
            shuffle(auctionAmountsOne)
            conditionSeven['auctionAmount'] = auctionAmountsOne
            auctionTrialList.append(deepcopy(conditionSeven))
            shuffle(auctionAmountsOne)
            conditionEight['auctionAmount'] = auctionAmountsOne
            auctionTrialList.append(deepcopy(conditionEight))
    elif l == 2:
        for m in range (1, eachAuctionAmountCount + 1):
            shuffle(auctionAmountsTwo)
            conditionOne['auctionAmount'] = auctionAmountsTwo
            auctionTrialList.append(deepcopy(conditionOne))
            shuffle(auctionAmountsTwo)
            conditionTwo['auctionAmount'] = auctionAmountsTwo
            auctionTrialList.append(deepcopy(conditionTwo))
            shuffle(auctionAmountsTwo)
            conditionThree['auctionAmount'] = auctionAmountsTwo
            auctionTrialList.append(deepcopy(conditionThree))
            shuffle(auctionAmountsTwo)
            conditionFour['auctionAmount'] = auctionAmountsTwo
            auctionTrialList.append(deepcopy(conditionFour))
            shuffle(auctionAmountsTwo)
            conditionFive['auctionAmount'] = auctionAmountsTwo
            auctionTrialList.append(deepcopy(conditionFive))
            shuffle(auctionAmountsTwo)
            conditionSix['auctionAmount'] = auctionAmountsTwo
            auctionTrialList.append(deepcopy(conditionSix))
            shuffle(auctionAmountsTwo)
            conditionSeven['auctionAmount'] = auctionAmountsTwo
            auctionTrialList.append(deepcopy(conditionSeven))
            shuffle(auctionAmountsTwo)
            conditionEight['auctionAmount'] = auctionAmountsTwo
            auctionTrialList.append(deepcopy(conditionEight))
    elif l == 3:
        for m in range (1, eachAuctionAmountCount + 1):
            shuffle(auctionAmountsThree)
            conditionOne['auctionAmount'] = auctionAmountsThree
            auctionTrialList.append(deepcopy(conditionOne))
            shuffle(auctionAmountsThree)
            conditionTwo['auctionAmount'] = auctionAmountsThree
            auctionTrialList.append(deepcopy(conditionTwo))
            shuffle(auctionAmountsThree)
            conditionThree['auctionAmount'] = auctionAmountsThree
            auctionTrialList.append(deepcopy(conditionThree))
            shuffle(auctionAmountsThree)
            conditionFour['auctionAmount'] = auctionAmountsThree
            auctionTrialList.append(deepcopy(conditionFour))
            shuffle(auctionAmountsThree)
            conditionFive['auctionAmount'] = auctionAmountsThree
            auctionTrialList.append(deepcopy(conditionFive))
            shuffle(auctionAmountsThree)
            conditionSix['auctionAmount'] = auctionAmountsThree
            auctionTrialList.append(deepcopy(conditionSix))
            shuffle(auctionAmountsThree)
            conditionSeven['auctionAmount'] = auctionAmountsThree
            auctionTrialList.append(deepcopy(conditionSeven))
            shuffle(auctionAmountsThree)
            conditionEight['auctionAmount'] = auctionAmountsThree
            auctionTrialList.append(deepcopy(conditionEight))
    elif l == 4:
        for m in range (1, eachAuctionAmountCount + 1):
            shuffle(auctionAmountsFour)
            conditionOne['auctionAmount'] = auctionAmountsFour
            auctionTrialList.append(deepcopy(conditionOne))
            shuffle(auctionAmountsFour)
            conditionTwo['auctionAmount'] = auctionAmountsFour
            auctionTrialList.append(deepcopy(conditionTwo))
            shuffle(auctionAmountsFour)
            conditionThree['auctionAmount'] = auctionAmountsFour
            auctionTrialList.append(deepcopy(conditionThree))
            shuffle(auctionAmountsFour)
            conditionFour['auctionAmount'] = auctionAmountsFour
            auctionTrialList.append(deepcopy(conditionFour))
            shuffle(auctionAmountsFour)
            conditionFive['auctionAmount'] = auctionAmountsFour
            auctionTrialList.append(deepcopy(conditionFive))
            shuffle(auctionAmountsFour)
            conditionSix['auctionAmount'] = auctionAmountsFour
            auctionTrialList.append(deepcopy(conditionSix))
            shuffle(auctionAmountsFour)
            conditionSeven['auctionAmount'] = auctionAmountsFour
            auctionTrialList.append(deepcopy(conditionSeven))
            shuffle(auctionAmountsFour)
            conditionEight['auctionAmount'] = auctionAmountsFour
            auctionTrialList.append(deepcopy(conditionEight))
    elif l == 5:
        for m in range (1, eachAuctionAmountCount + 1):
            shuffle(auctionAmountsFive)
            conditionOne['auctionAmount'] = auctionAmountsFive
            auctionTrialList.append(deepcopy(conditionOne))
            shuffle(auctionAmountsFive)
            conditionTwo['auctionAmount'] = auctionAmountsFive
            auctionTrialList.append(deepcopy(conditionTwo))
            shuffle(auctionAmountsFive)
            conditionThree['auctionAmount'] = auctionAmountsFive
            auctionTrialList.append(deepcopy(conditionThree))
            shuffle(auctionAmountsFive)
            conditionFour['auctionAmount'] = auctionAmountsFive
            auctionTrialList.append(deepcopy(conditionFour))
            shuffle(auctionAmountsFive)
            conditionFive['auctionAmount'] = auctionAmountsFive
            auctionTrialList.append(deepcopy(conditionFive))
            shuffle(auctionAmountsFive)
            conditionSix['auctionAmount'] = auctionAmountsFive
            auctionTrialList.append(deepcopy(conditionSix))
            shuffle(auctionAmountsFive)
            conditionSeven['auctionAmount'] = auctionAmountsFive
            auctionTrialList.append(deepcopy(conditionSeven))
            shuffle(auctionAmountsFive)
            conditionEight['auctionAmount'] = auctionAmountsFive
            auctionTrialList.append(deepcopy(conditionEight))

shuffle(auctionTrialList)