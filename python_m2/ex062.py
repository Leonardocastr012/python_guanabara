# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
#O programa encerrará quando ele disser que quer mostrar 0 termos.
n = int(input('Quantos termos de fibonacci você quer mostrar? '))
max = n
n1 = 0
n2 = 1
fn = n1 + n2
for c in range(1, n + 1):
    if c == 1:
        print(f'{n1}', end ='')
    if c >= 2:
        fn = n1 + n2
        print(f'->{fn}', end='')
        n2 = n1
        n1= fn