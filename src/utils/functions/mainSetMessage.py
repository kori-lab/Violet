def run(CommandsList, functions):
	message = '';
	i = 0;

	for command in CommandsList:
		command = command['name'];
		message += functions['colorize'](f':red:[::{i + 1}:red:]:: {command}\n');
		i += 1;

	message += functions['colorize'](f'\n:red:[::0:red:]:: Sair\n');

	return message;