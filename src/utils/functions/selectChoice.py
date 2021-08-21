def run(CommandsList, functions, nameMenu):

    message = functions['mainSetMessage'](CommandsList, functions)

    choice = functions['selfInput'](message);
    functions['clear']();

    if not choice.isdigit():
        functions['printLogo']();
        print(nameMenu);
        
        return print('\n\t\t\tDigite números!');

    if int(choice) > len(CommandsList) and choice != '99':
        functions['printLogo']();
        print(nameMenu);
        
        return print('\n\t\t\tDigite um número da lista!');

    elif choice == '0':
        functions['clear']();
        exit();

    elif choice == '99':
        functions['clear']();
        return choice;
    
    else:
        CommandsList[int(choice) - 1]['run'](functions);
        functions['printLogo']();
        print(nameMenu);