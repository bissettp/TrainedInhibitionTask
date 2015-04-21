#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Tue Mar 31 09:52:03 2015
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
    originPath='/Users/patrickbissett/OneDrive/Poldrack/TrainedInhibition/PsychoPy/ShapeLearningTaskCounterbalanceRemovePrac7.psyexp',
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

# Initialize components for Routine "instrPractice"
instrPracticeClock = core.Clock()
instruct1 = visual.TextStim(win=win, ori=0, name='instruct1',
    text='A shape stimulus will appear on every trial. \n\nIf it appears in the upper right quadrant, PRESS I\n\nIf it appears in the lower right quadrant, PRESS K\n\nIf it appears in the lower left quadrant, PRESS J\n\nIf it appears in the upper left quadrant, PRESS U\n\nPress any key when you are ready to proceed. ',    font='Arial',
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
    text=None,    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "ExitMain"
ExitMainClock = core.Clock()


# Initialize components for Routine "instrStopPrac"
instrStopPracClock = core.Clock()
instrStopText = visual.TextStim(win=win, ori=0, name='instrStopText',
    text='A shape stimulus will appear on the left or right side of the screen\n\nIf it appears on the left, press Z\n\nIf it appears on the right, press M\n\nIf you hear a tone, do not press anything on that trial',    font='Arial',
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
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='|',    font='Arial',
    pos=[0, 0], height=4, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image_3 = visual.ImageStim(win=win, name='image_3',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[151, 151],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
sound_1 = sound.Sound('900', secs=-1)
sound_1.setVolume(1)

# Initialize components for Routine "blankStop"
blankStopClock = core.Clock()
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text=u'THIS IS THE BLANK SCREEN',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "SSDChange"
SSDChangeClock = core.Clock()


# Initialize components for Routine "endOfStopBlockFeedback"
endOfStopBlockFeedbackClock = core.Clock()

text_5 = visual.TextStim(win=win, ori=0, name='text_5',
    text=u'blah',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "End"
EndClock = core.Clock()
text_6 = visual.TextStim(win=win, ori=0, name='text_6',
    text=u'This is the end, beautiful friend',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

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
Blocks = data.TrialHandler(nReps=0, method='sequential', 
    extraInfo=expInfo, originPath='/Users/patrickbissett/OneDrive/Poldrack/TrainedInhibition/PsychoPy/ShapeLearningTaskCounterbalanceRemovePrac7.psyexp',
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
        extraInfo=expInfo, originPath='/Users/patrickbissett/OneDrive/Poldrack/TrainedInhibition/PsychoPy/ShapeLearningTaskCounterbalanceRemovePrac7.psyexp',
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
        ReDoLoopMain = data.TrialHandler(nReps=999, method='random', 
            extraInfo=expInfo, originPath='/Users/patrickbissett/OneDrive/Poldrack/TrainedInhibition/PsychoPy/ShapeLearningTaskCounterbalanceRemovePrac7.psyexp',
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
                    theseKeys = event.getKeys(keyList=['u', 'i', 'j', 'k'])
                    
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
            
            if resp.corr:#stored on last run routine
                if displayReward == 1:
                        message = "You won $" + str(0);
                else: 
                        currentReward = currentLearningTrial['reward']
                        message = "You won $" + str(currentReward + (random.randrange(-25, 26)*.01))
            elif resp.keys is None: #or len(key_resp.keys)<1:
            #elif resp.rt == 0:
                message ="Too Slow"
            else:
              message="Wrong"
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
            # the Routine "ExitMain" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed 999 repeats of 'ReDoLoopMain'
        
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
    
# completed 0 repeats of 'Blocks'

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
InitSSD = 250
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
StopBlocks = data.TrialHandler(nReps=4, method='sequential', 
    extraInfo=expInfo, originPath='/Users/patrickbissett/OneDrive/Poldrack/TrainedInhibition/PsychoPy/ShapeLearningTaskCounterbalanceRemovePrac7.psyexp',
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
    StopTrials = data.TrialHandler(nReps=4, method='fullRandom', 
        extraInfo=expInfo, originPath='/Users/patrickbissett/OneDrive/Poldrack/TrainedInhibition/PsychoPy/ShapeLearningTaskCounterbalanceRemovePrac7.psyexp',
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
        
        if xPosGoStim == -200:
            SSD = SSDLeft + 500
        else:
            SSD = SSDRight + 500
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
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        image_3.setPos([xPosGoStim, yPosGoStim])
        image_3.setImage(currentGoStim)
        goResp = event.BuilderKeyResponse()  # create an object of type KeyResponse
        goResp.status = NOT_STARTED
        # keep track of which components have finished
        StopTrialComponents = []
        StopTrialComponents.append(text_3)
        StopTrialComponents.append(image_3)
        StopTrialComponents.append(sound_1)
        StopTrialComponents.append(goResp)
        for thisComponent in StopTrialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "StopTrial"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = StopTrialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
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
            # start/stop sound_1
            if t >= 750 and sound_1.status == NOT_STARTED:
                # keep track of start time/frame for later
                sound_1.tStart = t  # underestimates by a little under one frame
                sound_1.frameNStart = frameN  # exact frame index
                sound_1.play()  # start the sound (it finishes automatically)
            if sound_1.status == STARTED and t >= (750 + (.2-win.monitorFramePeriod*0.75)): #most of one frame period left
                sound_1.stop()  # stop the sound (if longer than duration)
            
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
        if goResp.keys is None:
            if xPosGoStim == -200:
                SSDLeft = SSDLeft  + 50
            if xPosGoStim == 200:
                SSDRight = SSDRight + 50
        else:
            if xPosGoStim == -200:
                SSDLeft = SSDLeft - 50
            if xPosGoStim == 200:
                SSDRight = SSDRight - 50
        
        if currentStopTrial['stopOrGo'] == 'go':
            goTrialCount = goTrialCount + 1
        
        if goResp.corr and currentStopTrial['stopOrGo'] == 'go':
            goCumRT = goCumRT + goResp.rt
            goRTCount = goRTCount + 1
        
        if currentStopTrial['stopOrGo'] == 'stop':
            stopTrialCount = stopTrialCount + 1
        
        if currentStopTrial['stopOrGo'] == 'stop' and goResp.keys is None:
            stopSuccessCount = stopSuccessCount + 1
        
        if goResp.keys is None and currentStopTrial['stopOrGo'] == 'go':
            omissionCount = 0
        
        if goResp != corrGoResp:
            commissionCount = commissionCount + 1
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
        
        # the Routine "SSDChange" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 4 repeats of 'StopTrials'
    
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
    goRTFeedback = str(goCumRT/goRTCount)
    commissionRate = str(commissionCount/goTrialCount)
    omissionRate = str(omissionCount/goTrialCount)
    probabilityOfStop = str(stopSuccessCount/stopTrialCount)
    SSDFeedback = str((SSDLeft+SSDRight)/2)
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
    
# completed 4 repeats of 'StopBlocks'

# get names of stimulus parameters
if StopBlocks.trialList in ([], [None], None):  params = []
else:  params = StopBlocks.trialList[0].keys()
# save data for this loop
StopBlocks.saveAsExcel(filename + '.xlsx', sheetName='StopBlocks',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "End"-------
t = 0
EndClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = []
EndComponents.append(text_6)
for thisComponent in EndComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "End"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t  # underestimates by a little under one frame
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    if text_6.status == STARTED and t >= (0.0 + (5-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_6.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)










win.close()
core.quit()
