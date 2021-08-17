from src.utils.functions.selfInput import *;
from src.utils.functions.clear import *;
from src.utils.others.server import *;
from src.utils.others.client import *;

def run():
    choice = '';
    Sair = False;
    while(Sair == False):
        clear();
        _input = input('\033[1;32m[?]\033[0;0m Escolha uma opção.\n[1] client \n[2] host do server');

        try:
            print(f'\n\033[1;32m{_input}\033[0;0m\n')
        except:
            return;

        choice = selfInput('\033[1;92m[1]\033[0;0m repetir\n\033[1;92m[2]\033[0;0m sair para menu\n');

        if choice == '1':
            client()

        elif choice == '2':
            server()
            
        else:
            print('opção invalida...');