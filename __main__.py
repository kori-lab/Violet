from src.utils.treeFiles import *;
import os, subprocess;

if "ANDROID_ARGUMENT" in os.environ:
    try:
        import androidhelper;
        droid = androidhelper.Android();
        droid.makeToast('oi');

    except:
        pass;

try:
    if __name__ == '__main__':
        update = subprocess.check_output('git pull', shell=True);

except:
    if os.path.exists('.git'):
            pass
    else:
        print('Falta de repositório GIT local')

functions = treePath('src/utils');

functions['clear'](); functions['printLogo']();

CommandsList = treePath('src/commands', True);

try:
	import requests;
except:
    os.system('python3 -m pip install --upgrade pip');
    os.system('pip3 install requests');

    functions['restart'].run()

message = functions['mainSetMessage'](CommandsList);

while True:
    functions['mainChoices'](message, CommandsList, functions);