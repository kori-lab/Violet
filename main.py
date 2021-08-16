from src.utils.functions.clear import *
from src.events.ready import *;
from src.utils.functions.selfInput import *;
import subprocess, os
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
try:
	import requests,random,json,phonenumbers
except:
    choice = input(f'Vejo que é sua primeira vez aqui,\n Deseja instalar o software necessário?\n1-Sim\n2-Não\n_')
    if choice:
        os.system("apt install figlet curl -y")
        os.system('python3 -m pip install --upgrade pip')
        os.system('pip3 install requests pytube phonenumbers')
    else:
        print(f'Ok,instale por si ou isso é um adeus.');exit()
    restart()

try:
    if __name__ == '__main__':
        print('Buscando atualizações...')
        update = subprocess.check_output('git pull', shell=True)
        if 'Already up to date' not in update.decode():
            print('Atualização instalada.')
        else:
            print(f'[i] Nenhuma atualizacao disponivel.')
except:
    if os.path.exists('.git'):
        pass
    else:
        print('Falta de repositório GIT local')

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


message = formatMessage();
while True:
    CeckChoice(message);
