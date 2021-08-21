import os, sys;

pid = os.getpid();

message = f'''
            Nome de usuário: {os.getlogin()}
            Sistema: {sys.platform}
            Byteorder: {sys.byteorder}
            Versão da api: {sys.api_version}
            ''';

try:
    apiAndroid = sys.getandroidapilevel();
    message += f'Android: {apiAndroid}\n';

except:
    pass;

def run(functions: dict) -> None:

    exit = False;
    while not exit:
        functions['clear']();
    
        try:
            print(message);
            
        except:
            return;

        functions['selfInput']('Aperte enter para ir ao menu...\n');
        
        functions['clear']();
        exit = True;