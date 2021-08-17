import colorama
import random

def randomColor(name):
    colors = list(vars(colorama.Fore).values())
    colored_lines = [random.choice(colors) + line for line in name.split('\n')]
    return '\n'.join(colored_lines)