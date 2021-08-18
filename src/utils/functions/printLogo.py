def run():
    ref_arquivo = open("logo.txt","r")

    print('\033[1;31m'+ ref_arquivo.read() +'\033[0;0m\n')

    ref_arquivo.close()