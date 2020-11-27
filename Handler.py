class MyLib():
    kr_install = 'sudok install MyLib'
    kr_myFunction = 'MyLib help'
    kr_quit = 'MyLib quit'



class MyLibFunctions():
    def OnInstall():
        print('Alright installing')
        print('Using ScriptLib 1.0.0') # Give some info on the installing process here!
        print('Foo') # This is where you Make a .kobash File.
        x = open('MyLib.kobash', 'w')
        x.write('MyLib.Scriptable = true;')
        x.close()
        print('Cree')
       	print('Done!')