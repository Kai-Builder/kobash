import os

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
        

