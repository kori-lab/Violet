from os import listdir;
from importlib import import_module;

def resumeFileName(fileName):

    fileNameList = list(fileName)
    result = ''

    for letter in fileNameList:

        if letter.isupper():
            result += ' '+ letter;

        else:
            result += letter;

    return result.capitalize();

def treePath(param, resume=False):

    folders = []
    files = []
    resumeTrue = {}
    for path in listdir(param):

        if not path[-3::] == '.py':
            
            folders.append(path);

            for file in listdir(param + '/' + path):

                if file[-3::] == '.py':
                    caminho = f'{param.replace("/", ".")}.{path}.{file[:-3]}'
                    
                    defs = import_module(caminho).run
                    fileName = ''
                    object = {}

                    if resume: 
                        fileName = resumeFileName(file[:-3]);
                        object = {
                            'name': fileName,
                            'run': defs
                        }

                    else:
                        fileName = file[:-3];

                        object = {
                            fileName: defs
                        }

                        resumeTrue.update(object)

                    files.append(object);
                    
    if not resume:
        return resumeTrue;
    return files;