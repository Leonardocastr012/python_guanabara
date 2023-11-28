#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. 
#Ex: n = leiaInt(‘Digite um n: ‘)
def leiaInt(msg):
    if msg.isnumeric():
        n = int(msg)
        return n
    else:
        return '\033[0;31mERRO! Não é um do tipo inteiro\033[m'

#Program principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')