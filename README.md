# KoBash. The Highly Extensible Prompt Used For General Purposes.

There is Much to love about The General Windows Command Prompt, Like the fact that you can add custom commands, Custom scripts, and much more. But have you heard of a command prompt that uses Features that are completely Customizable to the User Range? Exactly.





# Open Source Project

The KoBash Is Not What you think it is, It Has The Features of Linux Except it has the ability to Create its own scripts, Packages, languages, And Much, Much More.

KoBash Is A Open-Source Project On My [github](https://github.com/Kai-Builder/kobash) Which Means Anybody Can Contribute to the Cause.

If you Are Reading this Html, I Am Guessing You Have already Setup the prompt (very simple) Once you Have,  Double click the .exe file and you are good to go!

# Initial Procedures

- Make sure you have any version of python installed
- Make sure you have a good IDE. Pycharm Works.
- Make Sure to make a handler.py and import **buildtools** For Engine Access.
- Make sure to use the Plugin Wizard to setup installation.

# The Hard Part 1.0

Now you're Getting there, Open Handler.py And Write,

```python
from KoBashToolkit.sharedtoolkits.buildTools.cus import *
```

After that write,

```python
BuildTools.NewPlugin()
```

After That, Run the code.

There should be a **Json** File That Creates. Open it up and change it to your liking.



Now All you need to do is Start Scripting! Here Are some sample Libraries For you.



## Samples

- sudok
- ScriptLib
- KoBashToolKit
- operion




# Current Version Patch Notes
- Fixed Bugs 
- LintLib
- Now When you type '' it doesn't Do the error message.
- Finally Polished Addon Building! 
- Updated Integrated Libaries, PyGo, Operion, KoBashToolKit.
# API REFERENCE

- sudok -- `sudok` is the main Module Used for importing, Installing, Building, And using the terminal.
- sudox -- `Sudox` Uses The Sudok Module And Makes it into a portable socket module.
- Operion -- `Operion` Is Being Developed by one of the developers of KoBash.
- BuildTools -- `BuildTools` Is a Module Used for Developing Extensions.
- org -- The `org` Module Contains All Framework-Based Objects Made for Bigger Prompt Extensions.
- sub.linx -- The `linx` Module Contains all functionalities for the Commands!
- KoBashToolKit.engine -- The `Engine` Module is used By the scripting engine for Main Script.
# News
- FROM 11/26 TO 11/30 THERE WILL BE MATINENCE UPDATES MEANING NO MORE VERSIONS. 
- THERE WILL BE MULTIPLE CHANGES TO THE WAY USERS LOG IN, THE WAY INFO IS STORED, AND MORE.
