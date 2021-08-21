from requests import get

def formatResponse(_res):
    _res = _res.replace('\n', '').replace('\\u0000', '').replace(':','\033[0;0m: ').replace('<br>', '\n\033[1;31m').replace('DDD', '\033[1;31mDDD').replace('\\r', '').replace('<p>', '').replace('_', ' ')
    _res = '\033[1;31m' + _res;
    return _res.capitalize();

def run(functions):
    repeat = True
    
    while repeat:
        _num = functions['selfInput']('\nQual é o número que deseja consultar?\n');
        
        if len(_num) < 9:
            functions['clear']();
            print("Número não está nem digitado certo '-'\nEx: DDD+número");

        else:
            try:
                functions['clear']();
                _num = _num.replace(' ', '').replace('-', '').replace('+55', '');
                _res = '';
                
                if len(_num) != 11:
                    _num = _num[:2] + '9' + _num[2:];
                    _res = get(f"https://dualityapi.xyz/apis/flex_7/Consultas%20Privadas/HTML/numero.php?consulta={_num}").text;
                    
                else:
                    _res = get(f"https://dualityapi.xyz/apis/flex_7/Consultas%20Privadas/HTML/numero.php?consulta={_num}").text;
                    
                print(formatResponse(_res));
                
            except:
                return;

        choice = functions['selfInput'](
            functions['colorize'](
                '\n:red:[::1:red:]:: repetir \n:red:[::2:red:]:: sair para menu\n'
            )
        );

        if choice == '1':
            pass

        if choice == '2':
            functions['clear']();
            repeat = False;
            
        else:
            functions['clear']();
            print('opção invalida...');