#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Wed Oct 28 17:50:27 2020
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
psychopyVersion = '2020.1.2'
expName = 'PM'  # from the Builder filename that created this script
expInfo = {'participant': '', 'Group': 'A', 'session': '1'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s' % (expInfo['participant'], expInfo['session'],expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/francescopupillo/OneDrive - University of Aberdeen/prospective memory/Valence Arousal stud/Task/PM_images_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 1024], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "askforPractice"
askforPracticeClock = core.Clock()
PracticeYes=1
PanasYes=1
finalRatings=0
endFirstHalf =1
instructionwordfirst = 1
instructionimagefirst =0

# Initialize components for Routine "Instructions1"
Instructions1Clock = core.Clock()
instructions1 = visual.TextStim(win=win, name='instructions1',
    text='Welcome, \n\nThank you for participating in this experiment. \n\nYou will find all instructions on the screen. \nIf you have any questions please ask the experimenter. \n\nPress {SPACE} to continue. ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=2, ori=0, 
    color='White', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "instructionPanas"
instructionPanasClock = core.Clock()
text_34 = visual.TextStim(win=win, name='text_34',
    text='You are now going to see a number of words that describe different feelings and emotions.\nRead each item and then mark the appropriate answer in the scale underneath to that word, from 1 to 5. \nIndicate to what extent you feel these feelings/emotions right now, at the present moment. \n\nPlease press {Space} to continue.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_25 = keyboard.Keyboard()

# Initialize components for Routine "instructionPanas2"
instructionPanas2Clock = core.Clock()
text_36 = visual.TextStim(win=win, name='text_36',
    text='You can make your choice with the mouse. \nAfter that, click on the number that appears. \n\nClick {Space} to continue',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_27 = keyboard.Keyboard()

# Initialize components for Routine "PanasTest"
PanasTestClock = core.Clock()
text_37 = visual.TextStim(win=win, name='text_37',
    text='default text',
    font='Arial',
    pos=(0, 0.5), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rating = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=5, labels=[''], scale='')
text_38 = visual.TextStim(win=win, name='text_38',
    text='1=not at all 2 = A little 3 = Moderately 4 = Quite a bit 5 = extremely',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_39 = visual.TextStim(win=win, name='text_39',
    text='Click on the number to continue',
    font='Arial',
    pos=(0, -0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text='A series of images will be now presented on the screen.\n\nYour task is to press the {D} button for YES \nwhen the image you are currently seeing is the same as the image that you have seen two trials earlier.\n\nIf this is not the case, press the {L} button for NO.\n\nPress {SPACE} to see an illustration of the task. ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_12 = keyboard.Keyboard()

# Initialize components for Routine "illustration"
illustrationClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "instruction_practice"
instruction_practiceClock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='You will now engage in a short practice session of the image matching task, feedback will be provided after each trial. \n\nKeep in mind: Your task is to press the {D} button for YES when the image you are seeing is the same image that you have seen two trials earlier. \nIf this is not the case, press the {L} button for NO. \n\nPlease place your left index finger on the {D} button and your right index figer on the {L} button. \n\nPress {SPACE} to continue. ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_11 = keyboard.Keyboard()

# Initialize components for Routine "blank_screen"
blank_screenClock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "practice"
practiceClock = core.Clock()
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_10 = visual.TextStim(win=win, name='text_10',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedback=0
#msg=0
msg='doh!'#if this comes up we forgot to update the msg!

text_4 = visual.TextStim(win=win, name='text_4',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "practice_score"
practice_scoreClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "Practice_thanks"
Practice_thanksClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Thank you for completing the practice task!\n\nPress the SPACE BAR to continue. ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "cues_instructions"
cues_instructionsClock = core.Clock()
cues_instruction = visual.TextStim(win=win, name='cues_instruction',
    text='Six special images will now be displayed TWICE.  \n\nPlease remember these images as good as possible. \n   \nPress SPACE to continue. \n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "blank_screen"
blank_screenClock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "cues"
cuesClock = core.Clock()
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_12 = visual.TextStim(win=win, name='text_12',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "cue_instructions2"
cue_instructions2Clock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text='The six special images will be displayed ONE LAST TIME. \n\nPlease remember them as accurately as possible. \n\nPress {SPACE} to continue. ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_13 = keyboard.Keyboard()

# Initialize components for Routine "blank_screen"
blank_screenClock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "cues"
cuesClock = core.Clock()
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_12 = visual.TextStim(win=win, name='text_12',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "thank_you"
thank_youClock = core.Clock()
text_14 = visual.TextStim(win=win, name='text_14',
    text='Thank you!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "task_instructions"
task_instructionsClock = core.Clock()
text_15 = visual.TextStim(win=win, name='text_15',
    text='You will later be asked to work on the same image matching task as you did before. \n\nTherefore, you will have to press the {D} button for YES when the image you are seeing is the same image that you have seen two trials earlier. \nIf this is not the case, press the {L} button. \n\n\nPlease press {SPACE} to continue. ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_14 = keyboard.Keyboard()

# Initialize components for Routine "task_instruction_new"
task_instruction_newClock = core.Clock()
text_45 = visual.TextStim(win=win, name='text_45',
    text='You will later be asked to work on the same matching task as you did before. \n\nHowever, this time you will see images instead of words.\n\nTherefore, you will have to press the {D} button for YES when the image you are seeing is the same image that you have seen two trials earlier. \nIf this is not the case, press the {L} button. \n\n\nPlease press {SPACE} to continue.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_31 = keyboard.Keyboard()

# Initialize components for Routine "PM_instruction"
PM_instructionClock = core.Clock()
text_16 = visual.TextStim(win=win, name='text_16',
    text='In addition, we would like you to press the {H} button, instead of the {D} or or {L} button, every time you see one of the special images you were asked to remember before. \n\nIf you missed the {H} button when one of the previously learned special images appeared, you can always press it afterwards. \n\n\nPlease press {SPACE} to continue. ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_15 = keyboard.Keyboard()

# Initialize components for Routine "questionnaires"
questionnairesClock = core.Clock()
text_17 = visual.TextStim(win=win, name='text_17',
    text='Please approach the experimenter now. \npress {SPACE} to continue. ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_16 = keyboard.Keyboard()

# Initialize components for Routine "countdown"
countdownClock = core.Clock()
text_46 = visual.TextStim(win=win, name='text_46',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "PMintro"
PMintroClock = core.Clock()
text_18 = visual.TextStim(win=win, name='text_18',
    text='You will now engage in the task. \n\nPlease place your left finger on the {D} button and the right finger on the {L} button. \n\n\nPress {SPACE} to continue. ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_17 = keyboard.Keyboard()
sound_1 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1)

# Initialize components for Routine "blank_screen"
blank_screenClock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "PM_task"
PM_taskClock = core.Clock()
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_20 = visual.TextStim(win=win, name='text_20',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_PM = keyboard.Keyboard()

# Initialize components for Routine "end_block1"
end_block1Clock = core.Clock()
text_21 = visual.TextStim(win=win, name='text_21',
    text='Thank you!\n\nThis is the end of this block. ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "recog_task_instr"
recog_task_instrClock = core.Clock()
text_22 = visual.TextStim(win=win, name='text_22',
    text='You will now engage in a recognition task. \nA series of images will be displayed, among them the six special images that you have studied earlier. \n\nPress the {D} button for YES if the image you are seeing is one of the images you have studied earlier. \n\nPress the {L} button for NO if the image you are seeing is NOT on of the images you have studied earlier. \n\n\nPress {SPACE} to continue. ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_20 = keyboard.Keyboard()

# Initialize components for Routine "blank_screen"
blank_screenClock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "recog_task"
recog_taskClock = core.Clock()
image_6 = visual.ImageStim(
    win=win,
    name='image_6', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
key_resp_18 = keyboard.Keyboard()

# Initialize components for Routine "loopcounter"
loopcounterClock = core.Clock()

# Initialize components for Routine "end_first_half"
end_first_halfClock = core.Clock()
text_24 = visual.TextStim(win=win, name='text_24',
    text='Thank you!\n\nPlease approach the experimenter to continue. ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "InstructionCueRatings"
InstructionCueRatingsClock = core.Clock()
text_44 = visual.TextStim(win=win, name='text_44',
    text='You are now going to see the images and the words that you had to remember once again. \n\nPlease rate the valence (positive vs negative) and the arousal (excited vs calm) of each word and image. \n\nPress {Space} to start.  ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_30 = keyboard.Keyboard()

# Initialize components for Routine "Valence"
ValenceClock = core.Clock()
text_47 = visual.TextStim(win=win, name='text_47',
    text='default text',
    font='Arial',
    pos=(0, 0.3), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image_1 = visual.ImageStim(
    win=win,
    name='image_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.4), size=(1,1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
ValenceImg = visual.ImageStim(
    win=win,
    name='ValenceImg', 
    image='sam image.png', mask=None,
    ori=0, pos=(0, -0.3), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
slider_valence = visual.Slider(win=win, name='slider_valence',
    size=(0.81, 0.05), pos=(0, -0.6), units=None,
    labels=None, ticks=(1, 25, 50, 75, 100),
    granularity=1, style=['rating'],
    color='LightGray', font='HelveticaBold',
    flip=False)
text_40 = visual.TextStim(win=win, name='text_40',
    text='Positive                                                    Negative',
    font='Arial',
    pos=(0.015, -0.3), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_28 = keyboard.Keyboard()
text_41 = visual.TextStim(win=win, name='text_41',
    text='Press {Space} to continue',
    font='Arial',
    pos=(0, -0.9), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "Arousal"
ArousalClock = core.Clock()
text_48 = visual.TextStim(win=win, name='text_48',
    text='default text',
    font='Arial',
    pos=(0, 0.3), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.4), size=(1,1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Arousalimage = visual.ImageStim(
    win=win,
    name='Arousalimage', 
    image='sam arousal.png', mask=None,
    ori=0, pos=(0, -0.3), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
slider_arousal = visual.Slider(win=win, name='slider_arousal',
    size=(0.81, 0.05), pos=(0, -0.6), units=None,
    labels=None, ticks=(1, 25, 50, 75, 100),
    granularity=1, style=['rating'],
    color='LightGray', font='HelveticaBold',
    flip=False)
text_42 = visual.TextStim(win=win, name='text_42',
    text='Excited                                                    Calm',
    font='Arial',
    pos=(-0.025, -0.3), height=0.1, wrapWidth=2.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_29 = keyboard.Keyboard()
text_43 = visual.TextStim(win=win, name='text_43',
    text='Press {Space} to continue',
    font='Arial',
    pos=(0, -0.9), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "instruction_check"
instruction_checkClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='Which key were you supposed to press when one of the \nspecial words or special images appeared?\n\nPlease press this key now!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_23 = keyboard.Keyboard()

# Initialize components for Routine "endOfExpMessage"
endOfExpMessageClock = core.Clock()
text_33 = visual.TextStim(win=win, name='text_33',
    text='Thank you!\nThis is the end of the computer task. \n\n\nPlease press {SPACE} and wait for further instructions. \n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_24 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "askforPractice"-------
continueRoutine = True
# update component parameters for each repeat
#if expInfo['Group'] == 'C' or expInfo['Group'] == 'D' or expInfo['Group'] == 'c' or expInfo['Group'] == 'd':
if expInfo['session'] == '2':
    PracticeYes = 0
    PanasYes=0
    finalRatings=1
    endFirstHalf=0
    instructionwordfirst =0
    instructionimagefirst =1
# keep track of which components have finished
askforPracticeComponents = []
for thisComponent in askforPracticeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
askforPracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "askforPractice"-------
while continueRoutine:
    # get current time
    t = askforPracticeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=askforPracticeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in askforPracticeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "askforPractice"-------
for thisComponent in askforPracticeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "askforPractice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Panas_routine = data.TrialHandler(nReps=PanasYes, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Panas_routine')
thisExp.addLoop(Panas_routine)  # add the loop to the experiment
thisPanas_routine = Panas_routine.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPanas_routine.rgb)
if thisPanas_routine != None:
    for paramName in thisPanas_routine:
        exec('{} = thisPanas_routine[paramName]'.format(paramName))

for thisPanas_routine in Panas_routine:
    currentLoop = Panas_routine
    # abbreviate parameter names if possible (e.g. rgb = thisPanas_routine.rgb)
    if thisPanas_routine != None:
        for paramName in thisPanas_routine:
            exec('{} = thisPanas_routine[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Instructions1"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    Instructions1Components = [instructions1, key_resp_3]
    for thisComponent in Instructions1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Instructions1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Instructions1"-------
    while continueRoutine:
        # get current time
        t = Instructions1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Instructions1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions1* updates
        if instructions1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions1.frameNStart = frameN  # exact frame index
            instructions1.tStart = t  # local t and not account for scr refresh
            instructions1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions1, 'tStartRefresh')  # time at next scr refresh
            instructions1.setAutoDraw(True)
        
        # *key_resp_3* updates
        if key_resp_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            key_resp_3.clock.reset()  # now t=0
        if key_resp_3.status == STARTED:
            theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Instructions1"-------
    for thisComponent in Instructions1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Panas_routine.addData('instructions1.started', instructions1.tStartRefresh)
    Panas_routine.addData('instructions1.stopped', instructions1.tStopRefresh)
    # the Routine "Instructions1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "instructionPanas"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_25.keys = []
    key_resp_25.rt = []
    _key_resp_25_allKeys = []
    # keep track of which components have finished
    instructionPanasComponents = [text_34, key_resp_25]
    for thisComponent in instructionPanasComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructionPanasClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructionPanas"-------
    while continueRoutine:
        # get current time
        t = instructionPanasClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructionPanasClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_34* updates
        if text_34.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_34.frameNStart = frameN  # exact frame index
            text_34.tStart = t  # local t and not account for scr refresh
            text_34.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_34, 'tStartRefresh')  # time at next scr refresh
            text_34.setAutoDraw(True)
        
        # *key_resp_25* updates
        waitOnFlip = False
        if key_resp_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_25.frameNStart = frameN  # exact frame index
            key_resp_25.tStart = t  # local t and not account for scr refresh
            key_resp_25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_25, 'tStartRefresh')  # time at next scr refresh
            key_resp_25.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_25.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_25.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_25.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_25.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_25_allKeys.extend(theseKeys)
            if len(_key_resp_25_allKeys):
                key_resp_25.keys = _key_resp_25_allKeys[-1].name  # just the last key pressed
                key_resp_25.rt = _key_resp_25_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionPanasComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructionPanas"-------
    for thisComponent in instructionPanasComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Panas_routine.addData('text_34.started', text_34.tStartRefresh)
    Panas_routine.addData('text_34.stopped', text_34.tStopRefresh)
    # the Routine "instructionPanas" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "instructionPanas2"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_27.keys = []
    key_resp_27.rt = []
    _key_resp_27_allKeys = []
    # keep track of which components have finished
    instructionPanas2Components = [text_36, key_resp_27]
    for thisComponent in instructionPanas2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructionPanas2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructionPanas2"-------
    while continueRoutine:
        # get current time
        t = instructionPanas2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructionPanas2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_36* updates
        if text_36.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_36.frameNStart = frameN  # exact frame index
            text_36.tStart = t  # local t and not account for scr refresh
            text_36.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_36, 'tStartRefresh')  # time at next scr refresh
            text_36.setAutoDraw(True)
        
        # *key_resp_27* updates
        if key_resp_27.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_27.frameNStart = frameN  # exact frame index
            key_resp_27.tStart = t  # local t and not account for scr refresh
            key_resp_27.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_27, 'tStartRefresh')  # time at next scr refresh
            key_resp_27.status = STARTED
            # keyboard checking is just starting
            key_resp_27.clock.reset()  # now t=0
        if key_resp_27.status == STARTED:
            theseKeys = key_resp_27.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_27_allKeys.extend(theseKeys)
            if len(_key_resp_27_allKeys):
                key_resp_27.keys = _key_resp_27_allKeys[-1].name  # just the last key pressed
                key_resp_27.rt = _key_resp_27_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionPanas2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructionPanas2"-------
    for thisComponent in instructionPanas2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Panas_routine.addData('text_36.started', text_36.tStartRefresh)
    Panas_routine.addData('text_36.stopped', text_36.tStopRefresh)
    # the Routine "instructionPanas2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Panas 2\\panas.xlsx'),
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
        
        # ------Prepare to start Routine "PanasTest"-------
        continueRoutine = True
        # update component parameters for each repeat
        text_37.setText(adjective)
        rating.reset()
        # keep track of which components have finished
        PanasTestComponents = [text_37, rating, text_38, text_39]
        for thisComponent in PanasTestComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PanasTestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "PanasTest"-------
        while continueRoutine:
            # get current time
            t = PanasTestClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PanasTestClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_37* updates
            if text_37.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_37.frameNStart = frameN  # exact frame index
                text_37.tStart = t  # local t and not account for scr refresh
                text_37.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_37, 'tStartRefresh')  # time at next scr refresh
                text_37.setAutoDraw(True)
            # *rating* updates
            if rating.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rating.frameNStart = frameN  # exact frame index
                rating.tStart = t  # local t and not account for scr refresh
                rating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rating, 'tStartRefresh')  # time at next scr refresh
                rating.setAutoDraw(True)
            continueRoutine &= rating.noResponse  # a response ends the trial
            
            # *text_38* updates
            if text_38.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_38.frameNStart = frameN  # exact frame index
                text_38.tStart = t  # local t and not account for scr refresh
                text_38.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_38, 'tStartRefresh')  # time at next scr refresh
                text_38.setAutoDraw(True)
            
            # *text_39* updates
            if text_39.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_39.frameNStart = frameN  # exact frame index
                text_39.tStart = t  # local t and not account for scr refresh
                text_39.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_39, 'tStartRefresh')  # time at next scr refresh
                text_39.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PanasTestComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "PanasTest"-------
        for thisComponent in PanasTestComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('text_37.started', text_37.tStartRefresh)
        trials.addData('text_37.stopped', text_37.tStopRefresh)
        # store data for trials (TrialHandler)
        trials.addData('rating.response', rating.getRating())
        trials.addData('rating.rt', rating.getRT())
        trials.addData('rating.started', rating.tStart)
        trials.addData('rating.stopped', rating.tStop)
        trials.addData('text_38.started', text_38.tStartRefresh)
        trials.addData('text_38.stopped', text_38.tStopRefresh)
        trials.addData('text_39.started', text_39.tStartRefresh)
        trials.addData('text_39.stopped', text_39.tStopRefresh)
        # the Routine "PanasTest" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed PanasYes repeats of 'Panas_routine'


# set up handler to look after randomisation of conditions etc
skip_routine = data.TrialHandler(nReps=PracticeYes, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='skip_routine')
thisExp.addLoop(skip_routine)  # add the loop to the experiment
thisSkip_routine = skip_routine.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSkip_routine.rgb)
if thisSkip_routine != None:
    for paramName in thisSkip_routine:
        exec('{} = thisSkip_routine[paramName]'.format(paramName))

for thisSkip_routine in skip_routine:
    currentLoop = skip_routine
    # abbreviate parameter names if possible (e.g. rgb = thisSkip_routine.rgb)
    if thisSkip_routine != None:
        for paramName in thisSkip_routine:
            exec('{} = thisSkip_routine[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_12.keys = []
    key_resp_12.rt = []
    _key_resp_12_allKeys = []
    # keep track of which components have finished
    instructionsComponents = [text_9, key_resp_12]
    for thisComponent in instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructions"-------
    while continueRoutine:
        # get current time
        t = instructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_9* updates
        if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_9.frameNStart = frameN  # exact frame index
            text_9.tStart = t  # local t and not account for scr refresh
            text_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
            text_9.setAutoDraw(True)
        
        # *key_resp_12* updates
        waitOnFlip = False
        if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_12.frameNStart = frameN  # exact frame index
            key_resp_12.tStart = t  # local t and not account for scr refresh
            key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
            key_resp_12.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_12.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_12.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_12_allKeys.extend(theseKeys)
            if len(_key_resp_12_allKeys):
                key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
                key_resp_12.rt = _key_resp_12_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    skip_routine.addData('text_9.started', text_9.tStartRefresh)
    skip_routine.addData('text_9.stopped', text_9.tStopRefresh)
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    illustration_loop = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('illustrations2.xlsx'),
        seed=None, name='illustration_loop')
    thisExp.addLoop(illustration_loop)  # add the loop to the experiment
    thisIllustration_loop = illustration_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisIllustration_loop.rgb)
    if thisIllustration_loop != None:
        for paramName in thisIllustration_loop:
            exec('{} = thisIllustration_loop[paramName]'.format(paramName))
    
    for thisIllustration_loop in illustration_loop:
        currentLoop = illustration_loop
        # abbreviate parameter names if possible (e.g. rgb = thisIllustration_loop.rgb)
        if thisIllustration_loop != None:
            for paramName in thisIllustration_loop:
                exec('{} = thisIllustration_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "illustration"-------
        continueRoutine = True
        # update component parameters for each repeat
        image.setImage(images)
        key_resp_10.keys = []
        key_resp_10.rt = []
        _key_resp_10_allKeys = []
        # keep track of which components have finished
        illustrationComponents = [image, key_resp_10]
        for thisComponent in illustrationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        illustrationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "illustration"-------
        while continueRoutine:
            # get current time
            t = illustrationClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=illustrationClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image* updates
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                image.setAutoDraw(True)
            
            # *key_resp_10* updates
            waitOnFlip = False
            if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_10.frameNStart = frameN  # exact frame index
                key_resp_10.tStart = t  # local t and not account for scr refresh
                key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
                key_resp_10.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_10.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_10.getKeys(keyList=['space', 'l', 'd'], waitRelease=False)
                _key_resp_10_allKeys.extend(theseKeys)
                if len(_key_resp_10_allKeys):
                    key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
                    key_resp_10.rt = _key_resp_10_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in illustrationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "illustration"-------
        for thisComponent in illustrationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        illustration_loop.addData('image.started', image.tStartRefresh)
        illustration_loop.addData('image.stopped', image.tStopRefresh)
        # the Routine "illustration" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'illustration_loop'
    
    
    # ------Prepare to start Routine "instruction_practice"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_11.keys = []
    key_resp_11.rt = []
    _key_resp_11_allKeys = []
    # keep track of which components have finished
    instruction_practiceComponents = [text_8, key_resp_11]
    for thisComponent in instruction_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instruction_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instruction_practice"-------
    while continueRoutine:
        # get current time
        t = instruction_practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instruction_practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            text_8.setAutoDraw(True)
        
        # *key_resp_11* updates
        waitOnFlip = False
        if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_11.frameNStart = frameN  # exact frame index
            key_resp_11.tStart = t  # local t and not account for scr refresh
            key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
            key_resp_11.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_11.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_11.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_11_allKeys.extend(theseKeys)
            if len(_key_resp_11_allKeys):
                key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
                key_resp_11.rt = _key_resp_11_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruction_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instruction_practice"-------
    for thisComponent in instruction_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    skip_routine.addData('text_8.started', text_8.tStartRefresh)
    skip_routine.addData('text_8.stopped', text_8.tStopRefresh)
    # the Routine "instruction_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank_screen"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank_screenComponents = [blank]
    for thisComponent in blank_screenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank_screen"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank_screenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank_screenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank_screenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank_screen"-------
    for thisComponent in blank_screenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    skip_routine.addData('blank.started', blank.tStartRefresh)
    skip_routine.addData('blank.stopped', blank.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    repeat_practice = data.TrialHandler(nReps=999, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='repeat_practice')
    thisExp.addLoop(repeat_practice)  # add the loop to the experiment
    thisRepeat_practice = repeat_practice.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRepeat_practice.rgb)
    if thisRepeat_practice != None:
        for paramName in thisRepeat_practice:
            exec('{} = thisRepeat_practice[paramName]'.format(paramName))
    
    for thisRepeat_practice in repeat_practice:
        currentLoop = repeat_practice
        # abbreviate parameter names if possible (e.g. rgb = thisRepeat_practice.rgb)
        if thisRepeat_practice != None:
            for paramName in thisRepeat_practice:
                exec('{} = thisRepeat_practice[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        trials_2 = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('practice images.xlsx'),
            seed=None, name='trials_2')
        thisExp.addLoop(trials_2)  # add the loop to the experiment
        thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        for thisTrial_2 in trials_2:
            currentLoop = trials_2
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
            if thisTrial_2 != None:
                for paramName in thisTrial_2:
                    exec('{} = thisTrial_2[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "practice"-------
            continueRoutine = True
            routineTimer.add(1.700000)
            # update component parameters for each repeat
            image_3.setImage(images)
            key_resp_6.keys = []
            key_resp_6.rt = []
            _key_resp_6_allKeys = []
            # keep track of which components have finished
            practiceComponents = [image_3, text_10, key_resp_6]
            for thisComponent in practiceComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "practice"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = practiceClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=practiceClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_3* updates
                if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_3.frameNStart = frameN  # exact frame index
                    image_3.tStart = t  # local t and not account for scr refresh
                    image_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                    image_3.setAutoDraw(True)
                if image_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_3.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        image_3.tStop = t  # not accounting for scr refresh
                        image_3.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(image_3, 'tStopRefresh')  # time at next scr refresh
                        image_3.setAutoDraw(False)
                
                # *text_10* updates
                if text_10.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    text_10.frameNStart = frameN  # exact frame index
                    text_10.tStart = t  # local t and not account for scr refresh
                    text_10.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
                    text_10.setAutoDraw(True)
                if text_10.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_10.tStartRefresh + 0.2-frameTolerance:
                        # keep track of stop time/frame for later
                        text_10.tStop = t  # not accounting for scr refresh
                        text_10.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_10, 'tStopRefresh')  # time at next scr refresh
                        text_10.setAutoDraw(False)
                
                # *key_resp_6* updates
                waitOnFlip = False
                if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_6.frameNStart = frameN  # exact frame index
                    key_resp_6.tStart = t  # local t and not account for scr refresh
                    key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
                    key_resp_6.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
                if key_resp_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_6.tStartRefresh + 1.7-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_6.tStop = t  # not accounting for scr refresh
                        key_resp_6.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(key_resp_6, 'tStopRefresh')  # time at next scr refresh
                        key_resp_6.status = FINISHED
                if key_resp_6.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_6.getKeys(keyList=['d', 'l'], waitRelease=False)
                    _key_resp_6_allKeys.extend(theseKeys)
                    if len(_key_resp_6_allKeys):
                        key_resp_6.keys = [key.name for key in _key_resp_6_allKeys]  # storing all keys
                        key_resp_6.rt = [key.rt for key in _key_resp_6_allKeys]
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in practiceComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "practice"-------
            for thisComponent in practiceComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_2.addData('image_3.started', image_3.tStartRefresh)
            trials_2.addData('image_3.stopped', image_3.tStopRefresh)
            trials_2.addData('text_10.started', text_10.tStartRefresh)
            trials_2.addData('text_10.stopped', text_10.tStopRefresh)
            # check responses
            if key_resp_6.keys in ['', [], None]:  # No response was made
                key_resp_6.keys = None
            trials_2.addData('key_resp_6.keys',key_resp_6.keys)
            if key_resp_6.keys != None:  # we had a response
                trials_2.addData('key_resp_6.rt', key_resp_6.rt)
            trials_2.addData('key_resp_6.started', key_resp_6.tStartRefresh)
            trials_2.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
            
            # ------Prepare to start Routine "feedback"-------
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            if key_resp_6.keys in ['', [], None]:  # No response was made
                    key_resp_6.keys=None
                    key_resp_6.corr = 0
                    feedback='incorrect'
                    feedbcol='red'
                    trials_2.addData('key_resp_6.keys',key_resp_6.keys)
                    trials_2.addData('key_resp_6.corr', key_resp_6.corr)
            if key_resp_6.keys != None:
                if (str(key_resp_6.keys)[2] == str(corrAnsw)) or (str(key_resp_6.keys)[2] == corrAnsw):
                            key_resp_6.corr = 1
                            feedback='correct'
                            feedbcol='green'
                else:
                                key_resp_6.corr = 0
                                feedback='incorrect'
                                feedbcol='red'
            
            
            
            # check responses
            # check responses
            
                        # store data for trials_2 (TrialHandler)
                trials_2.addData('key_resp_6.keys',key_resp_6.keys)
                trials_2.addData('key_resp_6.corr', key_resp_6.corr)
                trials_2.addData('key_resp_6.rt', key_resp_6.rt)
                trials_2.addData('key_resp_6.rtFirst', key_resp_6.rt[0])
            
            
            nCorr = trials_2.data['key_resp_6.corr'].sum() #.std(), .mean() also available5
            #meanRt = trials_2.data['key_resp_6.rt'].mean()
            perCorr=round((trials_2.data['key_resp_6.corr'].sum()/len(trials_2.trialList))*100)
            #msg = "You got %d trials correct" %nCorr
            msg= "You got %d %% correct. \n\nPlease approach the experimenter \n\nPress 'y' to do the task again and 'n' to continue with the experiment" %perCorr
            
            text_4.setColor(feedbcol, colorSpace='rgb')
            text_4.setText(feedback)
            # keep track of which components have finished
            feedbackComponents = [text_4]
            for thisComponent in feedbackComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "feedback"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = feedbackClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_4* updates
                if text_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    text_4.frameNStart = frameN  # exact frame index
                    text_4.tStart = t  # local t and not account for scr refresh
                    text_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                    text_4.setAutoDraw(True)
                if text_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_4.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        text_4.tStop = t  # not accounting for scr refresh
                        text_4.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                        text_4.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in feedbackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "feedback"-------
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_2.addData('text_4.started', text_4.tStartRefresh)
            trials_2.addData('text_4.stopped', text_4.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'trials_2'
        
        
        # ------Prepare to start Routine "practice_score"-------
        continueRoutine = True
        # update component parameters for each repeat
        text_5.setColor('white', colorSpace='rgb')
        text_5.setText(msg
)
        key_resp_4.keys = []
        key_resp_4.rt = []
        _key_resp_4_allKeys = []
        # keep track of which components have finished
        practice_scoreComponents = [text_5, key_resp_4]
        for thisComponent in practice_scoreComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        practice_scoreClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "practice_score"-------
        while continueRoutine:
            # get current time
            t = practice_scoreClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=practice_scoreClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_5* updates
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                text_5.setAutoDraw(True)
            
            # *key_resp_4* updates
            waitOnFlip = False
            if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_4.frameNStart = frameN  # exact frame index
                key_resp_4.tStart = t  # local t and not account for scr refresh
                key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                key_resp_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            if key_resp_4.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_4.getKeys(keyList=['y', 'n', 'l', 'd'], waitRelease=False)
                _key_resp_4_allKeys.extend(theseKeys)
                if len(_key_resp_4_allKeys):
                    key_resp_4.keys = _key_resp_4_allKeys[0].name  # just the first key pressed
                    key_resp_4.rt = _key_resp_4_allKeys[0].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practice_scoreComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "practice_score"-------
        for thisComponent in practice_scoreComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        repeat_practice.addData('text_5.started', text_5.tStartRefresh)
        repeat_practice.addData('text_5.stopped', text_5.tStopRefresh)
        # check responses
        if key_resp_4.keys in ['', [], None]:  # No response was made
            key_resp_4.keys = None
        repeat_practice.addData('key_resp_4.keys',key_resp_4.keys)
        if key_resp_4.keys != None:  # we had a response
            repeat_practice.addData('key_resp_4.rt', key_resp_4.rt)
        repeat_practice.addData('key_resp_4.started', key_resp_4.tStartRefresh)
        repeat_practice.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
        if ((key_resp_4.keys) =='n'):
         repeat_practice.finished = True
        # the Routine "practice_score" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 999 repeats of 'repeat_practice'
    
    
    # ------Prepare to start Routine "Practice_thanks"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    # keep track of which components have finished
    Practice_thanksComponents = [text_6, key_resp_7]
    for thisComponent in Practice_thanksComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Practice_thanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Practice_thanks"-------
    while continueRoutine:
        # get current time
        t = Practice_thanksClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Practice_thanksClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        
        # *key_resp_7* updates
        waitOnFlip = False
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Practice_thanksComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Practice_thanks"-------
    for thisComponent in Practice_thanksComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    skip_routine.addData('text_6.started', text_6.tStartRefresh)
    skip_routine.addData('text_6.stopped', text_6.tStopRefresh)
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
    skip_routine.addData('key_resp_7.keys',key_resp_7.keys)
    if key_resp_7.keys != None:  # we had a response
        skip_routine.addData('key_resp_7.rt', key_resp_7.rt)
    skip_routine.addData('key_resp_7.started', key_resp_7.tStartRefresh)
    skip_routine.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
    # the Routine "Practice_thanks" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed PracticeYes repeats of 'skip_routine'


# set up handler to look after randomisation of conditions etc
Group = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions("Group"+expInfo['Group']+".xlsx"),
    seed=None, name='Group')
thisExp.addLoop(Group)  # add the loop to the experiment
thisGroup = Group.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisGroup.rgb)
if thisGroup != None:
    for paramName in thisGroup:
        exec('{} = thisGroup[paramName]'.format(paramName))

for thisGroup in Group:
    currentLoop = Group
    # abbreviate parameter names if possible (e.g. rgb = thisGroup.rgb)
    if thisGroup != None:
        for paramName in thisGroup:
            exec('{} = thisGroup[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "cues_instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_8.keys = []
    key_resp_8.rt = []
    _key_resp_8_allKeys = []
    # keep track of which components have finished
    cues_instructionsComponents = [cues_instruction, key_resp_8]
    for thisComponent in cues_instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    cues_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "cues_instructions"-------
    while continueRoutine:
        # get current time
        t = cues_instructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=cues_instructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cues_instruction* updates
        if cues_instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cues_instruction.frameNStart = frameN  # exact frame index
            cues_instruction.tStart = t  # local t and not account for scr refresh
            cues_instruction.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cues_instruction, 'tStartRefresh')  # time at next scr refresh
            cues_instruction.setAutoDraw(True)
        
        # *key_resp_8* updates
        waitOnFlip = False
        if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_8.frameNStart = frameN  # exact frame index
            key_resp_8.tStart = t  # local t and not account for scr refresh
            key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_8.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_8_allKeys.extend(theseKeys)
            if len(_key_resp_8_allKeys):
                key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
                key_resp_8.rt = _key_resp_8_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in cues_instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "cues_instructions"-------
    for thisComponent in cues_instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Group.addData('cues_instruction.started', cues_instruction.tStartRefresh)
    Group.addData('cues_instruction.stopped', cues_instruction.tStopRefresh)
    # the Routine "cues_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank_screen"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank_screenComponents = [blank]
    for thisComponent in blank_screenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank_screen"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank_screenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank_screenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank_screenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank_screen"-------
    for thisComponent in blank_screenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Group.addData('blank.started', blank.tStartRefresh)
    Group.addData('blank.stopped', blank.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    loop_cues = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(cueFileIm),
        seed=None, name='loop_cues')
    thisExp.addLoop(loop_cues)  # add the loop to the experiment
    thisLoop_cue = loop_cues.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_cue.rgb)
    if thisLoop_cue != None:
        for paramName in thisLoop_cue:
            exec('{} = thisLoop_cue[paramName]'.format(paramName))
    
    for thisLoop_cue in loop_cues:
        currentLoop = loop_cues
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_cue.rgb)
        if thisLoop_cue != None:
            for paramName in thisLoop_cue:
                exec('{} = thisLoop_cue[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "cues"-------
        continueRoutine = True
        routineTimer.add(2.500000)
        # update component parameters for each repeat
        image_4.setImage(cues)
        # keep track of which components have finished
        cuesComponents = [image_4, text_12]
        for thisComponent in cuesComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        cuesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "cues"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = cuesClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=cuesClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_4* updates
            if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_4.frameNStart = frameN  # exact frame index
                image_4.tStart = t  # local t and not account for scr refresh
                image_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
                image_4.setAutoDraw(True)
            if image_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_4.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    image_4.tStop = t  # not accounting for scr refresh
                    image_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_4, 'tStopRefresh')  # time at next scr refresh
                    image_4.setAutoDraw(False)
            
            # *text_12* updates
            if text_12.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                text_12.frameNStart = frameN  # exact frame index
                text_12.tStart = t  # local t and not account for scr refresh
                text_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
                text_12.setAutoDraw(True)
            if text_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_12.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_12.tStop = t  # not accounting for scr refresh
                    text_12.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_12, 'tStopRefresh')  # time at next scr refresh
                    text_12.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cuesComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "cues"-------
        for thisComponent in cuesComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        loop_cues.addData('image_4.started', image_4.tStartRefresh)
        loop_cues.addData('image_4.stopped', image_4.tStopRefresh)
        loop_cues.addData('text_12.started', text_12.tStartRefresh)
        loop_cues.addData('text_12.stopped', text_12.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'loop_cues'
    
    
    # ------Prepare to start Routine "cue_instructions2"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_13.keys = []
    key_resp_13.rt = []
    _key_resp_13_allKeys = []
    # keep track of which components have finished
    cue_instructions2Components = [text_13, key_resp_13]
    for thisComponent in cue_instructions2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    cue_instructions2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "cue_instructions2"-------
    while continueRoutine:
        # get current time
        t = cue_instructions2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=cue_instructions2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_13* updates
        if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_13.frameNStart = frameN  # exact frame index
            text_13.tStart = t  # local t and not account for scr refresh
            text_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
            text_13.setAutoDraw(True)
        
        # *key_resp_13* updates
        waitOnFlip = False
        if key_resp_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_13.frameNStart = frameN  # exact frame index
            key_resp_13.tStart = t  # local t and not account for scr refresh
            key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
            key_resp_13.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_13.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_13.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_13_allKeys.extend(theseKeys)
            if len(_key_resp_13_allKeys):
                key_resp_13.keys = _key_resp_13_allKeys[-1].name  # just the last key pressed
                key_resp_13.rt = _key_resp_13_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in cue_instructions2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "cue_instructions2"-------
    for thisComponent in cue_instructions2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Group.addData('text_13.started', text_13.tStartRefresh)
    Group.addData('text_13.stopped', text_13.tStopRefresh)
    # the Routine "cue_instructions2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank_screen"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank_screenComponents = [blank]
    for thisComponent in blank_screenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank_screen"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank_screenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank_screenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank_screenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank_screen"-------
    for thisComponent in blank_screenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Group.addData('blank.started', blank.tStartRefresh)
    Group.addData('blank.stopped', blank.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    loop_cues2 = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(cueFileIm),
        seed=None, name='loop_cues2')
    thisExp.addLoop(loop_cues2)  # add the loop to the experiment
    thisLoop_cues2 = loop_cues2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_cues2.rgb)
    if thisLoop_cues2 != None:
        for paramName in thisLoop_cues2:
            exec('{} = thisLoop_cues2[paramName]'.format(paramName))
    
    for thisLoop_cues2 in loop_cues2:
        currentLoop = loop_cues2
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_cues2.rgb)
        if thisLoop_cues2 != None:
            for paramName in thisLoop_cues2:
                exec('{} = thisLoop_cues2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "cues"-------
        continueRoutine = True
        routineTimer.add(2.500000)
        # update component parameters for each repeat
        image_4.setImage(cues)
        # keep track of which components have finished
        cuesComponents = [image_4, text_12]
        for thisComponent in cuesComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        cuesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "cues"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = cuesClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=cuesClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_4* updates
            if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_4.frameNStart = frameN  # exact frame index
                image_4.tStart = t  # local t and not account for scr refresh
                image_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
                image_4.setAutoDraw(True)
            if image_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_4.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    image_4.tStop = t  # not accounting for scr refresh
                    image_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_4, 'tStopRefresh')  # time at next scr refresh
                    image_4.setAutoDraw(False)
            
            # *text_12* updates
            if text_12.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                text_12.frameNStart = frameN  # exact frame index
                text_12.tStart = t  # local t and not account for scr refresh
                text_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
                text_12.setAutoDraw(True)
            if text_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_12.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_12.tStop = t  # not accounting for scr refresh
                    text_12.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_12, 'tStopRefresh')  # time at next scr refresh
                    text_12.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cuesComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "cues"-------
        for thisComponent in cuesComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        loop_cues2.addData('image_4.started', image_4.tStartRefresh)
        loop_cues2.addData('image_4.stopped', image_4.tStopRefresh)
        loop_cues2.addData('text_12.started', text_12.tStartRefresh)
        loop_cues2.addData('text_12.stopped', text_12.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'loop_cues2'
    
    
    # ------Prepare to start Routine "thank_you"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    thank_youComponents = [text_14]
    for thisComponent in thank_youComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    thank_youClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "thank_you"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = thank_youClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=thank_youClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_14* updates
        if text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_14.frameNStart = frameN  # exact frame index
            text_14.tStart = t  # local t and not account for scr refresh
            text_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
            text_14.setAutoDraw(True)
        if text_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_14.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_14.tStop = t  # not accounting for scr refresh
                text_14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_14, 'tStopRefresh')  # time at next scr refresh
                text_14.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in thank_youComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "thank_you"-------
    for thisComponent in thank_youComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Group.addData('text_14.started', text_14.tStartRefresh)
    Group.addData('text_14.stopped', text_14.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    instruction_wordfirst = data.TrialHandler(nReps=instructionwordfirst, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='instruction_wordfirst')
    thisExp.addLoop(instruction_wordfirst)  # add the loop to the experiment
    thisInstruction_wordfirst = instruction_wordfirst.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInstruction_wordfirst.rgb)
    if thisInstruction_wordfirst != None:
        for paramName in thisInstruction_wordfirst:
            exec('{} = thisInstruction_wordfirst[paramName]'.format(paramName))
    
    for thisInstruction_wordfirst in instruction_wordfirst:
        currentLoop = instruction_wordfirst
        # abbreviate parameter names if possible (e.g. rgb = thisInstruction_wordfirst.rgb)
        if thisInstruction_wordfirst != None:
            for paramName in thisInstruction_wordfirst:
                exec('{} = thisInstruction_wordfirst[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "task_instructions"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_14.keys = []
        key_resp_14.rt = []
        _key_resp_14_allKeys = []
        # keep track of which components have finished
        task_instructionsComponents = [text_15, key_resp_14]
        for thisComponent in task_instructionsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        task_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "task_instructions"-------
        while continueRoutine:
            # get current time
            t = task_instructionsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=task_instructionsClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_15* updates
            if text_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_15.frameNStart = frameN  # exact frame index
                text_15.tStart = t  # local t and not account for scr refresh
                text_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
                text_15.setAutoDraw(True)
            
            # *key_resp_14* updates
            waitOnFlip = False
            if key_resp_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_14.frameNStart = frameN  # exact frame index
                key_resp_14.tStart = t  # local t and not account for scr refresh
                key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
                key_resp_14.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_14.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_14.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_14_allKeys.extend(theseKeys)
                if len(_key_resp_14_allKeys):
                    key_resp_14.keys = _key_resp_14_allKeys[-1].name  # just the last key pressed
                    key_resp_14.rt = _key_resp_14_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in task_instructionsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "task_instructions"-------
        for thisComponent in task_instructionsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        instruction_wordfirst.addData('text_15.started', text_15.tStartRefresh)
        instruction_wordfirst.addData('text_15.stopped', text_15.tStopRefresh)
        # the Routine "task_instructions" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed instructionwordfirst repeats of 'instruction_wordfirst'
    
    
    # set up handler to look after randomisation of conditions etc
    instruction_image_first = data.TrialHandler(nReps=instructionimagefirst, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='instruction_image_first')
    thisExp.addLoop(instruction_image_first)  # add the loop to the experiment
    thisInstruction_image_first = instruction_image_first.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInstruction_image_first.rgb)
    if thisInstruction_image_first != None:
        for paramName in thisInstruction_image_first:
            exec('{} = thisInstruction_image_first[paramName]'.format(paramName))
    
    for thisInstruction_image_first in instruction_image_first:
        currentLoop = instruction_image_first
        # abbreviate parameter names if possible (e.g. rgb = thisInstruction_image_first.rgb)
        if thisInstruction_image_first != None:
            for paramName in thisInstruction_image_first:
                exec('{} = thisInstruction_image_first[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "task_instruction_new"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_31.keys = []
        key_resp_31.rt = []
        _key_resp_31_allKeys = []
        # keep track of which components have finished
        task_instruction_newComponents = [text_45, key_resp_31]
        for thisComponent in task_instruction_newComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        task_instruction_newClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "task_instruction_new"-------
        while continueRoutine:
            # get current time
            t = task_instruction_newClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=task_instruction_newClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_45* updates
            if text_45.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_45.frameNStart = frameN  # exact frame index
                text_45.tStart = t  # local t and not account for scr refresh
                text_45.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_45, 'tStartRefresh')  # time at next scr refresh
                text_45.setAutoDraw(True)
            
            # *key_resp_31* updates
            waitOnFlip = False
            if key_resp_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_31.frameNStart = frameN  # exact frame index
                key_resp_31.tStart = t  # local t and not account for scr refresh
                key_resp_31.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_31, 'tStartRefresh')  # time at next scr refresh
                key_resp_31.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_31.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_31.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_31.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_31.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_31_allKeys.extend(theseKeys)
                if len(_key_resp_31_allKeys):
                    key_resp_31.keys = _key_resp_31_allKeys[-1].name  # just the last key pressed
                    key_resp_31.rt = _key_resp_31_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in task_instruction_newComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "task_instruction_new"-------
        for thisComponent in task_instruction_newComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        instruction_image_first.addData('text_45.started', text_45.tStartRefresh)
        instruction_image_first.addData('text_45.stopped', text_45.tStopRefresh)
        # the Routine "task_instruction_new" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed instructionimagefirst repeats of 'instruction_image_first'
    
    
    # ------Prepare to start Routine "PM_instruction"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_15.keys = []
    key_resp_15.rt = []
    _key_resp_15_allKeys = []
    # keep track of which components have finished
    PM_instructionComponents = [text_16, key_resp_15]
    for thisComponent in PM_instructionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PM_instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "PM_instruction"-------
    while continueRoutine:
        # get current time
        t = PM_instructionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PM_instructionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_16* updates
        if text_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_16.frameNStart = frameN  # exact frame index
            text_16.tStart = t  # local t and not account for scr refresh
            text_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
            text_16.setAutoDraw(True)
        
        # *key_resp_15* updates
        waitOnFlip = False
        if key_resp_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_15.frameNStart = frameN  # exact frame index
            key_resp_15.tStart = t  # local t and not account for scr refresh
            key_resp_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_15, 'tStartRefresh')  # time at next scr refresh
            key_resp_15.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_15.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_15.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_15.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_15_allKeys.extend(theseKeys)
            if len(_key_resp_15_allKeys):
                key_resp_15.keys = _key_resp_15_allKeys[-1].name  # just the last key pressed
                key_resp_15.rt = _key_resp_15_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PM_instructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PM_instruction"-------
    for thisComponent in PM_instructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Group.addData('text_16.started', text_16.tStartRefresh)
    Group.addData('text_16.stopped', text_16.tStopRefresh)
    # the Routine "PM_instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "questionnaires"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_16.keys = []
    key_resp_16.rt = []
    _key_resp_16_allKeys = []
    # keep track of which components have finished
    questionnairesComponents = [text_17, key_resp_16]
    for thisComponent in questionnairesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    questionnairesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "questionnaires"-------
    while continueRoutine:
        # get current time
        t = questionnairesClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=questionnairesClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_17* updates
        if text_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_17.frameNStart = frameN  # exact frame index
            text_17.tStart = t  # local t and not account for scr refresh
            text_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
            text_17.setAutoDraw(True)
        
        # *key_resp_16* updates
        waitOnFlip = False
        if key_resp_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_16.frameNStart = frameN  # exact frame index
            key_resp_16.tStart = t  # local t and not account for scr refresh
            key_resp_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_16, 'tStartRefresh')  # time at next scr refresh
            key_resp_16.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_16.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_16.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_16.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_16.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_16_allKeys.extend(theseKeys)
            if len(_key_resp_16_allKeys):
                key_resp_16.keys = _key_resp_16_allKeys[-1].name  # just the last key pressed
                key_resp_16.rt = _key_resp_16_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in questionnairesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "questionnaires"-------
    for thisComponent in questionnairesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Group.addData('text_17.started', text_17.tStartRefresh)
    Group.addData('text_17.stopped', text_17.tStopRefresh)
    # the Routine "questionnaires" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "countdown"-------
    continueRoutine = True
    routineTimer.add(120.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    countdownComponents = [text_46]
    for thisComponent in countdownComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    countdownClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "countdown"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = countdownClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=countdownClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_46* updates
        if text_46.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_46.frameNStart = frameN  # exact frame index
            text_46.tStart = t  # local t and not account for scr refresh
            text_46.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_46, 'tStartRefresh')  # time at next scr refresh
            text_46.setAutoDraw(True)
        if text_46.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_46.tStartRefresh + 120-frameTolerance:
                # keep track of stop time/frame for later
                text_46.tStop = t  # not accounting for scr refresh
                text_46.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_46, 'tStopRefresh')  # time at next scr refresh
                text_46.setAutoDraw(False)
        if text_46.status == STARTED:  # only update if drawing
            text_46.setText(str(round(routineTimer.getTime(),1)) , log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in countdownComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "countdown"-------
    for thisComponent in countdownComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Group.addData('text_46.started', text_46.tStartRefresh)
    Group.addData('text_46.stopped', text_46.tStopRefresh)
    
    # ------Prepare to start Routine "PMintro"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_17.keys = []
    key_resp_17.rt = []
    _key_resp_17_allKeys = []
    sound_1.setSound('A', secs=1.0, hamming=True)
    sound_1.setVolume(1, log=False)
    # keep track of which components have finished
    PMintroComponents = [text_18, key_resp_17, sound_1]
    for thisComponent in PMintroComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PMintroClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "PMintro"-------
    while continueRoutine:
        # get current time
        t = PMintroClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PMintroClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_18* updates
        if text_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_18.frameNStart = frameN  # exact frame index
            text_18.tStart = t  # local t and not account for scr refresh
            text_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_18, 'tStartRefresh')  # time at next scr refresh
            text_18.setAutoDraw(True)
        
        # *key_resp_17* updates
        waitOnFlip = False
        if key_resp_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_17.frameNStart = frameN  # exact frame index
            key_resp_17.tStart = t  # local t and not account for scr refresh
            key_resp_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_17, 'tStartRefresh')  # time at next scr refresh
            key_resp_17.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_17.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_17.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_17.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_17.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_17_allKeys.extend(theseKeys)
            if len(_key_resp_17_allKeys):
                key_resp_17.keys = _key_resp_17_allKeys[-1].name  # just the last key pressed
                key_resp_17.rt = _key_resp_17_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # start/stop sound_1
        if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            sound_1.play(when=win)  # sync with win flip
        if sound_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
                sound_1.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PMintroComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PMintro"-------
    for thisComponent in PMintroComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Group.addData('text_18.started', text_18.tStartRefresh)
    Group.addData('text_18.stopped', text_18.tStopRefresh)
    sound_1.stop()  # ensure sound has stopped at end of routine
    Group.addData('sound_1.started', sound_1.tStartRefresh)
    Group.addData('sound_1.stopped', sound_1.tStopRefresh)
    # the Routine "PMintro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank_screen"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank_screenComponents = [blank]
    for thisComponent in blank_screenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank_screen"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank_screenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank_screenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank_screenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank_screen"-------
    for thisComponent in blank_screenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Group.addData('blank.started', blank.tStartRefresh)
    Group.addData('blank.stopped', blank.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    PM_task_loop = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(condFileIm),
        seed=None, name='PM_task_loop')
    thisExp.addLoop(PM_task_loop)  # add the loop to the experiment
    thisPM_task_loop = PM_task_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPM_task_loop.rgb)
    if thisPM_task_loop != None:
        for paramName in thisPM_task_loop:
            exec('{} = thisPM_task_loop[paramName]'.format(paramName))
    
    for thisPM_task_loop in PM_task_loop:
        currentLoop = PM_task_loop
        # abbreviate parameter names if possible (e.g. rgb = thisPM_task_loop.rgb)
        if thisPM_task_loop != None:
            for paramName in thisPM_task_loop:
                exec('{} = thisPM_task_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "PM_task"-------
        continueRoutine = True
        routineTimer.add(1.700000)
        # update component parameters for each repeat
        image_5.setImage(stimulus)
        key_resp_PM.keys = []
        key_resp_PM.rt = []
        _key_resp_PM_allKeys = []
        key_resp_PM.lenient = []
        key_resp_PM.RTfirst = []
        # keep track of which components have finished
        PM_taskComponents = [image_5, text_20, key_resp_PM]
        for thisComponent in PM_taskComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PM_taskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "PM_task"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = PM_taskClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PM_taskClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_5* updates
            if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_5.frameNStart = frameN  # exact frame index
                image_5.tStart = t  # local t and not account for scr refresh
                image_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
                image_5.setAutoDraw(True)
            if image_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_5.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_5.tStop = t  # not accounting for scr refresh
                    image_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_5, 'tStopRefresh')  # time at next scr refresh
                    image_5.setAutoDraw(False)
            
            # *text_20* updates
            if text_20.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                text_20.frameNStart = frameN  # exact frame index
                text_20.tStart = t  # local t and not account for scr refresh
                text_20.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_20, 'tStartRefresh')  # time at next scr refresh
                text_20.setAutoDraw(True)
            if text_20.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_20.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_20.tStop = t  # not accounting for scr refresh
                    text_20.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_20, 'tStopRefresh')  # time at next scr refresh
                    text_20.setAutoDraw(False)
            
            # *key_resp_PM* updates
            waitOnFlip = False
            if key_resp_PM.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_PM.frameNStart = frameN  # exact frame index
                key_resp_PM.tStart = t  # local t and not account for scr refresh
                key_resp_PM.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_PM, 'tStartRefresh')  # time at next scr refresh
                key_resp_PM.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_PM.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_PM.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_PM.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_PM.tStartRefresh + 1.7-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_PM.tStop = t  # not accounting for scr refresh
                    key_resp_PM.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_PM, 'tStopRefresh')  # time at next scr refresh
                    key_resp_PM.status = FINISHED
            if key_resp_PM.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_PM.getKeys(keyList=['l', 'd', 'h'], waitRelease=False)
                _key_resp_PM_allKeys.extend(theseKeys)
                if len(_key_resp_PM_allKeys):
                    key_resp_PM.keys = [key.name for key in _key_resp_PM_allKeys]  # storing all keys
                    key_resp_PM.rt = [key.rt for key in _key_resp_PM_allKeys]
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PM_taskComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "PM_task"-------
        for thisComponent in PM_taskComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        PM_task_loop.addData('image_5.started', image_5.tStartRefresh)
        PM_task_loop.addData('image_5.stopped', image_5.tStopRefresh)
        PM_task_loop.addData('text_20.started', text_20.tStartRefresh)
        PM_task_loop.addData('text_20.stopped', text_20.tStopRefresh)
        # check responses
        if key_resp_PM.keys in ['', [], None]:  # No response was made
            key_resp_PM.keys = None
        PM_task_loop.addData('key_resp_PM.keys',key_resp_PM.keys)
        if key_resp_PM.keys != None:  # we had a response
            PM_task_loop.addData('key_resp_PM.rt', key_resp_PM.rt)
        PM_task_loop.addData('key_resp_PM.started', key_resp_PM.tStartRefresh)
        PM_task_loop.addData('key_resp_PM.stopped', key_resp_PM.tStopRefresh)
        if key_resp_PM.keys in ['', [], None]:  # No response was made
             if str(CORRanswer)=='h':
                key_resp_PM.lenient = 0
                key_resp_PM.keys=None
                PM_task_loop.addData('key_resp_PM.lenient', key_resp_PM.lenient)
                PM_task_loop.addData('key_resp_PM.keys',key_resp_PM.keys)
             if str(CORRanswer)!='h':
                key_resp_PM.keys=None
                key_resp_PM.corr = 0
                PM_task_loop.addData('key_resp_PM.keys',key_resp_PM.keys)
                PM_task_loop.addData('key_resp_PM.corr', key_resp_PM.corr)
        
        if key_resp_PM.keys != None:  # we had a response
                PM_task_loop.addData('key_resp_PM.rtFirst', key_resp_PM.rt[0])
                if (str(key_resp_PM.keys)[2] == str(CORRanswer)) or (str(key_resp_PM.keys)[2] == CORRanswer):
                        key_resp_PM.corr = 1
                        
                else:
                        key_resp_PM.corr = 0
               # PM_task_loop.addData('key_resp_PM.corr', key_resp_PM.corr)
               # PM_task_loop.addData('key_resp_PM.rt', key_resp_PM.rt)
               # PM_task_loop.addData('key_resp_PM.rtFirst', key_resp_PM.rt[0])
                #PM_task_loop.addData('key_resp_PM.rtFirst', key_resp_PM.rt[0])
        #
        
                if str(CORRanswer)=='h' and ('h' in key_resp_PM.keys):
                        key_resp_PM.lenient = 1
                elif str(CORRanswer)=='h' and ('h' not in key_resp_PM.keys):
                        key_resp_PM.lenient = 0
                else:
                        key_resp_PM.lenient = []
        
        
        # check responses
        # check responses
        
        # store data for trials_2 (TrialHandler)
        PM_task_loop.addData('key_resp_PM.keys',key_resp_PM.keys)
        PM_task_loop.addData('key_resp_PM.corr', key_resp_PM.corr)
        PM_task_loop.addData('key_resp_PM.rt', key_resp_PM.rt)
        #PM_task_loop.addData('key_resp_PM.rtFirst', key_resp_PM.rt[0])
        PM_task_loop.addData('key_resp_PM.lenient', key_resp_PM.lenient)
        
        
        #meanRt = trials_2.data['key_resp_6.rt'].mean()
        #msg = "You got %d trials correct" %nCorr
        
        
        
        
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'PM_task_loop'
    
    
    # ------Prepare to start Routine "end_block1"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    end_block1Components = [text_21]
    for thisComponent in end_block1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    end_block1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "end_block1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = end_block1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=end_block1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_21* updates
        if text_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_21.frameNStart = frameN  # exact frame index
            text_21.tStart = t  # local t and not account for scr refresh
            text_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_21, 'tStartRefresh')  # time at next scr refresh
            text_21.setAutoDraw(True)
        if text_21.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_21.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_21.tStop = t  # not accounting for scr refresh
                text_21.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_21, 'tStopRefresh')  # time at next scr refresh
                text_21.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_block1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "end_block1"-------
    for thisComponent in end_block1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Group.addData('text_21.started', text_21.tStartRefresh)
    Group.addData('text_21.stopped', text_21.tStopRefresh)
    
    # ------Prepare to start Routine "recog_task_instr"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_20.keys = []
    key_resp_20.rt = []
    _key_resp_20_allKeys = []
    # keep track of which components have finished
    recog_task_instrComponents = [text_22, key_resp_20]
    for thisComponent in recog_task_instrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    recog_task_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "recog_task_instr"-------
    while continueRoutine:
        # get current time
        t = recog_task_instrClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=recog_task_instrClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_22* updates
        if text_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_22.frameNStart = frameN  # exact frame index
            text_22.tStart = t  # local t and not account for scr refresh
            text_22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_22, 'tStartRefresh')  # time at next scr refresh
            text_22.setAutoDraw(True)
        
        # *key_resp_20* updates
        waitOnFlip = False
        if key_resp_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_20.frameNStart = frameN  # exact frame index
            key_resp_20.tStart = t  # local t and not account for scr refresh
            key_resp_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_20, 'tStartRefresh')  # time at next scr refresh
            key_resp_20.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_20.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_20.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_20.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_20.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_20_allKeys.extend(theseKeys)
            if len(_key_resp_20_allKeys):
                key_resp_20.keys = _key_resp_20_allKeys[-1].name  # just the last key pressed
                key_resp_20.rt = _key_resp_20_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in recog_task_instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "recog_task_instr"-------
    for thisComponent in recog_task_instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Group.addData('text_22.started', text_22.tStartRefresh)
    Group.addData('text_22.stopped', text_22.tStopRefresh)
    # the Routine "recog_task_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank_screen"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank_screenComponents = [blank]
    for thisComponent in blank_screenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank_screen"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank_screenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank_screenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank_screenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank_screen"-------
    for thisComponent in blank_screenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Group.addData('blank.started', blank.tStartRefresh)
    Group.addData('blank.stopped', blank.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    recog_task_loop = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(recogFileIm),
        seed=None, name='recog_task_loop')
    thisExp.addLoop(recog_task_loop)  # add the loop to the experiment
    thisRecog_task_loop = recog_task_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRecog_task_loop.rgb)
    if thisRecog_task_loop != None:
        for paramName in thisRecog_task_loop:
            exec('{} = thisRecog_task_loop[paramName]'.format(paramName))
    
    for thisRecog_task_loop in recog_task_loop:
        currentLoop = recog_task_loop
        # abbreviate parameter names if possible (e.g. rgb = thisRecog_task_loop.rgb)
        if thisRecog_task_loop != None:
            for paramName in thisRecog_task_loop:
                exec('{} = thisRecog_task_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "recog_task"-------
        continueRoutine = True
        # update component parameters for each repeat
        image_6.setImage(stimulus)
        key_resp_18.keys = []
        key_resp_18.rt = []
        _key_resp_18_allKeys = []
        # keep track of which components have finished
        recog_taskComponents = [image_6, key_resp_18]
        for thisComponent in recog_taskComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        recog_taskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "recog_task"-------
        while continueRoutine:
            # get current time
            t = recog_taskClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=recog_taskClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_6* updates
            if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_6.frameNStart = frameN  # exact frame index
                image_6.tStart = t  # local t and not account for scr refresh
                image_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
                image_6.setAutoDraw(True)
            
            # *key_resp_18* updates
            waitOnFlip = False
            if key_resp_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_18.frameNStart = frameN  # exact frame index
                key_resp_18.tStart = t  # local t and not account for scr refresh
                key_resp_18.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_18, 'tStartRefresh')  # time at next scr refresh
                key_resp_18.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_18.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_18.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_18.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_18.getKeys(keyList=['l', 'd'], waitRelease=False)
                _key_resp_18_allKeys.extend(theseKeys)
                if len(_key_resp_18_allKeys):
                    key_resp_18.keys = _key_resp_18_allKeys[0].name  # just the first key pressed
                    key_resp_18.rt = _key_resp_18_allKeys[0].rt
                    # was this correct?
                    if (key_resp_18.keys == str(corrAnsw)) or (key_resp_18.keys == corrAnsw):
                        key_resp_18.corr = 1
                    else:
                        key_resp_18.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in recog_taskComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "recog_task"-------
        for thisComponent in recog_taskComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        recog_task_loop.addData('image_6.started', image_6.tStartRefresh)
        recog_task_loop.addData('image_6.stopped', image_6.tStopRefresh)
        # check responses
        if key_resp_18.keys in ['', [], None]:  # No response was made
            key_resp_18.keys = None
            # was no response the correct answer?!
            if str(corrAnsw).lower() == 'none':
               key_resp_18.corr = 1;  # correct non-response
            else:
               key_resp_18.corr = 0;  # failed to respond (incorrectly)
        # store data for recog_task_loop (TrialHandler)
        recog_task_loop.addData('key_resp_18.keys',key_resp_18.keys)
        recog_task_loop.addData('key_resp_18.corr', key_resp_18.corr)
        if key_resp_18.keys != None:  # we had a response
            recog_task_loop.addData('key_resp_18.rt', key_resp_18.rt)
        recog_task_loop.addData('key_resp_18.started', key_resp_18.tStartRefresh)
        recog_task_loop.addData('key_resp_18.stopped', key_resp_18.tStopRefresh)
        # the Routine "recog_task" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'recog_task_loop'
    
    
    # ------Prepare to start Routine "loopcounter"-------
    continueRoutine = True
    # update component parameters for each repeat
    #we can set instructionwordfirst =1 so participants will see the message
    #saying they have to continue to do what they did before. 
    instructionwordfirst = 1
    instructionimagefirst = 0
    
    # keep track of which components have finished
    loopcounterComponents = []
    for thisComponent in loopcounterComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    loopcounterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "loopcounter"-------
    while continueRoutine:
        # get current time
        t = loopcounterClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=loopcounterClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in loopcounterComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "loopcounter"-------
    for thisComponent in loopcounterComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "loopcounter" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'Group'


# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=endFirstHalf, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "end_first_half"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    end_first_halfComponents = [text_24]
    for thisComponent in end_first_halfComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    end_first_halfClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "end_first_half"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = end_first_halfClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=end_first_halfClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_24* updates
        if text_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_24.frameNStart = frameN  # exact frame index
            text_24.tStart = t  # local t and not account for scr refresh
            text_24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_24, 'tStartRefresh')  # time at next scr refresh
            text_24.setAutoDraw(True)
        if text_24.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_24.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_24.tStop = t  # not accounting for scr refresh
                text_24.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_24, 'tStopRefresh')  # time at next scr refresh
                text_24.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_first_halfComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "end_first_half"-------
    for thisComponent in end_first_halfComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('text_24.started', text_24.tStartRefresh)
    trials_3.addData('text_24.stopped', text_24.tStopRefresh)
    thisExp.nextEntry()
    
# completed endFirstHalf repeats of 'trials_3'


# set up handler to look after randomisation of conditions etc
finalLoop = data.TrialHandler(nReps=finalRatings, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='finalLoop')
thisExp.addLoop(finalLoop)  # add the loop to the experiment
thisFinalLoop = finalLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFinalLoop.rgb)
if thisFinalLoop != None:
    for paramName in thisFinalLoop:
        exec('{} = thisFinalLoop[paramName]'.format(paramName))

