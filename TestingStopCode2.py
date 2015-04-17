
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Tue Mar 24 16:06:33 2015
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

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'LearningTask'  # from the Builder filename that created this script
expInfo = {'participant':'', 'gender (m/f)':'', 'age':'', 'session':03}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.WARNING)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(2560, 1440), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "StimSetup"
StimSetupClock = core.Clock()
from copy import deepcopy
colors = ['yellow', 'white', 'orange', 'magenta', 'green', 'gray', 'cyan', 'blue']
shapes = ['triangle', 'square', 'line', 'invertedtriangle', 'hexagon', 'diamond', 'cross', 'circle']
rewards = [0.50, 1.00, 2.00, 4.00] * 2
conditions = ['go', 'go', 'go', 'go', 'stop', 'stop', 'stop', 'stop']
trialDetailsList = []
learningTrialList = []

shuffle(colors)
shuffle(shapes)

for i, color in enumerate(colors): # cycle through each color and keep track of an index number
    trialDetails = {} # a dictionary of key-value pairs
    trialDetails['fileName'] = shapes[i] + color + '.gif'
    trialDetails['reward'] = rewards[i]
    trialDetails['condition'] = conditions[i]
    trialDetailsList.append(trialDetails)

shuffle(trialDetailsList) # do this now to ensure that order of presentation of rewards and conditions is also shuffled

conditionOne = trialDetailsList[0]
conditionTwo = trialDetailsList[1]
conditionThree = trialDetailsList[2]
conditionFour = trialDetailsList[3]
conditionFive = trialDetailsList[4]
conditionSix = trialDetailsList[5]
conditionSeven = trialDetailsList[6]
conditionEight = trialDetailsList[7]

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

stopTaskTrials = 272
stopTrialsPerStopStim = 26
goTrialsPerStopStim = 8
goTrialsPerGoStim = 34
numStim = 8
stopTrialList = []

if conditionOne['condition'] == 'go':
    conditionOne['stopOrGo'] = 'go'
    for i in range(1, goTrialsPerGoStim + 1):
        stopTrialList.append(conditionOne)
else:
    for j in range(1, goTrialsPerStopStim + 1):
        conditionOne['stopOrGo'] = 'go'
        stopTrialList.append(deepcopy(conditionOne))
    for i in range(1, stopTrialsPerStopStim + 1):
        conditionOne['stopOrGo'] = 'stop'
        stopTrialList.append(deepcopy(conditionOne))
if conditionTwo['condition'] == 'go':
    conditionTwo['stopOrGo'] = 'go'
    for i in range(1, goTrialsPerGoStim + 1):
        stopTrialList.append(conditionTwo)
else:
    for j in range(1, goTrialsPerStopStim + 1):
        conditionTwo['stopOrGo'] = 'go'
        stopTrialList.append(deepcopy(conditionTwo))
    for i in range(1,  stopTrialsPerStopStim + 1):
        conditionTwo['stopOrGo'] = 'stop'
        stopTrialList.append(deepcopy(conditionTwo))
if conditionThree['condition'] == 'go':
    conditionThree['stopOrGo'] = 'go'
    for i in range(1, goTrialsPerGoStim + 1):
        stopTrialList.append(conditionThree)
else:
    for j in range(1, goTrialsPerStopStim + 1):
        conditionThree['stopOrGo'] = 'go'
        stopTrialList.append(deepcopy(conditionThree))
    for i in range(1, stopTrialsPerStopStim + 1):
        conditionThree['stopOrGo'] = 'stop'
        stopTrialList.append(deepcopy(conditionThree))
if conditionFour['condition'] == 'go':
    conditionFour['stopOrGo'] = 'go'
    for i in range(1, goTrialsPerGoStim + 1):
        stopTrialList.append(conditionFour)
else:
    for j in range(1, goTrialsPerStopStim + 1):
        conditionFour['stopOrGo'] = 'go'
        stopTrialList.append(deepcopy(conditionFour))
    for i in range(1, stopTrialsPerStopStim + 1):
        conditionFour['stopOrGo'] = 'stop'
        stopTrialList.append(deepcopy(conditionFour))
if conditionFive['condition'] == 'go':
    conditionFive['stopOrGo'] = 'go'
    for i in range(1, goTrialsPerGoStim + 1):
        stopTrialList.append(conditionFive)
else:
    for j in range(1, goTrialsPerStopStim + 1):
        conditionFive['stopOrGo'] = 'go'
        stopTrialList.append(deepcopy(conditionFive))
    for i in range(1, stopTrialsPerStopStim + 1):
        conditionFive['stopOrGo'] = 'stop'
        stopTrialList.append(deepcopy(conditionFive))
if conditionSix['condition'] == 'go':
    conditionSix['stopOrGo'] = 'go'
    for i in range(1, goTrialsPerGoStim + 1):
        stopTrialList.append(conditionSix)
else:
    for j in range(1, stopTrialsPerStopStim + 1):
        conditionSix['stopOrGo'] = 'go'
        stopTrialList.append(deepcopy(conditionSix))
    for i in range(1, goTrialsPerStopStim + 1):
        conditionSix['stopOrGo'] = 'stop'
        stopTrialList.append(deepcopy(conditionSix))
if conditionSeven['condition'] == 'go':
    conditionSeven['stopOrGo'] = 'go'
    for i in range(1, goTrialsPerGoStim + 1):
        stopTrialList.append(conditionSeven)
else:
    for j in range(1, goTrialsPerStopStim + 1):
        conditionSeven['stopOrGo'] = 'go'
        stopTrialList.append(deepcopy(conditionSeven))
    for i in range(1, stopTrialsPerStopStim + 1):
        conditionSeven['stopOrGo'] = 'stop'
        stopTrialList.append(deepcopy(conditionSeven))
if conditionEight['condition'] == 'go':
    conditionEight['stopOrGo'] = 'go'
    for i in range(1, goTrialsPerGoStim + 1):
        stopTrialList.append(conditionEight)
else:
    for j in range(1, goTrialsPerStopStim + 1):
        conditionEight['stopOrGo'] = 'go'
        stopTrialList.append(deepcopy(conditionEight))
    for i in range(1, stopTrialsPerStopStim + 1):
        conditionEight['stopOrGo'] = 'stop'
        stopTrialList.append(deepcopy(conditionEight))

shuffle(stopTrialList)