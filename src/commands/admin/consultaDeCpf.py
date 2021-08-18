from requests import get

def formatResponse(_res):
    r = '\033[1;31m'
    c = '\033[0;0m'
    nome = r + _res['retorno'].nome + c
    date = r + _res['retorno'].AnoNascimento + c
    cpf = r + _res['retorno'].CPF + c
    sexo = r + _res['retorno'].Sexo + c

    if not nome:
        _res = False;
    else:
        _res = f'CPF: {cpf}\nNome: {nome}\nAno de nascimento: {date}\nSexo: {sexo}'

    return _res;

def run(functions):
    repeat = True
    while repeat:
        _num = functions['selfInput']('Qual é o cpf que deseja consultar?');
        _num = _num.replace(' ', '').replace('-', '');

        try:
            functions['clear']();
            _res = get(f"https://netinnbapi.000webhostapp.com/clientesnetin/api.php?cpf={_num}").json();

            _res = formatResponse(_res);
            if not _res:
                print('Cpf não encontrado...');

            else:
                print(_res);

        except:
            print('Cpf não encontrado...')
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