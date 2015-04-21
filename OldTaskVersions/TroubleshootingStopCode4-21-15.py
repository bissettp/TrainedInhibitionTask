# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 16:30:58 2015

@author: patrickbissett
"""
from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
from copy import deepcopy
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
from copy import deepcopy
import os  # handy system and path functions

#Set up the 8 options for the four stimulus characteristics (color, shape, reward, condition)
colors = ['yellow', 'white', 'orange', 'magenta', 'green', 'gray', 'cyan', 'blue']
shapes = ['triangle', 'square', 'line', 'invertedtriangle', 'hexagon', 'diamond', 'cross', 'circle']
rewards = [0.50, 1.00, 2.00, 4.00] * 2
conditions = ['go', 'go', 'go', 'go', 'stop', 'stop', 'stop', 'stop']
#Initialize some lists and variables
trialDetailsList = []
learningTrialList = []
learningPracTrialList = []
auctionTrialList = []
rewardList = []
Redo = 1 
rewardCount = 1

shuffle(colors)
shuffle(shapes)

#Randomly select 8 stimuli, with each color and shape selected once, each reward selected twice, and each condition selected four times
for i, color in enumerate(colors): 
    trialDetails = {} 
    trialDetails['fileName'] = shapes[i] + color + '.gif'
    trialDetails['reward'] = rewards[i]
    trialDetails['condition'] = conditions[i]
    trialDetailsList.append(trialDetails)

shuffle(trialDetailsList)

#I was having trouble working with specific lines of the trialDetailsList list object, so I separated each row of the list into separated dict type variables. 
conditionOne = trialDetailsList[0]
conditionTwo = trialDetailsList[1]
conditionThree = trialDetailsList[2]
conditionFour = trialDetailsList[3]
conditionFive = trialDetailsList[4]
conditionSix = trialDetailsList[5]
conditionSeven = trialDetailsList[6]
conditionEight = trialDetailsList[7]

#This is creating the 400 learning trials, 50 from each condition
numLearningTrials = 400
numLearningRepetitions = 50
for k in range(1, numLearningRepetitions + 1):
    learningTrialList.append(conditionOne)
    learningTrialList.append(conditionTwo)
    learningTrialList.append(conditionThree)
    learningTrialList.append(conditionFour)
    learningTrialList.append(conditionFive)
    learningTrialList.append(conditionSix)
    learningTrialList.append(conditionSeven)
    learningTrialList.append(conditionEight)

shuffle(learningTrialList)

#This is a clunky way of creating the 10 learning practice trials. 
learningPracTrialList.append(conditionOne)
learningPracTrialList.append(conditionTwo)
learningPracTrialList.append(conditionThree)
learningPracTrialList.append(conditionFour)
learningPracTrialList.append(conditionFive)
learningPracTrialList.append(conditionSix)
learningPracTrialList.append(conditionSeven)
learningPracTrialList.append(conditionEight)
learningPracTrialList.append(conditionOne)
learningPracTrialList.append(conditionTwo)

shuffle(learningPracTrialList)

#Initializing the number of trials in the stop portion of the task (288 total, 36 per stim, for 'go' conditions all 36 do not have stop signals, for 'stop' conditions 27 of the 36 are stop trials and the other 9 of the 36 are go trials
stopTaskTrials = 288
stopTrialsPerStopStim = 27
goTrialsPerStopStim = 9
goTrialsPerGoStim = 36
numStim = 8
stopTrialList = []
stopPracTrialList = []

#This is really clunky. I would appreciate suggestions on how to improve this aspect of the code. If I could just step through rows of the trialDetailsList then I could have less redundancy hear and loop around the 8 conditions, but when I tried this I couldn't figure out the syntax
if conditionOne['condition'] == 'go':
    conditionOne['stopOrGo'] = 'go'
    stopPracTrialList.append(deepcopy(conditionOne))
    stopPracTrialList.append(deepcopy(conditionOne))
    for i in range(1, goTrialsPerGoStim + 1):
        stopTrialList.append(deepcopy(conditionOne))
else:
    for j in range(1, goTrialsPerStopStim + 1):
        conditionOne['stopOrGo'] = 'go'
        stopTrialList.append(deepcopy(conditionOne))
    stopPracTrialList.append(deepcopy(conditionOne))
    for i in range(1, stopTrialsPerStopStim + 1):
        conditionOne['stopOrGo'] = 'stop'
        stopTrialList.append(deepcopy(conditionOne))
    stopPracTrialList.append(deepcopy(conditionOne))
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

#Each of the 8 conditions (stimuli) are entered into an auction 10 times, with each of the 5 auction amounts presented twice. 
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