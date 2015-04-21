#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.03), Wed Mar  4 12:06:20 2015
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
    originPath=u'/Users/patrickbissett/OneDrive/Poldrack/TrainedInhibition/PsychoPy/ColorLoop.psyexp',
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

# Initialize components for Routine "StimSetup"
StimSetupClock = core.Clock()

# Initialize components for Routine "StimSetup"
StimSetupClock = core.Clock()

# Initialize components for Routine "instrPractice"
instrPracticeClock = core.Clock()
instruct1 = visual.TextStim(win=win, ori=0, name='instruct1',
    text='A shape stimulus will appear on every trial. \n\nIf it appears in the upper right quadrant, PRESS Y\n\nIf it appears in the lower right quadrant, PRESS H\n\nIf it appears in the lower left quadrant, PRESS G\n\nIf it appears in the upper left quadrant, PRESS T\n\nPress any key when you are ready to proceed. ',    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
ColorLoop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=u'/Users/patrickbissett/OneDrive/Poldrack/TrainedInhibition/PsychoPy/ColorLoop.psyexp',
    trialList=data.importConditions('Color.xlsx'),
    seed=None, name='ColorLoop')
thisExp.addLoop(ColorLoop)  # add the loop to the experiment
thisColorLoop = ColorLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisColorLoop.rgb)
if thisColorLoop != None:
    for paramName in thisColorLoop.keys():
        exec(paramName + '= thisColorLoop.' + paramName)

for thisColorLoop in ColorLoop:
    currentLoop = ColorLoop
    # abbreviate parameter names if possible (e.g. rgb = thisColorLoop.rgb)
    if thisColorLoop != None:
        for paramName in thisColorLoop.keys():
            exec(paramName + '= thisColorLoop.' + paramName)
    
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
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
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
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "StimSetup"-------
    for thisComponent in StimSetupComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'ColorLoop'

# get names of stimulus parameters
if ColorLoop.trialList in ([], [None], None):  params = []
else:  params = ColorLoop.trialList[0].keys()
# save data for this loop
ColorLoop.saveAsExcel(filename + '.xlsx', sheetName='ColorLoop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
ShapeLoop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=u'/Users/patrickbissett/OneDrive/Poldrack/TrainedInhibition/PsychoPy/ColorLoop.psyexp',
    trialList=data.importConditions(u'Shape.xlsx'),
    seed=None, name='ShapeLoop')
thisExp.addLoop(ShapeLoop)  # add the loop to the experiment
thisShapeLoop = ShapeLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisShapeLoop.rgb)
if thisShapeLoop != None:
    for paramName in thisShapeLoop.keys():
        exec(paramName + '= thisShapeLoop.' + paramName)

for thisShapeLoop in ShapeLoop:
    currentLoop = ShapeLoop
    # abbreviate parameter names if possible (e.g. rgb = thisShapeLoop.rgb)
    if thisShapeLoop != None:
        for paramName in thisShapeLoop.keys():
            exec(paramName + '= thisShapeLoop.' + paramName)
    
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
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
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
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "StimSetup"-------
    for thisComponent in StimSetupComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'ShapeLoop'

# get names of stimulus parameters
if ShapeLoop.trialList in ([], [None], None):  params = []
else:  params = ShapeLoop.trialList[0].keys()
# save data for this loop
ShapeLoop.saveAsExcel(filename + '.xlsx', sheetName='ShapeLoop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
RewardAmountLoop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=u'/Users/patrickbissett/OneDrive/Poldrack/TrainedInhibition/PsychoPy/ColorLoop.psyexp',
    trialList=data.importConditions(u'StopOrGoAndAmount.xlsx'),
    seed=None, name='RewardAmountLoop')
thisExp.addLoop(RewardAmountLoop)  # add the loop to the experiment
thisRewardAmountLoop = RewardAmountLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisRewardAmountLoop.rgb)
if thisRewardAmountLoop != None:
    for paramName in thisRewardAmountLoop.keys():
        exec(paramName + '= thisRewardAmountLoop.' + paramName)

for thisRewardAmountLoop in RewardAmountLoop:
    currentLoop = RewardAmountLoop
    # abbreviate parameter names if possible (e.g. rgb = thisRewardAmountLoop.rgb)
    if thisRewardAmountLoop != None:
        for paramName in thisRewardAmountLoop.keys():
            exec(paramName + '= thisRewardAmountLoop.' + paramName)
    
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
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
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
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "StimSetup"-------
    for thisComponent in StimSetupComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'RewardAmountLoop'

# get names of stimulus parameters
if RewardAmountLoop.trialList in ([], [None], None):  params = []
else:  params = RewardAmountLoop.trialList[0].keys()
# save data for this loop
RewardAmountLoop.saveAsExcel(filename + '.xlsx', sheetName='RewardAmountLoop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

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
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
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
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

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
win.close()
core.quit()
