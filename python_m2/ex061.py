# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
a1 = float(input('Digite o primeiro termo: '))
r = float(input('Qual a razão? '))
n = 1 #posição do número na sequência
while n != 11:  #para ir até 10
    an = a1 + (n -1)*r
    print(f'A termo {n}º da progressão é {an}')
    n += 1
print('Acabou')