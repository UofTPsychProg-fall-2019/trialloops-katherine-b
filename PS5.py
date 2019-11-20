#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Tue Nov 19 14:18:51 2019
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'PS5'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/katherinebak/Desktop/Grad School Classes/PSY1210-Programming/trialloops-katherine-b/PS5.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
Instruct = visual.TextStim(win=win, name='Instruct',
    text='You will hear a sentence and will be asked to respond to the last word in the sentence. \n\n\nPRESS ANY KEY TO CONTINUE',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_instruc = keyboard.Keyboard()

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
sound_1 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1)
rating = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.0, pos=[0.0, -0.4], choices=["'correct'", "'incorrect'"], tickHeight=-1)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
# update component parameters for each repeat
key_resp_instruc.keys = []
key_resp_instruc.rt = []
# keep track of which components have finished
InstructionsComponents = [Instruct, key_resp_instruc]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instruct* updates
    if Instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instruct.frameNStart = frameN  # exact frame index
        Instruct.tStart = t  # local t and not account for scr refresh
        Instruct.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruct, 'tStartRefresh')  # time at next scr refresh
        Instruct.setAutoDraw(True)
    
    # *key_resp_instruc* updates
    waitOnFlip = False
    if key_resp_instruc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_instruc.frameNStart = frameN  # exact frame index
        key_resp_instruc.tStart = t  # local t and not account for scr refresh
        key_resp_instruc.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_instruc, 'tStartRefresh')  # time at next scr refresh
        key_resp_instruc.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_instruc.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_instruc.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_instruc.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_instruc.getKeys(keyList=None, waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_instruc.keys = theseKeys.name  # just the last key pressed
            key_resp_instruc.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instruct.started', Instruct.tStartRefresh)
thisExp.addData('Instruct.stopped', Instruct.tStopRefresh)
# check responses
if key_resp_instruc.keys in ['', [], None]:  # No response was made
    key_resp_instruc.keys = None
thisExp.addData('key_resp_instruc.keys',key_resp_instruc.keys)
if key_resp_instruc.keys != None:  # we had a response
    thisExp.addData('key_resp_instruc.rt', key_resp_instruc.rt)
thisExp.addData('key_resp_instruc.started', key_resp_instruc.tStartRefresh)
thisExp.addData('key_resp_instruc.stopped', key_resp_instruc.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('audiostim.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Trial"-------
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    sound_1.setSound(audio, secs=10.0, hamming=True)
    sound_1.setVolume(1, log=False)
    rating.reset()
    # keep track of which components have finished
    TrialComponents = [sound_1, rating]
    for thisComponent in TrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_1
        if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            sound_1.play(when=win)  # sync with win flip
        if sound_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
                sound_1.stop()
        # *rating* updates
        if rating.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating.frameNStart = frameN  # exact frame index
            rating.tStart = t  # local t and not account for scr refresh
            rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating, 'tStartRefresh')  # time at next scr refresh
            rating.setAutoDraw(True)
        continueRoutine &= rating.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trial"-------
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_1.started', sound_1.tStartRefresh)
    trials.addData('sound_1.stopped', sound_1.tStopRefresh)
    # store data for trials (TrialHandler)
    trials.addData('rating.response', rating.getRating())
    trials.addData('rating.rt', rating.getRT())
    trials.addData('rating.started', rating.tStart)
    trials.addData('rating.stopped', rating.tStop)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
