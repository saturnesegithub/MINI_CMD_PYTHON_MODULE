def addusers(user):
    userlist = []
    userlist.append(user)
def choice(prompt):
    prompt = ""
    prompt = input()
def cipher(prompt):
    binary_text = ''.join(format(ord(char), '08b') for char in prompt)
    return binary_text
def date():
    import time
    calendar = time.strftime("%Y-%m-%d")
    print(calendar)
def exit():
    import sys
    sys.exit()
def hostname():
    import sys
    print(sys.platform)
def logoff():
    import sys
    sys.exit
def msg(prompt = ""):
    prompt = input()
    print("msg: " + prompt)
def msinfo32():
    import sys
    print(sys.version)
def now():
    import time
    print(time.localtime())
def pause(paused):
    import time
    time.sleep(paused)
def rcp(listname,copylist):
    copylist.extend(listname)
def sleep(sleep_time):
    import time
    time.sleep(sleep_time)
def t
    import sys
    print(sys.path)
def xcopy():
    import sys
    xcopy_data = [sys.path]
def run_calc():
    evaluate = input()
    print(int(eval(evaluate)))
def run_cmd():
    print("CMDCEPTION!")
def delt(name):
    import os
    os.remove(name)
def find(listname,listelement):
    if listelement in listname:
        print("True")
    else:
        print("False")
def systeminfo_plus():
    import platform
    print(platform.platform())