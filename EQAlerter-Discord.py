#!/usr/bin/python

# Program Name: EQAlerter-Discord.py 
#               'The EverQuest Alerter - Discord Bot Version'
# Original Author: Dr. Ronny Bull (A.K.A. Cubber on eqemulator.org)
# Python Version: 3.5
# Original Date: 11/12/2017
# Last Revision: 11/20/2017

# Purpose:  This program is intended to run on a Linux system running 'EverQuest' under 'Wine'.
#           When running the program will parse your EverQuest chat log file for key phrases
#           contained in the Config.py file and trigger alerts using the discord bot API.

# Dependencies: Python 3 && CMU Flite text to speech engine && discord module 
#               python3 -m pip install --user -U discord.py[voice] # discord module

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

import subprocess
import time
import sys
import os
import discord
import asyncio

from os import listdir
from os.path import isfile, join
from discord.ext import commands

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
print("\n\nStarting The EverQuest Alerter - Discord Bot Version\n")
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
LOGPATH = "Logs/eqlog_%s_%s.txt" % (CHARACTER, SERVER) 
LOGFILE = EQHOME+LOGPATH
print(LOGFILE)
DepCheck.verifyLogFile(CHARACTER, LOGFILE)

# start up the bot and log in to discord
client = discord.Client()

# start up the bot
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('----------')
    await client.send_message(discord.Object(id=GENERAL_ID), 'Hello, my name is AlerterBot.  I am here to assist you during your raid today. Type !help for more info. To find out what events I support please type !raids', tts=False)

# some bot commands for testing and information
@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
   
    # bot info
    elif message.content.startswith('!who'):
        await client.send_message(message.channel, 'Hello, my name is AlerterBot.  I am here to assist you during your adventures. My creator is Nuggethead.', tts=False)

    # help text
    elif message.content.startswith('!help'):
        await client.send_message(message.channel, 'Please see the following webpage for instructions on how to enable Text to Speach on your Discord client so you can hear my alerts during the raid.  https://support.discordapp.com/hc/en-us/articles/212517297-Text-to-Speech-101. Make sure that you enable both settings, and set the notifications setting to: For All Channels')

    # TODO: supported raids
    elif message.content.startswith('!raids'):
        await client.send_message(message.channel, 'I can provide support during the following raid events:\n - RoF(A Matter of Life and Death - Chapterhouse, Dispelling the Shadows - Plane of Shadow, Glimpse the Unseen - The Threshold, Ulrich the Ageless - The Threshold, Monarch Widow - The Threshold, An End to Fear - The Epicenter)\n - CoF(Bixie Warfront: Pelzias Plot, The Dead Hills: Xulous Prime, Neriak - Fourth Gate: Houses of Thex, Neriak - Fourth Gate: Hate Rising, Tower of Rot: Lord Kyle Bayle, Argin-Hiz: Burn Out, The Void (H): The Journey Home)\n - TDS(Defense of the City, Principal Quastori Numicia, Praetor Vitio, Principal Vicarum Nomia)\n - TBM( Plane of Hate: Revisited - Maestro of Rancor & Innorukk, Anashti Sul - Lady of Life, Wither and Decay, Grannus of the Cleansing Steam, Stem the Tide, Grummus!, High Bokon Boromas, Anashti Sul - Enslaver of Souls)\n - EoK(Doorstep of War - Lceanium, The Summoning of Droga - Droga, Prince Selrach Dizok - Chardok, Queen Velazul Dizok - Chardok)\n - Anniversary(The Plane of War: 15th anniversary, 17th Anniversary raid - Hates Fury: Seventeen Pieces of Silver)', tts=False)
    
# loop through log file
@client.event
async def readline(f):
    while True:
        data = f.readline()
        if data:
            return data
        await asyncio.sleep(.5)

