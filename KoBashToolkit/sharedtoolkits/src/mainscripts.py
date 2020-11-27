class PluginManager():
    class PluginWizard():
        def StartWizard(mes, args, kwargs, ext, a, requireExt: bool):
            if requireExt == False:
                print('KoBash Extension Setup Wizard for ' + mes)
                print('To Install ' + mes + " Say " + args + ".")
                print('You can Also Install it with ' + kwargs)
                print('This Prompt Can Take ' + a + " To Complete")
            else:
                print('KoBash Extension Setup Wizard for ' + mes)
                print('To Install ' + mes + " Say " + args + ".")
                print('You can Also Install it with ' + kwargs)
                print('There are some extra Modules that require this one you can install with ' + ext)
                print('This Prompt Can Take ' + a + " To Complete")
        def OnWizardError(errortype, gen):
            if errortype == 'Crash':
                raise LookupError
            if errortype == 'Import Error':
                raise ImportError
            
            """
            Generates WizardError.
            """
            
