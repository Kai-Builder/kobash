import os
from pathlib import Path
import time
import random
class BuildTools():
    def NewPlugin():
        a = open('plugin.json', "w")
        a.write('{\n\n\t"MyAddonName": "TestName",\n\t"LocalDependencies": "KoBashToolkit.engine.enginestart"\n}')
        a.close()
    def IDE(ide):
        """
        Determines Config Based On IDE Type.
        """
        if ide == 'vscode':
            a = open('vs.js', 'w')
            a.write('const vs;')
            a.close()
            n = open('Addon.json', 'w')
            n.write('{\n\n\t"Launch.NetConfig": "--launch"\n}')
            n.close()
    def StartFiles():
        i = open('MyPlugin.py', "w")
        i.write('from KoBashToolkit.sharedtoolkits.cus import BuildTools as Build\n\n\ndef Plugin():\n\tBuild.IDE("vscode") # Change to what you want\n\tBuild.NewPlugin()')
        i.close()
    def EnCryp():
        os.mkdir(".Net Encryption")
        print("Encrypting addon Files..")
        time.sleep(3)
        print('Started NET Encryption')
        print('Encrypted addon Data.')
    def LoadingSequence(type: int):
        if type == 1:
            print('Loading Scripts..')
            time.sleep(random.randint(0, 10))
            print('Gathering addon.json...')
            time.sleep(random.randint(0, 10))
            print('Starting Python Lib..')
            time.sleep(random.randint(0, 10))
            print('Installed Successfully')



class Prompt():
    def require(module):
        a = Path(str(module) + ".kobash")
