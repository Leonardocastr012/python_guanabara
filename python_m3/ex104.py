#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. 
#Ex: n = leiaInt(‘Digite um n: ‘)
def leiaInt(msg):
    valor = 0
    while True:
        n = str(input(msg)) #Vai ler a mensagem, que nem o scanf em C
        if n.isnumeric(): #Vai verificar se na string tem número
            valor = int(n) #Transformando string em inteiro
            break
        else:
            print('\033[0;31mERRO! Não é um do tipo inteiro\033[m')
    return valor
#Program principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')