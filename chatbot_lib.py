from pathlib import Path


u = Path("UserLogin.py")
if u.exists():
    from UserLogin import *

class ChatBot_Understnding():
    cht_Hello = 'hello'
    cht_help = 'help me'
    cht_socials = 'what are your social pages'
    cht_Who = 'who made you'
    cht_why = 'why were you made'
    cht_else = 'do you say anything else'
    cht_what = 'what do you do'

class Chatbot_UserDefinitions():
    myRep = 'i am a custom sentence'





class ChatBot_Responses():
    u = Path("UserLogin.py")
    if u.exists():
        HelloResponse = "Hi. " + user
    else:
        HelloResponse = "Hello."
    helpRep = 'So, Talk to me like you\'d talk to anybody else. You could ask me about Updates, Information About the creator, And More!'
    sociRep = 'I Don\'t Really have any socials... But you could mentally Follow me!'
    wRep = 'I Was created by Kai-Builder, And Another dude named Kai-Builder. Haha!'
    whRep = 'I Was made because I Felt People needed  Help With using the prompt. '
    elRep = 'Yeah. There are also Extensions for me. You could find out more By Going to DOCS >> Addons >> Chatbot >> Help'

