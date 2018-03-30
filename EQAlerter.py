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

from os import listdir
from os.path import isfile, join

# classes
from Config import *
from DepCheck import *
from CharacterList import *

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
    # sys.stdout.write("Command: " + command_line)
    subprocess.Popen(command_args, close_fds=True)

# begin parsing log file for triggers and perform actions
try:

    # open log file
    with open(LOGFILE, 'r+') as f:
        # move to the end of the file
        f.readlines()

        # loop over each new line of the file in realtime and
        # act on keywords from chat messages parsed from logfile by calling 
        # the proper method from the corresponding class for the action
        while True:
            time.sleep(0.1)
            line = f.readline()
            if line:
                #print("DEBUG: "+line)

                #### PARSE FOR TRIGGERS AND GENERATE AUDIBLE ALERT ####


                ##### START RoF #####

                # A Matter of Life and Death - Chapterhouse
                if (MARNEK1) in line:
                    os.system('flite -voice slt -t "Marnek is in skeleton form, shrouded players DPS now"')

                if (MARNEK2) in line:
                    os.system('flite -voice slt -t "Corpse collector is dragging a corpse"')

                # Dispelling the Shadows - Plane of Shadow
                if (SHADOW1) in line:
                    os.system('flite -voice slt -t "Group heal"')

                # single player
                SHAD2CHAR = SHADOW2 + CHARACTER
                if (SHAD2CHAR) in line:
                    os.system('flite -voice slt -t "D, A, and get aggro"')
                
                # single player
                SHAD3CHAR = SHADOW3 + CHARACTER
                if (SHAD3CHAR) in line:
                    os.system('flite -voice slt -t "Move away from the front"')

                # single player
                SHAD4CHAR = SHADOW4 + CHARACTER
                if (SHAD4CHAR) in line:
                    os.system('flite -voice slt -t "Move out of range"')

                if (SHADOW5) in line:
                    os.system('flite -voice slt -t "Back away from the mob A E incoming"')

                # single player
                SHAD6CHAR = SHADOW6 + CHARACTER
                if (SHAD6CHAR) in line:
                    os.system('flite -voice slt -t "Run away from the raid"')
                
                if (SHADOW7) in line:
                    os.system('flite -voice slt -t "Hide behind a pillar until the D, O, T, fades"')
                

                # Glimpse, the Unseen - The Threshold
                # single player
                GLIMPCHAR = GLIMPSE + CHARACTER
                if (GLIMPCHAR) in line:
                    os.system('flite -voice slt -t "run far away from the raid, east"')
                

                # Ulrich the Ageless - The Threshold
                # single player
                if (ULRICH1) in line:
                    os.system('flite -voice slt -t "run through an aura, do not linger"')
               
                # single player
                if (ULRICH2) in line:
                    os.system('flite -voice slt -t "run through an aura, or D A"')

                
                # Monarch Widow - The Threshold
                if (MONARCH) in line:
                    os.system('flite -voice slt -t "move raid 50 feet counter-clockwise to avoid web"')
                

                # An End to Fear - The Epicenter
                # single player
                if (ENDFEAR1) in line:
                    os.system('flite -voice slt -t "move out of melee range"')
                
                # single player
                if (ENDFEAR2) in line:
                    os.system('flite -voice slt -t "get curse cure"')
                
                # single player
                if (ENDFEAR3) in line:
                    os.system('flite -voice slt -t "get corruption cure"')
                
                if (ENDFEAR4) in line:
                    os.system('flite -voice slt -t "Xaric is vulnerable, kill kill kill"')
                
                # single player
                if (ENDFEAR5) in line:
                    os.system('flite -voice slt -t "stop D P S until effect wears off"')

                ##### END RoF #####


                ##### START CoF #####
                
                # Bixie Warfront: Pelzia's Plot raid.
                # single player
                PEL1CHAR = PELZIA1 + CHARACTER
                if (PEL1CHAR) in line:
                    os.system('flite -voice slt -t "run west away from raid"')

                # single player
                PEL2CHAR = PELZIA2 + CHARACTER
                if (PEL2CHAR) in line:
                    os.system('flite -voice slt -t "run east away from raid"')
                

                # The Dead Hills: Xulous Prime raid.
                # single player
                if (XULOUS1) in line:
                    os.system('flite -voice slt -t "kite the cloud of disease"')
                
                # single player
                if (XULOUS2) in line:
                    os.system('flite -voice slt -t "kite the cloud of disease"')
                
                # single player
                if (XULOUS3) in line:
                    os.system('flite -voice slt -t "get disease cure"')
                
                # single player
                if (XULOUS4) in line:
                    os.system('flite -voice slt -t "move out of the disease aura"')
                
                # single player
                if (XULOUS5) in line:
                    os.system('flite -voice slt -t "gate out now"')
                

                # Neriak - Fourth Gate: Houses of Thex raid.
                if (THEX1) in line:
                    os.system('flite -voice slt -t "move out of range"')

                # single player
                THEX2CHAR = THEX2 + CHARACTER
                if (THEX2CHAR) in line:
                    os.system('flite -voice slt -t "run east away from the raid"')

                # single player
                THEX3CHAR = THEX3 + CHARACTER
                if (THEX3CHAR) in line:
                    os.system('flite -voice slt -t "kite until the energy pulse fades away"')
               
                # single player
                if (THEX4) in line:
                    os.system('flite -voice slt -t "move out of the lightning pulse"')
                
                # single player
                THEX5CHAR = THEX5 + CHARACTER
                if (THEX5CHAR) in line:
                    os.system('flite -voice slt -t "run away from the raid"')
                

                # Neriak - Fourth Gate: Hate Rising raid.
                # single player
                if (HATERISING1) in line:
                    os.system('flite -voice slt -t "move out of the damaging aura"')

                if (HATERISING2) in line:
                    os.system('flite -voice slt -t "move away from the pinned player"')


                # Tower of Rot: Lord Kyle Bayle raid.
                if (BAYLE1) in line:
                    os.system('flite -voice slt -t "move out of melee range and hold pets"')
                
                if (BAYLE2) in line:
                    os.system('flite -voice slt -t "resume melee and send in pets"')


                # Argin-Hiz: Burn Out raid.
                # single player
                if (BURNOUT1) in line:
                    os.system('flite -voice slt -t "move out of the aura"')

                if (BURNOUT2) in line:
                    os.system('flite -voice slt -t "Imps are spawning, invis everyone now"')

                if (BURNOUT3) in line:
                    os.system('flite -voice slt -t "balance the mini bosses"')

                if (BURNOUT4) in line:
                    os.system('flite -voice slt -t "a phoenix spawned"')


                # The Void (H): The Journey Home raid.
                if (JOURNEY1) in line:
                    os.system('flite -voice slt -t "get out of melee range"')

                # single player
                if (JOURNEY2) in line:
                    os.system('flite -voice slt -t "take portal to another island"')

                if (JOURNEY3) in line:
                    os.system('flite -voice slt -t "Lanys is charming the main tank"')

                if (JOURNEY4) in line:
                    os.system('flite -voice slt -t "Lanys is casting beam DoT, prepare to mass a curse cure"')

                # single player
                if (JOURNEY5) in line:
                    os.system('flite -voice slt -t "get a curse cure"')

                if (JOURNEY6) in line:
                    os.system('flite -voice slt -t "move out of melee range"')

                # single player
                JOUR7CHAR = JOURNEY7 + CHARACTER
                if (JOUR7CHAR) in line:
                    os.system('flite -voice slt -t "run away from raid and hide"')

                # single player
                JOUR8CHAR = JOURNEY8 + CHARACTER
                if (JOUR8CHAR) in line:
                    os.system('flite -voice slt -t "get a corruption cure"')

                # single player
                JOUR9CHAR = JOURNEY9 + CHARACTER
                if (JOUR9CHAR) in line:
                    os.system('flite -voice slt -t "move away from the edge of the island now"')

                if (JOURNEY10) in line:
                    os.system('flite -voice slt -t "move to your assigned island now or die"')

                # single player
                if (JOURNEY11) in line:
                    os.system('flite -voice slt -t "get a corruption cure"')

                ##### END CoF #####


                ##### START Fifteenth Anniversary #####

                # The Plane of War: 15th anniversary raid.
                if (POW15) in line:
                    os.system('flite -voice slt -t "move away from the A E circle"')

                ##### END Fifteenth Anniversary #####
                

                ##### START TDS #####
                
                # Defense of the City
                # single player
                if (TDSDEF1) in line:
                    os.system('flite -voice slt -t "move away from the raid now"')
                
                # single player
                if (TDSDEF2) in line:
                    os.system('flite -voice slt -t "It is safe to return to the raid"')
                
                # single player
                if (TDSDEF3) in line:
                    os.system('flite -voice slt -t "It is safe to return to the raid"')
                
                # single player
                TDSD4CHAR = TDSDEF4 + CHARACTER
                if (TDSD4CHAR) in line:
                    os.system('flite -voice slt -t "It is safe to return to the raid"')
                
                # single player
                if (TDSDEF5) in line:
                    os.system('flite -voice slt -t "Get a disease cure"')
              

                # Principal Quastori Numicia
                # single player
                if (QUASI1) in line:
                    os.system('flite -voice slt -t "Move out of the aura"')

                # single player
                if (QUASI2) in line:
                    os.system('flite -voice slt -t "Move away from the raid"')


                # Praetor Vitio
                if (VITIO1) in line:
                    os.system('flite -voice slt -t "Move away from his left side"')

                if (VITIO2) in line:
                    os.system('flite -voice slt -t "Move away from his right side"')
                
                if (VITIO3) in line:
                    os.system('flite -voice slt -t "Move away from Vitio"')
                
                if (VITIO4) in line:
                    os.system('flite -voice slt -t "Get close to Vitio"')
                
                if (VITIO5) in line:
                    os.system('flite -voice slt -t "Move away from his back"')
                
                if (VITIO6) in line:
                    os.system('flite -voice slt -t "Main tank drop aggro"')
                
                if (VITIO7) in line:
                    os.system('flite -voice slt -t "Next tank start taunting"')


                # Principal Vicarum Nomia
                if (NOMIA1) in line:
                    os.system('flite -voice slt -t "Move away from the target"')
                
                if (NOMIA2) in line:
                    os.system('flite -voice slt -t "Move away from the blob"')
               
                # single player
                NOM3CHAR = CHARACTER + NOMIA3
                if (NOM3CHAR) in line:
                    os.system('flite -voice slt -t "Run away from the raid"')
                
                # single player
                if (NOMIA4) in line:
                    os.system('flite -voice slt -t "Start running or get a corruption cure"')
               
                if (NOMIA5) in line:
                    os.system('flite -voice slt -t "D P S on totems"')
               
                # single player
                if (NOMIA6) in line:
                    os.system('flite -voice slt -t "Move away from the raid"')
               
                if (NOMIA7) in line:
                    os.system('flite -voice slt -t "Move away from the target for 10 seconds"')
               
                if (NOMIA8) in line:
                    os.system('flite -voice slt -t "Heal the totems"')
               
                # single player
                if (NOMIA9) in line:
                    os.system('flite -voice slt -t "Run away you are the target for the A E"')
               
                ##### END TDS #####


                ##### START TBM RAIDS #####

                # Maestro TBM Raid
                if (MAESTRO) in line:
                    os.system('flite -voice slt -t "healer cure"')
              

                # Inny TBM Raid
                if (INNY1) in line:
                    os.system('flite -voice slt -t "fade or feign death"')

                if (INNY2) in line:
                    os.system('flite -voice slt -t "run through the aura now"')
              

                # Anashti Sul, Lady of Life
                if (LIFE1) in line:
                    os.system('flite -voice slt -t "Run into the aura"')
               
                # single player
                if (LIFE2) in line:
                    os.system('flite -voice slt -t "Do not get healed, you will explode"')
               
                if (LIFE3) in line:
                    os.system('flite -voice slt -t "Move to the area where the skull is facing"')
              

                # Wither and Decay
                if (WITHER1) in line:
                    os.system('flite -voice slt -t "Run away from the raid"')

                # single player
                if (WITHER2) in line:
                    os.system('flite -voice slt -t "Move off of the ooze"')


                # Anashti Sul, Damsel of Decay
                # single player
                ANASH1CHAR = ANASHTI1 + CHARACTER
                if (ANASH1CHAR) in line:
                    os.system('flite -voice slt -t "Stop casting disease and corruption based spells"')

                if (ANASHTI2) in line:
                    os.system('flite -voice slt -t "The boss has warped"')

                # single player
                if (ANASHTI3) in line:
                    os.system('flite -voice slt -t "Your cured"')
                
                # single player
                if (ANASHTI4) in line:
                    os.system('flite -voice slt -t "Do not cure the gift of endless life"')

                # single player
                if (ANASHTI5) in line:
                    os.system('flite -voice slt -t "Get curse cure if you do not have gift of endless life buff"')

                # single player
                if (ANASHTI6) in line:
                    os.system('flite -voice slt -t "move away from the tendrils"')

                # single player
                if (ANASHTI7) in line:
                    os.system('flite -voice slt -t "Cure disease"')

                # single player
                if (ANASHTI8) in line:
                    os.system('flite -voice slt -t "Cure disease twice"')

                # single player
                if (ANASHTI9) in line:
                    os.system('flite -voice slt -t "Cure disease once"')

                
                # Grannus of the Cleansing Steam
                # single player
                if (GRANNUS1) in line:
                    os.system('flite -voice slt -t "get a corruption cure"')

                if (GRANNUS2) in line:
                    os.system('flite -voice slt -t "Pally splash now"')

                if (GRANNUS3) in line:
                    os.system('flite -voice slt -t "D P S the portal now"')

                if (GRANNUS4) in line:
                    os.system('flite -voice slt -t "Stop nuking"')

                if (GRANNUS5) in line:
                    os.system('flite -voice slt -t "Resume nuking"')


                # Stem the Tide
                # single player
                TIDECHAR = TIDE + CHARACTER
                if (TIDECHAR) in line:
                    os.system('flite -voice slt -t "Run away from the raid"')


                # Grummus!
                # single player
                if (GRUMMUS1) in line:
                    os.system('flite -voice slt -t "Move away from the raid"')

                # single player
                GRUM2CHAR = GRUMMUS2 + CHARACTER
                if (GRUM2CHAR) in line:
                    os.system('flite -voice slt -t "Move away from the raid"')

                if (GRUMMUS3) in line:
                    os.system('flite -voice slt -t "Grummus is vulnerable, kill, kill, kill"')

                if (GRUMMUS4) in line:
                    os.system('flite -voice slt -t "Grummus is invulnerable, your D P S is wasted"')


                # High Bokon Boromas
                if (BOKON) in line:
                    os.system('flite -voice slt -t "Cure disease"')


                # Anashti Sul, Enslaver of Souls
                # single player
                ENSL1CHAR = ENSLAVER1 + CHARACTER
                if (ENSL1CHAR) in line:
                    os.system('flite -voice slt -t "Run north or south away from the raid"')
                
                if (ENSLAVER2) in line:
                    os.system('flite -voice slt -t "Get close to the raid"')

                if (ENSLAVER3) in line:
                    os.system('flite -voice slt -t "Run to the pool with the aura now"')

                if (ENSLAVER4) in line:
                    os.system('flite -voice slt -t "Cure disease twice"')

                ##### END TBM RAIDS #####

              
                ##### START 17th Anniversary Raid #####
               
                # Seventeen pieces of silver raid
                if (HF17) in line:
                    os.system('flite -voice slt -t "run through the aura now"')
                
                ##### END 17th Anniversary Raid #####


                ##### START EoK RAIDS #####
                
                # Doorstep of War - Lceanium
                if (LCE1) in line:
                    os.system('flite -voice slt -t "Move away from her front"')

                if (LCE2) in line:
                    os.system('flite -voice slt -t "Move away from her left side"')
                
                if (LCE3) in line:
                    os.system('flite -voice slt -t "Move away from her right side"')
                
                if (LCE4) in line:
                    os.system('flite -voice slt -t "Move away from her back"')
                

                # The Summoning of Droga - Droga
                # single player
                DROG1CHAR = DROGA1 + CHARACTER
                if (DROG1CHAR) in line:
                    os.system('flite -voice slt -t "move away from droga"')

                if (DROGA2) in line:
                    os.system('flite -voice slt -t "move away from the red ring around droga"')
                
                if (DROGA3) in line:
                    os.system('flite -voice slt -t "get corruption cure"')
                
                # single player
                DROG4CHAR = DROGA4 + CHARACTER
                if (DROG4CHAR) in line:
                    os.system('flite -voice slt -t "move away from raid and out of drogas line of sight"')
                
                # single player
                DROG5CHAR = DROGA5 + CHARACTER
                if (DROG5CHAR) in line:
                    os.system('flite -voice slt -t "move out of drogas line of sight"')

                # single player
                DROG6CHAR = DROGA6 + CHARACTER
                if (DROG6CHAR) in line:
                    os.system('flite -voice slt -t "you have the red ring. move away from the raid"')
                

                # Queen Velazul Di'zok - Chardok
                if (VELAZUL1) in line:
                    os.system('flite -voice slt -t "move north into the tunnel"')

                if (VELAZUL2) in line:
                    os.system('flite -voice slt -t "it is safe to return to the raid"')

                ##### END EoK RAIDS #####
                

                ##### START GENERAL UTILITY ALERTS #####

                # Invis dropped
                if (APPEARING) in line:
                    os.system('flite -voice slt -t "invis dropped"')

                if (VISIBLE1) in line:
                    os.system('flite -voice slt -t "invis dropped"')

                if (VISIBLE2) in line:
                    os.system('flite -voice slt -t "invis dropped"')

                if (VISIBLE3) in line:
                    os.system('flite -voice slt -t "invis dropped"')

                if (VISIBLE4) in line:
                    os.system('flite -voice slt -t "invis dropped"')

                if (VISIBLE5) in line:
                    os.system('flite -voice slt -t "invis dropped"')

                if (VISIBLE6) in line:
                    os.system('flite -voice slt -t "invis dropped"')

                if (VISIBLE7) in line:
                    os.system('flite -voice slt -t "invis dropped"')

                if (LOST_FOLLOW1) in line:
                    os.system('flite -voice slt -t "Follow fail"')

                if (LOST_FOLLOW2) in line:
                    os.system('flite -voice slt -t "Follow fail"')

                if (ALERT_HAIL) in line:
                    os.system('flite -voice slt -t "Hail"')

                if (INVITE) in line:
                    os.system('flite -voice slt -t "Invite"')

                if (ROOTBREAK1) in line:
                    os.system('flite -voice slt -t "Root break"')

                if (ROOTBREAK2) in line:
                    os.system('flite -voice slt -t "Root break"')

                if (MEZBREAK1) in line:
                    os.system('flite -voice slt -t "Mez break"')

                if (ENTHRALLBREAK1) in line:
                    os.system('flite -voice slt -t "Mez break"')

                if (ENTRANCEBREAK1) in line:
                    os.system('flite -voice slt -t "Mez break"')

                if (DAZZLEBREAK1) in line:
                    os.system('flite -voice slt -t "Mez break"')

                if (FASCINATEBREAK1) in line:
                    os.system('flite -voice slt -t "Mez break"')

                if (DROPPED_ITEM1) in line:
                    os.system('flite -voice slt -t "Item Drop"')

                if (DROPPED_ITEM2) in line:
                    os.system('flite -voice slt -t "Item Drop"')

                if (DROPPED_ITEM3) in line:
                    os.system('flite -voice slt -t "Item Drop"')

                if (LORE_ITEM) in line:
                    os.system('flite -voice slt -t "Lore duplicate"')

                if (REAGENT_FAIL) in line:
                    os.system('flite -voice slt -t "Missing component"')

                if (NO_MANA) in line:
                    os.system('flite -voice slt -t "Out of Mana"')

                if (SPELL_FIZZLE) in line:
                    os.system('flite -voice slt -t "Fizzle"')

                if (SPELL_RESIST) in line:
                    os.system('flite -voice slt -t "Resist"')

                if (SPELL_INTERRUPT) in line:
                    os.system('flite -voice slt -t "Interrupted"')


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
                    os.system('flite -voice slt -t "Tell"')


                # Feign death failed
                CHARFALL = CHARACTER + FALLEN
                if (CHARFALL) in line:
                    os.system('flite -voice slt -t "feign death failed"')

                if (FDBROKEN) in line:
                    os.system('flite -voice slt -t "feign death was broken"')
                
                # Feign death all clear
                if (FDCLEAR) in line:
                    os.system('flite -voice slt -t "you can get up now"')

                # Feign death resist
                if (FDRESIST) in line:
                    os.system('flite -voice slt -t "you resume feigning death"')

                # Mez Timers
                if (MEZ) in line:
                    background_task(19, 'Mez Warn', 'Mez')

                if (FASCINATE) in line:
                    background_task(31, 'Mez Warn', 'Fas')

                if (ENTHRALL) in line:
                    background_task(43, 'Enthrall Warn', 'Etl')

                if (ENTRANCE) in line:
                    background_task(67, 'Entrance Warn', 'Etc')

                if (DAZZLE) in line:
                    background_task(91, 'Dazzle Warn', 'Daz')

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
