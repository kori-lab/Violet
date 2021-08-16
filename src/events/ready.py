from os import listdir, system, name;
from importlib import import_module;

def clear():
    system('cls' if name == 'nt' else 'clear');

def resumeFileName(fileName):
    fileNameList = list(fileName)
    result = ''

    for letter in fileNameList:
        if letter.isupper():
            result += ' '+ letter
        else:
            result += letter
    
    return result.capitalize();

def start(param):
    clear();
    print ('\033[1;32m[/]\033[0;0m Inicando a aplição mestre, aguarde... 🍙');

    folders = [];
    files = [];

    for path in listdir(param):

        if not path[-3::] == '.py':
            
            folders.append(path);
            print(f'\n\033[0;0m\033[1;34mᆫ {path}\033[1;94m');

            for file in listdir(param + '/' + path):
                if file[-3::] == '.py':
                    caminho = f'src.commands.{path}.{file[:-3]}'
                    
                    defs = import_module(caminho).run
                
                    object = {
                        'name': resumeFileName(file[:-3]),
                        'run': defs
                    }

                    files.append(object);
                    print(f'    ᆫ  {file}');

    print(f'\n\033[1;92m[i]\033[0;0m Eu achei {len(folders)} pastas e {len(files)} arquivos .py');

    ref_arquivo = open("logo.txt","r")

    print('\033[1;31m'+ ref_arquivo.read() +'\033[0;0m\n')

    ref_arquivo.close()

    return files;
