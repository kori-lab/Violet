from os import listdir;
from importlib import import_module;

def resumeFileName(fileName: str) -> str:

    fileNameList = list(fileName);
    result = '';

    for letter in fileNameList:

        if letter.isupper():
            result += ' '+ letter;

        else:
            result += letter;

    return result.capitalize();
Vector = list[float]
def treePath(param: str, resume: bool = False) -> dict:

    folders = {};
    objectFiles = {};

    for path in listdir(param):

        if not path[-3::] == '.py':
            folders.setdefault(path, []);

            for file in listdir(param + '/' + path):
                if file[-3::] == '.py':
                    caminho = f'{param.replace("/", ".")}.{path}.{file[:-3]}';
                    
                    defs = import_module(caminho).run;
                    fileName = '';
                    object = {};

                    if resume:
                        fileName = resumeFileName(file[:-3]);
                        
                        object = {
                            'name': fileName,
                            'run': defs
                        };

                        folders[path].append(object);

                    else:
                        fileName = file[:-3];

                        object = {
                            fileName: defs
                        };

                        objectFiles.update(object);
    
    if not resume:
        return objectFiles;

    if resume:
        return folders;