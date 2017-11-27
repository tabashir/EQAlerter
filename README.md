# EQAlerter 'The EverQuest Alerter System'
A Python based audio trigger alert system for EverQuest.  With Discord Bot support!

Author: Dr. Ronny Bull (A.K.A. Cubber on http://eqemultor.org)

Python Version: 3.5

Original Date: 11/12/2017

Last Revision: 11/27/2017

Purpose:  This program is intended to run on a Linux system running 'EverQuest' under 'Wine'.
          When running the program will parse your EverQuest chat log file for key phrases
          contained in the Config.py file and trigger alerts using the flite TTS engine.  

Dependencies: Python 3.5 and CMU Flite text to speech engine
	      Discord version requires discord.py library: 
              python3 -m pip install --user -U discord.py[voice]

IMPORTANT: Verify that your 'eqclient.ini' file contains the following line: LOG=TRUE, and that your game path is setup properly in Config.py.

# FAQ

Q. What Operating Systems does this program work on?

A. Currently EQAlerter is being developed on the Linux Operating System, however it is developed in the Python 3 programming language which is supported across most Operating Systems including Linux, Mac OS, and Windows. With a bit of tweaking it could easily be ported to Windows and Mac OS.


Q. Can I use this program to monitor multiple characters running on the same system?

A. Yes, just run a separate instance of the EQAlerter program for each character.


Q. Why did you develop this program in the first place?

A. In the current state of EverQuest many raiding guilds are REQUIRING the use of a utility called GINA (https://eq.gimasoft.com/gina/). While GINA is a great utility for Windows users, it is not supported on Linux due to its dependency on the .Net 4.0 framework. Also it is not Open Source.  EQAlerter is an attempt to create a cross platform log monitoring and alerting solution that has a small footprint and few dependencies.  The other limitation of GINA is that it requires sound files to be generated and installed on the system in order to be used with alerts.  EQAlerter uses the CMU Flite text to speech engine or a Discord Bot in order to generate SPOKEN alerts to the user and/or raid.


Q. Why are there two versions?

A. EQAlerter.py is the standalone version intended to be run in order to alert a single user during a supported raid event. It also provides alerting of failure of some basic utility functions like invisibility and feign death. EQAlerter-Discord.py is a fully functional Discord bot that provides the same functionality as the standalone version, and also pushes out alerts to a Discord server channel which will benefit an entire raid.


Q. Why are the flite TTS calls still in the Discord version?

A. This is to support the text to speech alerts to the user about their own character during the event that are not intended for the entire raid to here.


Q. Why can't I hear any TTS alerts on the Linux Discord client?

A. The Linux Discord binary does not support TTS at this time.  Windows users will still hear the alerts from your bot if they have TTS enabled in their Discord settings. If you want to use the Linux Discord binary then uncomment the flite TTS calls under each 'multiplayer' trigger in the EQAlerter-Discord.py file.  Or alternatively you can run Discord in Google Chrome on Linux and hear the TTS using the Google Assistant voice provided by the browser.


Q. Why is there not a Windows version available?

A. Because I use Linux and am a Linux developer, and I develop this in my limited spare time. I wrote the software in Python so that it could be easily forked and ported to Windows by anyone in the community. Please contact me if you wish to take this on.  Note that all of the flite TTS calls will have to be replaced with calls to the native Windows TTS engine.


Q. What raid events are supported by EQAlerter?

A. EQAlerter supports the following raid events: 

	- RoF(A Matter of Life and Death - Chapterhouse, Dispelling the Shadows - Plane of Shadow, Glimpse the Unseen - The Threshold, Ulrich the Ageless - The Threshold, Monarch Widow - The Threshold, 
		An End to Fear - The Epicenter)
	- CoF(Bixie Warfront: Pelzias Plot, The Dead Hills: Xulous Prime, Neriak - Fourth Gate: Houses of Thex, Neriak - Fourth Gate: Hate Rising, Tower of Rot: Lord Kyle Bayle, Argin-Hiz: Burn Out, 
		The Void (H): The Journey Home)
	- TDS(Defense of the City, Principal Quastori Numicia, Praetor Vitio, Principal Vicarum Nomia)
	- TBM( Plane of Hate: Revisited - Maestro of Rancor & Innorukk, Anashti Sul - Lady of Life, Wither and Decay, Grannus of the Cleansing Steam, Stem the Tide, Grummus!, High Bokon Boromas, 
		Anashti Sul - Enslaver of Souls)
	- EoK(Doorstep of War - Lceanium, The Summoning of Droga - Droga, Prince Selrach Dizok - Chardok, Queen Velazul Dizok - Chardok)
	- Anniversary(The Plane of War: 15th anniversary, 17th Anniversary raid - Hates Fury: Seventeen Pieces of Silver)


Q. What other triggers are supported?

A. All forms of invisibility dropping as well as feign death failures and breaks.


Q. What is GuildChat-Discord.py?

A. A stand-alone program created to relay guild chat messages from a character log file to a private guild chat channel on Discord.  
