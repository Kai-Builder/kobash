from datetime import datetime
from time import process_time_ns
from sudok.linx import *
import time
import sys
import random
from Handler import *
sys.version
op = datetime.now()
import os
from pathlib import Path
g = ['h', 'e', 'l', 'p']
path = os.getcwd()

bqui = ['What did you do today?', 'What could you do better?', 'Name Every Sport.', 'have you tried sudok?', 'This Bash Is Used as a Fast little terminal project i made.']
a = Path("UserLogin.py")
if a.exists():
    from UserLogin import *
    print('FOR LOGGED IN USERS')
    print('FROM 11/26 TO 11/30 NO MORE VERSIONS WILL BE UPDATED AND SUPPORT WILL END UNTIL AFTER.')
    print('THE REASON IS THAT I NEED TO UPDATE THE LOGIN SYSTEM AND THE WAY DATA IS EXCHANGED. THANKS!')
    time.sleep(1)
    u = Path("operion.kb")
    if u.exists():
        print('Running Operion 1.23.0')
    i = Path("pygo.kobash")
    if i.exists():
        print('PyGo Powered By ScriptLib 1.03')
    print('full info in either DOCS >> Support >> supportIssues OR say loginIssues')
    print('-------------------------------------------------------')
    print('Hello, ' + user + ". How are you?")
else:
    print('You Have Not signed into An account yet. This Copy Is Unliscenced.')
    print('You can make one by saying signup')
