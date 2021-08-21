def run(CommandsList, functions: dict) -> str:
	message = '';
	isCommands = False;
	i = 0;
 
	for command in CommandsList:
			if type(command) == dict:
				command = command['name'];
				isCommands = True;

			else:
				command = command;

			message += functions['colorize'](f':red:[::{i + 1}:red:]:: {command.title()}\n');
			i += 1;

	message += functions['colorize'](f'\n:red:[::0:red:]:: Sair\n');
	if isCommands: 
		message += functions['colorize'](f':red:[::99:red:]:: Voltar ao menu\n');
 
	return message;