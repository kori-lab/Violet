from os import execl
from sys import executable, argv

def run():
    python = executable;
    execl(python, python, *argv);