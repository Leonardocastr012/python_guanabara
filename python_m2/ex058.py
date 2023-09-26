#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
numeroSorteado = randint(1,10)
print(numeroSorteado)
count = 0
while True:
    numeroUsuario = int(input('Adivinhe um número entre 0 e 10: '))
    if (numeroUsuario == numeroSorteado):
        print('Você acertou!')
        count += 1
        break #Força a parada pois o loop é infinito
    else:
        print('Você errou!')
        count += 1
print(f'Foram necessários {count} palpites')