import sys;

def organizationChoice(choice: str, menu) -> tuple:
    listCommands = menu[list(menu.keys())[int(choice)-1]];
    nameMenu = list(menu.keys())[int(choice) - 1];
    
    return listCommands, nameMenu;

def run(menu, functions: dict) -> None:
    message = functions['mainSetMessage'](menu.keys(), functions);
    
    choice = functions['selfInput'](message);
    functions['clear']();

    if not choice.isdigit():
        functions['printLogo']();
        return print('\t\tDigite números!');

    if int(choice) > len(menu):
        functions['printLogo']();
        return print('\t\tDigite um número da lista!');

    elif choice == '0':
        functions['clear']();
        sys.exit();

    else:
        CommandsList, nameMenu = organizationChoice(choice, menu, functions);
        nameMenu = functions['colorize'](f'\t\t\t:red:[:: \u001b[1m{nameMenu.title()} :red:]::');
        
        functions['printLogo']();
        print(nameMenu);
        
        exit = False;
        while not exit:
            choice = functions['selectChoice'](CommandsList, functions, nameMenu);

            if choice == '99':
                functions['clear']();
                exit = True;
            
        functions['printLogo']();