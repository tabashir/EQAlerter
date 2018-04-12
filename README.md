# EQAlerter 'The EverQuest Alerter System'
A Python based audio trigger alert system for EverQuest.  With Discord Bot support!

Author: Dr. Ronny Bull (A.K.A. Cubber on http://eqemultor.org)
        Extended by Jez McKinley (A.K.A. Tabashir on TAKP and P1999)

Python Version: 3.5

Original Date: 11/12/2017

Last Revision: 11/27/2017

Purpose:  This program is intended to run on a Linux system running 'EverQuest' under 'Wine'.
          When running the program will parse your EverQuest chat log file for key phrases
          contained in the Config.py file and trigger alerts using the flite TTS engine.
          Ideas from: http://everquest.fanra.info/wiki/Raid_audio_triggers

Dependencies: * Python 3.5 
              * CMU Flite text to speech engine for audio notifications
              * urxvt terminal emulator for visual notifications
              * Discord version requires discord.py library: 
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


Q. What is GuildChat-Discord.py?

A. A stand-alone program created to relay guild chat messages from a character log file to a private guild chat channel on Discord.  

# Additions by Jez

Most of the additional ideas came from here: http://www.icynic.com/~don/EQ/triggers/

Q. What other triggers are supported?

A. Current implemented list:

* All forms of invisibility dropping as well 
* Feign death failures and breaks.
* Spell worn off
* Root/Charm breaks
* Mez breaks

Q. What other features does it have?
A. Timers and Ignores

* Timers are so that you know when to refresh a spell, for example, Mez, Fascinate etc. On a mez landing, it will pop up a separate console window (currently set to urxvt) that will count down, then issue an audible warning and notification to refresh. 

* Ignores are so that you can get an alert on a class of events, but don't want a subset of them to alert you. For example, you want a tell from a player to notify, but don't want one when a vendor 'tells you that will be 10 plat'

Q. How do I add my own notifications?
A. All messages and notifications are editable in the actions.yml file. This should be fairly self explanatory.

An action is in the following format:

For all events:

* NAME: Just an identifier, but will need to be unique, othewise the last one in the file will prevail
* expect: This is the phrase to trigger the event. If you want it to only trigger with your character name, use the tag {CHARACTER} where you would expect to see it in the phrase.
* ignore: an array (inside []) of phrases that will mean you don't get a notification
* message: phrase for the speech and visual notification

For timed events:

* title: short title for the window
* time: the amount of time before the notification fires. These are set currently to 5 seconds less than the actual spell duration. Using urxvt allows the window to be minimised so that you get a nice countdown on your task bar in your window manager, other terminals may need tweaking here.


Examples:

```yaml
SHADOW4:
  expect: "aims a straight cut at {CHARACTER}"
  message: "Move out of range"

TELL:
  message: "Incoming Tell"
  expect: "tells you,"
  ignore: [
    "That'll be",
    "I'll give you",
  ]

MEZ:
  expect: "has been mesmerized"
  title: "Mezmerize"
  message: "Mesmerize warning"
  time: 19
```


TODO:
* Config override (so that it does not need checking in to git), likely getopts or similar
* Actions should have class structure
* Ability to configure whether an action is audio, visual or both from the config file
* Decent folder structure (src/test etc). This was Jez's first major python code and could not work out how to nicely load includes from other folders!
* Tests around the main script
* configure in config (not hard code) the terminal and window parameters for the delayed notification
* add optional character name into notification for use if running multiple instances
