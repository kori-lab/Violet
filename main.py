from src.utils.functions.clear import *
from src.events.ready import *;
from src.utils.functions.selfInput import *;
import os
CommandsList = start("./src/commands");

def printLogo():
    ref_arquivo = open("logo.txt","r")

    print('\033[1;31m'+ ref_arquivo.read() +'\033[0;0m\n')

    ref_arquivo.close()

def formatMessage():
    message = ''
    i = 0
    for command in CommandsList:
        command = command['name']
        message += f'\033[1;91m[\033[0;0m{i + 1}\033[1;91m]\033[0;0m {command}\n'
        i += 1
    return message;


def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)

import os,sys,time,json,subprocess,platform


def CeckChoice(message):
    choice = selfInput(message);
    clear()
    if not choice.isdigit():
        printLogo();
        return print('\nDigite números!')

    if int(choice) > len(CommandsList):
        printLogo();
        return print('Digite um número da lista!')

    elif True:
        CommandsList[int(choice) - 1]['run']();
        printLogo()


message = formatMessage();
while True:
    CeckChoice(message);
