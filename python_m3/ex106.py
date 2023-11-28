#Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. 
#Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
def cabeçalho():
    nome = 'SISTEMA DE AJUDA PyHELP'
    print('\033[0;30;42m~\033[m'*len(nome))
    print(f'\033[0;30;42m{nome:^}\033[m')
    print('\033[0;30;42m~\033[m'*len(nome))
def cabeçalhoInterno(msg):
    nome = 'ACESSANDO O MANUAL DE COMANDO: '
    print('\033[0;30;46m~\033[m'*(len(nome)+len(msg)))
    print(f'\033[0;30;46m{nome:^}{msg:<}\033[m')
    print('\033[0;30;46m~\033[m'*(len(nome)+len(msg)))
def menu(msg):
    print('\033[7;37m',end='')
    help(msg)
    print('\033[m',end='')
    
def PyHelp():
    while True:
        cabeçalho()
        scan = str(input('Função ou biblioteca> '))
        if scan.upper().strip() == 'FIM':
            break
        cabeçalhoInterno(scan)
        menu(scan)
PyHelp()