for thisFinalLoop in finalLoop:
    currentLoop = finalLoop
    # abbreviate parameter names if possible (e.g. rgb = thisFinalLoop.rgb)
    if thisFinalLoop != None:
        for paramName in thisFinalLoop:
            exec('{} = thisFinalLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "InstructionCueRatings"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_30.keys = []
    key_resp_30.rt = []
    _key_resp_30_allKeys = []
    # keep track of which components have finished
    InstructionCueRatingsComponents = [text_44, key_resp_30]
    for thisComponent in InstructionCueRatingsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    InstructionCueRatingsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "InstructionCueRatings"-------
    while continueRoutine:
        # get current time
        t = InstructionCueRatingsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=InstructionCueRatingsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_44* updates
        if text_44.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_44.frameNStart = frameN  # exact frame index
            text_44.tStart = t  # local t and not account for scr refresh
            text_44.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_44, 'tStartRefresh')  # time at next scr refresh
            text_44.setAutoDraw(True)
        
        # *key_resp_30* updates
        waitOnFlip = False
        if key_resp_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_30.frameNStart = frameN  # exact frame index
            key_resp_30.tStart = t  # local t and not account for scr refresh
            key_resp_30.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_30, 'tStartRefresh')  # time at next scr refresh
            key_resp_30.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_30.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_30.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_30.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_30.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_30_allKeys.extend(theseKeys)
            if len(_key_resp_30_allKeys):
                key_resp_30.keys = _key_resp_30_allKeys[-1].name  # just the last key pressed
                key_resp_30.rt = _key_resp_30_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionCueRatingsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "InstructionCueRatings"-------
    for thisComponent in InstructionCueRatingsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    finalLoop.addData('text_44.started', text_44.tStartRefresh)
    finalLoop.addData('text_44.stopped', text_44.tStopRefresh)
    # the Routine "InstructionCueRatings" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    SAMratings = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('CueRatings.xlsx'),
        seed=None, name='SAMratings')
    thisExp.addLoop(SAMratings)  # add the loop to the experiment
    thisSAMrating = SAMratings.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSAMrating.rgb)
    if thisSAMrating != None:
        for paramName in thisSAMrating:
            exec('{} = thisSAMrating[paramName]'.format(paramName))
    
    for thisSAMrating in SAMratings:
        currentLoop = SAMratings
        # abbreviate parameter names if possible (e.g. rgb = thisSAMrating.rgb)
        if thisSAMrating != None:
            for paramName in thisSAMrating:
                exec('{} = thisSAMrating[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Valence"-------
        continueRoutine = True
        # update component parameters for each repeat
        text_47.setText(words)
        image_1.setImage(images)
        slider_valence.reset()
        key_resp_28.keys = []
        key_resp_28.rt = []
        _key_resp_28_allKeys = []
        # keep track of which components have finished
        ValenceComponents = [text_47, image_1, ValenceImg, slider_valence, text_40, key_resp_28, text_41]
        for thisComponent in ValenceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ValenceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Valence"-------
        while continueRoutine:
            # get current time
            t = ValenceClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ValenceClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_47* updates
            if text_47.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_47.frameNStart = frameN  # exact frame index
                text_47.tStart = t  # local t and not account for scr refresh
                text_47.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_47, 'tStartRefresh')  # time at next scr refresh
                text_47.setAutoDraw(True)
            
            # *image_1* updates
            if image_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_1.frameNStart = frameN  # exact frame index
                image_1.tStart = t  # local t and not account for scr refresh
                image_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_1, 'tStartRefresh')  # time at next scr refresh
                image_1.setAutoDraw(True)
            
            # *ValenceImg* updates
            if ValenceImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ValenceImg.frameNStart = frameN  # exact frame index
                ValenceImg.tStart = t  # local t and not account for scr refresh
                ValenceImg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ValenceImg, 'tStartRefresh')  # time at next scr refresh
                ValenceImg.setAutoDraw(True)
            
            # *slider_valence* updates
            if slider_valence.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_valence.frameNStart = frameN  # exact frame index
                slider_valence.tStart = t  # local t and not account for scr refresh
                slider_valence.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_valence, 'tStartRefresh')  # time at next scr refresh
                slider_valence.setAutoDraw(True)
            
            # *text_40* updates
            if text_40.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_40.frameNStart = frameN  # exact frame index
                text_40.tStart = t  # local t and not account for scr refresh
                text_40.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_40, 'tStartRefresh')  # time at next scr refresh
                text_40.setAutoDraw(True)
            
            # *key_resp_28* updates
            waitOnFlip = False
            if key_resp_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_28.frameNStart = frameN  # exact frame index
                key_resp_28.tStart = t  # local t and not account for scr refresh
                key_resp_28.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_28, 'tStartRefresh')  # time at next scr refresh
                key_resp_28.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_28.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_28.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_28.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_28.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_28_allKeys.extend(theseKeys)
                if len(_key_resp_28_allKeys):
                    key_resp_28.keys = _key_resp_28_allKeys[-1].name  # just the last key pressed
                    key_resp_28.rt = _key_resp_28_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_41* updates
            if text_41.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_41.frameNStart = frameN  # exact frame index
                text_41.tStart = t  # local t and not account for scr refresh
                text_41.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_41, 'tStartRefresh')  # time at next scr refresh
                text_41.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ValenceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Valence"-------
        for thisComponent in ValenceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        SAMratings.addData('text_47.started', text_47.tStartRefresh)
        SAMratings.addData('text_47.stopped', text_47.tStopRefresh)
        SAMratings.addData('image_1.started', image_1.tStartRefresh)
        SAMratings.addData('image_1.stopped', image_1.tStopRefresh)
        SAMratings.addData('ValenceImg.started', ValenceImg.tStartRefresh)
        SAMratings.addData('ValenceImg.stopped', ValenceImg.tStopRefresh)
        SAMratings.addData('slider_valence.response', slider_valence.getRating())
        SAMratings.addData('slider_valence.rt', slider_valence.getRT())
        SAMratings.addData('slider_valence.started', slider_valence.tStartRefresh)
        SAMratings.addData('slider_valence.stopped', slider_valence.tStopRefresh)
        SAMratings.addData('text_40.started', text_40.tStartRefresh)
        SAMratings.addData('text_40.stopped', text_40.tStopRefresh)
        SAMratings.addData('text_41.started', text_41.tStartRefresh)
        SAMratings.addData('text_41.stopped', text_41.tStopRefresh)
        # the Routine "Valence" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Arousal"-------
        continueRoutine = True
        # update component parameters for each repeat
        text_48.setText(words)
        image_2.setImage(images)
        slider_arousal.reset()
        key_resp_29.keys = []
        key_resp_29.rt = []
        _key_resp_29_allKeys = []
        # keep track of which components have finished
        ArousalComponents = [text_48, image_2, Arousalimage, slider_arousal, text_42, key_resp_29, text_43]
        for thisComponent in ArousalComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ArousalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Arousal"-------
        while continueRoutine:
            # get current time
            t = ArousalClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ArousalClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_48* updates
            if text_48.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_48.frameNStart = frameN  # exact frame index
                text_48.tStart = t  # local t and not account for scr refresh
                text_48.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_48, 'tStartRefresh')  # time at next scr refresh
                text_48.setAutoDraw(True)
            
            # *image_2* updates
            if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_2.frameNStart = frameN  # exact frame index
                image_2.tStart = t  # local t and not account for scr refresh
                image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                image_2.setAutoDraw(True)
            
            # *Arousalimage* updates
            if Arousalimage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Arousalimage.frameNStart = frameN  # exact frame index
                Arousalimage.tStart = t  # local t and not account for scr refresh
                Arousalimage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Arousalimage, 'tStartRefresh')  # time at next scr refresh
                Arousalimage.setAutoDraw(True)
            
            # *slider_arousal* updates
            if slider_arousal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_arousal.frameNStart = frameN  # exact frame index
                slider_arousal.tStart = t  # local t and not account for scr refresh
                slider_arousal.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_arousal, 'tStartRefresh')  # time at next scr refresh
                slider_arousal.setAutoDraw(True)
            
            # *text_42* updates
            if text_42.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_42.frameNStart = frameN  # exact frame index
                text_42.tStart = t  # local t and not account for scr refresh
                text_42.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_42, 'tStartRefresh')  # time at next scr refresh
                text_42.setAutoDraw(True)
            
            # *key_resp_29* updates
            waitOnFlip = False
            if key_resp_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_29.frameNStart = frameN  # exact frame index
                key_resp_29.tStart = t  # local t and not account for scr refresh
                key_resp_29.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_29, 'tStartRefresh')  # time at next scr refresh
                key_resp_29.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_29.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_29.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_29.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_29.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
                _key_resp_29_allKeys.extend(theseKeys)
                if len(_key_resp_29_allKeys):
                    key_resp_29.keys = _key_resp_29_allKeys[-1].name  # just the last key pressed
                    key_resp_29.rt = _key_resp_29_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_43* updates
            if text_43.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_43.frameNStart = frameN  # exact frame index
                text_43.tStart = t  # local t and not account for scr refresh
                text_43.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_43, 'tStartRefresh')  # time at next scr refresh
                text_43.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ArousalComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Arousal"-------
        for thisComponent in ArousalComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        SAMratings.addData('text_48.started', text_48.tStartRefresh)
        SAMratings.addData('text_48.stopped', text_48.tStopRefresh)
        SAMratings.addData('image_2.started', image_2.tStartRefresh)
        SAMratings.addData('image_2.stopped', image_2.tStopRefresh)
        SAMratings.addData('Arousalimage.started', Arousalimage.tStartRefresh)
        SAMratings.addData('Arousalimage.stopped', Arousalimage.tStopRefresh)
        SAMratings.addData('slider_arousal.response', slider_arousal.getRating())
        SAMratings.addData('slider_arousal.rt', slider_arousal.getRT())
        SAMratings.addData('slider_arousal.started', slider_arousal.tStartRefresh)
        SAMratings.addData('slider_arousal.stopped', slider_arousal.tStopRefresh)
        SAMratings.addData('text_42.started', text_42.tStartRefresh)
        SAMratings.addData('text_42.stopped', text_42.tStopRefresh)
        SAMratings.addData('text_43.started', text_43.tStartRefresh)
        SAMratings.addData('text_43.stopped', text_43.tStopRefresh)
        # the Routine "Arousal" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'SAMratings'
    
    
    # ------Prepare to start Routine "instruction_check"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_23.keys = []
    key_resp_23.rt = []
    _key_resp_23_allKeys = []
    # keep track of which components have finished
    instruction_checkComponents = [text_32, key_resp_23]
    for thisComponent in instruction_checkComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instruction_checkClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instruction_check"-------
    while continueRoutine:
        # get current time
        t = instruction_checkClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instruction_checkClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_32* updates
        if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_32.frameNStart = frameN  # exact frame index
            text_32.tStart = t  # local t and not account for scr refresh
            text_32.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
            text_32.setAutoDraw(True)
        
        # *key_resp_23* updates
        waitOnFlip = False
        if key_resp_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_23.frameNStart = frameN  # exact frame index
            key_resp_23.tStart = t  # local t and not account for scr refresh
            key_resp_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_23, 'tStartRefresh')  # time at next scr refresh
            key_resp_23.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_23.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_23.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_23.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_23.getKeys(keyList=['y', 'n', 'l', 'd', 'space', 'h'], waitRelease=False)
            _key_resp_23_allKeys.extend(theseKeys)
            if len(_key_resp_23_allKeys):
                key_resp_23.keys = _key_resp_23_allKeys[0].name  # just the first key pressed
                key_resp_23.rt = _key_resp_23_allKeys[0].rt
                # was this correct?
                if (key_resp_23.keys == str("'h'")) or (key_resp_23.keys == "'h'"):
                    key_resp_23.corr = 1
                else:
                    key_resp_23.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruction_checkComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instruction_check"-------
    for thisComponent in instruction_checkComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    finalLoop.addData('text_32.started', text_32.tStartRefresh)
    finalLoop.addData('text_32.stopped', text_32.tStopRefresh)
    # check responses
    if key_resp_23.keys in ['', [], None]:  # No response was made
        key_resp_23.keys = None
        # was no response the correct answer?!
        if str("'h'").lower() == 'none':
           key_resp_23.corr = 1;  # correct non-response
        else:
           key_resp_23.corr = 0;  # failed to respond (incorrectly)
    # store data for finalLoop (TrialHandler)
    finalLoop.addData('key_resp_23.keys',key_resp_23.keys)
    finalLoop.addData('key_resp_23.corr', key_resp_23.corr)
    if key_resp_23.keys != None:  # we had a response
        finalLoop.addData('key_resp_23.rt', key_resp_23.rt)
    finalLoop.addData('key_resp_23.started', key_resp_23.tStartRefresh)
    finalLoop.addData('key_resp_23.stopped', key_resp_23.tStopRefresh)
    # the Routine "instruction_check" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "endOfExpMessage"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_24.keys = []
    key_resp_24.rt = []
    _key_resp_24_allKeys = []
    # keep track of which components have finished
    endOfExpMessageComponents = [text_33, key_resp_24]
    for thisComponent in endOfExpMessageComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    endOfExpMessageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "endOfExpMessage"-------
    while continueRoutine:
        # get current time
        t = endOfExpMessageClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=endOfExpMessageClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_33* updates
        if text_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_33.frameNStart = frameN  # exact frame index
            text_33.tStart = t  # local t and not account for scr refresh
            text_33.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_33, 'tStartRefresh')  # time at next scr refresh
            text_33.setAutoDraw(True)
        
        # *key_resp_24* updates
        waitOnFlip = False
        if key_resp_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_24.frameNStart = frameN  # exact frame index
            key_resp_24.tStart = t  # local t and not account for scr refresh
            key_resp_24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_24, 'tStartRefresh')  # time at next scr refresh
            key_resp_24.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_24.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_24.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_24.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_24.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_24_allKeys.extend(theseKeys)
            if len(_key_resp_24_allKeys):
                key_resp_24.keys = _key_resp_24_allKeys[-1].name  # just the last key pressed
                key_resp_24.rt = _key_resp_24_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endOfExpMessageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "endOfExpMessage"-------
    for thisComponent in endOfExpMessageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    finalLoop.addData('text_33.started', text_33.tStartRefresh)
    finalLoop.addData('text_33.stopped', text_33.tStopRefresh)
    # the Routine "endOfExpMessage" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed finalRatings repeats of 'finalLoop'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
