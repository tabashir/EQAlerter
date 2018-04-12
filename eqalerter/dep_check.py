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
import sys
import os
import platform

from os.path import isfile

from config import *

# DepCheck - verifies dependencies are met prior to running
#            also contains a method to validate users
class DepCheck:

    def __init__(self):
        print("DEBUG: Checking dependencies")


    # verify the plaftform is Linux
    def verifyOS():
        if platform.system() != 'Linux':
            print("Here is a nickle, go get yourself a real Operating System kid!")
            print("")
            print("Note: This application only works on Linux due to the CMU flite TTS engine dependency.")
            sys.exit()

    # verify that CMU flite TTS engine is installed
    def verifyFlite():
        print("DEBUG: flite install path:")
        if subprocess.call(["which", "flite"]) == 1:
            print("")
            print("ERROR: flite is either not installed on the system or not in your path. Please install it via your distro's package manager or from source and add it to your path")
            sys.exit()
        print("")

    # verify that URXVT Terminal emulator is installed
    def verifyUrxvt():
        print("DEBUG: urxvt install path:")
        if subprocess.call(["which", "urxvt"]) == 1:
            print("")
            print("ERROR: urxvt is either not installed on the system or not in your path. Please install it via your distro's package manager or from source and add it to your path")
            sys.exit()
        print("")


    # verify that LOG=TRUE in eqclient.ini
    def verifyLogging(eqhome):
        # open eqclient.ini for reading
        # search the file for LOG=TRUE
        # if not found error out
        # else proceed on
        if 'Log=TRUE' in open(eqhome+"eqclient.ini").read():
            print("DEBUG: Logging is enabled")
        else:
            print("ERROR: Please enable logging in your 'eqclient.ini' file by setting Log=TRUE")
            sys.exit()

    # check for character log file
    def getLogFile(eqhome, character, logpath):
        logfile = DepCheck.pathScan(eqhome, logpath)
        if logfile:
            print("\n\nMonitoring [%s] using the following log file: %s \n" % (character, logfile))
            return logfile
        else:
            print("\n\nERROR: No chat log file exists for the selected character.\n")
            print("Please verify that 'Log=TRUE' in 'eqclient.ini',\n")
            print("then log the character into the game and re-run this utility.\n")
            sys.exit()

    def pathScan(base_folder, filename):
        if os.path.isfile(base_folder+filename):
            return base_folder+filename
        if os.path.isfile(base_folder + "Logs/" + filename):
            return base_folder + "Logs/" + filename
        return

#End of Class
