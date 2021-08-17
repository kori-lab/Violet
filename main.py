from src.utils.functions.clear import *
from src.events.ready import *;
from src.utils.functions.selfInput import *;
from src.utils.functions.printLogo import *;
import os, subprocess, sys

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
clear();

def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)

try:
	import requests;
except:
    choice = selfInput(f'Você deve baixar alguns modulos, digite 1 para baixa-los.')
    if choice == '1':
        os.system("apt install figlet curl -y")
        os.system('python3 -m pip install --upgrade pip')
        os.system('pip3 install requests')
    else:
        print(f'Ok, instale por si ou não dará para rodar a aplicação...');exit()
    restart()

CommandsList = start("./src/commands");

def formatMessage():
    message = ''
    i = 0
    for command in CommandsList:
        command = command['name']
        message += f'\033[1;91m[\033[0;0m{i + 1}\033[1;91m]\033[0;0m {command}\n'
        i += 1

    message += f'\n\033[1;91m[\033[0;0m0\033[1;91m]\033[0;0m Sair\n'

    return message;

def CeckChoice(message):
    choice = selfInput(message);
    clear()
    if not choice.isdigit():
        printLogo();
        return print('\nDigite números!')

    if int(choice) > len(CommandsList):
        printLogo();
        return print('Digite um número da lista!')

    elif choice == '0':
        clear();
        sys.exit();

    else:
        CommandsList[int(choice) - 1]['run']();
        printLogo()


message = formatMessage();
while True:
    CeckChoice(message);
