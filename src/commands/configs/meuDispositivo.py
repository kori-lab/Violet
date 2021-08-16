from src.utils.functions.selfInput import *;
from src.utils.functions.clear import *;
import os;

pid = os.getpid()

message = f'''
            nome de usuario: {os.getlogin()}
        '''
def run():
    Sair = False;
    while(Sair == False):
        clear();
    
        try:
            print(message)
        except:
            a = 0;

        choice = selfInput('Aperte enter para ir ao menu...');
        
        if True:
            clear();
            Sair = True;