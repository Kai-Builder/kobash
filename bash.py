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
        print('"sudok" -- sudok Libary\n"cppLib" -- Reach out to the C++ Library.')
        print()