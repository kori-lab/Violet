from requests import get

def formatResponse(_res):
    r = '\033[1;31m'
    c = '\033[0;0m'

    message = '';
    values = {"country" : "Pais", "countryCode" : "Código do Pais", 
            "region" : "Região", "regionName" : "Nome da Região", 
            "city" : "Cidade", "query" : "Ip"};
    
    for key in _res:
        if key in values.keys(): 
            message += f"{r}{values[key]}{c}: {_res[key]}\n";

        else: 
            message += f"{r}{key}{c}: {_res[key]}\n";
        
    return message.replace('_', ' ').replace('State of ', '');

def run(functions):

    repeat = True

    while repeat:
        _num = functions['selfInput']('Qual é Ip que deseja consultar?');
        _num = _num.replace(' ', '').replace('-', '');

        try:
            functions['clear']();
            _res = get(f"http://ip-api.com/json/{_num}?fields=258047").json();

            print(formatResponse(_res));

        except:
            print('Ip incorreto ou não encontrado...\n')
            pass;

        choice = functions['selfInput']('\n\033[1;92m[1]\033[0;0m repetir\n\033[1;92m[2]\033[0;0m sair para menu\n');

        if choice == '1':
            pass;

        elif choice == '2':
            functions['clear']();
            repeat = False;
            
        else:
            print('opção invalida...');
        functions['clear']();