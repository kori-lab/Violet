import os;

pid = os.getpid()

message = f'''
            Nome de usuário: {os.getlogin()}
        ''';

def run(functions):
    Sair = False;
    while(Sair == False):
        functions['clear']();
    
        try:
            print(message);
        except:
            return;

        functions['selfInput']('Aperte enter para ir ao menu...\n');
        
        functions['clear']();
        Sair = True;