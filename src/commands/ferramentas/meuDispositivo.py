import os, sys, socket;
from requests import get

hostname = socket.gethostname()
ip_interno = socket.gethostbyname(hostname)
ip_externo = get('https://api.ipify.org').text

pid = os.getpid();

def run(functions: dict) -> None:

    message = functions['colorize'](f'''
            :r:Nome de usuário::: {os.getlogin()}
            :r:Sistema::: {sys.platform}
            :r:Hostname::: {hostname}
            :r:Ip interno::: {ip_interno}
            :r:Ip externo::: {ip_externo}
            :r:Versão da api::: {sys.api_version}
            ''');

    try:
        apiAndroid = sys.getandroidapilevel();
        message += functions['colorize'](f':r:Versão da api android::: {apiAndroid}\n');

    except:
        pass;

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