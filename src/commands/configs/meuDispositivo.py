from src.utils.functions.selfInput import *;
from src.utils.functions.clear import *;
import os;

pid = os.getpid()

message = f'''
            Nome de usuário: {os.getlogin()}
        ''';

def run():
    Sair = False;
    while(Sair == False):
        clear();
    
        try:
            print(message);
        except:
            return;

        choice = selfInput('Aperte enter para ir ao menu...\n');
        
        clear();
        Sair = True;