from os import scandir


class functions():
    k_help = 'help'
    k_bash_Scripts = 'sudok scripts'
    k_bash_Init = 'sudok __init__'
    k_scrap_write = 'sudok scrap write'
    k_scrap_create = 'sudok scrap create'
    k_Influx = '~influx'
    k_Path = 'cd sub'
    k_Path_foreign = 'cd ForeignPath'
    startPath = '~~ change startpath'
    reach = '$sys reach'

class sudokLib():
    s_secConsole = 'sudok ~console~'
    s_sodium = 'sudok sodium'
    s_killTer = 'sudok KillProcess'
    s_Switch = 'sudok cpp'
    s_graph = 'sudok graph', 'sudok diag'
    s_Keepover = 'sudok KeepHere'

class OperionSetup():
    Oper_Install = 'sudok install operion'
    Oper_helpCmd = 'op help'
    Oper_crust = 'op __crust__'
    Oper_crouton = 'op devConsole --InPrompt'
    Oper_info = 'op help Info'
    oper_DisplayName = 'Operion Lib. -- 1.0'
    oper_Description = 'Operion Library Contains Easier Prompt Source Access'

class PyGo():
    pygo_install = 'sudok install PyGo'
    pygo_test = 'pygo __test__' # Test If PyGo Works.
    pygo_help = 'pygo _manual_'
    pygo_Description = 'PyGo Is a library For Kobash That contains A Better Integrated terminal, Easier BashExtension, And PreBuilt Functions.'
    pygo_DisplayName = 'PYGO -- 1.1.334.f.04.2020'
    class PyGO_IntTerm():
        int_help = 'help'
        int_printback = '**back'
        int_EnableMessageOnStart = '&echoStart'
    class LocalDependencies():
        class Modules():
            k_First = 'ModuleType'



class ToolKitLib():
    class functions():
        init = '__strt__'
        func_installer = 'TK install'
        func_ExternalTerm = 'tk externalterm'

    class Scripts():
        def Install():
            print('To install type sudok install toolkit')
    class ext():
        ToolKit_Desc = 'lightweight toolkit made for Extension Building'
        ToolKit_Display = 'TK-Tools'
    class InstallerLib():
        class MyMod():
            def Create():
                y = open('Addon.json', 'w')
                y.write('{\n\n\t"Script": true,\n\t"Args": "--add"\n}')
                y.close()