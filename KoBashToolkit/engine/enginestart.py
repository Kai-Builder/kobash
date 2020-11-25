class EngineCommand():
    E_Help = 'help'
    E_terminalStart = 'terminal -run'


class Engine():
    def StartScriptingEngine():
        Bash_Ready = True
        Bash_Help = EngineCommand.E_Help
        Bash_Execute = EngineCommand.E_terminalStart
        Bash_settings = '$cfg'
        
