from src.utils.treeFiles import *; import os, subprocess; from sys import executable, argv;

try:
    if __name__ == '__main__':
        update = subprocess.check_output('git pull', shell=True);

except:
    if os.path.exists('.git'):
        pass;

    else:
        print('Falta .git local');

try:
	import requests;

except:
    os.system('python3 -m pip install --upgrade pip');
    os.system('pip3 install requests');
    os.execl(executable, executable, *argv);

functions = treePath('src/utils');

functions['clear'](); functions['printLogo']();

CommandsList = treePath('src/commands', True);
message = functions['mainSetMessage'](CommandsList, functions);

while True:
    functions['mainChoices'](CommandsList, functions);