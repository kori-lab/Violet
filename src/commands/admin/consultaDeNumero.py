from requests import get
from src.utils.functions.selfInput import *
from src.utils.functions.clear import *

def formatResponse(_res):
    _res = _res.replace('\n', '').replace('\\u0000', '').replace(':','\033[0;0m: ').replace('<br>', '\n\033[1;31m').replace('DDD', '\033[1;31mDDD').replace('\\r', '').replace('<p>', '').replace('_', ' ')

    return _res.capitalize();

def run(functions):
    repeat = True
    while repeat:
        _num = functions['selfInput']('Qual é o número que deseja consultar?');
        _num = _num.replace(' ', '').replace('-', '').replace('+55', '');

        if len(_num) < 11:
            functions['clear']();
            print("Número não está nem digitado certo '-'\nEx: DDD+número");

        elif len(_num) > 11:
            functions['clear']();
            print("Número não está nem digitado certo '-'\nEx: DDD+número");

        else:
            try:
                functions['clear']();
                _res = get(f"https://dualityapi.xyz/apis/flex_7/Consultas%20Privadas/HTML/numero.php?consulta={_num}").text;
                print(formatResponse(_res));
            except:
                return;

        choice = functions['selfInput']('\n\033[1;92m[1]\033[0;0m repetir\n\033[1;92m[2]\033[0;0m sair para menu\n');

        if choice == '1':
            pass

        elif choice == '2':
            functions['clear']();
            repeat = False;
            
        else:
            print('opção invalida...');
        functions['clear']();