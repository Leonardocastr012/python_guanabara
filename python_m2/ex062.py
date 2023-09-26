# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
#O programa encerrará quando ele disser que quer mostrar 0 termos.
n = int(input('Quantos termos de fibonacci você quer mostrar? '))
#fn = n1 = n2
n1 = 0
n2 = 1

while n != 0:
    if n >= 3:
        fn = n1 + n2
        print(f'->{fn}', end='')
        n2 = n1
        n1= fn
        n -= 1