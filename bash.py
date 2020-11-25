from datetime import datetime
from sub.linx import functions
op = datetime.now()
import os

path = os.getcwd()


print("Saved.")
while True:
    i = input(path + '> $ .. ')
    if i.strip() == functions.k_bash_Init:
        print('Creating __init__.py At' + path + "\init.py")
        a = open("init.py", 'w')
        a.write("# Development Kit.\n\n\n\nclass toolkit():\n\tdef UserScript():\n\t# You write here.")
        a.close()