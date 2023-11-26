#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:   
from time import sleep
def linha():
    print('-='*15)

def contador():
    # a) de 1 até 10, de 1 em 1
    linha()
    print('Contagem de 1 até 10, de 1 em 1')
    for i in range(1, 11, 1):
        print(f'{i}', end=' ')
        sleep(1)
    print('FIM!')
    linha()
    # b) de 10 até 0, de 2 em 2
    print('Contagem de 10 até 0, de 2 em 2')
    for i in range(10, -1, -2):#o passo tem que tá negativo para correr ao contrário
        print(f'{i}', end=' ')
        sleep(1)
    print('FIM!')
    linha()                                                                                                                                            
    # c) uma contagem personalizada
    print('Contagem Personalizada')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    for i in range(inicio, fim, passo):
        print(f'{i}', end=' ')
        sleep(1)
    print('FIM!')

contador()
