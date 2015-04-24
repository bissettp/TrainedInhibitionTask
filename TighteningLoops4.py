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
import random
import os  # handy system and path functions

# Initialize components for Routine "StimSetup"
StimSetupClock = core.Clock()

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
numStopPracTrial = 10
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
        learningTrialList.append(deepcopy(trialDetailsList[n]))

shuffle(learningTrialList)

for o in range(0, numLearningPracTrial):
    p = random.randrange(0, numStim)
    learningPracTrialList.append(deepcopy(trialDetailsList[p]))

shuffle(learningPracTrialList)

for q in range(0, numStim):
    if trialDetailsList[q]['condition'] == 'go':
        trialDetailsList[q]['stopOrGo'] =  'go'
        for i in range(0, goTrialsPerGoStim):
            stopTrialList.append(deepcopy(trialDetailsList[q]))
    elif trialDetailsList[q]['condition'] == 'stop': 
        for j in range(0, goTrialsPerStopStim):
            trialDetailsList[q]['stopOrGo'] = 'go'
            stopTrialList.append(deepcopy(trialDetailsList[q]))
        for r in range(0, stopTrialsPerStopStim):
            trialDetailsList[q]['stopOrGo'] = 'stop'
            stopTrialList.append(deepcopy(trialDetailsList[q]))

shuffle(stopTrialList)

for s in range(0, numStopPracTrial):
    s = random.randrange(0, numStim)
    stopPracTrialList.append(deepcopy(trialDetailsList[s]))
    
shuffle(stopPracTrialList)

auctionTrials = 80
auctionTrialsPerStim = 10
auctionAmounts = 5
eachAuctionAmountCount = 2
auctionAmountsList = [[34, 68, 102, 136, 170, 204], [39, 78, 117, 156, 195, 234], [44, 88, 132, 176, 220, 264], [49, 98, 147, 196, 245, 294], [54, 108, 162, 216, 270, 324]]

for l in range(0, auctionAmounts):
    for t in range(0, numStim):
        for u in range(0, eachAuctionAmountCount):
            shuffle(auctionAmountsList[l])
            trialDetailsList[t]['auctionAmount'] = auctionAmountsList[l]
            auctionTrialList.append(deepcopy(trialDetailsList[t]))

shuffle(auctionTrialList)