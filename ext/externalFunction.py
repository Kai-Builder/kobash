class External():
    class Drive(): # Where Most shared Data Will be stored.
        def Store(var):
            a = open('code.py', 'w')
            a.write(var)
            a.close()
    e_help = 'ext $help'
    e_short = 'ext $short'
    e_Second = '$help$'
    e_secondShort = '$$off$$'
    e_Write_Library = 'ext WriteLib'
    e_write_second = '$sysWri$'
    e_Libary_View = '$std getlib'
    class extLib():
        def Here(ga):
            gathered = True
            whatToGather = ga