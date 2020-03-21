#!/usr/bin/env python
#
#
#    Thomas "Mr Men" Etcheverria
#    <tetcheve (at) gmail .com>
#
#    Created on : 21-03-2020 15:24:16
#    Time-stamp: <21-03-2020 17:05:42>
#
#    File name : /tmp/pys.py
#    Description :
#
import re
import os
DEBUG=0
if DEBUG==1:
    dbg=print
else:
    dbg = (lambda x,y : 1)


def seds(p1, p2, text, occur="g"):
    '''Similar sed s function'''
    try:
        f = open(text, "r")
        content = f.readlines()
        f.close()
    except:
        content = [text]
        text+" is not a file"        
    output = []
    for element in content:
        if occur != "g" and type(occur)==type(1):
            output.append(re.sub(p1, p2, element, occur))
        else:
            output.append(re.sub(p1, p2, element))            
    return "".join(output)

def sedd(p, text, t="!"):
    '''Similar sed d function'''
    try:
        re.compile(p)
    except re.error:
        print("{} is not a valid regexp".format(p))
    try:
        f = open(text, "r")
        content = f.readlines()
        f.close()
    except:
        content = [text]
        text+" is not a file"        
    output = []
    for element in content:
        if t=="!" and not(re.search(p, element)):
            output.append(element)
        elif t!="!" and re.search(p, element):
            output.append(element)
    return "".join(output)

def parseArgs(args):
    args = args.replace(" | ", "æ")
    actions = args.split("æ")
    argsOut = []
    for action in actions:
        argsOut.append(action.split("/"))
    return argsOut

def sed(args, text):
    liste = parseArgs(args)
    out = text
    for element in liste:
        dbg(element, out)
        action = element[0]
        if action == "s":
            if len(element) == 3:
                out = seds(*element[1:], out)
            elif len(element) == 4:
                out = seds(*element[1:-1], out, element[-1])
        elif action == "d":
            if len(element) == 2:
                out = sedd(element[1], out)
            elif len(element) == 4:
                out = sedd(element[1], out, element[-1])
        else:
            return "Error on {}".format(element)
    return out

def Tests():
    tests = [
        ["sed 's/ouu\+/@/g' ouiouiouuui", seds("ouu+", "@", "ouiouiouuui"), "ouioui@i"],
        ["sed 's/ou/@/1' ouiouiouuui", seds("ou", "@", "ouiouiouuui",1), "@iouiouuui"],
        ["sed '/ouu/d' ouiouiouuui", sedd("ouu", "ouiouiouuui"), ""],
        ["sed '/ouu/d' ouiouiouuui", sedd("ouu", "ouiouiouuui", ""), "ouiouiouuui"],
        ["sed 's/a+/o/g, s/o++/_/g, /unt/!d", sed('s/a+/o | s/oo+/_ | d/unt/', "sauaaoaunt"), "sou_unt"]
    ]
    for t in tests:
        if t[1] == t[2]:
            print("[\u2713] Testing : {}".format(t[0]))
        else:
            print("[ ] Testing : {}".format(t[0]))
            print("\t getting {} instead of {}".format(t[1],t[2]))

def usage():
    print('''pysed : a naive sed like python module
    
s et d operator are implemented naively for small changes.

Examples :
    sed 's/ouu\+/@/g' ouiouiouuui       seds("ouu+", "@", "ouiouiouuui")
    sed 's/ou/@/1' ouiouiouuui          seds("ou", "@", "ouiouiouuui",1)
    sed '/ouu/d' ouiouiouuui            sedd("ouu", "ouiouiouuui"), ""]
    sed '/ouu/d' ouiouiouuui            sedd("ouu", "ouiouiouuui", "")
    sed 's/a+/o/g, s/o++/_/g, /unt/!d"  sed('s/a+/o | s/oo+/_ | d/unt/', "sauaaoaunt")

''')
            
if __name__ == "__main__":
    Tests()

