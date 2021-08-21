from requests import get;

def formatResponse(_res: dict) -> str:
    nome = _res['retorno'].nome;
    date = _res['retorno'].AnoNascimento;
    cpf = _res['retorno'].CPF;
    sexo = _res['retorno'].Sexo;

    if not nome:
        _res = False;

    else:
        _res = f'CPF: {cpf}\nNome: {nome}\nAno de nascimento: {date}\nSexo: {sexo}';

    return _res;

def run(functions: dict) -> None:

    exit = False;
    while not exit:
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
            print('Cpf não encontrado, api não deu nenhuma resposta.');
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
            repeat = False;
            
        else:
            print('opção invalida...');
        functions['clear']();