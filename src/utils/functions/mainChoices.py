from sys import exit

def run(message, CommandsList, functions):

    choice = functions['selfInput'](message);
    functions['clear']();

    if not choice.isdigit():
        functions['printLogo']();
        return print('\n\t\t\tDigite números!');

    if int(choice) > len(CommandsList):
        functions['printLogo']();
        return print('\n\t\t\tDigite um número da lista!');

    elif choice == '0':
        functions['clear']();
        exit();

    else:
        CommandsList[int(choice) - 1]['run'](functions);
        functions['printLogo']();