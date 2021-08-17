from src.utils.functions.selfInput import *;
from src.utils.functions.clear import *;
from src.utils.others.server import *;
from src.utils.others.client import *;

def run():
    choice = '';
    Sair = False;
    while(Sair == False):
        clear();
        _input = input('\033[1;32m[#]\033[0;0m Escolha uma opção para se conectar.\n\n\033[1;92m[1]\033[0;0m client \n\033[1;92m[2]\033[0;0m host do server\n\n\033[1;92m>\033[0;0m ');

        try:
            if _input == '1':
                clear()
                client()

            elif _input == '2':
                clear()
                server()
        except:
            return;
        
        choice = selfInput('\n\033[1;92m[1]\033[0;0m repetir\n\033[1;92m[2]\033[0;0m sair para menu\n');

        if choice == '1':
            pass

        elif choice == '2':
            clear()
            Sair = True;
            
        else:
            print('opção invalida...');