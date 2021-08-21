from os import execl;
from sys import executable, argv;

def run() -> None:
    python = executable;
    execl(python, python, *argv);