# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Digite um ano para saber se ele é bissexto: '))

if (ano % 4 == 0):
    print('Esse ano é bissexto!')
else:
    print('Esse ano não é bissexto!')