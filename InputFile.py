import sys
import os
import argparse
import subprocess

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--task', '--choice', choices=['Quick', 'Merge', 'Split', 'Split10'], default='Split')
    return parser

try:
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.task == 'Quick':
        print("Quick")
        #subprocess.call(["Laba1.py", "CheckNumbs.txt"], stdout="OutPut.txt")
    elif namespace.task == 'Merge':
        print("Merge")
    elif namespace.task == 'Split':
        print("Split")
    else:
        print("Split10")
except:
    print("Wrong choice")