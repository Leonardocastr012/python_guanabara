#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
a = float(input('Digite o comprimento da reta: '))
b = float(input('Digite o comprimento da outra reta: '))
c = float(input('Digite o comprimento da outra reta: '))

if a > b + c:
    print('Não é triângulo!')
if b > a + c:
    print('Não é triângulo!')
if c > a + b:
    print('Não é triângulo!')
else:
    print('É triângulo!')