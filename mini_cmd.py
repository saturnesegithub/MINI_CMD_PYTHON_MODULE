import time

import sys

import os

import subprocess

import platform

###########CODE##############

def addusers(user):

    userlist = []

    userlist.append(user)

    return userlist

def choice(prompt):

    prompt = ""

    prompt = input()

def cipher(prompt):

    binary_text = ''.join(format(ord(char), '08b') for char in prompt)

    return binary_text

def date():

    calendar = time.strftime("%Y-%m-%d")

    print(calendar)

def exit():

    sys.exit()

def hostname():

    print(sys.platform)

def logoff():

    sys.exit

def msg(prompt = ""):

    prompt = input()

    print("msg: " + prompt)

def msinfo32():

    print(sys.version)

def now():

    print(time.localtime())

def pause(paused):

    time.sleep(paused)

def rcp(listname,copylist):

    return copylist.extend(listname)

def sleep(sleep_time):

    time.sleep(sleep_time)

def tree():

    print(sys.path)

def xcopy():

    xcopy_data = [sys.path]

def run_calc():

    evaluate = input()

    print(int(literal_eval(evaluate)))

def run_cmd(input):

    subprocess.run(input)

def delt(name):

    os.remove(name)

def find(listname,listelement):

    if listelement in listname:

        print("True")

    else:

        print("False")

def systeminfo_plus():

    print(platform.platform())

def dir():

    return os.listdir()

    file_list = dir()

    return file_list
