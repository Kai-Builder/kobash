from pathlib import Path
class MainPanel(object):
    def __init__(inputmethod, dosomething):
        a = input('$ { ')
        if a == inputmethod:
            print(dosomething)
    def __attributes__(attr, removeCache: bool):
        if removeCache == True:
            a = Path("__pycache__")
            if a.exists():
                a.rename("Not Cache")


