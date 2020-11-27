from datetime import datetime
from sudok.linx import *
import time
import sys
import random
sys.version
op = datetime.now()
import os
from pathlib import Path

path = os.getcwd()

bqui = ['What did you do today?', 'What could you do better?', 'Name Every Sport.', 'have you tried sudok?', 'This Bash Is Used as a Fast little terminal project i made.']
a = Path("UserLogin.py")
if a.exists():
    from UserLogin import *
    print('Hello, ' + user + ". ")
else:
    print('You Have Not signed into An account yet. This Copy Is Unliscenced.')
    print('You can make one by saying login.')
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
        a = Path("UserLogin.py")
        if a.exists():
            from UserLogin import *
            print('You Must Log In With Your Correct UserName And Password Before Proceeding.')
            x = input('.. ')
            y = input('.. ')
            if x == user and y == passw:
                print('Successfully Logged Into Influx Mode. Restarting')
                print("Recreating Influx..")
                time.sleep(3)
                print('Data Logging..')
                time.sleep(5)
                print("ReBuilding...")
                print("(Rebuilding can take up to a minute or two, so in the meantime)")
                print(random.choice(bqui))
                time.sleep(random.randint(0,120))
                print('All Scripts Have Been ReLoaded With Exit Code -1')
            else:
                print("Invalid UserName. Quitting Influx..")
        else:
            print('Unliscenced Copy. Quitting Influx.')
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
        a = open('Operion 1.230.0.bashExtension', "w")
        a.write("Gathered Data")
        a.close()
        time.sleep(random.randint(5,10))
        print('Operion directory Created.')
        time.sleep(random.randint(5,10))
        print('Polishing Files..')
        time.sleep(random.randint(5,10))
    elif i.strip() == OperionSetup.Oper_helpCmd:
        a = Path("Operion 1.230.0.bashExtension")
        if a.exists():
            print('op __crust__ -- Creates a Struct based on User input')
            print('op devConsole --InPrompt -- Integrated Shell Inside KoBash.')
            print('op help info -- Build info.')
        else:
            print('op is not recognized as a .bashExtension File.')

    elif i.strip() == OperionSetup.Oper_crouton:
        print('Integrated Shell 1.0.\nMade For Kobash.')
        while True:
            o = input('$ { ')
            if o.strip() == OperionSetup.Oper_helpCmd:
                print('**back -- Prints Back What user Says After execution.\n&echostart -- Startup Message.')
    elif i.strip() == 'login':
        x = input('Choose a username: ')
        y = input('Choose a password: ')
        print('Logging you in...')
        time.sleep(random.randint(0,20))
        print('Thank You For Signing into KoBash.')
        a = open('UserLogin.py', 'w')
        a.write('user = "' + x + '"\npassw = "' + y + '"')
        a.close()
    elif i.strip() == '{.bashExtension execute --Program5':
        i = input('.. ')
        a = Path(i)
        if a.exists():
            print('Loading User Defined Scripts..')
            time.sleep(random.randint(1,20))
            print('')
    elif i.strip() == PyGo.pygo_install:
        print('Gathering Pygo..')
        time.sleep(4)
        print('Tasks')
        print('1. Build PyGo')
        print('2. Define Pygo ScriptPATH')
        time.sleep(6)
        print('PYGO.DATA')
        time.sleep(random.randint(3, 4))
        print('PYG.LIB')
        time.sleep(random.randint(1, 9))
        print("ScriptLib.h")
        time.sleep(random.randint(1, 3))
        print('Letters.')
        time.sleep(random.randint(2, 4))
        time.sleep(random.randint(3, 9))
        print('Finished.')
        print('Defining ScriptPath..')
        time.sleep(random.randint(4, 13))
        print('Finished!')
        A = open('PygO.kobash', 'w')
        A.write("Pygo.scriptable == True")
        A.close()


    elif i.strip() == PyGo.pygo_test:
        u = Path("PygO.kobash")
        if u.exists():
            print('Thank you for installing pygo.')
        else:
             print(i + ' is not recognized as a cmd, .bashExtension, External File, .kobash, Or Operable Program.')
    else:
        print(i + ' is not recognized as a cmd, .bashExtension, External File, Or Operable Program.')
