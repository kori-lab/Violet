from random import choice;

def run(name: str) -> str:
    colors = [
        '👿 \033[1;31m', '🍃 \033[1;32m', '🙄 \033[1;33m', 
        '🎐 \033[1;34m', '🍧 \033[1;35m', '👩‍🦳 \033[1;36m', 
        '👳‍♂️ \033[1;97m', '💤 \033[1;95m', '😨 \033[1;93m',
    ];

    colored_lines = [choice(colors) + line for line in name.split('\n')];

    return '\n'.join(colored_lines);