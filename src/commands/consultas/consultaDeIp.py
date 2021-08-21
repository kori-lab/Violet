from requests import get

def formatResponse(_res: dict, functions: dict) -> str:
    message = '';
    values = {
        "country": "Pais", "countryCode": "Código do Pais", 
        "region": "Região", "regionName": "Nome da Região", 
        "city": "Cidade", "query": "Ip"
    };

    for key in _res:
        if key in values.keys():
            message += functions['colorize'](f":red:{values[key]}::: {_res[key]}\n");
    
        else:
            message += functions['colorize'](f":red:{key}::: {_res[key]}\n");
    
    return message.replace('_', ' ').replace('State of ', '');

def run(functions: dict) -> None:

    exit = False;
    while not exit:
        _num = functions['selfInput']('Qual é Ip que deseja consultar?');
        _num = _num.replace(' ', '').replace('-', '');

        try:
            functions['clear']();
            _res = get(f"http://ip-api.com/json/{_num}?fields=258047").json();

            print(formatResponse(_res, functions));

        except:
            print('Ip incorreto ou não encontrado...\n');
            pass;

        choice = functions['selfInput'](
            functions['colorize'](
                '\n:red:[::1:red:]:: repetir \n:red:[::2:red:]:: sair para menu\n'
            )
        );
        
        if choice == '1':
            pass;

        elif choice == '2':
            functions['clear']();
            exit = True;
            
        else:
            print('opção invalida...');
            
        functions['clear']();