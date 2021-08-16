from src.utils.functions.selfInput import *;
from src.utils.functions.clear import *;

def run():
    choice = '';
    Sair = False;
    while(Sair == False):
        clear();
        _input = input('[?] Oque é que você quer que eu repita? ');

        try:
            print(f'\n\033[1;32m{_input}\033[0;0m\n')
        except:
            return;

        choice = selfInput('[1] repetir\n[2] sair para menu');

        if choice == '1':
            pass;

        elif choice == '2':
            clear();
            Sair = True;
            
        else:
            print('opção invalida...');