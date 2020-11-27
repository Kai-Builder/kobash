from KoBashToolkit.sharedtoolkits.buildTools.cus import *
from addons.KoBashToolKit.toolkitscripts import *
from addons.operion.OperionLib import *
from addons.PyGo.pygo_class import * # Functions Is not The Functions we will be using
import time


time.sleep(3) # Pause and let user read PYGO start message.
BuildTools.NewPlugin() # addon.json
BuildTools.LoadingSequence(1) # One Is the Default Message. Will Fallbackw If no number specified. Supported integers, 1,2,3,4,5.
BuildTools.EnCryp() # Safely Create Addon.