# begin parsing log file for triggers and perform actions
@client.event
async def logfile_loop():
    
    # open log file for reading
    with open(LOGFILE, 'r+') as f:

        # move to the end of the file
        f.truncate()
    
        
        #### PARSE FOR TRIGGERS AND GENERATE ALERT IN DISCORD ####
        while True:
            line = await readline(f)
            # print(line)  # for debugging

            if line:

                ##### START RoF #####

                # A Matter of Life and Death - Chapterhouse
                # multiplayer - send to discord
                if (MARNEK1) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Marnek is in skeleton form, shrouded players DPS now', tts=True)
                    #os.system('flite -voice slt -t "Marnek is in skeleton form, shrouded players DPS now"')

                # multiplayer - send to discord
                if (MARNEK2) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Corpse collector is dragging a corpse', tts=True)
                    #os.system('flite -voice slt -t "Corpse collector is dragging a corpse"')
                
                # Dispelling the Shadows - Plane of Shadow
                # multiplayer - send to discord
                if (SHADOW1) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Group heal', tts=True)
                    #os.system('flite -voice slt -t "Group heal"')
                
                # single player - use local tts
                SHAD2CHAR = SHADOW2 + CHARACTER
                if (SHAD2CHAR) in line:
                    os.system('flite -voice slt -t "D, A, and get aggro"')
                
                # single player - use local tts
                SHAD3CHAR = SHADOW3 + CHARACTER
                if (SHAD3CHAR) in line:
                    os.system('flite -voice slt -t "Move away from the front"')
                
                # single player - use local tts
                SHAD4CHAR = SHADOW4 + CHARACTER
                if (SHAD4CHAR) in line:
                    os.system('flite -voice slt -t "Move out of range"')
               
                # multiplayer - send to discord
                if (SHADOW5) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Back away from the mob A E incoming', tts=True)
                    #os.system('flite -voice slt -t "Back away from the mob A E incoming"')
                
                # single player - use local tts
                SHAD6CHAR = SHADOW6 + CHARACTER
                if (SHAD6CHAR) in line:
                    os.system('flite -voice slt -t "Run away from the raid"')
                
                # multiplayer - send to discord
                if (SHADOW7) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Hide behind a pillar until the D, O, T, fades', tts=True)
                    #os.system('flite -voice slt -t "Hide behind a pillar until the D, O, T, fades"')
                

                # Glimpse, the Unseen - The Threshold
                # single player - use local tts
                GLIMPCHAR = GLIMPSE + CHARACTER
                if (GLIMPCHAR) in line:
                    os.system('flite -voice slt -t "run far away from the raid, east"')
                

                # Ulrich the Ageless - The Threshold
                # single player - use local tts
                if (ULRICH1) in line:
                    os.system('flite -voice slt -t "run through an aura, do not linger"')
               
                # single player - use local tts
                if (ULRICH2) in line:
                    os.system('flite -voice slt -t "run through an aura, or D A"')

                
                # Monarch Widow - The Threshold
                # multiplayer - send to discord
                if (MONARCH) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'move raid 50 feet counter-clockwise to avoid web', tts=True)
                    #os.system('flite -voice slt -t "move raid 50 feet counter-clockwise to avoid web"')
                

                # An End to Fear - The Epicenter
                # single player - use local tts
                if (ENDFEAR1) in line:
                    os.system('flite -voice slt -t "move out of melee range"')
                
                # single player - use local tts
                if (ENDFEAR2) in line:
                    os.system('flite -voice slt -t "get curse cure"')
                
                # single player - use local tts
                if (ENDFEAR3) in line:
                    os.system('flite -voice slt -t "get corruption cure"')
                
                # multiplayer - send to discord
                if (ENDFEAR4) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Xaric is vulnerable, kill kill kill', tts=True)
                    #os.system('flite -voice slt -t "Xaric is vulnerable, kill kill kill"')
                
                # single player - use local tts
                if (ENDFEAR5) in line:
                    os.system('flite -voice slt -t "stop D P S until effect wears off"')

                ##### END RoF #####


                ##### START CoF #####
                
                # Bixie Warfront: Pelzia's Plot raid.
                # single player - use local tts
                PEL1CHAR = PELZIA1 + CHARACTER
                if (PEL1CHAR) in line:
                    os.system('flite -voice slt -t "run west away from raid"')

                # single player - use local tts
                PEL2CHAR = PELZIA2 + CHARACTER
                if (PEL2CHAR) in line:
                    os.system('flite -voice slt -t "run east away from raid"')
                

                # The Dead Hills: Xulous Prime raid.
                # single player - use local tts
                if (XULOUS1) in line:
                    os.system('flite -voice slt -t "kite the cloud of disease"')
                
                # single player - use local tts
                if (XULOUS2) in line:
                    os.system('flite -voice slt -t "kite the cloud of disease"')
                
                # single player - use local tts
                if (XULOUS3) in line:
                    os.system('flite -voice slt -t "get disease cure"')
                
                # single player - use local tts
                if (XULOUS4) in line:
                    os.system('flite -voice slt -t "move out of the disease aura"')
                
                # single player - use local tts
                if (XULOUS5) in line:
                    os.system('flite -voice slt -t "gate out now"')
                

                # Neriak - Fourth Gate: Houses of Thex raid.
                # multiplayer - send to discord
                if (THEX1) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'move out of range', tts=True)
                    #os.system('flite -voice slt -t "move out of range"')

                # single player - use local tts
                THEX2CHAR = THEX2 + CHARACTER
                if (THEX2CHAR) in line:
                    os.system('flite -voice slt -t "run east away from the raid"')

                # single player - use local tts
                THEX3CHAR = THEX3 + CHARACTER
                if (THEX3CHAR) in line:
                    os.system('flite -voice slt -t "kite until the energy pulse fades away"')
               
                # single player - use local tts
                if (THEX4) in line:
                    os.system('flite -voice slt -t "move out of the lightning pulse"')
                
                # single player - use local tts
                THEX5CHAR = THEX5 + CHARACTER
                if (THEX5CHAR) in line:
                    os.system('flite -voice slt -t "run away from the raid"')
                

                # Neriak - Fourth Gate: Hate Rising raid.
                # single player - use local tts
                if (HATERISING1) in line:
                    os.system('flite -voice slt -t "move out of the damaging aura"')

                # multiplayer - send to discord
                if (HATERISING2) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'move away from the pinned player', tts=True)
                    #os.system('flite -voice slt -t "move away from the pinned player"')


                # Tower of Rot: Lord Kyle Bayle raid.
                # multiplayer - send to discord
                if (BAYLE1) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'move out of melee range and hold pets', tts=True)
                    #os.system('flite -voice slt -t "move out of melee range and hold pets"')
                
                # multiplayer - send to discord
                if (BAYLE2) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'resume melee and send in pets', tts=True)
                    #os.system('flite -voice slt -t "resume melee and send in pets"')


                # Argin-Hiz: Burn Out raid.
                # single player - use local tts
                if (BURNOUT1) in line:
                    os.system('flite -voice slt -t "move out of the aura"')

                # multiplayer - send to discord
                if (BURNOUT2) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Imps are spawning, invis everyone now', tts=True)
                    #os.system('flite -voice slt -t "Imps are spawning, invis everyone now"')

                # multiplayer - send to discord
                if (BURNOUT3) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'balance the mini bosses', tts=True)
                    #os.system('flite -voice slt -t "balance the mini bosses"')

                # multiplayer - send to discord
                if (BURNOUT4) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'a phoenix spawned', tts=True)
                    #os.system('flite -voice slt -t "a phoenix spawned"')


                # The Void (H): The Journey Home raid.
                # multiplayer - send to discord
                if (JOURNEY1) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'get out of melee range', tts=True)
                    #os.system('flite -voice slt -t "get out of melee range"')

                # single player - use local tts
                if (JOURNEY2) in line:
                    os.system('flite -voice slt -t "take portal to another island"')

                # multiplayer - send to discord
                if (JOURNEY3) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Lanys is charming the main tank', tts=True)
                    #os.system('flite -voice slt -t "Lanys is charming the main tank"')

                # multiplayer - send to discord
                if (JOURNEY4) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Lanys is casting beam DoT, prepare to mass a curse cure', tts=True)
                    #os.system('flite -voice slt -t "Lanys is casting beam DoT, prepare to mass a curse cure"')

                # single player - use local tts
                if (JOURNEY5) in line:
                    os.system('flite -voice slt -t "get a curse cure"')

                # multiplayer - send to discord
                if (JOURNEY6) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'move out of melee range', tts=True)
                    #os.system('flite -voice slt -t "move out of melee range"')

                # single player - use local tts
                JOUR7CHAR = JOURNEY7 + CHARACTER
                if (JOUR7CHAR) in line:
                    os.system('flite -voice slt -t "run away from raid and hide"')

                # single player - use local tts
                JOUR8CHAR = JOURNEY8 + CHARACTER
                if (JOUR8CHAR) in line:
                    os.system('flite -voice slt -t "get a corruption cure"')

                # single player - use local tts
                JOUR9CHAR = JOURNEY9 + CHARACTER
                if (JOUR9CHAR) in line:
                    os.system('flite -voice slt -t "move away from the edge of the island now"')

                # multiplayer - send to discord
                if (JOURNEY10) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'move to your assigned island now or die', tts=True)
                    #os.system('flite -voice slt -t "move to your assigned island now or die"')

                # single player - use local tts
                if (JOURNEY11) in line:
                    os.system('flite -voice slt -t "get a corruption cure"')

                ##### END CoF #####


                ##### START Fifteenth Anniversary #####

                # The Plane of War: 15th anniversary raid.
                # multiplayer - send to discord
                if (POW15) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'move away from the A E circle', tts=True)
                    #os.system('flite -voice slt -t "move away from the A E circle"')

                ##### END Fifteenth Anniversary #####
                

                ##### START TDS #####
                
                # Defense of the City
                # single player - use local tts
                if (TDSDEF1) in line:
                    os.system('flite -voice slt -t "move away from the raid now"')
                
                # single player - use local tts
                if (TDSDEF2) in line:
                    os.system('flite -voice slt -t "It is safe to return to the raid"')
                
                # single player - use local tts
                if (TDSDEF3) in line:
                    os.system('flite -voice slt -t "It is safe to return to the raid"')
                
                # single player - use local tts
                TDSD4CHAR = TDSDEF4 + CHARACTER
                if (TDSD4CHAR) in line:
                    os.system('flite -voice slt -t "It is safe to return to the raid"')
                
                # single player - use local tts
                if (TDSDEF5) in line:
                    os.system('flite -voice slt -t "Get a disease cure"')
              

                # Principal Quastori Numicia
                # single player - use local tts
                if (QUASI1) in line:
                    os.system('flite -voice slt -t "Move out of the aura"')

                # single player - use local tts
                if (QUASI2) in line:
                    os.system('flite -voice slt -t "Move away from the raid"')


                # Praetor Vitio
                # multiplayer - send to discord
                if (VITIO1) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Move away from his left side', tts=True)
                    #os.system('flite -voice slt -t "Move away from his left side"')

                # multiplayer - send to discord
                if (VITIO2) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Move away from his right side', tts=True)
                    #os.system('flite -voice slt -t "Move away from his right side"')
                
                # multiplayer - send to discord
                if (VITIO3) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Move away from Vitio', tts=True)
                    #os.system('flite -voice slt -t "Move away from Vitio"')
                
                # multiplayer - send to discord
                if (VITIO4) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Get close to Vitio', tts=True)
                    #os.system('flite -voice slt -t "Get close to Vitio"')
                
                # multiplayer - send to discord
                if (VITIO5) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'move away from his back', tts=True)
                    #os.system('flite -voice slt -t "Move away from his back"')
                
                # multiplayer - send to discord
                if (VITIO6) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Main tank drop aggro now', tts=True)
                    #os.system('flite -voice slt -t "Main tank drop aggro now"')
                
                # multiplayer - send to discord
                if (VITIO7) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Next tank start taunting now', tts=True)
                    #os.system('flite -voice slt -t "Next tank start taunting now"')


                # Principal Vicarum Nomia
                # multiplayer - send to discord
                if (NOMIA1) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Move away from the target', tts=True)
                    #os.system('flite -voice slt -t "Move away from the target"')
                
                # multiplayer - send to discord
                if (NOMIA2) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Move away from the blob', tts=True)
                    #os.system('flite -voice slt -t "Move away from the blob"')
               
                # single player - use local tts
                NOM3CHAR = CHARACTER + NOMIA3
                if (NOM3CHAR) in line:
                    os.system('flite -voice slt -t "Run away from the raid"')
                
                # single player - use local tts
                if (NOMIA4) in line:
                    os.system('flite -voice slt -t "Start running or get a corruption cure"')
               
                # multiplayer - send to discord
                if (NOMIA5) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'D P S on totems', tts=True)
                    #os.system('flite -voice slt -t "D P S on totems"')
               
                # single player - use local tts
                if (NOMIA6) in line:
                    os.system('flite -voice slt -t "Move away from the raid"')
               
                # multiplayer - send to discord
                if (NOMIA7) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Move away from the target for 10 seconds', tts=True)
                    #os.system('flite -voice slt -t "Move away from the target for 10 seconds"')
               
                # multiplayer - send to discord
                if (NOMIA8) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Heal the totems', tts=True)
                    #os.system('flite -voice slt -t "Heal the totems"')
               
                # single player - use local tts
                if (NOMIA9) in line:
                    os.system('flite -voice slt -t "Run away you are the target for the A E"')
               
                ##### END TDS #####


                ##### START TBM RAIDS #####

                # Maestro TBM Raid
                # multiplayer - send to discord
                if (MAESTRO) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'healer cure', tts=True)
                    #os.system('flite -voice slt -t "healer cure"')


                # Inny TBM Raid
                # multiplayer - send to discord
                if (INNY1) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'fade or feign death', tts=True)
                    #os.system('flite -voice slt -t "fade or feign death"')

                # multiplayer - send to discord
                if (INNY2) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'run through the aura now', tts=True)
                    #os.system('flite -voice slt -t "run through the aura now"')


                # Anashti Sul, Lady of Life
                # multiplayer - send to discord
                if (LIFE1) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'run into the aura now', tts=True)
                    #os.system('flite -voice slt -t "Run into the aura now"')
               
                # single player - use local tts
                if (LIFE2) in line:
                    os.system('flite -voice slt -t "Do not get healed, you will explode"')
               
                # multiplayer - send to discord
                if (LIFE3) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Move to the area where the skull is facing', tts=True)
                    #os.system('flite -voice slt -t "Move to the area where the skull is facing"')
              

                # Wither and Decay
                # multiplayer - send to discord
                if (WITHER1) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Run away from the raid', tts=True)
                    #os.system('flite -voice slt -t "Run away from the raid"')

                # single player - use local tts
                if (WITHER2) in line:
                    os.system('flite -voice slt -t "Move off of the ooze"')


                # Anashti Sul, Damsel of Decay
                # single player - use local tts
                ANASH1CHAR = ANASHTI1 + CHARACTER
                if (ANASH1CHAR) in line:
                    os.system('flite -voice slt -t "Stop casting disease and corruption based spells"')

                # multiplayer - send to discord
                if (ANASHTI2) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'The boss has warped', tts=True)
                    #os.system('flite -voice slt -t "The boss has warped"')

                # single player - use local tts
                if (ANASHTI3) in line:
                    os.system('flite -voice slt -t "Your cured"')
                
                # single player - use local tts
                if (ANASHTI4) in line:
                    os.system('flite -voice slt -t "Do not cure the gift of endless life"')

                # single player - use local tts
                if (ANASHTI5) in line:
                    os.system('flite -voice slt -t "Get curse cure if you do not have gift of endless life buff"')

                # single player - use local tts
                if (ANASHTI6) in line:
                    os.system('flite -voice slt -t "move away from the tendrils"')

                # single player - use local tts
                if (ANASHTI7) in line:
                    os.system('flite -voice slt -t "Cure disease"')

                # single player - use local tts
                if (ANASHTI8) in line:
                    os.system('flite -voice slt -t "Cure disease twice"')

                # single player - use local tts
                if (ANASHTI9) in line:
                    os.system('flite -voice slt -t "Cure disease once"')

                
                # Grannus of the Cleansing Steam
                # single player - use local tts
                if (GRANNUS1) in line:
                    os.system('flite -voice slt -t "get a corruption cure"')

                # multiplayer - send to discord
                if (GRANNUS2) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Pally splash now', tts=True)
                    #os.system('flite -voice slt -t "Pally splash now"')

                # multiplayer - send to discord
                if (GRANNUS3) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'D P S the portal now', tts=True)
                    #os.system('flite -voice slt -t "D P S the portal now"')

                # multiplayer - send to discord
                if (GRANNUS4) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Stop nuking', tts=True)
                    #os.system('flite -voice slt -t "Stop nuking"')

                # multiplayer - send to discord
                if (GRANNUS5) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Resume nuking', tts=True)
                    #os.system('flite -voice slt -t "Resume nuking"')


                # Stem the Tide
                # single player - use local tts
                TIDECHAR = TIDE + CHARACTER
                if (TIDECHAR) in line:
                    os.system('flite -voice slt -t "Run away from the raid"')


                # Grummus!
                # single player - use local tts
                if (GRUMMUS1) in line:
                    os.system('flite -voice slt -t "Move away from the raid"')

                # single player - use local tts
                GRUM2CHAR = GRUMMUS2 + CHARACTER
                if (GRUM2CHAR) in line:
                    os.system('flite -voice slt -t "Move away from the raid"')

                # multiplayer - send to discord
                if (GRUMMUS3) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Grummus is vulnerable, kill, kill, kill', tts=True)
                    #os.system('flite -voice slt -t "Grummus is vulnerable, kill, kill, kill"')

                # multiplayer - send to discord
                if (GRUMMUS4) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Grummus is invulnerable, your D P S is wasted', tts=True)
                    #os.system('flite -voice slt -t "Grummus is invulnerable, your D P S is wasted"')


                # High Bokon Boromas
                # multiplayer - send to discord
                if (BOKON) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Cure disease', tts=True)
                    #os.system('flite -voice slt -t "Cure disease"')


                # Anashti Sul, Enslaver of Souls
                # single player - use local tts
                ENSL1CHAR = ENSLAVER1 + CHARACTER
                if (ENSL1CHAR) in line:
                    os.system('flite -voice slt -t "Run north or south away from the raid"')
                
                # multiplayer - send to discord
                if (ENSLAVER2) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Get close to the raid', tts=True)
                    #os.system('flite -voice slt -t "Get close to the raid"')

                # multiplayer - send to discord
                if (ENSLAVER3) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Run to the pool with the aura now', tts=True)
                    #os.system('flite -voice slt -t "Run to the pool with the aura now"')

                # multiplayer - send to discord
                if (ENSLAVER4) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Cure disease twice', tts=True)
                    #os.system('flite -voice slt -t "Cure disease twice"')

                ##### END TBM RAIDS #####


                ##### START 17th Anniversary Raid #####
               
                # Seventeen pieces of silver raid
                # multiplayer - send to discord
                if (HF17) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'run through the aura now', tts=True)
                    #os.system('flite -voice slt -t "run through the aura now"')
                
                ##### END 17th Anniversary Raid #####


                ##### START EoK RAIDS #####
                
                # Doorstep of War - Lceanium
                # multiplayer - send to discord
                if (LCE1) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Move away from her front', tts=True)
                    #os.system('flite -voice slt -t "Move away from her front"')

                # multiplayer - send to discord
                if (LCE2) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Move away from her left side', tts=True)
                    #os.system('flite -voice slt -t "Move away from her left side"')
                
                # multiplayer - send to discord
                if (LCE3) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Move away from her right side', tts=True)
                    #os.system('flite -voice slt -t "Move away from her right side"')
                
                # multiplayer - send to discord
                if (LCE4) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'Move away from her back', tts=True)
                    #os.system('flite -voice slt -t "Move away from her back"')


                # The Summoning of Droga - Droga
                # single player - use local tts
                DROG1CHAR = DROGA1 + CHARACTER
                if (DROG1CHAR) in line:
                    os.system('flite -voice slt -t "move away from droga"')

                # multiplayer - send to discord
                if (DROGA2) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'move away from the red ring around droga', tts=True)
                    #os.system('flite -voice slt -t "move away from the red ring around droga"')
                
                # multiplayer - send to discord
                if (DROGA3) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'cure corruption', tts=True)
                    #os.system('flite -voice slt -t "cure corruption"')
                
                # single player - use local tts
                DROG4CHAR = DROGA4 + CHARACTER
                if (DROG4CHAR) in line:
                    os.system('flite -voice slt -t "move away from raid and out of drogas line of sight"')
                
                # single player - use local tts
                DROG5CHAR = DROGA5 + CHARACTER
                if (DROG5CHAR) in line:
                    os.system('flite -voice slt -t "move out of drogas line of sight"')

                # single player - use local tts
                DROG6CHAR = DROGA6 + CHARACTER
                if (DROG6CHAR) in line:
                    os.system('flite -voice slt -t "you have the red ring. move away from the raid"')


                # Queen Velazul Di'zok - Chardok
                # multiplayer - send to discord
                if (VELAZUL1) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'move north into the tunnel', tts=True)
                    #os.system('flite -voice slt -t "move north into the tunnel"')

                # multiplayer - send to discord
                if (VELAZUL2) in line:
                    await client.send_message(discord.Object(id=GENERAL_ID), 'it is safe to return to the raid', tts=True)
                    #os.system('flite -voice slt -t "it is safe to return to the raid"')

                ##### END EoK RAIDS #####


                ##### START GENERAL UTILITY ALERTS #####
                
                # NOTE: These are for the user running the script, and will not be sent to the Discord channel

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
                
                ##### END GENERAL UTILITY ALERTS #####

            # end outer if

# run logfile loop
client.loop.create_task(logfile_loop())

# run the bot using the TOKEN defined in Config.py 
client.run(TOKEN)
