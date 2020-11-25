from datetime import datetime
from sub.linx import *
from checkers.easycompil import *
import time
import sys
import random
sys.version
op = datetime.now()
import os
from pathlib import Path

path = os.getcwd()

bqui = ['What did you do today?', 'What could you do better?', 'Name Every Sport.', 'have you tried sudok?', 'This Bash Is Used as a Fast little terminal project i made.']

print("Saved.")
while True:
    i = input(path + '\private> $ .. ')
    if i.strip() == functions.k_bash_Init:
        print('Creating __init__.py At' + path + "\init.py")
        a = open("init.py", 'w')
        a.write("# Development Kit.\n\n\n\nclass toolkit():\n\tdef UserScript():\n\t# You write here.")
        a.close()
    elif i.strip() == functions.k_bash_Scripts:
        a = Path("scrit.py")
        if a.exists():
            print("You currently Have a script made already.")
        else:
            print("You do not have any sudok scripts installed.")
            print("Would You like to install some? {y/n}")
            s = input("$ .. ")
            if s.strip() == 'y':
                print('Downloading Required dependencies for script creation...')
                time.sleep(5)
                print('Compiling Import Files used for Script creation..')
                time.sleep(3)
                print('CommonError #23: ScriptPath Cannot be inside a folder.')
                time.sleep(1)
                print('Loading..')
                time.sleep(3)
                print('Finalizing..')
                time.sleep(5)
                print('Adding Extra..')
                time.sleep(2)
                print('Finished! Retry this by saying sudok scripts')
    elif i.strip() == functions.k_Influx:
        print("Recreating Influx..")
        time.sleep(3)
        print('Data Logging..')
        time.sleep(5)
        print("ReBuilding...")
        print("(Rebuilding can take up to a minute or two, so in the meantime)")
        print(random.choice(bqui))
        time.sleep(random.randint(0,120))
        print('All Scripts Have Been ReLoaded With Exit Code -1')
    elif i.strip() == functions.k_Path + " hidden":
        print('Successfully Pathed to' + path + "\.hidden")
    elif i.strip() == functions.k_scrap_write:
        fn = input('.. ')
        con = input(".. ")
        a = open(fn, "w")
        a.write(con)
        a.close
        print("Wrote " + con + " in " + fn + ".")
    elif i.strip() == 'sudok':
        print('Sudok v1.0.0')
        print('[sudok scrap write] -- Writes a file with user contents.')
        print('[sudok __init__] -- Creates an Init.py File With Preset Assets and definitions..')
        print('[sudok Function.]')
        print('[sudok path ext] -- Paths to the "External" Libary')
        print('[sudok --influxonly +1] -- Only Refreshes the sudok functions only.')
        print('[crout updt sudok] -- Updates Sudok.')
        print('Every functionality starts with SUDOK')
    elif i.strip() == functions.k_help:
        print('"sudok" -- sudok Libary\n"cppLib" -- Reach out to the C++ Library.\n-------WHERE ALL THE STUFF IS AT---------------\n\nsudok -- Integrated Libary with utils and devkit built in')
    elif i.strip() == OperionSetup.Oper_Install:
        print('gathering operion..')
        time.sleep(random.randint(0,10))
        print('Local Tasks:')
        print('1. Install Libaries Required For Operion')
        print('2. Install Operion 1.23 Directory')
        print('3. Polish Final Files And Finish Config.')
        time.sleep(random.randint(1,10))
        print('Installing Proper Libraries...')
        time.sleep(random.randint(5,15))
        print('RandomLib')
        time.sleep(random.randint(2,10))
        print('scriptLib')
        time.sleep(random.randint(5,15))
        print('UnixForPython1.2.49')
        time.sleep(random.randint(5,15))
        print('GetLibSearch')
        time.sleep(random.randint(5,10))
        print('Tasks:')
        print('1. Install Operion Library')
        print('2. polish')
        time.sleep(3)
        print('Installing Operion Dir..')
        time.sleep(random.randint(5,10))
        os.mkdir("Operion 1.230.0")
        time.sleep(random.randint(5,10))
        print('Operion directory Created.')
        time.sleep(random.randint(5,10))
        print('Polishing Files..')
        time.sleep(random.randint(5,10))
    elif i.strip() == OperionSetup.Oper_helpCmd:
        a = Path("Operion 1.230.0")
        if a.exists():
            print('op __crust__ -- Creates a Str')