#!/usr/bin/python

# Program Name: EQAlerter.py 
#               'The EverQuest Alerter'
# Original Author: Dr. Ronny Bull (A.K.A. Cubber on eqemulator.org)
# Python Version: 3.5
# Original Date: 11/12/2017
# Last Revision: 11/20/2017

# Purpose:  This program is intended to run on a Linux system running 'EverQuest' under 'Wine'.
#           When running the program will parse your EverQuest chat log file for key phrases
#           contained in the Config.py file and trigger alerts using the flite TTS engine.

# Dependencies: Python 3 & CMU Flite text to speech engine

# IMPORTANT: Verify that your 'eqclient.ini' file contains the following line: Log=TRUE
#            and that your game path is setup properly in Config.py.

#    This file is part of EQAlerter.

#    EQAlerter is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    EQAlerter is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with EQAlerter.  If not, see <http://www.gnu.org/licenses/>.

# libraries
import subprocess
import time
import sys
import os
import subprocess
import shlex
import yaml

from os import listdir
from os.path import isfile, join

# classes
from config import *
from dep_check import DepCheck
from character_list import CharacterList
from message_generator import MessageGenerator


with open("alerts.yaml", 'r') as stream:
    try:
        alerts = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

#### MAIN PROGRAM ####

# dependency checks
DepCheck.verifyOS()
DepCheck.verifyFlite()
DepCheck.verifyLogging()

# program banner 
# TODO: NEED FUNKY ASCII ART HERE 
print("\n\nStarting The EverQuest Alerter\n")
print("Press Ctrl+C to exit\n")

# get character info
ALLFILES = [u for u in listdir(EQHOME) if isfile(join(EQHOME, u))]
sub = "UI_"
UIFILES = [s for s in ALLFILES if sub in s]

# create linked list of characters and generate menu
CHARLIST = LinkedList()

count = 0
for i in UIFILES:
    count = count + 1
    tmp = i.split("_")
    CHARNAME = tmp[1]
    CHARSERVER = tmp[2].split(".")
    CHARSERVER = CHARSERVER[0]
    CHARLIST.add(CHARNAME, CHARSERVER)

iterator = iter(CHARLIST)
count = 0
for c in CHARLIST:
    print("%d: %s" % (count, next(iterator)))
    count = count + 1

# ask user to pick character to control from list
CHARNUM = input("\n\nEnter the number of the character's log file that you would like to monitor from the list: ")
CHARACTER = CHARLIST.getName(CHARNUM)
SERVER = CHARLIST.getServer(CHARNUM)

# generate logfile path
LOGPATH = "eqlog_%s_%s.txt" % (CHARACTER, SERVER) 
LOGFILE = EQHOME+LOGPATH
DepCheck.verifyLogFile(CHARACTER, LOGFILE)


def background_task(time, message, name='EQT'):
    command_line = 'urxvt -iconic -geometry 15x1 -bg red -fg white -title ' + name + ' -e python StopWatchTest.py ' + str(time) + ' "' + message + '" 1'
    print(command_line)
    command_args = shlex.split(command_line)
    subprocess.Popen(command_args, close_fds=True)

def gui_notify(message):
    notify_line='notify-send --urgency low --expire-time=1000 --icon='+EQHOME+'EverQuest.ico '
    command_line = notify_line + '"' + message + '"'
    os.system(command_line)

def audio_notify(message):
    notify_line='flite -voice slt -t '
    command_line = notify_line + '"' + message + '"'
    os.system(command_line)

def all_notify(message):
    gui_notify(message)
    audio_notify(message)



# begin parsing log file for triggers and perform actions
try:

    # open log file
    with open(LOGFILE, 'r+') as f:
        # move to the end of the file
        f.seek(0,2)

        # loop over each new line of the file
        # act on keywords from chat messages parsed from logfile by calling
        # the proper method from the corresponding class for the action
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue

            print("DEBUG: "+line)
            action = MessageGenerator.action_for(line, CHARACTER)
            if action:
                action.run()



# handle ctrl+c for clean exit
except KeyboardInterrupt:
    print("")
    print("Closing The EverQuest Alerter")

finally:
    # close log file and exit
    f.close()
    sys.exit()
