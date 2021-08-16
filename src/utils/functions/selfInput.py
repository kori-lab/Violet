from src.utils.functions.clear import clear;

R = '\033[1;31m';
C = '\033[0;0m'; 

def selfInput(text):
    print(text);
    return input(f'{R}>{C} ');

