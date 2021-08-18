def run(CommandsList):
    message = '';
    i = 0;
    
    for command in CommandsList:
        command = command['name'];
        message += f'\033[1;91m[\033[0;0m{i + 1}\033[1;91m]\033[0;0m {command}\n';
        i += 1;

    message += f'\n\033[1;91m[\033[0;0m0\033[1;91m]\033[0;0m Sair\n';

    return message;