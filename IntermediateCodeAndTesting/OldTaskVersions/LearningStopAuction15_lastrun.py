#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Sun Apr 12 11:06:39 2015
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
    originPath=u'/Users/patrickbissett/OneDrive/Poldrack/TrainedInhibition/PsychoPy/LearningStopAuction15.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.WARNING)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1440, 900), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
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
learningPracTrialList = []
auctionTrialList = []
rewardList = []
Redo = 1 
rewardCount = 1

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

stopTaskTrials = 288
stopTrialsPerStopStim = 27
goTrialsPerStopStim = 9
goTrialsPerGoStim = 36
numStim = 8
stopTrialList = []
stopPracTrialList = []

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

# Initialize components for Routine "instrPractice"
instrPracticeClock = core.Clock()
instruct1 = visual.TextStim(win=win, ori=0, name='instruct1',
    text='A shape stimulus will appear on every trial. \n\nIf it appears in the upper right quadrant, PRESS W\n\nIf it appears in the lower right quadrant, PRESS S\n\nIf it appears in the lower left quadrant, PRESS A\n\nIf it appears in the upper left quadrant, PRESS Q\n\nResponding as fast and as accurately as possible will lead to higher rewards. \n\nPress any key when you are ready to proceed. ',    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "NewPracStim"
NewPracStimClock = core.Clock()


# Initialize components for Routine "trial"
trialClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='+',    font='Arial',
    pos=[0, 0], height=1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
image_2 = visual.ImageStim(win=win, name='image_2',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[151, 151],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
#message variable just needs some value at start
message=0
feedback_2 = visual.TextStim(win=win, ori=0, name='feedback_2',
    text='default text',    font='Arial',
    pos=[0, 0], height=.2, wrapWidth=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    depth=-1.0)
image = visual.ImageStim(win=win, name='image',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[151, 151],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "Blank"
BlankClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text=None,    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "ExitPrac"
ExitPracClock = core.Clock()


# Initialize components for Routine "instrStopPrac"
instrStopPracClock = core.Clock()
instrStopText = visual.TextStim(win=win, ori=0, name='instrStopText',
    text='A shape stimulus will appear on the left or right side of the screen\n\nIf it appears on the left, press Z\n\nIf it appears on the right, press M\n\nIf you hear a tone, do not press anything on that trial\n\nResponding quickly to the location of the shape and withholding your response when you hear a tone are equally important. ',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "newPracStopStim"
newPracStopStimClock = core.Clock()


# Initialize components for Routine "StopTrial"
StopTrialClock = core.Clock()
sound_1 = sound.Sound('900', secs=-1)
sound_1.setVolume(.2)
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='|',    font='Arial',
    pos=[0, 0], height=4, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
image_3 = visual.ImageStim(win=win, name='image_3',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[151, 151],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "blankStop"
blankStopClock = core.Clock()
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text=None,    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "pracStopCleanUp"
pracStopCleanUpClock = core.Clock()


# Initialize components for Routine "endOfStopBlockFeedback"
endOfStopBlockFeedbackClock = core.Clock()

text_5 = visual.TextStim(win=win, ori=0, name='text_5',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "instrPractice"
instrPracticeClock = core.Clock()
instruct1 = visual.TextStim(win=win, ori=0, name='instruct1',
    text='A shape stimulus will appear on every trial. \n\nIf it appears in the upper right quadrant, PRESS W\n\nIf it appears in the lower right quadrant, PRESS S\n\nIf it appears in the lower left quadrant, PRESS A\n\nIf it appears in the upper left quadrant, PRESS Q\n\nResponding as fast and as accurately as possible will lead to higher rewards. \n\nPress any key when you are ready to proceed. ',    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "ResetAtBlock"
ResetAtBlockClock = core.Clock()


# Initialize components for Routine "NewStim"
NewStimClock = core.Clock()


# Initialize components for Routine "trial"
trialClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='+',    font='Arial',
    pos=[0, 0], height=1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
image_2 = visual.ImageStim(win=win, name='image_2',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[151, 151],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
#message variable just needs some value at start
message=0
feedback_2 = visual.TextStim(win=win, ori=0, name='feedback_2',
    text='default text',    font='Arial',
    pos=[0, 0], height=.2, wrapWidth=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    depth=-1.0)
image = visual.ImageStim(win=win, name='image',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[151, 151],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "Blank"
BlankClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text=None,    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "ExitMain"
ExitMainClock = core.Clock()


# Initialize components for Routine "instrStopPrac"
instrStopPracClock = core.Clock()
instrStopText = visual.TextStim(win=win, ori=0, name='instrStopText',
    text='A shape stimulus will appear on the left or right side of the screen\n\nIf it appears on the left, press Z\n\nIf it appears on the right, press M\n\nIf you hear a tone, do not press anything on that trial\n\nResponding quickly to the location of the shape and withholding your response when you hear a tone are equally important. ',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "stopBlockSetup"
stopBlockSetupClock = core.Clock()
goCumRT = 0
goRTCount = 0
omissionCount = 0
commissionCount = 0
stopTrialCount = 0
stopSuccessCount = 0
goTrialCount = 0

# Initialize components for Routine "newStopStim"
newStopStimClock = core.Clock()


# Initialize components for Routine "StopTrial"
StopTrialClock = core.Clock()
sound_1 = sound.Sound('900', secs=-1)
sound_1.setVolume(.2)
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='|',    font='Arial',
    pos=[0, 0], height=4, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
image_3 = visual.ImageStim(win=win, name='image_3',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[151, 151],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "blankStop"
blankStopClock = core.Clock()
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text=None,    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "SSDChange"
SSDChangeClock = core.Clock()


# Initialize components for Routine "endOfStopBlockFeedback"
endOfStopBlockFeedbackClock = core.Clock()

text_5 = visual.TextStim(win=win, ori=0, name='text_5',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "instrAuction"
instrAuctionClock = core.Clock()
text_7 = visual.TextStim(win=win, ori=0, name='text_7',
    text='You will now read instructions on the final phase of the study\n\nPress any key to continue',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "auctionBreak"
auctionBreakClock = core.Clock()
text_9 = visual.TextStim(win=win, ori=0, name='text_9',
    text='Please Take a Break',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "newAuctionStim"
newAuctionStimClock = core.Clock()


# Initialize components for Routine "auctionTrial"
auctionTrialClock = core.Clock()
Fix = visual.TextStim(win=win, ori=0, name='Fix',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
R = visual.TextStim(win=win, ori=0, name='R',
    text=u'R',    font=u'Arial',
    units='norm', pos=[-.75, -.7], height=.2, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)
auctionStim = visual.ImageStim(win=win, name='auctionStim',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[151, 151],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
T = visual.TextStim(win=win, ori=0, name='T',
    text=u'T',    font=u'Arial',
    units='norm', pos=[-.45, -.7], height=0.2, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-3.0)
Y = visual.TextStim(win=win, ori=0, name='Y',
    text=u'Y',    font=u'Arial',
    units='norm', pos=[-.15, -.7], height=0.2, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0)
U = visual.TextStim(win=win, ori=0, name='U',
    text=u'U',    font=u'Arial',
    units='norm', pos=[.15, -.7], height=0.2, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-5.0)
I = visual.TextStim(win=win, ori=0, name='I',
    text=u'I',    font=u'Arial',
    units='norm', pos=[.45, -.7], height=0.2, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-6.0)
O = visual.TextStim(win=win, ori=0, name='O',
    text=u'O',    font=u'Arial',
    units='norm', pos=[.75, -.7], height=0.2, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-7.0)
RAmount = visual.TextStim(win=win, ori=0, name='RAmount',
    text='default text',    font=u'Arial',
    units='norm', pos=[-.75, -.4], height=0.2, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-8.0)
TAmount = visual.TextStim(win=win, ori=0, name='TAmount',
    text='default text',    font=u'Arial',
    units='norm', pos=[-.45, -.4], height=0.2, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-9.0)
YAmount = visual.TextStim(win=win, ori=0, name='YAmount',
    text='default text',    font=u'Arial',
    units='norm', pos=[-.15, -.4], height=0.2, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-10.0)
UAmount = visual.TextStim(win=win, ori=0, name='UAmount',
    text='default text',    font=u'Arial',
    units='norm', pos=[.15, -.4], height=0.2, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-11.0)
IAmount = visual.TextStim(win=win, ori=0, name='IAmount',
    text='default text',    font=u'Arial',
    units='norm', pos=[.45, -.4], height=0.2, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-12.0)
OAmount = visual.TextStim(win=win, ori=0, name='OAmount',
    text='default text',    font=u'Arial',
    units='norm', pos=[.75, -.4], height=0.2, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-13.0)

# Initialize components for Routine "rewardCalc"
rewardCalcClock = core.Clock()

text_11 = visual.TextStim(win=win, ori=0, name='text_11',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "StimSetup"-------
t = 0
StimSetupClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat

# keep track of which components have finished
StimSetupComponents = []
for thisComponent in StimSetupComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "StimSetup"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = StimSetupClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StimSetupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "StimSetup"-------
for thisComponent in StimSetupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "StimSetup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instrPractice"-------
t = 0
instrPracticeClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
ok1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
ok1.status = NOT_STARTED
# keep track of which components have finished
instrPracticeComponents = []
instrPracticeComponents.append(instruct1)
instrPracticeComponents.append(ok1)
for thisComponent in instrPracticeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instrPractice"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instrPracticeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct1* updates
    if t >= 0.0 and instruct1.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruct1.tStart = t  # underestimates by a little under one frame
        instruct1.frameNStart = frameN  # exact frame index
        instruct1.setAutoDraw(True)
    
    # *ok1* updates
    if t >= 0.0 and ok1.status == NOT_STARTED:
        # keep track of start time/frame for later
        ok1.tStart = t  # underestimates by a little under one frame
        ok1.frameNStart = frameN  # exact frame index
        ok1.status = STARTED
        # keyboard checking is just starting
        ok1.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if ok1.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            ok1.keys = theseKeys[-1]  # just the last key pressed
            ok1.rt = ok1.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrPracticeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instrPractice"-------
for thisComponent in instrPracticeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if ok1.keys in ['', [], None]:  # No response was made
   ok1.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('ok1.keys',ok1.keys)
if ok1.keys != None:  # we had a response
    thisExp.addData('ok1.rt', ok1.rt)
thisExp.nextEntry()
# the Routine "instrPractice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
pracTrials = data.TrialHandler(nReps=1, method='fullRandom', 
    extraInfo=expInfo, originPath=u'/Users/patrickbissett/OneDrive/Poldrack/TrainedInhibition/PsychoPy/LearningStopAuction15.psyexp',
    trialList=data.importConditions('TrialtypesLearningPrac.xlsx'),
    seed=None, name='pracTrials')
thisExp.addLoop(pracTrials)  # add the loop to the experiment
thisPracTrial = pracTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisPracTrial.rgb)
if thisPracTrial != None:
    for paramName in thisPracTrial.keys():
        exec(paramName + '= thisPracTrial.' + paramName)

for thisPracTrial in pracTrials:
    currentLoop = pracTrials
    # abbreviate parameter names if possible (e.g. rgb = thisPracTrial.rgb)
    if thisPracTrial != None:
        for paramName in thisPracTrial.keys():
            exec(paramName + '= thisPracTrial.' + paramName)
    
    #------Prepare to start Routine "NewPracStim"-------
    t = 0
    NewPracStimClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    currentLearningPracTrial = learningPracTrialList.pop(0)
    currentStimulus = currentLearningPracTrial['fileName']
    currentReward = currentLearningPracTrial['reward']
    # keep track of which components have finished
    NewPracStimComponents = []
    for thisComponent in NewPracStimComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "NewPracStim"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = NewPracStimClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NewPracStimComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "NewPracStim"-------
    for thisComponent in NewPracStimComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "NewPracStim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    ReDoLoopPrac = data.TrialHandler(nReps=999, method='sequential', 
        extraInfo=expInfo, originPath=u'/Users/patrickbissett/OneDrive/Poldrack/TrainedInhibition/PsychoPy/LearningStopAuction15.psyexp',
        trialList=[None],
        seed=None, name='ReDoLoopPrac')
    thisExp.addLoop(ReDoLoopPrac)  # add the loop to the experiment
    thisReDoLoopPrac = ReDoLoopPrac.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisReDoLoopPrac.rgb)
    if thisReDoLoopPrac != None:
        for paramName in thisReDoLoopPrac.keys():
            exec(paramName + '= thisReDoLoopPrac.' + paramName)
    
    for thisReDoLoopPrac in ReDoLoopPrac:
        currentLoop = ReDoLoopPrac
        # abbreviate parameter names if possible (e.g. rgb = thisReDoLoopPrac.rgb)
        if thisReDoLoopPrac != None:
            for paramName in thisReDoLoopPrac.keys():
                exec(paramName + '= thisReDoLoopPrac.' + paramName)
        
        #------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
        resp.status = NOT_STARTED
        image_2.setPos([xPos, yPos])
        image_2.setImage(currentStimulus)
        # keep track of which components have finished
        trialComponents = []
        trialComponents.append(resp)
        trialComponents.append(text)
        trialComponents.append(image_2)
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "trial"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *resp* updates
            if t >= .5 and resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                resp.tStart = t  # underestimates by a little under one frame
                resp.frameNStart = frameN  # exact frame index
                resp.status = STARTED
                # keyboard checking is just starting
                resp.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if resp.status == STARTED and t >= (.5 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
                resp.status = STOPPED
            if resp.status == STARTED:
                theseKeys = event.getKeys(keyList=['q', 'w', 's', 'a'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    resp.keys = theseKeys[-1]  # just the last key pressed
                    resp.rt = resp.clock.getTime()
                    # was this 'correct'?
                    if (resp.keys == str(corrAns)) or (resp.keys == corrAns):
                        resp.corr = 1
                    else:
                        resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *text* updates
            if t >= 0.0 and text.status == NOT_STARTED:
                # keep track of start time/frame for later
                text.tStart = t  # underestimates by a little under one frame
                text.frameNStart = frameN  # exact frame index
                text.setAutoDraw(True)
            if text.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                text.setAutoDraw(False)
            
            # *image_2* updates
            if t >= .5 and image_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_2.tStart = t  # underestimates by a little under one frame
                image_2.frameNStart = frameN  # exact frame index
                image_2.setAutoDraw(True)
            if image_2.status == STARTED and t >= (.5 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                image_2.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if resp.keys in ['', [], None]:  # No response was made
           resp.keys=None
           # was no response the correct answer?!
           if str(corrAns).lower() == 'none': resp.corr = 1  # correct non-response
           else: resp.corr = 0  # failed to respond (incorrectly)
        # store data for ReDoLoopPrac (TrialHandler)
        ReDoLoopPrac.addData('resp.keys',resp.keys)
        ReDoLoopPrac.addData('resp.corr', resp.corr)
        if resp.keys != None:  # we had a response
            ReDoLoopPrac.addData('resp.rt', resp.rt)
        
        #------Prepare to start Routine "feedback"-------
        t = 0
        feedbackClock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        import random
        
        displayReward = random.randrange(1, 6)
        computedReward = round(currentReward + (random.randrange(-25, 26)*.01), 2)
        
        
        if resp.corr:#stored on last run routine
            if displayReward == 1:
                    message = "You won $0.00"
            else: 
                    message = "You won $ %.2f" %computedReward
        elif resp.keys is None: #or len(key_resp.keys)<1:
        #elif resp.rt == 0:
            message ="Too Slow"
        else:
          message="Wrong"
        
          msg="Correct! RT=%.3f" %(resp.rt)
        feedback_2.setText(message)
        image.setPos([xPos, yPos])
        image.setImage(currentStimulus)
        # keep track of which components have finished
        feedbackComponents = []
        feedbackComponents.append(feedback_2)
        feedbackComponents.append(image)
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "feedback"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = feedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *feedback_2* updates
            if t >= 0.0 and feedback_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedback_2.tStart = t  # underestimates by a little under one frame
                feedback_2.frameNStart = frameN  # exact frame index
                feedback_2.setAutoDraw(True)
            if feedback_2.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                feedback_2.setAutoDraw(False)
            
            # *image* updates
            if t >= 0.0 and image.status == NOT_STARTED:
                # keep track of start time/frame for later
                image.tStart = t  # underestimates by a little under one frame
                image.frameNStart = frameN  # exact frame index
                image.setAutoDraw(True)
            if image.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                image.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "feedback"-------
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        
        #------Prepare to start Routine "Blank"-------
        t = 0
        BlankClock.reset()  # clock 
        frameN = -1
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        BlankComponents = []
        BlankComponents.append(text_2)
        for thisComponent in BlankComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "Blank"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = BlankClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            if t >= 0 and text_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_2.tStart = t  # underestimates by a little under one frame
                text_2.frameNStart = frameN  # exact frame index
                text_2.setAutoDraw(True)
            if text_2.status == STARTED and t >= (0 + (.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                text_2.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BlankComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "Blank"-------
        for thisComponent in BlankComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        #------Prepare to start Routine "ExitPrac"-------
        t = 0
        ExitPracClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        
        # keep track of which components have finished
        ExitPracComponents = []
        for thisComponent in ExitPracComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "ExitPrac"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = ExitPracClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ExitPracComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "ExitPrac"-------
        for thisComponent in ExitPracComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if resp.corr:
            ReDoLoopPrac.finished = True
        # the Routine "ExitPrac" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 999 repeats of 'ReDoLoopPrac'
    
    # get names of stimulus parameters
    if ReDoLoopPrac.trialList in ([], [None], None):  params = []
    else:  params = ReDoLoopPrac.trialList[0].keys()
    # save data for this loop
    ReDoLoopPrac.saveAsExcel(filename + '.xlsx', sheetName='ReDoLoopPrac',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    thisExp.nextEntry()
    
# completed 1 repeats of 'pracTrials'

# get names of stimulus parameters
if pracTrials.trialList in ([], [None], None):  params = []
else:  params = pracTrials.trialList[0].keys()
# save data for this loop
pracTrials.saveAsExcel(filename + '.xlsx', sheetName='pracTrials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "instrStopPrac"-------
t = 0
instrStopPracClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
InitSSD = .25
SSDLeft = InitSSD
SSDRight = InitSSD
# keep track of which components have finished
instrStopPracComponents = []
instrStopPracComponents.append(instrStopText)
instrStopPracComponents.append(key_resp_2)
for thisComponent in instrStopPracComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instrStopPrac"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instrStopPracClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrStopText* updates
    if t >= 0.0 and instrStopText.status == NOT_STARTED:
        # keep track of start time/frame for later
        instrStopText.tStart = t  # underestimates by a little under one frame
        instrStopText.frameNStart = frameN  # exact frame index
        instrStopText.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrStopPracComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instrStopPrac"-------
for thisComponent in instrStopPracComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "instrStopPrac" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
pracStopTrials = data.TrialHandler(nReps=5, method='fullRandom', 
    extraInfo=expInfo, originPath=u'/Users/patrickbissett/OneDrive/Poldrack/TrainedInhibition/PsychoPy/LearningStopAuction15.psyexp',
    trialList=data.importConditions('trialtypeStop.xlsx'),
    seed=None, name='pracStopTrials')
thisExp.addLoop(pracStopTrials)  # add the loop to the experiment
thisPracStopTrial = pracStopTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisPracStopTrial.rgb)
if thisPracStopTrial != None:
    for paramName in thisPracStopTrial.keys():
        exec(paramName + '= thisPracStopTrial.' + paramName)

for thisPracStopTrial in pracStopTrials:
    currentLoop = pracStopTrials
    # abbreviate parameter names if possible (e.g. rgb = thisPracStopTrial.rgb)
    if thisPracStopTrial != None:
        for paramName in thisPracStopTrial.keys():
            exec(paramName + '= thisPracStopTrial.' + paramName)
    
    #------Prepare to start Routine "newPracStopStim"-------
    t = 0
    newPracStopStimClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    currentStopPracTrial = stopPracTrialList.pop(0)
    currentGoStim = currentStopPracTrial['fileName']
    currentStopOrGo = currentStopPracTrial['stopOrGo']
    
    if currentStopOrGo == 'stop':
        SSD = .25
    elif currentStopOrGo == 'go':
        SSD = -1
    
    pracStopTrials.addData("beginningSSD", SSD)
    pracStopTrials.addData("trialType", currentStopOrGo)
    pracStopTrials.addData("goStim", currentGoStim)
    SSDInput = SSD + .5
    # keep track of which components have finished
    newPracStopStimComponents = []
    for thisComponent in newPracStopStimComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "newPracStopStim"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = newPracStopStimClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in newPracStopStimComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "newPracStopStim"-------
    for thisComponent in newPracStopStimComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "newPracStopStim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "StopTrial"-------
    t = 0
    StopTrialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    image_3.setPos([xPosGoStim, yPosGoStim])
    image_3.setImage(currentGoStim)
    goResp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    goResp.status = NOT_STARTED
    # keep track of which components have finished
    StopTrialComponents = []
    StopTrialComponents.append(sound_1)
    StopTrialComponents.append(text_3)
    StopTrialComponents.append(image_3)
    StopTrialComponents.append(goResp)
    for thisComponent in StopTrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "StopTrial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = StopTrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_1
        if t >= SSDInput and sound_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_1.tStart = t  # underestimates by a little under one frame
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.play()  # start the sound (it finishes automatically)
        if sound_1.status == STARTED and t >= (SSDInput + (.2-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_1.stop()  # stop the sound (if longer than duration)
        
        # *text_3* updates
        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t  # underestimates by a little under one frame
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        if text_3.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_3.setAutoDraw(False)
        
        # *image_3* updates
        if t >= .5 and image_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_3.tStart = t  # underestimates by a little under one frame
            image_3.frameNStart = frameN  # exact frame index
            image_3.setAutoDraw(True)
        if image_3.status == STARTED and t >= (.5 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_3.setAutoDraw(False)
        
        # *goResp* updates
        if t >= .5 and goResp.status == NOT_STARTED:
            # keep track of start time/frame for later
            goResp.tStart = t  # underestimates by a little under one frame
            goResp.frameNStart = frameN  # exact frame index
            goResp.status = STARTED
            # keyboard checking is just starting
            goResp.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if goResp.status == STARTED and t >= (.5 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
            goResp.status = STOPPED
        if goResp.status == STARTED:
            theseKeys = event.getKeys(keyList=['z', 'm'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if goResp.keys == []:  # then this was the first keypress
                    goResp.keys = theseKeys[0]  # just the first key pressed
                    goResp.rt = goResp.clock.getTime()
                    # was this 'correct'?
                    if (goResp.keys == str(corrGoResp)) or (goResp.keys == corrGoResp):
                        goResp.corr = 1
                    else:
                        goResp.corr = 0
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StopTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "StopTrial"-------
    for thisComponent in StopTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop() #ensure sound has stopped at end of routine
    # check responses
    if goResp.keys in ['', [], None]:  # No response was made
       goResp.keys=None
       # was no response the correct answer?!
       if str(corrGoResp).lower() == 'none': goResp.corr = 1  # correct non-response
       else: goResp.corr = 0  # failed to respond (incorrectly)
    # store data for pracStopTrials (TrialHandler)
    pracStopTrials.addData('goResp.keys',goResp.keys)
    pracStopTrials.addData('goResp.corr', goResp.corr)
    if goResp.keys != None:  # we had a response
        pracStopTrials.addData('goResp.rt', goResp.rt)
    # the Routine "StopTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "blankStop"-------
    t = 0
    blankStopClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankStopComponents = []
    blankStopComponents.append(text_4)
    for thisComponent in blankStopComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "blankStop"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankStopClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if t >= 0.0 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t  # underestimates by a little under one frame
            text_4.frameNStart = frameN  # exact frame index
            text_4.setAutoDraw(True)
        if text_4.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_4.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankStopComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "blankStop"-------
    for thisComponent in blankStopComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "pracStopCleanUp"-------
    t = 0
    pracStopCleanUpClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    if currentStopPracTrial['stopOrGo'] == 'go':
        goTrialCount = goTrialCount + 1
    
    if goResp.corr and currentStopPracTrial['stopOrGo'] == 'go':
        goCumRT = goCumRT + goResp.rt
        goRTCount = goRTCount + 1
    
    if currentStopPracTrial['stopOrGo'] == 'stop':
        stopTrialCount = stopTrialCount + 1
    
    if currentStopPracTrial['stopOrGo'] == 'stop' and goResp.keys is None:
        stopSuccessCount = stopSuccessCount + 1
    
    if currentStopPracTrial['stopOrGo'] == 'go':
        if goResp.keys is None:
            omissionCount = omissionCount + 1
        elif goResp.corr == 0:
            commissionCount = commissionCount + 1
    
    pracStopTrials.addData("goTrailCountOutput", goTrialCount)
    pracStopTrials.addData("goCumRTOutput", goCumRT)
    pracStopTrials.addData("goRTCountOutput", goRTCount)
    pracStopTrials.addData("stopTrialCountOutput", stopTrialCount)
    pracStopTrials.addData("stopSuccessCountOutput", stopSuccessCount)
    pracStopTrials.addData("omissionCountOutput", omissionCount)
    pracStopTrials.addData("commissionCountOutput", commissionCount)
    # keep track of which components have finished
    pracStopCleanUpComponents = []
    for thisComponent in pracStopCleanUpComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "pracStopCleanUp"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = pracStopCleanUpClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pracStopCleanUpComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "pracStopCleanUp"-------
    for thisComponent in pracStopCleanUpComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "pracStopCleanUp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5 repeats of 'pracStopTrials'

# get names of stimulus parameters
if pracStopTrials.trialList in ([], [None], None):  params = []
else:  params = pracStopTrials.trialList[0].keys()
# save data for this loop
pracStopTrials.saveAsExcel(filename + '.xlsx', sheetName='pracStopTrials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "endOfStopBlockFeedback"-------
t = 0
endOfStopBlockFeedbackClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
if goRTCount > 0:
    goRTFeedback = goCumRT/goRTCount
    goRTFeedback = round(goRTFeedback, 2)
else:
    goRTFeedback = 'Null'

if goTrialCount > 0:
    commissionRate = commissionCount/goTrialCount
    commissionRate = round(commissionRate, 2)
    omissionRate = omissionCount/goTrialCount
    omissionRate = round(omissionRate, 2)
else: 
    commissionRate = 'Null'
    omissionRate = 'Null'

if stopTrialCount > 0: 
    probabilityOfStop = stopSuccessCount/stopTrialCount
    probabilityOfStop = round(probabilityOfStop, 2)
else:
    probabilityOfStop = 'Null'

SSDFeedback = (SSDLeft+SSDRight)/2
SSDFeedback = round(SSDFeedback, 2)

stopMessage = " RT = " + str(goRTFeedback) + "\n Omission % = " + str(omissionRate) + "\n Commission % = " + str(commissionRate) + "\n\n\n\n " + str(probabilityOfStop) + "\n " + str(SSDFeedback)
text_5.setText(stopMessage
)
key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_3.status = NOT_STARTED
# keep track of which components have finished
endOfStopBlockFeedbackComponents = []
endOfStopBlockFeedbackComponents.append(text_5)
endOfStopBlockFeedbackComponents.append(key_resp_3)
for thisComponent in endOfStopBlockFeedbackComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "endOfStopBlockFeedback"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = endOfStopBlockFeedbackClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t  # underestimates by a little under one frame
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # underestimates by a little under one frame
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        key_resp_3.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endOfStopBlockFeedbackComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "endOfStopBlockFeedback"-------
for thisComponent in endOfStopBlockFeedbackComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
   key_resp_3.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "endOfStopBlockFeedback" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instrPractice"-------
t = 0
instrPracticeClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
ok1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
ok1.status = NOT_STARTED
# keep track of which components have finished
instrPracticeComponents = []
instrPracticeComponents.append(instruct1)
instrPracticeComponents.append(ok1)
for thisComponent in instrPracticeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instrPractice"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instrPracticeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct1* updates
    if t >= 0.0 and instruct1.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruct1.tStart = t  # underestimates by a little under one frame
        instruct1.frameNStart = frameN  # exact frame index
        instruct1.setAutoDraw(True)
    
    # *ok1* updates
    if t >= 0.0 and ok1.status == NOT_STARTED:
        # keep track of start time/frame for later
        ok1.tStart = t  # underestimates by a little under one frame
        ok1.frameNStart = frameN  # exact frame index
        ok1.status = STARTED
        # keyboard checking is just starting
        ok1.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if ok1.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            ok1.keys = theseKeys[-1]  # just the last key pressed
            ok1.rt = ok1.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrPracticeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instrPractice"-------
for thisComponent in instrPracticeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if ok1.keys in ['', [], None]:  # No response was made
   ok1.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('ok1.keys',ok1.keys)
if ok1.keys != None:  # we had a response
    thisExp.addData('ok1.rt', ok1.rt)
thisExp.nextEntry()
# the Routine "instrPractice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Blocks = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=u'/Users/patrickbissett/OneDrive/Poldrack/TrainedInhibition/PsychoPy/LearningStopAuction15.psyexp',
    trialList=[None],
    seed=None, name='Blocks')
thisExp.addLoop(Blocks)  # add the loop to the experiment
thisBlock = Blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock.keys():
        exec(paramName + '= thisBlock.' + paramName)

for thisBlock in Blocks:
    currentLoop = Blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock.keys():
            exec(paramName + '= thisBlock.' + paramName)
    
    #------Prepare to start Routine "ResetAtBlock"-------
    t = 0
    ResetAtBlockClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    Redo = 1
    # keep track of which components have finished
    ResetAtBlockComponents = []
    for thisComponent in ResetAtBlockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "ResetAtBlock"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = ResetAtBlockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ResetAtBlockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "ResetAtBlock"-------
    for thisComponent in ResetAtBlockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "ResetAtBlock" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=25.0, method='fullRandom', 
        extraInfo=expInfo, originPath=u'/Users/patrickbissett/OneDrive/Poldrack/TrainedInhibition/PsychoPy/LearningStopAuction15.psyexp',
        trialList=data.importConditions('TrialtypesLearning.xlsx'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial.keys():
                exec(paramName + '= thisTrial.' + paramName)
        
        #------Prepare to start Routine "NewStim"-------
        t = 0
        NewStimClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        currentLearningTrial = learningTrialList.pop(0)
        currentStimulus = currentLearningTrial['fileName']
        currentReward = currentLearningTrial['reward']
        # keep track of which components have finished
        NewStimComponents = []
        for thisComponent in NewStimComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "NewStim"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = NewStimClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in NewStimComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "NewStim"-------
        for thisComponent in NewStimComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "NewStim" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        ReDoLoopMain = data.TrialHandler(nReps=5, method='sequential', 
            extraInfo=expInfo, originPath=u'/Users/patrickbissett/OneDrive/Poldrack/TrainedInhibition/PsychoPy/LearningStopAuction15.psyexp',
            trialList=[None],
            seed=None, name='ReDoLoopMain')
        thisExp.addLoop(ReDoLoopMain)  # add the loop to the experiment
        thisReDoLoopMain = ReDoLoopMain.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb=thisReDoLoopMain.rgb)
        if thisReDoLoopMain != None:
            for paramName in thisReDoLoopMain.keys():
                exec(paramName + '= thisReDoLoopMain.' + paramName)
        
        for thisReDoLoopMain in ReDoLoopMain:
            currentLoop = ReDoLoopMain
            # abbreviate parameter names if possible (e.g. rgb = thisReDoLoopMain.rgb)
            if thisReDoLoopMain != None:
                for paramName in thisReDoLoopMain.keys():
                    exec(paramName + '= thisReDoLoopMain.' + paramName)
            
            #------Prepare to start Routine "trial"-------
            t = 0
            trialClock.reset()  # clock 
            frameN = -1
            routineTimer.add(1.500000)
            # update component parameters for each repeat
            resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
            resp.status = NOT_STARTED
            image_2.setPos([xPos, yPos])
            image_2.setImage(currentStimulus)
            # keep track of which components have finished
            trialComponents = []
            trialComponents.append(resp)
            trialComponents.append(text)
            trialComponents.append(image_2)
            for thisComponent in trialComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "trial"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = trialClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *resp* updates
                if t >= .5 and resp.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    resp.tStart = t  # underestimates by a little under one frame
                    resp.frameNStart = frameN  # exact frame index
                    resp.status = STARTED
                    # keyboard checking is just starting
                    resp.clock.reset()  # now t=0
                    event.clearEvents(eventType='keyboard')
                if resp.status == STARTED and t >= (.5 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
                    resp.status = STOPPED
                if resp.status == STARTED:
                    theseKeys = event.getKeys(keyList=['q', 'w', 's', 'a'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        resp.keys = theseKeys[-1]  # just the last key pressed
                        resp.rt = resp.clock.getTime()
                        # was this 'correct'?
                        if (resp.keys == str(corrAns)) or (resp.keys == corrAns):
                            resp.corr = 1
                        else:
                            resp.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *text* updates
                if t >= 0.0 and text.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text.tStart = t  # underestimates by a little under one frame
                    text.frameNStart = frameN  # exact frame index
                    text.setAutoDraw(True)
                if text.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                    text.setAutoDraw(False)
                
                # *image_2* updates
                if t >= .5 and image_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_2.tStart = t  # underestimates by a little under one frame
                    image_2.frameNStart = frameN  # exact frame index
                    image_2.setAutoDraw(True)
                if image_2.status == STARTED and t >= (.5 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                    image_2.setAutoDraw(False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "trial"-------
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if resp.keys in ['', [], None]:  # No response was made
               resp.keys=None
               # was no response the correct answer?!
               if str(corrAns).lower() == 'none': resp.corr = 1  # correct non-response
               else: resp.corr = 0  # failed to respond (incorrectly)
            # store data for ReDoLoopMain (TrialHandler)
            ReDoLoopMain.addData('resp.keys',resp.keys)
            ReDoLoopMain.addData('resp.corr', resp.corr)
            if resp.keys != None:  # we had a response
                ReDoLoopMain.addData('resp.rt', resp.rt)
            
            #------Prepare to start Routine "feedback"-------
            t = 0
            feedbackClock.reset()  # clock 
            frameN = -1
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            import random
            
            displayReward = random.randrange(1, 6)
            computedReward = round(currentReward + (random.randrange(-25, 26)*.01), 2)
            
            
            if resp.corr:#stored on last run routine
                if displayReward == 1:
                        message = "You won $0.00"
                else: 
                        message = "You won $ %.2f" %computedReward
            elif resp.keys is None: #or len(key_resp.keys)<1:
            #elif resp.rt == 0:
                message ="Too Slow"
            else:
              message="Wrong"
            
              msg="Correct! RT=%.3f" %(resp.rt)
            feedback_2.setText(message)
            image.setPos([xPos, yPos])
            image.setImage(currentStimulus)
            # keep track of which components have finished
            feedbackComponents = []
            feedbackComponents.append(feedback_2)
            feedbackComponents.append(image)
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "feedback"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = feedbackClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *feedback_2* updates
                if t >= 0.0 and feedback_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    feedback_2.tStart = t  # underestimates by a little under one frame
                    feedback_2.frameNStart = frameN  # exact frame index
                    feedback_2.setAutoDraw(True)
                if feedback_2.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                    feedback_2.setAutoDraw(False)
                
                # *image* updates
                if t >= 0.0 and image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image.tStart = t  # underestimates by a little under one frame
                    image.frameNStart = frameN  # exact frame index
                    image.setAutoDraw(True)
                if image.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                    image.setAutoDraw(False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in feedbackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "feedback"-------
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            
            #------Prepare to start Routine "Blank"-------
            t = 0
            BlankClock.reset()  # clock 
            frameN = -1
            routineTimer.add(0.500000)
            # update component parameters for each repeat
            # keep track of which components have finished
            BlankComponents = []
            BlankComponents.append(text_2)
            for thisComponent in BlankComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "Blank"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = BlankClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_2* updates
                if t >= 0 and text_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_2.tStart = t  # underestimates by a little under one frame
                    text_2.frameNStart = frameN  # exact frame index
                    text_2.setAutoDraw(True)
                if text_2.status == STARTED and t >= (0 + (.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                    text_2.setAutoDraw(False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in BlankComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "Blank"-------
            for thisComponent in BlankComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            #------Prepare to start Routine "ExitMain"-------
            t = 0
            ExitMainClock.reset()  # clock 
            frameN = -1
            # update component parameters for each repeat
            
            # keep track of which components have finished
            ExitMainComponents = []
            for thisComponent in ExitMainComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "ExitMain"-------
            continueRoutine = True
            while continueRoutine:
                # get current time
                t = ExitMainClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ExitMainComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "ExitMain"-------
            for thisComponent in ExitMainComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            if resp.corr:
                ReDoLoopMain.finished = True
                rewardList.append(deepcopy(computedReward))
            
            trials.addData("computedRewardOutput", computedReward)
            # the Routine "ExitMain" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 5 repeats of 'ReDoLoopMain'
        
        # get names of stimulus parameters
        if ReDoLoopMain.trialList in ([], [None], None):  params = []
        else:  params = ReDoLoopMain.trialList[0].keys()
        # save data for this loop
        ReDoLoopMain.saveAsExcel(filename + '.xlsx', sheetName='ReDoLoopMain',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        thisExp.nextEntry()
        
    # completed 25.0 repeats of 'trials'
    
    # get names of stimulus parameters
    if trials.trialList in ([], [None], None):  params = []
    else:  params = trials.trialList[0].keys()
    # save data for this loop
    trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    thisExp.nextEntry()
    
# completed 1 repeats of 'Blocks'

# get names of stimulus parameters
if Blocks.trialList in ([], [None], None):  params = []
else:  params = Blocks.trialList[0].keys()
# save data for this loop
Blocks.saveAsExcel(filename + '.xlsx', sheetName='Blocks',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "instrStopPrac"-------
t = 0
instrStopPracClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
InitSSD = .25
SSDLeft = InitSSD
SSDRight = InitSSD
# keep track of which components have finished
instrStopPracComponents = []
instrStopPracComponents.append(instrStopText)
instrStopPracComponents.append(key_resp_2)
for thisComponent in instrStopPracComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instrStopPrac"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instrStopPracClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrStopText* updates
    if t >= 0.0 and instrStopText.status == NOT_STARTED:
        # keep track of start time/frame for later
        instrStopText.tStart = t  # underestimates by a little under one frame
        instrStopText.frameNStart = frameN  # exact frame index
        instrStopText.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrStopPracComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instrStopPrac"-------
for thisComponent in instrStopPracComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "instrStopPrac" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
StopBlocks = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=u'/Users/patrickbissett/OneDrive/Poldrack/TrainedInhibition/PsychoPy/LearningStopAuction15.psyexp',
    trialList=[None],
    seed=None, name='StopBlocks')
thisExp.addLoop(StopBlocks)  # add the loop to the experiment
thisStopBlock = StopBlocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisStopBlock.rgb)
if thisStopBlock != None:
    for paramName in thisStopBlock.keys():
        exec(paramName + '= thisStopBlock.' + paramName)

for thisStopBlock in StopBlocks:
    currentLoop = StopBlocks
    # abbreviate parameter names if possible (e.g. rgb = thisStopBlock.rgb)
    if thisStopBlock != None:
        for paramName in thisStopBlock.keys():
            exec(paramName + '= thisStopBlock.' + paramName)
    
    #------Prepare to start Routine "stopBlockSetup"-------
    t = 0
    stopBlockSetupClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    
    # keep track of which components have finished
    stopBlockSetupComponents = []
    for thisComponent in stopBlockSetupComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "stopBlockSetup"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = stopBlockSetupClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stopBlockSetupComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "stopBlockSetup"-------
    for thisComponent in stopBlockSetupComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "stopBlockSetup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    StopTrials = data.TrialHandler(nReps=18, method='fullRandom', 
        extraInfo=expInfo, originPath=u'/Users/patrickbissett/OneDrive/Poldrack/TrainedInhibition/PsychoPy/LearningStopAuction15.psyexp',
        trialList=data.importConditions('trialtypeStop.xlsx'),
        seed=None, name='StopTrials')
    thisExp.addLoop(StopTrials)  # add the loop to the experiment
    thisStopTrial = StopTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisStopTrial.rgb)
    if thisStopTrial != None:
        for paramName in thisStopTrial.keys():
            exec(paramName + '= thisStopTrial.' + paramName)
    
    for thisStopTrial in StopTrials:
        currentLoop = StopTrials
        # abbreviate parameter names if possible (e.g. rgb = thisStopTrial.rgb)
        if thisStopTrial != None:
            for paramName in thisStopTrial.keys():
                exec(paramName + '= thisStopTrial.' + paramName)
        
        #------Prepare to start Routine "newStopStim"-------
        t = 0
        newStopStimClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        currentStopTrial = stopTrialList.pop(0)
        currentGoStim = currentStopTrial['fileName']
        currentStopOrGo = currentStopTrial['stopOrGo']
        
        if currentStopOrGo == 'stop':
            if xPosGoStim == -200:
                SSD = deepcopy(SSDLeft)
            else:
                SSD = deepcopy(SSDRight)
        elif currentStopOrGo == 'go':
            SSD = -1
        
        StopTrials.addData("beginningSSD", SSD)
        StopTrials.addData("trialType", currentStopOrGo)
        StopTrials.addData("goStim", currentGoStim)
        SSDInput = SSD + .5
        # keep track of which components have finished
        newStopStimComponents = []
        for thisComponent in newStopStimComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "newStopStim"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = newStopStimClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in newStopStimComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "newStopStim"-------
        for thisComponent in newStopStimComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "newStopStim" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        #------Prepare to start Routine "StopTrial"-------
        t = 0
        StopTrialClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        image_3.setPos([xPosGoStim, yPosGoStim])
        image_3.setImage(currentGoStim)
        goResp = event.BuilderKeyResponse()  # create an object of type KeyResponse
        goResp.status = NOT_STARTED
        # keep track of which components have finished
        StopTrialComponents = []
        StopTrialComponents.append(sound_1)
        StopTrialComponents.append(text_3)
        StopTrialComponents.append(image_3)
        StopTrialComponents.append(goResp)
        for thisComponent in StopTrialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "StopTrial"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = StopTrialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop sound_1
            if t >= SSDInput and sound_1.status == NOT_STARTED:
                # keep track of start time/frame for later
                sound_1.tStart = t  # underestimates by a little under one frame
                sound_1.frameNStart = frameN  # exact frame index
                sound_1.play()  # start the sound (it finishes automatically)
            if sound_1.status == STARTED and t >= (SSDInput + (.2-win.monitorFramePeriod*0.75)): #most of one frame period left
                sound_1.stop()  # stop the sound (if longer than duration)
            
            # *text_3* updates
            if t >= 0.0 and text_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_3.tStart = t  # underestimates by a little under one frame
                text_3.frameNStart = frameN  # exact frame index
                text_3.setAutoDraw(True)
            if text_3.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                text_3.setAutoDraw(False)
            
            # *image_3* updates
            if t >= .5 and image_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_3.tStart = t  # underestimates by a little under one frame
                image_3.frameNStart = frameN  # exact frame index
                image_3.setAutoDraw(True)
            if image_3.status == STARTED and t >= (.5 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                image_3.setAutoDraw(False)
            
            # *goResp* updates
            if t >= .5 and goResp.status == NOT_STARTED:
                # keep track of start time/frame for later
                goResp.tStart = t  # underestimates by a little under one frame
                goResp.frameNStart = frameN  # exact frame index
                goResp.status = STARTED
                # keyboard checking is just starting
                goResp.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if goResp.status == STARTED and t >= (.5 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
                goResp.status = STOPPED
            if goResp.status == STARTED:
                theseKeys = event.getKeys(keyList=['z', 'm'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if goResp.keys == []:  # then this was the first keypress
                        goResp.keys = theseKeys[0]  # just the first key pressed
                        goResp.rt = goResp.clock.getTime()
                        # was this 'correct'?
                        if (goResp.keys == str(corrGoResp)) or (goResp.keys == corrGoResp):
                            goResp.corr = 1
                        else:
                            goResp.corr = 0
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in StopTrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "StopTrial"-------
        for thisComponent in StopTrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sound_1.stop() #ensure sound has stopped at end of routine
        # check responses
        if goResp.keys in ['', [], None]:  # No response was made
           goResp.keys=None
           # was no response the correct answer?!
           if str(corrGoResp).lower() == 'none': goResp.corr = 1  # correct non-response
           else: goResp.corr = 0  # failed to respond (incorrectly)
        # store data for StopTrials (TrialHandler)
        StopTrials.addData('goResp.keys',goResp.keys)
        StopTrials.addData('goResp.corr', goResp.corr)
        if goResp.keys != None:  # we had a response
            StopTrials.addData('goResp.rt', goResp.rt)
        # the Routine "StopTrial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        #------Prepare to start Routine "blankStop"-------
        t = 0
        blankStopClock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        blankStopComponents = []
        blankStopComponents.append(text_4)
        for thisComponent in blankStopComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "blankStop"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = blankStopClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_4* updates
            if t >= 0.0 and text_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_4.tStart = t  # underestimates by a little under one frame
                text_4.frameNStart = frameN  # exact frame index
                text_4.setAutoDraw(True)
            if text_4.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                text_4.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blankStopComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "blankStop"-------
        for thisComponent in blankStopComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        #------Prepare to start Routine "SSDChange"-------
        t = 0
        SSDChangeClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        if currentStopTrial['stopOrGo'] == 'stop':
            if goResp.keys is None:
                if SSD <= 800:
                    if xPosGoStim == -200:
                        SSDLeft = deepcopy(SSDLeft)  + .05
                        SSD = SSDLeft
                    if xPosGoStim == 200:
                        SSDRight = deepcopy(SSDRight) + .05
                        SSD = SSDRight
            else:
                if SSD > 0:
                    if xPosGoStim == -200:
                        SSDLeft = deepcopy(SSDLeft) - .05
                        SSD = SSDLeft
                    if xPosGoStim == 200:
                        SSDRight = deepcopy(SSDRight) - .05
                        SSD = SSDRight
        
        if currentStopTrial['stopOrGo'] == 'go':
            goTrialCount = goTrialCount + 1
        
        if goResp.corr and currentStopTrial['stopOrGo'] == 'go':
            goCumRT = goCumRT + goResp.rt
            goRTCount = goRTCount + 1
        
        if currentStopTrial['stopOrGo'] == 'stop':
            stopTrialCount = stopTrialCount + 1
        
        if currentStopTrial['stopOrGo'] == 'stop' and goResp.keys is None:
            stopSuccessCount = stopSuccessCount + 1
        
        if currentStopTrial['stopOrGo'] == 'go':
            if goResp.keys is None:
                omissionCount = omissionCount + 1
            elif goResp.corr == 0:
                commissionCount = commissionCount + 1
        
        StopTrials.addData("goTrailCountOutput", goTrialCount)
        StopTrials.addData("goCumRTOutput", goCumRT)
        StopTrials.addData("goRTCountOutput", goRTCount)
        StopTrials.addData("stopTrialCountOutput", stopTrialCount)
        StopTrials.addData("stopSuccessCountOutput", stopSuccessCount)
        StopTrials.addData("omissionCountOutput", omissionCount)
        StopTrials.addData("commissionCountOutput", commissionCount)
        
        # keep track of which components have finished
        SSDChangeComponents = []
        for thisComponent in SSDChangeComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "SSDChange"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = SSDChangeClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in SSDChangeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "SSDChange"-------
        for thisComponent in SSDChangeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        StopTrials.addData("EndingSSD", SSD)
        # the Routine "SSDChange" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 18 repeats of 'StopTrials'
    
    # get names of stimulus parameters
    if StopTrials.trialList in ([], [None], None):  params = []
    else:  params = StopTrials.trialList[0].keys()
    # save data for this loop
    StopTrials.saveAsExcel(filename + '.xlsx', sheetName='StopTrials',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    #------Prepare to start Routine "endOfStopBlockFeedback"-------
    t = 0
    endOfStopBlockFeedbackClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    if goRTCount > 0:
        goRTFeedback = goCumRT/goRTCount
        goRTFeedback = round(goRTFeedback, 2)
    else:
        goRTFeedback = 'Null'
    
    if goTrialCount > 0:
        commissionRate = commissionCount/goTrialCount
        commissionRate = round(commissionRate, 2)
        omissionRate = omissionCount/goTrialCount
        omissionRate = round(omissionRate, 2)
    else: 
        commissionRate = 'Null'
        omissionRate = 'Null'
    
    if stopTrialCount > 0: 
        probabilityOfStop = stopSuccessCount/stopTrialCount
        probabilityOfStop = round(probabilityOfStop, 2)
    else:
        probabilityOfStop = 'Null'
    
    SSDFeedback = (SSDLeft+SSDRight)/2
    SSDFeedback = round(SSDFeedback, 2)
    
    stopMessage = " RT = " + str(goRTFeedback) + "\n Omission % = " + str(omissionRate) + "\n Commission % = " + str(commissionRate) + "\n\n\n\n " + str(probabilityOfStop) + "\n " + str(SSDFeedback)
    text_5.setText(stopMessage
)
    key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_3.status = NOT_STARTED
    # keep track of which components have finished
    endOfStopBlockFeedbackComponents = []
    endOfStopBlockFeedbackComponents.append(text_5)
    endOfStopBlockFeedbackComponents.append(key_resp_3)
    for thisComponent in endOfStopBlockFeedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "endOfStopBlockFeedback"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = endOfStopBlockFeedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *text_5* updates
        if t >= 0.0 and text_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_5.tStart = t  # underestimates by a little under one frame
            text_5.frameNStart = frameN  # exact frame index
            text_5.setAutoDraw(True)
        
        # *key_resp_3* updates
        if t >= 0.0 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t  # underestimates by a little under one frame
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            key_resp_3.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_3.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_3.keys = theseKeys[-1]  # just the last key pressed
                key_resp_3.rt = key_resp_3.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endOfStopBlockFeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "endOfStopBlockFeedback"-------
    for thisComponent in endOfStopBlockFeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
       key_resp_3.keys=None
    # store data for StopBlocks (TrialHandler)
    StopBlocks.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        StopBlocks.addData('key_resp_3.rt', key_resp_3.rt)
    # the Routine "endOfStopBlockFeedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'StopBlocks'

# get names of stimulus parameters
if StopBlocks.trialList in ([], [None], None):  params = []
else:  params = StopBlocks.trialList[0].keys()
# save data for this loop
StopBlocks.saveAsExcel(filename + '.xlsx', sheetName='StopBlocks',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "instrAuction"-------
t = 0
instrAuctionClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_4.status = NOT_STARTED
# keep track of which components have finished
instrAuctionComponents = []
instrAuctionComponents.append(text_7)
instrAuctionComponents.append(key_resp_4)
for thisComponent in instrAuctionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instrAuction"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instrAuctionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t  # underestimates by a little under one frame
        text_7.frameNStart = frameN  # exact frame index
        text_7.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t  # underestimates by a little under one frame
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        key_resp_4.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys = theseKeys[-1]  # just the last key pressed
            key_resp_4.rt = key_resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrAuctionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instrAuction"-------
for thisComponent in instrAuctionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
   key_resp_4.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "instrAuction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
auctionBlocks = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=u'/Users/patrickbissett/OneDrive/Poldrack/TrainedInhibition/PsychoPy/LearningStopAuction15.psyexp',
    trialList=[None],
    seed=None, name='auctionBlocks')
thisExp.addLoop(auctionBlocks)  # add the loop to the experiment
thisAuctionBlock = auctionBlocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisAuctionBlock.rgb)
if thisAuctionBlock != None:
    for paramName in thisAuctionBlock.keys():
        exec(paramName + '= thisAuctionBlock.' + paramName)

for thisAuctionBlock in auctionBlocks:
    currentLoop = auctionBlocks
    # abbreviate parameter names if possible (e.g. rgb = thisAuctionBlock.rgb)
    if thisAuctionBlock != None:
        for paramName in thisAuctionBlock.keys():
            exec(paramName + '= thisAuctionBlock.' + paramName)
    
    #------Prepare to start Routine "auctionBreak"-------
    t = 0
    auctionBreakClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_5.status = NOT_STARTED
    # keep track of which components have finished
    auctionBreakComponents = []
    auctionBreakComponents.append(text_9)
    auctionBreakComponents.append(key_resp_5)
    for thisComponent in auctionBreakComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "auctionBreak"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = auctionBreakClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_9* updates
        if t >= 0.0 and text_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_9.tStart = t  # underestimates by a little under one frame
            text_9.frameNStart = frameN  # exact frame index
            text_9.setAutoDraw(True)
        
        # *key_resp_5* updates
        if t >= 0.0 and key_resp_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_5.tStart = t  # underestimates by a little under one frame
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            key_resp_5.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_5.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_5.keys = theseKeys[-1]  # just the last key pressed
                key_resp_5.rt = key_resp_5.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in auctionBreakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "auctionBreak"-------
    for thisComponent in auctionBreakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
       key_resp_5.keys=None
    # store data for auctionBlocks (TrialHandler)
    auctionBlocks.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        auctionBlocks.addData('key_resp_5.rt', key_resp_5.rt)
    # the Routine "auctionBreak" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    auctionTrials = data.TrialHandler(nReps=20, method='sequential', 
        extraInfo=expInfo, originPath=u'/Users/patrickbissett/OneDrive/Poldrack/TrainedInhibition/PsychoPy/LearningStopAuction15.psyexp',
        trialList=[None],
        seed=None, name='auctionTrials')
    thisExp.addLoop(auctionTrials)  # add the loop to the experiment
    thisAuctionTrial = auctionTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisAuctionTrial.rgb)
    if thisAuctionTrial != None:
        for paramName in thisAuctionTrial.keys():
            exec(paramName + '= thisAuctionTrial.' + paramName)
    
    for thisAuctionTrial in auctionTrials:
        currentLoop = auctionTrials
        # abbreviate parameter names if possible (e.g. rgb = thisAuctionTrial.rgb)
        if thisAuctionTrial != None:
            for paramName in thisAuctionTrial.keys():
                exec(paramName + '= thisAuctionTrial.' + paramName)
        
        #------Prepare to start Routine "newAuctionStim"-------
        t = 0
        newAuctionStimClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        currentAuctionTrial = auctionTrialList.pop(0)
        currentAuctionStim = currentAuctionTrial['fileName']
        currentAuctionAmount = currentAuctionTrial['auctionAmount']
        currentAuctionAmountOne = currentAuctionAmount[0]
        currentAuctionAmountTwo = currentAuctionAmount[1]
        currentAuctionAmountThree = currentAuctionAmount[2]
        currentAuctionAmountFour = currentAuctionAmount[3]
        currentAuctionAmountFive = currentAuctionAmount[4]
        currentAuctionAmountSix = currentAuctionAmount[5]
        # keep track of which components have finished
        newAuctionStimComponents = []
        for thisComponent in newAuctionStimComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "newAuctionStim"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = newAuctionStimClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in newAuctionStimComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "newAuctionStim"-------
        for thisComponent in newAuctionStimComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "newAuctionStim" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        #------Prepare to start Routine "auctionTrial"-------
        t = 0
        auctionTrialClock.reset()  # clock 
        frameN = -1
        routineTimer.add(6.000000)
        # update component parameters for each repeat
        auctionStim.setImage(currentAuctionStim)
        RAmount.setText(currentAuctionAmountOne)
        TAmount.setText(currentAuctionAmountTwo)
        YAmount.setText(currentAuctionAmountThree)
        UAmount.setText(currentAuctionAmountFour)
        IAmount.setText(currentAuctionAmountFive)
        OAmount.setText(currentAuctionAmountSix)
        auctionResponse = event.BuilderKeyResponse()  # create an object of type KeyResponse
        auctionResponse.status = NOT_STARTED
        # keep track of which components have finished
        auctionTrialComponents = []
        auctionTrialComponents.append(Fix)
        auctionTrialComponents.append(R)
        auctionTrialComponents.append(auctionStim)
        auctionTrialComponents.append(T)
        auctionTrialComponents.append(Y)
        auctionTrialComponents.append(U)
        auctionTrialComponents.append(I)
        auctionTrialComponents.append(O)
        auctionTrialComponents.append(RAmount)
        auctionTrialComponents.append(TAmount)
        auctionTrialComponents.append(YAmount)
        auctionTrialComponents.append(UAmount)
        auctionTrialComponents.append(IAmount)
        auctionTrialComponents.append(OAmount)
        auctionTrialComponents.append(auctionResponse)
        for thisComponent in auctionTrialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "auctionTrial"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = auctionTrialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fix* updates
            if t >= 0.0 and Fix.status == NOT_STARTED:
                # keep track of start time/frame for later
                Fix.tStart = t  # underestimates by a little under one frame
                Fix.frameNStart = frameN  # exact frame index
                Fix.setAutoDraw(True)
            if Fix.status == STARTED and t >= (0.0 + (.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                Fix.setAutoDraw(False)
            
            # *R* updates
            if t >= 1.0 and R.status == NOT_STARTED:
                # keep track of start time/frame for later
                R.tStart = t  # underestimates by a little under one frame
                R.frameNStart = frameN  # exact frame index
                R.setAutoDraw(True)
            if R.status == STARTED and t >= (1.0 + (5-win.monitorFramePeriod*0.75)): #most of one frame period left
                R.setAutoDraw(False)
            
            # *auctionStim* updates
            if t >= .5 and auctionStim.status == NOT_STARTED:
                # keep track of start time/frame for later
                auctionStim.tStart = t  # underestimates by a little under one frame
                auctionStim.frameNStart = frameN  # exact frame index
                auctionStim.setAutoDraw(True)
            if auctionStim.status == STARTED and t >= (.5 + (5.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                auctionStim.setAutoDraw(False)
            
            # *T* updates
            if t >= 1.0 and T.status == NOT_STARTED:
                # keep track of start time/frame for later
                T.tStart = t  # underestimates by a little under one frame
                T.frameNStart = frameN  # exact frame index
                T.setAutoDraw(True)
            if T.status == STARTED and t >= (1.0 + (5.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                T.setAutoDraw(False)
            
            # *Y* updates
            if t >= 1.0 and Y.status == NOT_STARTED:
                # keep track of start time/frame for later
                Y.tStart = t  # underestimates by a little under one frame
                Y.frameNStart = frameN  # exact frame index
                Y.setAutoDraw(True)
            if Y.status == STARTED and t >= (1.0 + (5.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                Y.setAutoDraw(False)
            
            # *U* updates
            if t >= 1.0 and U.status == NOT_STARTED:
                # keep track of start time/frame for later
                U.tStart = t  # underestimates by a little under one frame
                U.frameNStart = frameN  # exact frame index
                U.setAutoDraw(True)
            if U.status == STARTED and t >= (1.0 + (5.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                U.setAutoDraw(False)
            
            # *I* updates
            if t >= 1.0 and I.status == NOT_STARTED:
                # keep track of start time/frame for later
                I.tStart = t  # underestimates by a little under one frame
                I.frameNStart = frameN  # exact frame index
                I.setAutoDraw(True)
            if I.status == STARTED and t >= (1.0 + (5.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                I.setAutoDraw(False)
            
            # *O* updates
            if t >= 1.0 and O.status == NOT_STARTED:
                # keep track of start time/frame for later
                O.tStart = t  # underestimates by a little under one frame
                O.frameNStart = frameN  # exact frame index
                O.setAutoDraw(True)
            if O.status == STARTED and t >= (1.0 + (5.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                O.setAutoDraw(False)
            
            # *RAmount* updates
            if t >= 1.0 and RAmount.status == NOT_STARTED:
                # keep track of start time/frame for later
                RAmount.tStart = t  # underestimates by a little under one frame
                RAmount.frameNStart = frameN  # exact frame index
                RAmount.setAutoDraw(True)
            if RAmount.status == STARTED and t >= (1.0 + (5.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                RAmount.setAutoDraw(False)
            
            # *TAmount* updates
            if t >= 1.0 and TAmount.status == NOT_STARTED:
                # keep track of start time/frame for later
                TAmount.tStart = t  # underestimates by a little under one frame
                TAmount.frameNStart = frameN  # exact frame index
                TAmount.setAutoDraw(True)
            if TAmount.status == STARTED and t >= (1.0 + (5.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                TAmount.setAutoDraw(False)
            
            # *YAmount* updates
            if t >= 1.0 and YAmount.status == NOT_STARTED:
                # keep track of start time/frame for later
                YAmount.tStart = t  # underestimates by a little under one frame
                YAmount.frameNStart = frameN  # exact frame index
                YAmount.setAutoDraw(True)
            if YAmount.status == STARTED and t >= (1.0 + (5.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                YAmount.setAutoDraw(False)
            
            # *UAmount* updates
            if t >= 1.0 and UAmount.status == NOT_STARTED:
                # keep track of start time/frame for later
                UAmount.tStart = t  # underestimates by a little under one frame
                UAmount.frameNStart = frameN  # exact frame index
                UAmount.setAutoDraw(True)
            if UAmount.status == STARTED and t >= (1.0 + (5.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                UAmount.setAutoDraw(False)
            
            # *IAmount* updates
            if t >= 1.0 and IAmount.status == NOT_STARTED:
                # keep track of start time/frame for later
                IAmount.tStart = t  # underestimates by a little under one frame
                IAmount.frameNStart = frameN  # exact frame index
                IAmount.setAutoDraw(True)
            if IAmount.status == STARTED and t >= (1.0 + (5.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                IAmount.setAutoDraw(False)
            
            # *OAmount* updates
            if t >= 1.0 and OAmount.status == NOT_STARTED:
                # keep track of start time/frame for later
                OAmount.tStart = t  # underestimates by a little under one frame
                OAmount.frameNStart = frameN  # exact frame index
                OAmount.setAutoDraw(True)
            if OAmount.status == STARTED and t >= (1.0 + (5.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                OAmount.setAutoDraw(False)
            
            # *auctionResponse* updates
            if t >= 1.0 and auctionResponse.status == NOT_STARTED:
                # keep track of start time/frame for later
                auctionResponse.tStart = t  # underestimates by a little under one frame
                auctionResponse.frameNStart = frameN  # exact frame index
                auctionResponse.status = STARTED
                # keyboard checking is just starting
                auctionResponse.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if auctionResponse.status == STARTED and t >= (1.0 + (5-win.monitorFramePeriod*0.75)): #most of one frame period left
                auctionResponse.status = STOPPED
            if auctionResponse.status == STARTED:
                theseKeys = event.getKeys(keyList=['r', 't', 'y', 'u', 'i', 'o'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if auctionResponse.keys == []:  # then this was the first keypress
                        auctionResponse.keys = theseKeys[0]  # just the first key pressed
                        auctionResponse.rt = auctionResponse.clock.getTime()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in auctionTrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "auctionTrial"-------
        for thisComponent in auctionTrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if auctionResponse.keys in ['', [], None]:  # No response was made
           auctionResponse.keys=None
        # store data for auctionTrials (TrialHandler)
        auctionTrials.addData('auctionResponse.keys',auctionResponse.keys)
        if auctionResponse.keys != None:  # we had a response
            auctionTrials.addData('auctionResponse.rt', auctionResponse.rt)
        thisExp.nextEntry()
        
    # completed 20 repeats of 'auctionTrials'
    
    # get names of stimulus parameters
    if auctionTrials.trialList in ([], [None], None):  params = []
    else:  params = auctionTrials.trialList[0].keys()
    # save data for this loop
    auctionTrials.saveAsExcel(filename + '.xlsx', sheetName='auctionTrials',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    thisExp.nextEntry()
    
# completed 1 repeats of 'auctionBlocks'

# get names of stimulus parameters
if auctionBlocks.trialList in ([], [None], None):  params = []
else:  params = auctionBlocks.trialList[0].keys()
# save data for this loop
auctionBlocks.saveAsExcel(filename + '.xlsx', sheetName='auctionBlocks',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "rewardCalc"-------
t = 0
rewardCalcClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
shuffle(rewardList)
chosenReward1 = rewardList.pop(0)
chosenReward2 = rewardList.pop(1)
chosenReward3 = rewardList.pop(2)
chosenReward4 = rewardList.pop(3)
chosenReward5 = rewardList.pop(4)

totalReward = 12 + chosenReward1 + chosenReward2 + chosenReward3 + chosenReward4 + chosenReward5

displayedReward = "In total, you earned $ %.2f" %totalReward

text_11.setText(displayedReward)
key_resp_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_6.status = NOT_STARTED
# keep track of which components have finished
rewardCalcComponents = []
rewardCalcComponents.append(text_11)
rewardCalcComponents.append(key_resp_6)
for thisComponent in rewardCalcComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rewardCalc"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = rewardCalcClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *text_11* updates
    if t >= 0.0 and text_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_11.tStart = t  # underestimates by a little under one frame
        text_11.frameNStart = frameN  # exact frame index
        text_11.setAutoDraw(True)
    
    # *key_resp_6* updates
    if t >= 0.0 and key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_6.tStart = t  # underestimates by a little under one frame
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        key_resp_6.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_6.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_6.keys = theseKeys[-1]  # just the last key pressed
            key_resp_6.rt = key_resp_6.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in rewardCalcComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rewardCalc"-------
for thisComponent in rewardCalcComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
   key_resp_6.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# the Routine "rewardCalc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()



















win.close()
core.quit()