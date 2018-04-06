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
from Config import *
from DepCheck import *
from CharacterList import *


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
    command_line = 'urxvt -iconic -geometry 15x1 -bg red -fg white -title ' + name + ' -e perl ./StopWatchTest.py ' + str(time) + ' "' + message + '" 1'
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

            #print("DEBUG: "+line)

            #### PARSE FOR TRIGGERS AND GENERATE AUDIBLE ALERT ####
            ##### START RoF #####

            # A Matter of Life and Death - Chapterhouse
            if (MARNEK1) in line:
                os.system('flite -voice slt -t "Marnek is in skeleton form, shrouded players DPS now"')
                continue

            if (MARNEK2) in line:
                os.system('flite -voice slt -t "Corpse collector is dragging a corpse"')
                continue

            # Dispelling the Shadows - Plane of Shadow
            if (SHADOW1) in line:
                os.system('flite -voice slt -t "Group heal"')
                continue

            # single player
            SHAD2CHAR = SHADOW2 + CHARACTER
            if (SHAD2CHAR) in line:
                os.system('flite -voice slt -t "D, A, and get aggro"')
                continue

            # single player
            SHAD3CHAR = SHADOW3 + CHARACTER
            if (SHAD3CHAR) in line:
                os.system('flite -voice slt -t "Move away from the front"')
                continue

            # single player
            SHAD4CHAR = SHADOW4 + CHARACTER
            if (SHAD4CHAR) in line:
                os.system('flite -voice slt -t "Move out of range"')
                continue

            if (SHADOW5) in line:
                os.system('flite -voice slt -t "Back away from the mob A E incoming"')
                continue

            # single player
            SHAD6CHAR = SHADOW6 + CHARACTER
            if (SHAD6CHAR) in line:
                os.system('flite -voice slt -t "Run away from the raid"')
                continue

            if (SHADOW7) in line:
                os.system('flite -voice slt -t "Hide behind a pillar until the D, O, T, fades"')
                continue


            # Glimpse, the Unseen - The Threshold
            # single player
            GLIMPCHAR = GLIMPSE + CHARACTER
            if (GLIMPCHAR) in line:
                os.system('flite -voice slt -t "run far away from the raid, east"')
                continue


            # Ulrich the Ageless - The Threshold
            # single player
            if (ULRICH1) in line:
                os.system('flite -voice slt -t "run through an aura, do not linger"')
                continue

            # single player
            if (ULRICH2) in line:
                os.system('flite -voice slt -t "run through an aura, or D A"')
                continue


            # Monarch Widow - The Threshold
            if (MONARCH) in line:
                os.system('flite -voice slt -t "move raid 50 feet counter-clockwise to avoid web"')
                continue


            # An End to Fear - The Epicenter
            # single player
            if (ENDFEAR1) in line:
                os.system('flite -voice slt -t "move out of melee range"')
                continue

            # single player
            if (ENDFEAR2) in line:
                os.system('flite -voice slt -t "get curse cure"')
                continue

            # single player
            if (ENDFEAR3) in line:
                os.system('flite -voice slt -t "get corruption cure"')
                continue

            if (ENDFEAR4) in line:
                os.system('flite -voice slt -t "Xaric is vulnerable, kill kill kill"')
                continue

            # single player
            if (ENDFEAR5) in line:
                os.system('flite -voice slt -t "stop D P S until effect wears off"')
                continue

            ##### END RoF #####


            ##### START CoF #####

            # Bixie Warfront: Pelzia's Plot raid.
            # single player
            PEL1CHAR = PELZIA1 + CHARACTER
            if (PEL1CHAR) in line:
                os.system('flite -voice slt -t "run west away from raid"')
                continue

            # single player
            PEL2CHAR = PELZIA2 + CHARACTER
            if (PEL2CHAR) in line:
                os.system('flite -voice slt -t "run east away from raid"')
                continue


            # The Dead Hills: Xulous Prime raid.
            # single player
            if (XULOUS1) in line:
                os.system('flite -voice slt -t "kite the cloud of disease"')
                continue

            # single player
            if (XULOUS2) in line:
                os.system('flite -voice slt -t "kite the cloud of disease"')
                continue

            # single player
            if (XULOUS3) in line:
                os.system('flite -voice slt -t "get disease cure"')
                continue

            # single player
            if (XULOUS4) in line:
                os.system('flite -voice slt -t "move out of the disease aura"')
                continue

            # single player
            if (XULOUS5) in line:
                os.system('flite -voice slt -t "gate out now"')
                continue


            # Neriak - Fourth Gate: Houses of Thex raid.
            if (THEX1) in line:
                os.system('flite -voice slt -t "move out of range"')
                continue

            # single player
            THEX2CHAR = THEX2 + CHARACTER
            if (THEX2CHAR) in line:
                os.system('flite -voice slt -t "run east away from the raid"')
                continue

            # single player
            THEX3CHAR = THEX3 + CHARACTER
            if (THEX3CHAR) in line:
                os.system('flite -voice slt -t "kite until the energy pulse fades away"')
                continue

            # single player
            if (THEX4) in line:
                os.system('flite -voice slt -t "move out of the lightning pulse"')
                continue

            # single player
            THEX5CHAR = THEX5 + CHARACTER
            if (THEX5CHAR) in line:
                os.system('flite -voice slt -t "run away from the raid"')
                continue


            # Neriak - Fourth Gate: Hate Rising raid.
            # single player
            if (HATERISING1) in line:
                os.system('flite -voice slt -t "move out of the damaging aura"')
                continue

            if (HATERISING2) in line:
                os.system('flite -voice slt -t "move away from the pinned player"')
                continue


            # Tower of Rot: Lord Kyle Bayle raid.
            if (BAYLE1) in line:
                os.system('flite -voice slt -t "move out of melee range and hold pets"')
                continue

            if (BAYLE2) in line:
                os.system('flite -voice slt -t "resume melee and send in pets"')
                continue


            # Argin-Hiz: Burn Out raid.
            # single player
            if (BURNOUT1) in line:
                os.system('flite -voice slt -t "move out of the aura"')
                continue

            if (BURNOUT2) in line:
                os.system('flite -voice slt -t "Imps are spawning, invis everyone now"')
                continue

            if (BURNOUT3) in line:
                os.system('flite -voice slt -t "balance the mini bosses"')
                continue

            if (BURNOUT4) in line:
                os.system('flite -voice slt -t "a phoenix spawned"')
                continue


            # The Void (H): The Journey Home raid.
            if (JOURNEY1) in line:
                os.system('flite -voice slt -t "get out of melee range"')
                continue

            # single player
            if (JOURNEY2) in line:
                os.system('flite -voice slt -t "take portal to another island"')
                continue

            if (JOURNEY3) in line:
                os.system('flite -voice slt -t "Lanys is charming the main tank"')
                continue

            if (JOURNEY4) in line:
                os.system('flite -voice slt -t "Lanys is casting beam DoT, prepare to mass a curse cure"')
                continue

            # single player
            if (JOURNEY5) in line:
                os.system('flite -voice slt -t "get a curse cure"')
                continue

            if (JOURNEY6) in line:
                os.system('flite -voice slt -t "move out of melee range"')
                continue

            # single player
            JOUR7CHAR = JOURNEY7 + CHARACTER
            if (JOUR7CHAR) in line:
                os.system('flite -voice slt -t "run away from raid and hide"')
                continue

            # single player
            JOUR8CHAR = JOURNEY8 + CHARACTER
            if (JOUR8CHAR) in line:
                os.system('flite -voice slt -t "get a corruption cure"')
                continue

            # single player
            JOUR9CHAR = JOURNEY9 + CHARACTER
            if (JOUR9CHAR) in line:
                os.system('flite -voice slt -t "move away from the edge of the island now"')
                continue

            if (JOURNEY10) in line:
                os.system('flite -voice slt -t "move to your assigned island now or die"')
                continue

            # single player
            if (JOURNEY11) in line:
                os.system('flite -voice slt -t "get a corruption cure"')
                continue

            ##### END CoF #####


            ##### START Fifteenth Anniversary #####

            # The Plane of War: 15th anniversary raid.
            if (POW15) in line:
                os.system('flite -voice slt -t "move away from the A E circle"')
                continue

            ##### END Fifteenth Anniversary #####


            ##### START TDS #####

            # Defense of the City
            # single player
            if (TDSDEF1) in line:
                os.system('flite -voice slt -t "move away from the raid now"')
                continue

            # single player
            if (TDSDEF2) in line:
                os.system('flite -voice slt -t "It is safe to return to the raid"')
                continue

            # single player
            if (TDSDEF3) in line:
                os.system('flite -voice slt -t "It is safe to return to the raid"')
                continue

            # single player
            TDSD4CHAR = TDSDEF4 + CHARACTER
            if (TDSD4CHAR) in line:
                os.system('flite -voice slt -t "It is safe to return to the raid"')
                continue

            # single player
            if (TDSDEF5) in line:
                os.system('flite -voice slt -t "Get a disease cure"')
                continue


            # Principal Quastori Numicia
            # single player
            if (QUASI1) in line:
                os.system('flite -voice slt -t "Move out of the aura"')
                continue

            # single player
            if (QUASI2) in line:
                os.system('flite -voice slt -t "Move away from the raid"')
                continue


            # Praetor Vitio
            if (VITIO1) in line:
                os.system('flite -voice slt -t "Move away from his left side"')
                continue

            if (VITIO2) in line:
                os.system('flite -voice slt -t "Move away from his right side"')
                continue

            if (VITIO3) in line:
                os.system('flite -voice slt -t "Move away from Vitio"')
                continue

            if (VITIO4) in line:
                os.system('flite -voice slt -t "Get close to Vitio"')
                continue

            if (VITIO5) in line:
                os.system('flite -voice slt -t "Move away from his back"')
                continue

            if (VITIO6) in line:
                os.system('flite -voice slt -t "Main tank drop aggro"')
                continue

            if (VITIO7) in line:
                os.system('flite -voice slt -t "Next tank start taunting"')
                continue


            # Principal Vicarum Nomia
            if (NOMIA1) in line:
                os.system('flite -voice slt -t "Move away from the target"')
                continue

            if (NOMIA2) in line:
                os.system('flite -voice slt -t "Move away from the blob"')
                continue

            # single player
            NOM3CHAR = CHARACTER + NOMIA3
            if (NOM3CHAR) in line:
                os.system('flite -voice slt -t "Run away from the raid"')
                continue

            # single player
            if (NOMIA4) in line:
                os.system('flite -voice slt -t "Start running or get a corruption cure"')
                continue

            if (NOMIA5) in line:
                os.system('flite -voice slt -t "D P S on totems"')
                continue

            # single player
            if (NOMIA6) in line:
                os.system('flite -voice slt -t "Move away from the raid"')
                continue

            if (NOMIA7) in line:
                os.system('flite -voice slt -t "Move away from the target for 10 seconds"')
                continue

            if (NOMIA8) in line:
                os.system('flite -voice slt -t "Heal the totems"')
                continue

            # single player
            if (NOMIA9) in line:
                os.system('flite -voice slt -t "Run away you are the target for the A E"')
                continue

            ##### END TDS #####


            ##### START TBM RAIDS #####

            # Maestro TBM Raid
            if (MAESTRO) in line:
                os.system('flite -voice slt -t "healer cure"')
                continue


            # Inny TBM Raid
            if (INNY1) in line:
                os.system('flite -voice slt -t "fade or feign death"')
                continue

            if (INNY2) in line:
                os.system('flite -voice slt -t "run through the aura now"')
                continue


            # Anashti Sul, Lady of Life
            if (LIFE1) in line:
                os.system('flite -voice slt -t "Run into the aura"')
                continue

            # single player
            if (LIFE2) in line:
                os.system('flite -voice slt -t "Do not get healed, you will explode"')
                continue

            if (LIFE3) in line:
                os.system('flite -voice slt -t "Move to the area where the skull is facing"')
                continue


            # Wither and Decay
            if (WITHER1) in line:
                os.system('flite -voice slt -t "Run away from the raid"')
                continue

            # single player
            if (WITHER2) in line:
                os.system('flite -voice slt -t "Move off of the ooze"')
                continue


            # Anashti Sul, Damsel of Decay
            # single player
            ANASH1CHAR = ANASHTI1 + CHARACTER
            if (ANASH1CHAR) in line:
                os.system('flite -voice slt -t "Stop casting disease and corruption based spells"')
                continue

            if (ANASHTI2) in line:
                os.system('flite -voice slt -t "The boss has warped"')
                continue

            # single player
            if (ANASHTI3) in line:
                os.system('flite -voice slt -t "Your cured"')
                continue

            # single player
            if (ANASHTI4) in line:
                os.system('flite -voice slt -t "Do not cure the gift of endless life"')
                continue

            # single player
            if (ANASHTI5) in line:
                os.system('flite -voice slt -t "Get curse cure if you do not have gift of endless life buff"')
                continue

            # single player
            if (ANASHTI6) in line:
                os.system('flite -voice slt -t "move away from the tendrils"')
                continue

            # single player
            if (ANASHTI7) in line:
                os.system('flite -voice slt -t "Cure disease"')
                continue

            # single player
            if (ANASHTI8) in line:
                os.system('flite -voice slt -t "Cure disease twice"')
                continue

            # single player
            if (ANASHTI9) in line:
                os.system('flite -voice slt -t "Cure disease once"')
                continue


            # Grannus of the Cleansing Steam
            # single player
            if (GRANNUS1) in line:
                os.system('flite -voice slt -t "get a corruption cure"')
                continue

            if (GRANNUS2) in line:
                os.system('flite -voice slt -t "Pally splash now"')
                continue

            if (GRANNUS3) in line:
                os.system('flite -voice slt -t "D P S the portal now"')
                continue

            if (GRANNUS4) in line:
                os.system('flite -voice slt -t "Stop nuking"')
                continue

            if (GRANNUS5) in line:
                os.system('flite -voice slt -t "Resume nuking"')
                continue


            # Stem the Tide
            # single player
            TIDECHAR = TIDE + CHARACTER
            if (TIDECHAR) in line:
                os.system('flite -voice slt -t "Run away from the raid"')
                continue


            # Grummus!
            # single player
            if (GRUMMUS1) in line:
                os.system('flite -voice slt -t "Move away from the raid"')
                continue

            # single player
            GRUM2CHAR = GRUMMUS2 + CHARACTER
            if (GRUM2CHAR) in line:
                os.system('flite -voice slt -t "Move away from the raid"')
                continue

            if (GRUMMUS3) in line:
                os.system('flite -voice slt -t "Grummus is vulnerable, kill, kill, kill"')
                continue

            if (GRUMMUS4) in line:
                os.system('flite -voice slt -t "Grummus is invulnerable, your D P S is wasted"')
                continue


            # High Bokon Boromas
            if (BOKON) in line:
                os.system('flite -voice slt -t "Cure disease"')
                continue


            # Anashti Sul, Enslaver of Souls
            # single player
            ENSL1CHAR = ENSLAVER1 + CHARACTER
            if (ENSL1CHAR) in line:
                os.system('flite -voice slt -t "Run north or south away from the raid"')
                continue

            if (ENSLAVER2) in line:
                os.system('flite -voice slt -t "Get close to the raid"')
                continue

            if (ENSLAVER3) in line:
                os.system('flite -voice slt -t "Run to the pool with the aura now"')
                continue

            if (ENSLAVER4) in line:
                os.system('flite -voice slt -t "Cure disease twice"')
                continue

            ##### END TBM RAIDS #####


            ##### START 17th Anniversary Raid #####

            # Seventeen pieces of silver raid
            if (HF17) in line:
                os.system('flite -voice slt -t "run through the aura now"')
                continue

            ##### END 17th Anniversary Raid #####


            ##### START EoK RAIDS #####

            # Doorstep of War - Lceanium
            if (LCE1) in line:
                os.system('flite -voice slt -t "Move away from her front"')
                continue

            if (LCE2) in line:
                os.system('flite -voice slt -t "Move away from her left side"')
                continue

            if (LCE3) in line:
                os.system('flite -voice slt -t "Move away from her right side"')
                continue

            if (LCE4) in line:
                os.system('flite -voice slt -t "Move away from her back"')
                continue


            # The Summoning of Droga - Droga
            # single player
            DROG1CHAR = DROGA1 + CHARACTER
            if (DROG1CHAR) in line:
                os.system('flite -voice slt -t "move away from droga"')
                continue

            if (DROGA2) in line:
                os.system('flite -voice slt -t "move away from the red ring around droga"')
                continue

            if (DROGA3) in line:
                os.system('flite -voice slt -t "get corruption cure"')
                continue

            # single player
            DROG4CHAR = DROGA4 + CHARACTER
            if (DROG4CHAR) in line:
                os.system('flite -voice slt -t "move away from raid and out of drogas line of sight"')
                continue

            # single player
            DROG5CHAR = DROGA5 + CHARACTER
            if (DROG5CHAR) in line:
                os.system('flite -voice slt -t "move out of drogas line of sight"')
                continue

            # single player
            DROG6CHAR = DROGA6 + CHARACTER
            if (DROG6CHAR) in line:
                os.system('flite -voice slt -t "you have the red ring. move away from the raid"')
                continue


            # Queen Velazul Di'zok - Chardok
            if (VELAZUL1) in line:
                os.system('flite -voice slt -t "move north into the tunnel"')
                continue

            if (VELAZUL2) in line:
                os.system('flite -voice slt -t "it is safe to return to the raid"')
                continue

            ##### END EoK RAIDS #####


            ##### START GENERAL UTILITY ALERTS #####

            # Invis dropped
            if (APPEARING) in line:
                all_notify("Invisibility Drop")
                continue

            if (VISIBLE1) in line:
                all_notify("Invisibility Drop")
                continue

            if (VISIBLE2) in line:
                continue

            if (VISIBLE3) in line:
                all_notify("Invisibility Drop")
                continue

            if (VISIBLE4) in line:
                all_notify("Invisibility Drop")
                continue

            if (VISIBLE5) in line:
                all_notify("Invisibility Drop")
                continue

            if (VISIBLE6) in line:
                continue

            if (VISIBLE7) in line:
                all_notify("Invisibility Drop")
                continue

            if (LOST_FOLLOW1) in line:
                all_notify("Not Following")
                continue

            if (LOST_FOLLOW2) in line:
                all_notify("Not Following")
                continue

            if (ALERT_HAIL) in line:
                all_notify("Hail!")
                continue

            if (INVITE) in line:
                all_notify("Invite")
                continue

            if (CHARMBREAK) in line:
                all_notify("Charm break")
                continue

            if (ROOTBREAK1) in line:
                all_notify("Root break")
                continue

            if (ROOTBREAK2) in line:
                all_notify("Root break")
                continue

                all_notify("Mez break")
                continue

            if (ENTHRALLBREAK1) in line:
                all_notify("Mez break")
                continue

            if (ENTRANCEBREAK1) in line:
                all_notify("Mez break")
                continue

            if (DAZZLEBREAK1) in line:
                all_notify("Mez break")
                continue

            if (FASCINATEBREAK1) in line:
                all_notify("Mez break")
                continue

            if (GENERALBREAK) in line:
                all_notify("Spell break")
                continue

            if (DROPPED_ITEM1) in line:
                all_notify("Item Drop")
                continue

            if (DROPPED_ITEM2) in line:
                all_notify("Item Drop")
                continue

            if (DROPPED_ITEM3) in line:
                all_notify("Item Drop")
                continue

            if (LORE_ITEM) in line:
                all_notify("Lore Dupe")
                continue

            if (REAGENT_FAIL) in line:
                all_notify("Missing reagent")
                continue

            if (NO_MANA) in line:
                all_notify("Out of Mana")
                continue

            if (SPELL_FIZZLE) in line:
                all_notify("Fizzle")
                continue

            if (SPELL_RESIST) in line:
                all_notify("Resist")
                continue

            if (SPELL_INTERRUPT) in line:
                all_notify("Interrupted")
                continue


            if ('tells you,') in line:
                if (TELL_TO_IGNORE1) in line:
                    continue
                if (TELL_TO_IGNORE2) in line:
                    continue
                if (TELL_TO_IGNORE3) in line:
                    continue
                if (TELL_TO_IGNORE4) in line:
                    continue
                if (TELL_TO_IGNORE5) in line:
                    continue
                if (TELL_TO_IGNORE6) in line:
                    continue
                if (TELL_TO_IGNORE7) in line:
                    continue
                if (TELL_TO_IGNORE8) in line:
                    continue
                if (TELL_TO_IGNORE9) in line:
                    continue
                if (TELL_TO_IGNOREA) in line:
                    continue
                all_notify("Incoming Tell")
                continue


            # Feign death failed
            CHARFALL = CHARACTER + FALLEN
            if (CHARFALL) in line:
                os.system('flite -voice slt -t "feign death failed"')
                continue

            if (FDBROKEN) in line:
                os.system('flite -voice slt -t "feign death was broken"')
                continue

            # Feign death all clear
            if (FDCLEAR) in line:
                os.system('flite -voice slt -t "you can get up now"')
                continue

            # Feign death resist
            if (FDRESIST) in line:
                os.system('flite -voice slt -t "you resume feigning death"')
                continue

            # Mez Timers
            if (MEZ) in line:
                background_task(19, 'Mez Warn', 'Mez')
                continue

            if (FASCINATE) in line:
                background_task(31, 'Mez Warn', 'Fas')
                continue

            if (ENTHRALL) in line:
                background_task(43, 'Enthrall Warn', 'Etl')
                continue

            if (ENTRANCE) in line:
                background_task(67, 'Entrance Warn', 'Etc')
                continue

            if (DAZZLE) in line:
                background_task(91, 'Dazzle Warn', 'Daz')
                continue

                ##### END GENERAL UTILITY ALERTS #####

            # end outer if

        # end while

    # end with

# handle ctrl+c for clean exit
except KeyboardInterrupt:
    print("")
    print("Closing The EverQuest Alerter")

finally:
    # close log file and exit
    f.close()
    sys.exit()