while True:
    i = input(path + '\session> $ .. ')
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
        o = Path("operion.kb")
        if o.exists():
            print('REQUIREMENT ALREADY SATISFIED')
            time.sleep(1)
            print(path + "\.scripts\PYGO\pygo-init Already Exists")
            print(path + "\.scripts\PYGO\pygo Already Exists")
            print(path + "\.scripts\PYGO\pygo\lib Already Exists")
            print(path + "\.scripts\PYGO\pygo\lib Already Exists")
            print(path + "\.scripts\PYGO\pygo\dlHosting\C\LibraryData.py Already Exists")
            time.sleep(3)
            print('Failed Installation.')
        else:
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
            a = open('operion.kb', "w")
            a.write("Gathered Data")
            a.close()
            time.sleep(random.randint(5,10))
            print('Operion directory Created.')
            time.sleep(random.randint(5,10))
            print('Polishing Files..')
            time.sleep(random.randint(5,10))
    elif i.strip() == OperionSetup.Oper_helpCmd:
        a = Path("operion.kb")
        if a.exists():
            print('op __crust__ -- Creates a Struct based on User input')
            print('op devConsole --InPrompt -- Integrated Shell Inside KoBash.')
            print('op help info -- Build info.')
        else:
            print('op is not recognized as a .bashExtension File.')
    elif i.strip() == 'signup':
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
        A = open('pygo.kobash', 'w')
        A.write("Pygo.scriptable == True")
        A.close()


    elif i.strip() == PyGo.pygo_test:
        u = Path("PygO.kobash")
        if u.exists():
            print('Thank you for installing pygo.')

    elif i.strip() == 'sudok alternative':
        print('Sudok-Like Extensions (to Sign up go to DOC_2.html.)')
        print("1. Pygo -- " + str(PyGo.pygo_Description) + "")
        print('2. Operion -- ' + str(OperionSetup.oper_Description))
        print('3. ToolKitBash -- ' + str(ToolKitLib.ext.ToolKit_Desc))
        # Linter Lib Section
    elif i.strip() == linterLib.Help.lint_helpcmd1:
        print('Incoming Interference to KOBASH, \nMESSAGE: Did you mean, "help" ?\n\nHOSTNAME: LintLib 1.0v')
    elif i.strip() == linterLib.Help.lint_helpcmd2:
        print('Incoming Interference to KOBASH, \nMESSAGE: Did you mean, "help" ?\n\nHOSTNAME: LintLib 1.0v')
    elif i.strip() == linterLib.Help.lint_help3:
        print('Incoming Interference to KOBASH, \nMESSAGE: Did you mean, "help" ?\n\nHOSTNAME: LintLib 1.0v')
    elif i.strip() == linterLib.Help.lint_help4:
        print('Incoming Interference to KOBASH, \nMESSAGE: Did you mean, "help" ?\n\nHOSTNAME: LintLib 1.0v')
    elif i.strip() == linterLib.Help.lint_help5:
        print('Incoming Interference to KOBASH, \nMESSAGE: Did you mean, "help" ?\n\nHOSTNAME: LintLib 1.0v')
    elif i.strip() == linterLib.Help.lint_help6:
        print('Incoming Interference to KOBASH, \nMESSAGE: Did you mean, "help" ?\n\nHOSTNAME: LintLib 1.0v')
    elif i.strip() == linterLib.Help.lint_help7:
        print('Incoming Interference to KOBASH, \nMESSAGE: Did you mean, "help" ?\n\nHOSTNAME: LintLib 1.0v')
    elif i.strip() == linterLib.Help.lint_help8:
        print('Incoming Interference to KOBASH, \nMESSAGE: Did you mean, "help" ?\n\nHOSTNAME: LintLib 1.0v')
    elif i.strip() == linterLib.Help.lint_help9:
        print('Incoming Interference to KOBASH, \nMESSAGE: Did you mean, "help" ?\n\nHOSTNAME: LintLib 1.0v')
    elif i.strip() == g:
        print('Did you Mean help?')

    elif i.strip() == '':
        print('Nothing.')
    elif i.strip() == OperionSetup.Oper_crouton:
        print('Unloading Console Scripts...')
        time.sleep(random.randint(1, 10))
        print('Operion Library ppsc')
        time.sleep(random.randint(1, 10))
        print('toolkit library KoBash')
        time.sleep(random.randint(1, 10))
        print("Starting Python..")
        time.sleep(random.randint(1, 16))
        print('Operion Console 1.0.')
        print('For Help say')
        print('opc help')
        while True:
            a = input(path + "\OperionLib\Scripts\OPERION_1.332.334.5.3.f.2020> ")
            if a.strip() == 'opc help':
                print('Operion Lib 1.0')
                print('op __path__')
            elif a.strip() == 'op __path__':
                print('path to?')
                filetopath = input('> {')
    elif i.strip() == 'opc':
        print("Operion Console. Made For Kobash 1.3")
        while True:
            a = input(path + "\OperionLib\Scripts\OPERION_1.332.334.5.3.f.2020> ")
            if a.strip() == 'opc help':
                print('Operion Lib 1.0')
                print('op __path__')
            elif a.strip() == 'op __path__':
                print('path to?')
                filetopath = input('> {')
    elif i.strip() == ChatBotClient.chatbot_install:
        print('Using PyGo Install Client Version 0.45.0')
        time.sleep(5)
        print(path + "\chatbot\.pygoinstaller\scripts Has Been Installed.")
        time.sleep(random.randint(0, 12))
        print(path + "\.pygo\Libary Has Been Installed")
        time.sleep(random.randint(0, 12))
        print(path + "\msf\script\chatbotclient.exe Has Been installed")
        time.sleep(random.randint(0, 12))
        u  = open('dclient.KoRunTime', 'w')
        u.write('keepClient = true;\nClientRuntime = true;\nfor socket in client;\n\tNETQUIRE.Tree.Scripts.Main(arg[], str, scrt-())')
        u.close()
        print(path + "\dclient Has Been Installed.")
        time.sleep(random.randint(0, 12))
        print('ChatBot1._3._4323 Successfully Installed.')
        time.sleep(random.randint(0, 12))

    elif i.strip() == ChatBotClient.chatbot_initializeCommand:
        o = Path("dclient.KoRunTime")
        if o.exists():
            print('Starting KoBash Chatbot runtime..')
            time.sleep(3)
            while True:
                ch = input(path + "> -- .. ")
                if ch.strip() == ChatBot_Understnding.cht_Hello:
                    print(ChatBot_Responses.HelloResponse)
                elif ch.strip() == ChatBot_Understnding.cht_help:
                    print(ChatBot_Responses.helpRep)
                elif ch.strip() == ChatBot_Understnding.cht_why:
                    print(ChatBot_Responses.whRep)
                elif ch.strip() == ChatBot_Understnding.cht_Who:
                    print(ChatBot_Responses.wRep)
        else:
            print('KoBash Runtime Not installed.')
    elif i.strip() == 'userdata':
        y = Path("UserLogin.py")
        if y.exists():
            print('User.Username = ' + user)
            print('User.Password = ' + passw)
        else:
            print('You cannot use the userdata command without a liscense.')

    elif i.strip() == MyLib.kr_install:
        MyLibFunctions.OnInstall() 
    else:
        print(i + ' is not recognized as a cmd, .kb, External File, Or Operable Program.')
