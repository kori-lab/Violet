R = '\033[1;31m';
C = '\033[0;0m';

def run(text: str) -> str:
    print(text);
    return input(f'{R}>{C} ');